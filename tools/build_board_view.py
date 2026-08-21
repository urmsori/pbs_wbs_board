#!/usr/bin/env python3
"""보드의 게시글을 취합해 WBS/Gantt/PBS 현황 페이지를 만든다.

PBS WBS Board 규칙 5절의 도구. 표준 라이브러리만 사용한다.
Gantt는 after 종속성을 화살표로 그리고, 취합 순서 위반(4절)을 경고한다.
게시글이 100건을 넘는 큰 보드에서는 요약 중심 뷰로 바뀐다(v2.0):
레벨×상태 요약표, 접히는 WBS/PBS(하위 진행률), 요약 Gantt(레벨 2까지) +
서브트리별 상세 Gantt(접힘), 디렉토리로 묶인 Product 구성, 트랙별 목록.

사용법: python3 tools/build_board_view.py [보드 디렉토리] [출력 html] [--ready]
  인자를 생략하면 board/와 board.html (규칙 프로젝트의 보드).
  --ready: 아무 파일도 쓰지 않고 "집기 가능"(OPEN이고 선행 모두 DONE) 게시글
  목록만 출력한다 — 병렬 웨이브 중간에 에이전트가 쓰는 읽기 전용 조회.
  deliverable 경로는 저장소 루트 기준으로 적고, 링크는 출력 위치 기준으로
  계산되므로 보드가 저장소 어디에 있어도 된다.
"""
import datetime
import html
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOARD = ROOT / "board"   # main()에서 인자로 대체될 수 있다
OUT = ROOT / "board.html"

LARGE = 100  # 게시글이 이보다 많으면 요약 중심 뷰


def href(repo_rel_path):
    """저장소 루트 기준 경로 → 출력 html 위치 기준 상대 링크."""
    return os.path.relpath(ROOT / repo_rel_path, OUT.parent)


def parse_post(path):
    post = {
        "id": "",
        "title": path.stem,
        "status": "OPEN",
        "parent": "-",
        "owner": "-",
        "deliverable": "-",
        "after": "-",
        "track": "-",
        "started": "-",
        "finished": "-",
        "body": "",
        "file": path.name,
    }
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        post["body"] = "\n".join(lines).strip()
        return post
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        line = lines[i]
        if ":" in line:
            key, value = line.split(":", 1)
            post[key.strip()] = value.strip()
        i += 1
    post["body"] = "\n".join(lines[i + 1:]).strip()
    return post


def parse_dt(value):
    if not value or value == "-":
        return None
    try:
        return datetime.datetime.fromisoformat(value.replace(" ", "T"))
    except ValueError:
        return None


def after_ids(post):
    if post["after"] == "-":
        return []
    return [a.strip() for a in post["after"].split(",") if a.strip() and a.strip() != "-"]


def deliverables(post):
    """deliverable 필드의 경로들. 여러 개면 쉼표로 구분된다(규칙 3절)."""
    if post["deliverable"] == "-":
        return []
    return [d.strip() for d in post["deliverable"].split(",") if d.strip() and d.strip() != "-"]


def topo_siblings(kids):
    """형제들 사이의 after 간선으로 위상 정렬 — 뷰의 행 순서가 시간 논리를 따른다."""
    ids = {k["id"] for k in kids}
    remaining, out, placed = kids[:], [], set()
    while remaining:
        progressed = False
        for k in remaining[:]:
            if all(d in placed for d in after_ids(k) if d in ids):
                out.append(k)
                placed.add(k["id"])
                remaining.remove(k)
                progressed = True
        if not progressed:  # 순환이면 남은 순서대로
            out.extend(remaining)
            break
    return out


def load_posts():
    posts = [parse_post(p) for p in sorted(BOARD.glob("*.md"))]
    by_id = {p["id"]: p for p in posts if p["id"]}
    children = {}
    roots = []
    for p in posts:
        if p["parent"] in by_id:
            children.setdefault(p["parent"], []).append(p)
        else:
            roots.append(p)
    for pid in children:
        children[pid] = topo_siblings(children[pid])
    roots = topo_siblings(roots)
    return posts, by_id, roots, children


def dfs_order(roots, children):
    out = []

    def walk(p):
        out.append(p)
        for c in children.get(p["id"], []):
            walk(c)

    for r in roots:
        walk(r)
    return out


def esc(s):
    return html.escape(s, quote=True)


TRACK_COLORS = [
    ("#e8f0fe", "#1a56c4"), ("#fce8f3", "#b4257a"), ("#e6f4ea", "#1e7e34"),
    ("#fef3e0", "#a05a00"), ("#ede7f6", "#5e35b1"), ("#e0f2f1", "#00695c"),
    ("#fdecea", "#b42318"), ("#f1f3f4", "#5f6368"), ("#e0f7fa", "#006064"),
    ("#f9fbe7", "#616f00"), ("#efebe9", "#5d4037"), ("#e8eaf6", "#283593"),
]
_track_color = {}


def track_badge(post):
    """track 필드를 색 배지로. 같은 track = 같은 색 (등장 순서대로 배정)."""
    t = post.get("track", "-")
    if not t or t == "-":
        return ""
    if t not in _track_color:
        _track_color[t] = TRACK_COLORS[len(_track_color) % len(TRACK_COLORS)]
    bg, fg = _track_color[t]
    return f'<span class="tbadge" style="background:{bg};color:{fg}">{esc(t)}</span> '


def is_ready(post, by_id):
    """집기 가능: OPEN이고 after의 게시글이 모두 DONE."""
    if post["status"].upper() != "OPEN":
        return False
    return all(
        by_id[a]["status"].upper() == "DONE" for a in after_ids(post) if a in by_id
    )


def depth_of(post, by_id):
    depth, seen = 0, set()
    while post["parent"] in by_id and post["parent"] not in seen:
        seen.add(post["parent"])
        post = by_id[post["parent"]]
        depth += 1
    return depth


def subtree_stats(post, children, memo):
    """(자기 포함 하위 게시글 수, 그중 DONE 수)."""
    if post["id"] in memo:
        return memo[post["id"]]
    total, done = 1, 1 if post["status"].upper() == "DONE" else 0
    for c in children.get(post["id"], []):
        t, d = subtree_stats(c, children, memo)
        total += t
        done += d
    memo[post["id"]] = (total, done)
    return memo[post["id"]]


def post_line(post, by_id, stats=None):
    status = post["status"].upper()
    badge = f'<span class="badge {status.lower()}">{esc(status)}</span>'
    ready = ' <span class="ready">집기 가능</span>' if is_ready(post, by_id) else ""
    owner = f' <span class="meta">담당: {esc(post["owner"])}</span>' if post["owner"] != "-" else ""
    after = f' <span class="meta">선행: {esc(post["after"])}</span>' if post["after"] != "-" else ""
    prog = ""
    if stats and stats[0] > 1:
        prog = f' <span class="prog">{stats[1]}/{stats[0]}</span>'
    return (
        f'{badge} <span class="pid">{esc(post["id"])}</span> {track_badge(post)}'
        f'<a href="{esc(os.path.relpath(BOARD / post["file"], OUT.parent))}">{esc(post["title"])}</a>'
        f'{prog}{ready}{owner}{after}'
    )


def wbs_node(post, children, by_id, memo, depth=0, open_depth=2):
    kids = children.get(post["id"], [])
    line = post_line(post, by_id, subtree_stats(post, children, memo))
    if not kids:
        return f'<div class="wbs-leaf">{line}</div>'
    inner = "".join(wbs_node(c, children, by_id, memo, depth + 1, open_depth) for c in kids)
    op = " open" if depth < open_depth else ""
    return (
        f'<details class="wbs"{op}><summary>{line}</summary>'
        f'<div class="wbs-kids">{inner}</div></details>'
    )


def pbs_node(post, children, by_id, depth=0, open_depth=2):
    status = post["status"].upper()
    paths = deliverables(post)
    if status == "DONE" and paths:
        links = " · ".join(f'<a class="deliv" href="{esc(href(d))}">{esc(d)}</a>' for d in paths)
        item = (
            f'<span class="pid">{esc(post["id"])}</span> {links} '
            f'<span class="meta">← {esc(post["title"])}</span>'
        )
    else:
        item = (
            f'<span class="pid">{esc(post["id"])}</span> '
            f'<span class="pending">(산출물 아직 없음)</span> '
            f'<span class="meta">← {esc(post["title"])}</span>'
        )
    kids = children.get(post["id"], [])
    if not kids:
        return f'<div class="wbs-leaf">{item}</div>'
    inner = "".join(pbs_node(c, children, by_id, depth + 1, open_depth) for c in kids)
    op = " open" if depth < open_depth else ""
    return (
        f'<details class="wbs"{op}><summary>{item}</summary>'
        f'<div class="wbs-kids">{inner}</div></details>'
    )


GANTT_W = 1000.0  # SVG 가로 가상 좌표(시간축). 화면 폭에 맞춰 늘어난다.
ROW_H = 26        # 한 Work 행의 높이(px). 세로는 1:1이라 왜곡이 없다.


def build_gantt(sel_posts, by_id, now, base_depth=0):
    """선택된 게시글들의 started~finished 막대 + after 화살표(선택 안에서만)."""
    spans = []
    for p in sel_posts:
        start = parse_dt(p["started"])
        end = parse_dt(p["finished"])
        if start and not end:
            end = now  # TAKEN: 진행 중이므로 현재 시각까지
        spans.append((p, start, end))

    times = [t for _, s, e in spans for t in (s, e) if t]
    if not times:
        return "<p class='meta'>시간이 기록된 게시글이 없다.</p>"
    t_min, t_max = min(times), max(times)
    total = max((t_max - t_min).total_seconds(), 60)

    def x(t):
        return (t - t_min).total_seconds() / total * GANTT_W

    labels, strips, bars, arrows = [], [], [], []
    pos = {}  # id -> (행 번호, start, end)
    for i, (p, start, end) in enumerate(spans):
        if p["id"]:
            pos[p["id"]] = (i, start, end)
        status = p["status"].upper()
        depth = max(depth_of(p, by_id) - base_depth, 0)
        if start or p.get("_synth"):
            wait = ""
        elif is_ready(p, by_id):
            wait = ' <span class="ready">집기 가능</span>'
        else:
            wait = ' <span class="meta">— 대기(선행 미완)</span>'
        labels.append(
            f'<div class="g-label" style="padding-left:{depth * 0.9}rem">'
            f'<span class="pid">{esc(p["id"])}</span> {track_badge(p)}{esc(p["title"])}{wait}</div>'
        )
        y = i * ROW_H
        if i % 2 == 1:
            strips.append(f'<rect class="g-strip" x="0" y="{y}" width="{GANTT_W:.0f}" height="{ROW_H}"/>')
        if start:
            x1 = x(start)
            w = max(x(end) - x1, 12)
            tip = f'{p["id"]} {p["title"]} — {p["started"]} ~ {p["finished"] if p["finished"] != "-" else "진행 중"}'
            bars.append(
                f'<rect class="g-bar {status.lower()}" x="{x1:.1f}" y="{y + 6}" '
                f'width="{w:.1f}" height="{ROW_H - 12}" rx="2"><title>{esc(tip)}</title></rect>'
            )

    # after 종속성: 선행 Work의 끝 → 후행 Work의 시작 (이 Gantt 안의 것만)
    for i, (p, start, end) in enumerate(spans):
        if not start:
            continue
        yy = i * ROW_H + ROW_H / 2
        for dep in after_ids(p):
            if dep not in pos:
                continue  # 이 Gantt 밖의 선행은 라벨의 "선행: "으로만 보인다
            j, ds, de = pos[dep]
            if not de:
                continue
            x1, y1 = x(de), j * ROW_H + ROW_H / 2
            x2 = x(start)
            midx = x1 + 6
            if x2 >= x1 + 14:
                path = f"M {x1:.1f} {y1:.1f} H {midx:.1f} V {yy:.1f} H {x2 - 7:.1f}"
                head = f"{x2:.1f},{yy:.1f} {x2 - 7:.1f},{yy - 3.5:.1f} {x2 - 7:.1f},{yy + 3.5:.1f}"
            else:
                path = f"M {x1:.1f} {y1:.1f} H {midx:.1f} V {yy:.1f} H {x2 + 7:.1f}"
                head = f"{x2:.1f},{yy:.1f} {x2 + 7:.1f},{yy - 3.5:.1f} {x2 + 7:.1f},{yy + 3.5:.1f}"
            arrows.append(f'<path class="g-dep" d="{path}"/><polygon class="g-dep-head" points="{head}"/>')

    height = len(spans) * ROW_H
    svg = (
        f'<svg class="g-chart" viewBox="0 0 {GANTT_W:.0f} {height}" '
        f'preserveAspectRatio="none" style="height:{height}px">'
        f'{"".join(strips)}{"".join(bars)}{"".join(arrows)}</svg>'
    )
    axis = (
        f'<div class="g-row g-axis"><div class="g-label"></div>'
        f'<div class="g-track"><span>{esc(t_min.strftime("%Y-%m-%d %H:%M:%S"))}</span>'
        f'<span class="g-right">{esc(t_max.strftime("%Y-%m-%d %H:%M:%S"))}</span></div></div>'
    )
    body = f'<div class="g-body"><div class="g-labels">{"".join(labels)}</div><div class="g-area">{svg}</div></div>'
    return f'<div class="gantt">{axis}{body}</div>'


def synthetic_rollup(key, group, now):
    """그룹(트랙/사람)의 Work 전체를 한 줄 막대로 요약하는 합성 게시글."""
    starts = [parse_dt(p["started"]) for p in group if parse_dt(p["started"])]
    ends = [parse_dt(p["finished"]) for p in group if parse_dt(p["finished"])]
    done = sum(1 for p in group if p["status"].upper() == "DONE")
    all_done = done == len(group)
    return {
        "id": key, "title": f"{done}/{len(group)}건",
        "status": "DONE" if all_done and group else ("TAKEN" if starts else "OPEN"),
        "parent": "-", "owner": "-", "deliverable": "x", "after": "-",
        "track": key, "body": "", "file": "", "_synth": True,
        "started": min(starts).strftime("%Y-%m-%d %H:%M:%S") if starts else "-",
        "finished": max(ends).strftime("%Y-%m-%d %H:%M:%S") if (all_done and ends) else "-",
    }


def build_lane_gantt(posts, by_id, now, keyname):
    """레인 Gantt: 그룹(track 또는 owner) 롤업 막대 + 그룹별 상세(접힘)."""
    groups = {}
    for p in posts:
        k = p.get(keyname, "-") or "-"
        if k == "-":
            k = "(미배정)" if keyname == "owner" else "(트랙 없음)"
        groups.setdefault(k, []).append(p)

    def group_start(kv):
        starts = [parse_dt(p["started"]) for p in kv[1] if parse_dt(p["started"])]
        return (min(starts) if starts else datetime.datetime.max, kv[0])

    ordered = sorted(groups.items(), key=group_start)
    rollups = [synthetic_rollup(k, g, now) for k, g in ordered]
    out = [build_gantt(rollups, by_id, now)]
    out.append('<p class="legend">레인 막대 = 그 그룹 Work 전체 구간. 아래에서 그룹을 펼치면 개별 Work가 보인다.</p>')
    for k, g in ordered:
        g_sorted = sorted(g, key=lambda p: (parse_dt(p["started"]) or datetime.datetime.max, p["id"]))
        done = sum(1 for p in g_sorted if p["status"].upper() == "DONE")
        out.append(
            f'<details class="gsec"><summary>{track_badge({"track": k})}{esc(k)} '
            f'<span class="prog">{done}/{len(g_sorted)}</span></summary>'
            f'{build_gantt(g_sorted, by_id, now)}</details>'
        )
    return "".join(out)


def build_gantt_section(posts, by_id, children, now, memo, roots):
    """작은 보드: Gantt 하나. 큰 보드: 요약 Gantt(레벨 2까지) + 서브트리별 상세(접힘)."""
    ordered = dfs_order(roots, children)
    seen = {q["id"] for q in ordered}
    posts = ordered + [p for p in posts if p["id"] not in seen]
    if len(posts) <= LARGE:
        return build_gantt(posts, by_id, now)
    depths = {p["id"]: depth_of(p, by_id) for p in posts}
    summary_posts = [p for p in posts if depths[p["id"]] <= 2]
    out = ["<h3>요약 — 레벨 2까지 (하위는 부모 막대에 합쳐 보인다)</h3>",
           build_gantt(summary_posts, by_id, now)]
    out.append("<h3>상세 — 서브트리별 (접힘)</h3>")
    sections = [p for p in posts if depths[p["id"]] == 2 and children.get(p["id"])]
    for sp in sections:
        sub = []

        def collect(q):
            sub.append(q)
            for c in children.get(q["id"], []):
                collect(c)

        collect(sp)
        t, d = subtree_stats(sp, children, memo)
        head = (
            f'<span class="pid">{esc(sp["id"])}</span> {track_badge(sp)}{esc(sp["title"])} '
            f'<span class="prog">{d}/{t}</span>'
        )
        out.append(
            f'<details class="gsec"><summary>{head}</summary>'
            f'{build_gantt(sub, by_id, now, base_depth=2)}</details>'
        )
    return "".join(out)


def level_summary(posts, by_id):
    """레벨(트리 깊이)×상태 요약표. 레벨-에이전트 등급 규칙(4절)의 현황판."""
    rows = {}
    for p in posts:
        d = depth_of(p, by_id)
        r = rows.setdefault(d, {"OPEN": 0, "TAKEN": 0, "DONE": 0})
        r[p["status"].upper()] = r.get(p["status"].upper(), 0) + 1
    trs = []
    for d in sorted(rows):
        r = rows[d]
        n = sum(r.values())
        pct = (r["DONE"] * 100) // n if n else 0
        trs.append(
            f'<tr><td>L{d}</td><td>{n}</td><td>{r["OPEN"]}</td><td>{r["TAKEN"]}</td>'
            f'<td>{r["DONE"]}</td><td><div class="bar"><div style="width:{pct}%"></div></div> {pct}%</td></tr>'
        )
    return (
        '<table class="lvl"><tr><th>레벨</th><th>게시글</th><th>OPEN</th>'
        '<th>TAKEN</th><th>DONE</th><th>진행률</th></tr>' + "".join(trs) + "</table>"
    )


def track_summary(posts):
    rows = {}
    for p in posts:
        t = p.get("track", "-")
        r = rows.setdefault(t, {"OPEN": 0, "TAKEN": 0, "DONE": 0})
        r[p["status"].upper()] = r.get(p["status"].upper(), 0) + 1
    if len(rows) > 30:
        return ""
    trs = []
    for t in sorted(rows):
        r = rows[t]
        n = sum(r.values())
        pct = (r["DONE"] * 100) // n if n else 0
        trs.append(
            f'<tr><td>{esc(t)}</td><td>{n}</td><td>{r["OPEN"]}</td><td>{r["TAKEN"]}</td>'
            f'<td>{r["DONE"]}</td><td><div class="bar"><div style="width:{pct}%"></div></div> {pct}%</td></tr>'
        )
    return (
        '<table class="lvl"><tr><th>track</th><th>게시글</th><th>OPEN</th>'
        '<th>TAKEN</th><th>DONE</th><th>진행률</th></tr>' + "".join(trs) + "</table>"
    )


def product_composition(posts, large):
    """PBS — Product 구성: DONE 산출물 경로를 중복 제거해 모은다."""
    comp = {}
    for p in posts:
        if p["status"].upper() != "DONE":
            continue
        for d in deliverables(p):
            comp.setdefault(d, []).append((p["finished"], p["id"]))
    items = {}
    for path, hits in sorted(comp.items(), key=lambda kv: (min(kv[1]), kv[0])):
        hits.sort()
        last_f, _ = hits[-1]
        ids = ", ".join(i for _, i in hits[:8]) + (f" 외 {len(hits) - 8}건" if len(hits) > 8 else "")
        li = (
            f'<li><a class="deliv" href="{esc(href(path))}">{esc(path)}</a> '
            f'<span class="meta">← Work {esc(ids)} · 마지막 갱신 {esc(last_f)}</span></li>'
        )
        items.setdefault(os.path.dirname(path) or ".", []).append(li)
    if not large or len(items) <= 2:
        return "<ul>" + "".join(li for g in items.values() for li in g) + "</ul>"
    out = []
    for g in sorted(items):
        out.append(
            f'<details class="gsec"><summary><span class="deliv">{esc(g)}/</span> '
            f'<span class="meta">{len(items[g])}개 파일</span></summary><ul>{"".join(items[g])}</ul></details>'
        )
    return "".join(out)


def timeline_section(posts, large):
    done = sorted(
        (p for p in posts if p["status"].upper() == "DONE" and deliverables(p)),
        key=lambda p: (p["finished"], p["id"]),
    )

    def li(p):
        return (
            f'<li><span class="pid">{esc(p["id"])}</span> '
            + " · ".join(f'<a class="deliv" href="{esc(href(d))}">{esc(d)}</a>' for d in deliverables(p))
            + f' <span class="meta">← {esc(p["title"])} ({esc(p["finished"])})</span></li>'
        )

    if not large:
        return "<ul>" + "".join(li(p) for p in done) + "</ul>"
    groups = {}
    for p in done:
        groups.setdefault(p.get("track", "-"), []).append(p)
    out = []
    for t in sorted(groups):
        out.append(
            f'<details class="gsec"><summary>{esc(t)} <span class="meta">{len(groups[t])}건 '
            f'(마지막 {esc(groups[t][-1]["finished"])})</span></summary>'
            f'<ul>{"".join(li(p) for p in groups[t])}</ul></details>'
        )
    return "".join(out)


def aggregation_warnings(posts, by_id, roots, children):
    """규칙 4절: 부모(취합)의 finished는 모든 자식보다 늦어야 하고, 루트는 전체의 마지막이다.
    DONE 게시글은 산출물 경로가 있어야 한다."""
    warns = []
    for p in posts:
        if p["status"].upper() == "DONE" and not deliverables(p):
            warns.append(f'{p["id"]}가 산출물 경로 없이 DONE이다 — 산출물 없는 Work는 없다(규칙 4절).')
        s, f = parse_dt(p["started"]), parse_dt(p["finished"])
        if s and f and s > f:
            warns.append(f'{p["id"]}의 started({p["started"]})가 finished({p["finished"]})보다 늦다 — 시각 오기입.')
    for pid, kids in children.items():
        parent = by_id[pid]
        p_done = parent["status"].upper() == "DONE"
        pf = parse_dt(parent["finished"])
        for c in kids:
            cf = parse_dt(c["finished"])
            if p_done and c["status"].upper() != "DONE":
                warns.append(f'부모 {pid}가 DONE인데 자식 {c["id"]}가 아직 DONE이 아니다.')
            elif p_done and pf and cf and pf < cf:
                warns.append(
                    f'부모 {pid}의 finished({parent["finished"]})가 자식 {c["id"]}'
                    f'({c["finished"]})보다 이르다 — 재취합해 finished를 갱신해야 한다.'
                )
    all_finished = [parse_dt(p["finished"]) for p in posts if parse_dt(p["finished"])]
    for r in roots:
        rf = parse_dt(r["finished"])
        if r["status"].upper() == "DONE" and rf and all_finished and rf < max(all_finished):
            warns.append(f'루트 {r["id"]}의 finished가 전체 타임라인의 마지막이 아니다.')
    return warns


def rules_version_warning():
    """RULES.md 머리의 '버전:' 줄이 개정 이력의 마지막 항목과 다르면 경고."""
    import re
    try:
        head = (ROOT / "RULES.md").read_text(encoding="utf-8").split("\n\n")[1]
        ver = re.match(r"버전:\s*([\d.]+)", head)
        hist = re.findall(r"v([\d.]+)\s*`", head)
        if ver and hist and ver.group(1) != hist[-1]:
            return [f"RULES.md 버전 줄({ver.group(1)})이 개정 이력의 마지막 항목(v{hist[-1]})과 다르다."]
    except OSError:
        pass
    return []


def main():
    global BOARD, OUT
    args = [a for a in sys.argv[1:] if a != "--ready"]
    ready_only = "--ready" in sys.argv[1:]
    if len(args) > 0:
        BOARD = pathlib.Path(args[0]).resolve()
    if len(args) > 1:
        OUT = pathlib.Path(args[1]).resolve()
    elif len(args) > 0:
        OUT = BOARD.parent / "board.html"
    posts, by_id, roots, children = load_posts()
    if ready_only:
        for p in posts:
            if is_ready(p, by_id):
                print(f'{p["id"]}\t{p.get("track", "-")}\t{p["title"]}')
        return

    large = len(posts) > LARGE
    now = datetime.datetime.now().replace(microsecond=0)
    memo = {}
    counts = {"OPEN": 0, "TAKEN": 0, "DONE": 0}
    for p in posts:
        counts[p["status"].upper()] = counts.get(p["status"].upper(), 0) + 1
    finished = counts.get("OPEN", 0) == 0 and counts.get("TAKEN", 0) == 0 and roots and all(
        r["status"].upper() == "DONE" for r in roots
    )
    if finished:
        state_line = "프로젝트 완료: OPEN·TAKEN 게시글이 없고 루트 게시글이 DONE이다."
    elif counts.get("OPEN", 0) > 0:
        state_line = "진행 중: OPEN 게시글을 집어 계속한다."
    else:
        state_line = f'진행 중: TAKEN 게시글 {counts.get("TAKEN", 0)}건이 끝나기를 기다린다.'
    warns = aggregation_warnings(posts, by_id, roots, children) + rules_version_warning()
    warn_html = (
        '<div class="warnbox"><strong>취합 순서 경고 (규칙 4절)</strong><ul>'
        + "".join(f"<li>{esc(w)}</li>" for w in warns[:50])
        + (f"<li>... 외 {len(warns) - 50}건</li>" if len(warns) > 50 else "")
        + "</ul></div>"
        if warns
        else ""
    )

    ready_ids = [p["id"] for p in posts if is_ready(p, by_id)]
    ready_line = ""
    if ready_ids:
        shown = ", ".join(ready_ids[:20]) + (f" 외 {len(ready_ids) - 20}건" if len(ready_ids) > 20 else "")
        ready_line = f"<br>집기 가능 {len(ready_ids)}건: {esc(shown)}"

    wbs = "".join(wbs_node(r, children, by_id, memo) for r in roots)
    pbs = "".join(pbs_node(r, children, by_id) for r in roots)
    gantt_hier = build_gantt_section(posts, by_id, children, now, memo, roots)
    gantt_track = build_lane_gantt(posts, by_id, now, "track")
    gantt_owner = build_lane_gantt(posts, by_id, now, "owner")
    composition = product_composition(posts, large)
    timeline = timeline_section(posts, large)
    lvl = level_summary(posts, by_id)
    trk = track_summary(posts)

    page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PBS WBS Board — {esc(" · ".join(r["title"] for r in roots) or BOARD.name)}</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem auto; max-width: 62rem;
         padding: 0 1rem; color: #1a1a1a; background: #fff; line-height: 1.6; }}
  h1 {{ font-size: 1.5rem; }} h2 {{ font-size: 1.15rem; margin-top: 2rem;
       border-bottom: 1px solid #ddd; padding-bottom: .3rem; }}
  h3 {{ font-size: .95rem; color: #555; }}
  ul {{ list-style: none; padding-left: 1.2rem; border-left: 1px solid #e5e5e5; }}
  li {{ margin: .35rem 0; }}
  .badge {{ display: inline-block; font-size: .7rem; font-weight: 700;
            padding: .1rem .45rem; border-radius: .6rem; vertical-align: middle; }}
  .badge.open  {{ background: #fde8e8; color: #b42318; }}
  .badge.taken {{ background: #fef4e6; color: #b25e09; }}
  .badge.done  {{ background: #e6f4ea; color: #1e7e34; }}
  .tbadge {{ display: inline-block; font-size: .68rem; font-weight: 600;
             padding: 0 .4rem; border-radius: .5rem; vertical-align: middle; }}
  .ready {{ display: inline-block; font-size: .68rem; font-weight: 700;
            padding: 0 .4rem; border-radius: .5rem; background: #d3e3fd;
            color: #0b57d0; vertical-align: middle; }}
  .prog {{ font-size: .72rem; color: #1e7e34; background: #eef7f0;
           padding: 0 .35rem; border-radius: .5rem; }}
  .pid {{ color: #888; font-family: monospace; }}
  .meta {{ color: #888; font-size: .85rem; }}
  .pending {{ color: #aaa; }}
  .deliv {{ font-family: monospace; }}
  .summary {{ background: #f6f8fa; border: 1px solid #e5e5e5; border-radius: .5rem;
              padding: .8rem 1rem; }}
  .warnbox {{ background: #fdecea; border: 1px solid #f5c6c0; border-radius: .5rem;
              padding: .8rem 1rem; margin-top: 1rem; color: #8a1f11; }}
  .warnbox ul {{ border-left: none; margin: .3rem 0 0; }}
  a {{ color: #0b57d0; text-decoration: none; }} a:hover {{ text-decoration: underline; }}
  table.lvl {{ border-collapse: collapse; font-size: .85rem; margin: .5rem 0; }}
  table.lvl th, table.lvl td {{ border: 1px solid #e5e5e5; padding: .2rem .6rem; text-align: right; }}
  table.lvl th {{ background: #f6f8fa; }} table.lvl td:first-child {{ text-align: left; }}
  .bar {{ display: inline-block; width: 6rem; height: .55rem; background: #eee;
          border-radius: .3rem; vertical-align: middle; overflow: hidden; }}
  .bar div {{ height: 100%; background: #34a853; }}
  details.wbs {{ margin: .15rem 0; }}
  details.wbs > summary {{ cursor: pointer; list-style-position: outside; }}
  .wbs-kids {{ margin-left: 1.1rem; padding-left: .5rem; border-left: 1px solid #e5e5e5; }}
  .wbs-leaf {{ margin: .15rem 0 .15rem 1.1rem; padding-left: .5rem; }}
  details.gsec {{ margin: .4rem 0; border: 1px solid #eee; border-radius: .4rem;
                  padding: .3rem .6rem; }}
  details.gsec > summary {{ cursor: pointer; }}
  details.top {{ margin: 1.6rem 0 0; }}
  details.top > summary {{ cursor: pointer; font-size: 1.15rem; font-weight: 700;
                           border-bottom: 1px solid #ddd; padding-bottom: .3rem; }}
  .gmode {{ margin: .4rem 0 .6rem; }}
  .gmode button {{ font: inherit; font-size: .85rem; padding: .25rem .8rem;
                   border: 1px solid #ccc; background: #f6f8fa; cursor: pointer; }}
  .gmode button:first-child {{ border-radius: .4rem 0 0 .4rem; }}
  .gmode button:last-child {{ border-radius: 0 .4rem .4rem 0; }}
  .gmode button.on {{ background: #0b57d0; color: #fff; border-color: #0b57d0; }}
  .gantt {{ border: 1px solid #e5e5e5; border-radius: .5rem; padding: .6rem .8rem;
            margin: .4rem 0; }}
  .g-row {{ display: flex; align-items: center; gap: .6rem; margin: .3rem 0; }}
  .g-body {{ display: flex; gap: .6rem; align-items: flex-start; }}
  .g-labels {{ flex: 0 0 20rem; }}
  .g-label {{ flex: 0 0 20rem; height: {ROW_H}px; line-height: {ROW_H}px; font-size: .85rem;
              overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .g-area {{ flex: 1; min-width: 0; }}
  .g-chart {{ width: 100%; display: block; background: #f8fafc; border-radius: .3rem; }}
  .g-strip {{ fill: #eef1f5; }}
  .g-bar.done  {{ fill: #34a853; }}
  .g-bar.taken {{ fill: #f9ab00; }}
  .g-bar.open  {{ fill: #d93025; }}
  .g-dep {{ fill: none; stroke: #5f6b7a; stroke-width: 1.3; opacity: .75; }}
  .g-dep-head {{ fill: #5f6b7a; opacity: .85; }}
  .g-axis .g-track {{ background: none; display: flex; justify-content: space-between;
                      font-size: .75rem; color: #888; height: auto; flex: 1; }}
  .legend {{ font-size: .8rem; color: #666; margin-top: .4rem; }}
  .chip {{ display: inline-block; width: .8rem; height: .8rem; border-radius: .2rem;
           vertical-align: -.1rem; }}
</style>
</head>
<body>
<h1>PBS WBS Board <span class="meta">— {esc(" · ".join(r["title"] for r in roots) or BOARD.name)}</span></h1>
<p class="summary">게시글 {len(posts)}건 —
  <span class="badge open">OPEN</span> {counts.get("OPEN", 0)} ·
  <span class="badge taken">TAKEN</span> {counts.get("TAKEN", 0)} ·
  <span class="badge done">DONE</span> {counts.get("DONE", 0)}<br>
  {esc(state_line)}{ready_line}</p>
{warn_html}

<h2>Gantt — Work 시간표 <span class="meta">(겹치는 막대 = 병렬, 화살표 = after 종속성)</span></h2>
<div class="gmode">
  <button data-g="g-track" class="on">모듈별</button>
  <button data-g="g-owner">사람별</button>
  <button data-g="g-hier">계층</button>
</div>
<div id="g-track">{gantt_track}</div>
<div id="g-owner" hidden>{gantt_owner}</div>
<div id="g-hier" hidden>{gantt_hier}</div>
<p class="legend">
  <span class="chip" style="background:#34a853"></span> DONE ·
  <span class="chip" style="background:#f9ab00"></span> TAKEN(진행 중, 현재 시각까지 표시) ·
  화살표는 같은 Gantt 안의 선행만 그린다(밖의 선행은 라벨의 "선행: "으로 표시).
  루트(취합) Work의 막대는 항상 가장 늦게 끝난다.</p>

<details class="top"><summary>레벨·트랙 요약 <span class="meta">(레벨이 깊을수록 가벼운 에이전트 — 규칙 4절)</span></summary>
{lvl}
{trk}
</details>

<details class="top"><summary>WBS — Work 분해 트리 <span class="meta">(부모의 n/m = 하위 DONE/전체)</span></summary>
{wbs}
</details>

<details class="top"><summary>PBS — Product 구성 <span class="meta">(산출물 중복 제거, 그 시점의 Product)</span></summary>
{composition}
<p class="legend">같은 파일을 여러 Work가 갱신해도 한 번만 나타난다 —
일부만 갱신한 Work는 이 목록을 바꾸지 않을 수 있다.</p>
</details>

<details class="top"><summary>PBS — 산출물 분해 트리 (구조로 취합)</summary>
{pbs}
</details>

<details class="top"><summary>산출물 시간 순 목록 (finished 순으로 취합)</summary>
{timeline}
</details>

<script>
document.querySelectorAll('.gmode button').forEach(function (b) {{
  b.addEventListener('click', function () {{
    document.querySelectorAll('.gmode button').forEach(function (x) {{ x.classList.remove('on'); }});
    b.classList.add('on');
    ['g-track', 'g-owner', 'g-hier'].forEach(function (id) {{
      document.getElementById(id).hidden = (id !== b.dataset.g);
    }});
  }});
}});
</script>

<p class="meta">이 페이지는 <code>python3 tools/build_board_view.py
{esc(os.path.relpath(BOARD, ROOT))}</code>가 보드의 게시글에서 생성한다.
규칙은 <a href="{esc(href("RULES.md"))}">RULES.md</a> 참고.</p>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    for w in warns[:20]:
        print(f"경고: {w}")
    if len(warns) > 20:
        print(f"경고 ... 외 {len(warns) - 20}건")
    if ready_ids:
        shown = ", ".join(ready_ids[:20]) + (f" 외 {len(ready_ids) - 20}건" if len(ready_ids) > 20 else "")
        print(f"집기 가능 {len(ready_ids)}건: {shown}")
    print(f"{os.path.relpath(OUT, ROOT)}: 게시글 {len(posts)}건 취합 완료 — {state_line}")


if __name__ == "__main__":
    main()
