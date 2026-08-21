#!/usr/bin/env python3
"""보드의 게시글을 취합해 WBS/Gantt/PBS 현황 페이지를 만든다 (v2.9 백지 재설계).

PBS WBS Board 규칙 5절의 도구. 표준 라이브러리만 사용한다.

구조: python은 게시글을 파싱·검사해 JSON으로 페이지에 내장하고,
그리기는 페이지 안의 단일 렌더러(JS)가 한다 — 모드(모듈별/사람별/계층)는
묶음 방식일 뿐 자료는 한 벌이다. 큰 보드도 보이는 행만 그린다(가상화).
시간 눈금 축·행 라벨은 스크롤에 고정, 줌(버튼·핀치·ctrl+휠)·검색·
그룹/서브트리 접기, Work 선택 시 선행·후행 사슬 강조 + 상세 패널.
취합 순서 위반(4절)·산출물 결손(v2.6)은 python이 검사해 경고로 내장한다.

사용법: python3 tools/build_board_view.py [보드 디렉토리] [출력 html] [--ready]
  인자를 생략하면 board/와 board.html (규칙 프로젝트의 보드).
  --ready: 아무 파일도 쓰지 않고 "집기 가능"(OPEN이고 선행 모두 DONE) 게시글
  목록만 출력한다 — 병렬 웨이브 중간에 에이전트가 쓰는 읽기 전용 조회.
  deliverable 경로는 저장소 루트 기준으로 적고, 링크는 출력 위치 기준으로
  계산되므로 보드가 저장소 어디에 있어도 된다.
"""
import datetime
import html
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOARD = ROOT / "board"   # main()에서 인자로 대체될 수 있다
OUT = ROOT / "board.html"

LARGE = 100  # 게시글이 이보다 많으면 기본 접힘을 더 깊게 한다


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
    """형제들 사이의 after 간선으로 위상 정렬 — 행 순서가 시간 논리를 따른다."""
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


def ver_line(body):
    """본문의 마지막 '검증:' 줄 — 상세 패널에 보여줄 정본 한 줄."""
    vs = [ln.strip() for ln in body.splitlines() if ln.strip().startswith("검증:")]
    return vs[-1][:300] if vs else ""


def aggregation_warnings(posts, by_id, roots, children):
    """규칙 4절: 부모(취합)의 finished는 모든 자식보다 늦어야 하고, 루트는 전체의 마지막이다.
    DONE 게시글은 산출물 경로가 있어야 하고 파일이 실제로 있어야 한다(v2.6)."""
    warns = []
    for p in posts:
        if p["status"].upper() == "DONE" and not deliverables(p):
            warns.append(f'{p["id"]}가 산출물 경로 없이 DONE이다 — 산출물 없는 Work는 없다(규칙 4절).')
        elif p["status"].upper() == "DONE":
            for d in deliverables(p):
                if not (ROOT / d).exists():
                    warns.append(f'{p["id"]}의 산출물 파일이 디스크에 없다: {d} (v2.6).')
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


def esc(s):
    return html.escape(s, quote=True)


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
    ready_ids = [p["id"] for p in posts if is_ready(p, by_id)]

    # 자료 한 벌: 계층 DFS 순서(형제는 위상 정렬)를 정본 순서로 내장한다.
    ordered = dfs_order(roots, children)
    seen = {id(q) for q in ordered}
    ordered += [p for p in posts if id(p) not in seen]
    data_posts = []
    for p in ordered:
        st = p["status"].upper()
        data_posts.append({
            "id": p["id"], "t": p["title"], "st": st,
            "pa": p["parent"] if p["parent"] in by_id else "",
            "ow": p["owner"] if p["owner"] != "-" else "",
            "tr": p.get("track", "-") if p.get("track", "-") != "-" else "",
            "af": after_ids(p),
            "s": p["started"] if p["started"] != "-" else "",
            "f": p["finished"] if p["finished"] != "-" else "",
            "dl": deliverables(p), "fi": p["file"],
            "d": depth_of(p, by_id), "rd": is_ready(p, by_id),
            "sub": list(subtree_stats(p, children, memo)) if p["id"] else [1, 1 if st == "DONE" else 0],
            "v": ver_line(p["body"]),
        })
    title = " · ".join(r["title"] for r in roots) or BOARD.name
    meta = {
        "title": title,
        "generated": now.strftime("%Y-%m-%d %H:%M:%S"),
        "counts": counts, "state": state_line, "ready": ready_ids,
        "warnings": warns, "large": len(posts) > LARGE,
        "rootRel": os.path.relpath(ROOT, OUT.parent),
        "boardRel": os.path.relpath(BOARD, OUT.parent),
        "boardArg": os.path.relpath(BOARD, ROOT),
    }
    data = json.dumps({"meta": meta, "posts": data_posts}, ensure_ascii=False)
    data = data.replace("</", "<\\/")

    page = (TEMPLATE
            .replace("@@TITLE@@", esc(title))
            .replace("@@DATA@@", data))
    OUT.write_text(page, encoding="utf-8")
    for w in warns[:20]:
        print(f"경고: {w}")
    if len(warns) > 20:
        print(f"경고 ... 외 {len(warns) - 20}건")
    if ready_ids:
        shown = ", ".join(ready_ids[:20]) + (f" 외 {len(ready_ids) - 20}건" if len(ready_ids) > 20 else "")
        print(f"집기 가능 {len(ready_ids)}건: {shown}")
    print(f"{os.path.relpath(OUT, ROOT)}: 게시글 {len(posts)}건 취합 완료 — {state_line}")


# ── 페이지 틀: 정적 뼈대 + 내장 JSON + 단일 렌더러 ──────────────────────────
TEMPLATE = r"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PBS WBS Board — @@TITLE@@</title>
<style>
:root {
  color-scheme: light;
  --plane:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e;
  --muted:#898781; --grid:#e1e0d9; --axis:#c3c2b7; --ring:rgba(11,11,11,.10);
  --done:#0ca30c; --done-bg:rgba(12,163,12,.16);
  --taken:#c98500; --taken-bg:rgba(250,178,25,.28);
  --wait:#898781;  --ready:#2a78d6; --ready-bg:rgba(42,120,214,.12);
  --crit:#d03b3b;  --crit-bg:rgba(208,59,59,.10);
  --sel:#2a78d6; --stripe:rgba(11,11,11,.027); --chip:rgba(252,252,251,.82);
}
@media (prefers-color-scheme: dark) {
  :root:where(:not([data-theme="light"])) {
    color-scheme: dark;
    --plane:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7;
    --muted:#898781; --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,.10);
    --done:#0ca30c; --done-bg:rgba(12,163,12,.24);
    --taken:#fab219; --taken-bg:rgba(250,178,25,.26);
    --wait:#898781; --ready:#3987e5; --ready-bg:rgba(57,135,229,.20);
    --crit:#d03b3b; --crit-bg:rgba(208,59,59,.22);
    --sel:#3987e5; --stripe:rgba(255,255,255,.03); --chip:rgba(26,26,25,.82);
  }
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --plane:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7;
  --muted:#898781; --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,.10);
  --done:#0ca30c; --done-bg:rgba(12,163,12,.24);
  --taken:#fab219; --taken-bg:rgba(250,178,25,.26);
  --wait:#898781; --ready:#3987e5; --ready-bg:rgba(57,135,229,.20);
  --crit:#d03b3b; --crit-bg:rgba(208,59,59,.22);
  --sel:#3987e5; --stripe:rgba(255,255,255,.03); --chip:rgba(26,26,25,.82);
}
* { box-sizing: border-box; }
body { font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
       margin: 0; padding: 1.2rem 1rem 3rem; color: var(--ink);
       background: var(--plane); line-height: 1.55; }
.wrap { max-width: 74rem; margin: 0 auto; }
h1 { font-size: 1.35rem; margin: .2rem 0 .6rem; }
h1 .meta { font-weight: 400; }
a { color: var(--ready); text-decoration: none; }
a:hover { text-decoration: underline; }
.meta { color: var(--muted); font-size: .85em; }
.pid { color: var(--muted); font-family: ui-monospace, monospace; }
.card { background: var(--surface); border: 1px solid var(--ring);
        border-radius: .6rem; padding: .7rem .9rem; }
#summary { display: flex; flex-wrap: wrap; gap: .4rem 1.2rem; align-items: baseline;
           margin-bottom: .8rem; }
#summary b { font-size: 1.05rem; }
.stat { white-space: nowrap; }
.stat .dot { font-weight: 700; }
#warnbox { border-color: var(--crit); background: var(--crit-bg);
           margin-bottom: .8rem; }
#warnbox summary { cursor: pointer; font-weight: 700; color: var(--crit); }
#warnbox ul { margin: .4rem 0 0; padding-left: 1.2rem; }

/* ── 도구줄 ── */
#toolbar { display: flex; flex-wrap: wrap; gap: .45rem; align-items: center;
           margin: .6rem 0; }
#toolbar .seg { display: inline-flex; }
#toolbar button { font: inherit; font-size: .84rem; padding: .3rem .7rem;
  border: 1px solid var(--axis); background: var(--surface); color: var(--ink);
  cursor: pointer; border-radius: .45rem; }
#toolbar .seg button { border-radius: 0; margin-left: -1px; }
#toolbar .seg button:first-child { border-radius: .45rem 0 0 .45rem; margin-left: 0; }
#toolbar .seg button:last-child { border-radius: 0 .45rem .45rem 0; }
#toolbar button.on { background: var(--sel); border-color: var(--sel); color: #fff; }
#q { font: inherit; font-size: .84rem; padding: .3rem .55rem; width: 13rem;
     border: 1px solid var(--axis); border-radius: .45rem;
     background: var(--surface); color: var(--ink); }

/* ── Gantt ── */
#gscroll { overflow: auto; max-height: 74vh; border: 1px solid var(--ring);
           border-radius: .6rem; background: var(--surface);
           overscroll-behavior-x: contain; touch-action: pan-x pan-y; }
#gcanvas { position: relative; }
#gaxis { position: sticky; top: 0; z-index: 30; height: 34px;
         background: var(--surface); border-bottom: 1px solid var(--axis); }
.tick { position: absolute; bottom: 4px; font-size: .68rem; color: var(--muted);
        font-variant-numeric: tabular-nums; transform: translateX(-50%);
        white-space: nowrap; }
#gcorner { position: sticky; left: 0; z-index: 31; width: var(--labw); height: 100%;
           background: var(--surface); border-right: 1px solid var(--grid);
           font-size: .72rem; color: var(--muted); padding: 8px 8px 0;
           white-space: nowrap; overflow: hidden; }
.gline { position: absolute; top: 34px; bottom: 0; width: 0;
         border-left: 1px solid var(--grid); }
#gnow { position: absolute; top: 34px; bottom: 0; width: 0;
        border-left: 2px dashed var(--taken); opacity: .85; }
.row { position: absolute; left: 0; height: 30px; width: 100%; }
.row.even { background: var(--stripe); }
.row.dim .bar, .row.dim .bt, .row.dim .ghost { opacity: .25; }
.row.dim .lab > * { opacity: .35; } /* 라벨 배경은 불투명하게 유지 — 뒤 막대 이름이 비치지 않게 */
.row.selrow { background: var(--ready-bg); }
.lab { position: sticky; left: 0; z-index: 20; display: inline-block;
       width: var(--labw); height: 100%; background: var(--surface);
       border-right: 1px solid var(--grid); font-size: .76rem; line-height: 30px;
       white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
       padding: 0 6px; cursor: pointer; vertical-align: top; }
.row.even .lab { background: color-mix(in srgb, var(--ink) 3%, var(--surface)); }
.row.selrow .lab { background: color-mix(in srgb, var(--sel) 12%, var(--surface)); }
body.labels-off .lab, body.labels-off #gcorner { display: none; }
.caret { display: inline-block; width: 1em; color: var(--muted); }
.sic { font-weight: 700; }
.sic.done { color: var(--done); } .sic.taken { color: var(--taken); }
.sic.open { color: var(--wait); } .sic.ready { color: var(--ready); }
.bar { position: absolute; top: 7px; height: 16px; border-radius: 4px;
       cursor: pointer; min-width: 3px; }
.bar.done  { background: var(--done-bg);  border: 1.5px solid var(--done); }
.bar.taken { background: var(--taken-bg); border: 1.5px solid var(--taken); }
.bar.group { top: 11px; height: 8px; border-radius: 4px; }
.bar.rollup { cursor: pointer; }
.ghost { position: absolute; top: 7px; height: 16px; border-radius: 8px;
         border: 1.5px dashed var(--wait); color: var(--muted);
         font-size: .68rem; line-height: 13px; padding: 0 8px; cursor: pointer;
         white-space: nowrap; background: var(--surface); }
.ghost.ready { border-color: var(--ready); color: var(--ready);
               border-style: solid; background: var(--ready-bg); }
.bt { position: absolute; top: 50%; transform: translateY(-50%); z-index: 5;
      font-size: .72rem; color: var(--ink); background: var(--chip);
      padding: 0 4px; border-radius: 3px; white-space: nowrap;
      pointer-events: none; }
#garrows { position: absolute; left: 0; top: 0; z-index: 10; pointer-events: none; }
#garrows path { fill: none; stroke: var(--ink2); stroke-width: 1.4; opacity: .8; }
#garrows polygon { fill: var(--ink2); opacity: .9; }
#legend { display: flex; flex-wrap: wrap; gap: .4rem 1.1rem; margin: .5rem 0 0;
          font-size: .78rem; color: var(--ink2); }

/* ── 상세 패널 ── */
#panel { position: fixed; right: 1rem; bottom: 1rem; z-index: 50;
         width: min(26rem, calc(100vw - 2rem)); max-height: 46vh; overflow: auto;
         box-shadow: 0 8px 28px rgba(0,0,0,.25); font-size: .85rem; }
#panel h3 { margin: 0 0 .3rem; font-size: .95rem; }
#panel .x { float: right; cursor: pointer; border: 0; background: none;
            font-size: 1rem; color: var(--muted); }
#panel dl { margin: .3rem 0; display: grid; grid-template-columns: 4.4rem 1fr;
            gap: .12rem .5rem; }
#panel dt { color: var(--muted); } #panel dd { margin: 0; overflow-wrap: anywhere; }
#panel .dep { display: inline-block; margin: 0 .3rem .2rem 0; padding: .05rem .45rem;
              border: 1px solid var(--axis); border-radius: .9rem; cursor: pointer;
              background: var(--surface); color: var(--ink); font: inherit; font-size: .78rem; }

/* ── 아래 섹션 ── */
details.top { margin: 1.3rem 0 0; }
details.top > summary { cursor: pointer; font-size: 1.05rem; font-weight: 700;
  border-bottom: 1px solid var(--axis); padding-bottom: .25rem; }
details.sec { margin: .35rem 0; border: 1px solid var(--ring); border-radius: .45rem;
              padding: .25rem .6rem; background: var(--surface); }
details.sec > summary { cursor: pointer; }
.tree { margin: .15rem 0 .15rem .2rem; }
.tree .node { margin: .12rem 0; }
.tree details { margin: .12rem 0; }
.tree summary { cursor: pointer; }
.tree .kids { margin-left: .95rem; padding-left: .55rem; border-left: 1px solid var(--grid); }
table.lvl { border-collapse: collapse; font-size: .84rem; margin: .5rem 0; }
table.lvl th, table.lvl td { border: 1px solid var(--grid); padding: .18rem .6rem;
  text-align: right; font-variant-numeric: tabular-nums; }
table.lvl th { background: var(--stripe); }
table.lvl td:first-child { text-align: left; }
.pbar { display: inline-block; width: 6rem; height: .5rem; background: var(--grid);
        border-radius: .3rem; vertical-align: middle; overflow: hidden; }
.pbar div { height: 100%; background: var(--done); }
.tb { display: inline-block; font-size: .68rem; font-weight: 600; padding: 0 .4rem;
      border-radius: .45rem; border-left: 3px solid var(--muted);
      background: var(--stripe); vertical-align: middle; }
ul.flat { list-style: none; padding-left: 1rem; border-left: 1px solid var(--grid); }
ul.flat li { margin: .3rem 0; }
.deliv { font-family: ui-monospace, monospace; font-size: .92em; }
footer { margin-top: 2rem; color: var(--muted); font-size: .8rem; }
@media (max-width: 700px) {
  body { padding: .7rem .5rem 3rem; }
  #q { width: 100%; }
  #toolbar button { padding: .45rem .8rem; }
  #gscroll { max-height: 66vh; }
  #panel { left: .5rem; right: .5rem; bottom: .5rem; width: auto; max-height: 42vh; }
  details.top > summary { font-size: .95rem; }
}
</style>
</head>
<body>
<div class="wrap">
<h1>PBS WBS Board <span class="meta">— @@TITLE@@</span></h1>
<div id="summary" class="card"></div>
<details id="warnbox" class="card" hidden></details>

<div id="toolbar">
  <div class="seg" id="modes">
    <button data-m="track" class="on">모듈</button>
    <button data-m="owner">사람</button>
    <button data-m="hier">계층</button>
  </div>
  <input id="q" type="search" placeholder="검색: id · 제목 · 사람 · 트랙">
  <div class="seg">
    <button id="zo" title="줌아웃">−</button>
    <button id="zf" title="전체가 화면에 들어오게">맞춤</button>
    <button id="zi" title="줌인">+</button>
  </div>
  <button id="lt" title="라벨 열 표시/숨김">라벨</button>
  <button id="ar" title="종속성 화살표 (선택 사슬/전체/끄기)">화살표: 선택</button>
  <button id="xp" title="모든 그룹 펼치기/접기">펼침</button>
</div>

<div id="gscroll"><div id="gcanvas">
  <div id="gaxis"><div id="gticks"></div><div id="gcorner"></div></div>
  <div id="ggrid"></div>
  <div id="gnow" hidden></div>
  <div id="grows"></div>
  <svg id="garrows"></svg>
</div></div>
<div id="legend">
  <span><span class="sic open">○</span> OPEN(대기)</span>
  <span><span class="sic ready">◍</span> 집기 가능</span>
  <span><span class="sic taken">◐</span> TAKEN(진행 — 현재 시각까지 표시)</span>
  <span><span class="sic done">●</span> DONE(완료)</span>
  <span>막대 클릭 = 선행·후행 사슬 강조 · 그룹/부모 라벨 클릭 = 접기</span>
  <span>루트(취합) Work는 항상 가장 늦게 끝난다(규칙 4절)</span>
</div>
<div id="panel" class="card" hidden></div>

<details class="top" data-sec="lvl"><summary>레벨·트랙 요약 <span class="meta">(레벨이 깊을수록 가벼운 에이전트 — 규칙 4절)</span></summary><div></div></details>
<details class="top" data-sec="wbs"><summary>WBS — Work 분해 트리 <span class="meta">(부모의 n/m = 하위 DONE/전체)</span></summary><div></div></details>
<details class="top" data-sec="comp"><summary>PBS — Product 구성 <span class="meta">(산출물 중복 제거, 그 시점의 Product)</span></summary><div></div></details>
<details class="top" data-sec="pbs"><summary>PBS — 산출물 분해 트리 (구조로 취합)</summary><div></div></details>
<details class="top" data-sec="tl"><summary>산출물 시간 순 목록 (finished 순으로 취합)</summary><div></div></details>

<footer id="foot"></footer>
</div>
<script id="data" type="application/json">@@DATA@@</script>
<script>
"use strict";
const DATA = JSON.parse(document.getElementById('data').textContent);
const M = DATA.meta, POSTS = DATA.posts;
const byId = new Map(); POSTS.forEach(p => { if (p.id) byId.set(p.id, p); });
const kidsOf = new Map();
POSTS.forEach(p => { if (p.pa && byId.has(p.pa)) {
  if (!kidsOf.has(p.pa)) kidsOf.set(p.pa, []); kidsOf.get(p.pa).push(p); } });
const rootsArr = POSTS.filter(p => !(p.pa && byId.has(p.pa)));
const depOf = new Map(); // 역방향: 이 Work가 끝나기를 기다리는 것들
POSTS.forEach(p => p.af.forEach(a => { if (byId.has(a)) {
  if (!depOf.has(a)) depOf.set(a, []); depOf.get(a).push(p.id); } }));

const ts = s => s ? new Date(s.replace(' ', 'T')).getTime() : null;
const NOW = ts(M.generated);
POSTS.forEach(p => { p._s = ts(p.s); p._f = ts(p.f);
  p._e = p._f != null ? p._f : (p._s != null ? NOW : null); });
let T0 = Infinity, T1 = -Infinity;
POSTS.forEach(p => { if (p._s != null) { T0 = Math.min(T0, p._s); T1 = Math.max(T1, p._e); } });
if (!isFinite(T0)) { T0 = NOW - 3600e3; T1 = NOW; }
if (T1 - T0 < 60e3) T1 = T0 + 60e3;
const SPAN = T1 - T0;

// 트랙 배지: 고정 순서 배정(등장순), 8색을 넘으면 중립 회색(순환 금지)
const CAT = ['#2a78d6','#eb6834','#1baf7a','#eda100','#e87ba4','#008300','#4a3aa7','#e34948'];
const trackColor = new Map();
function tbadge(t) {
  if (!t) return '';
  if (!trackColor.has(t)) trackColor.set(t, trackColor.size < 8 ? CAT[trackColor.size] : '');
  const c = trackColor.get(t);
  const st = c ? ` style="border-left-color:${c};background:${c}1f"` : '';
  return `<span class="tb"${st}>${esc(t)}</span>`;
}
function esc(s) { return String(s).replace(/[&<>"]/g,
  c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function sic(p) {
  const s = p.st === 'DONE' ? ['done','●'] : p.st === 'TAKEN' ? ['taken','◐']
        : p.rd ? ['ready','◍'] : ['open','○'];
  return `<span class="sic ${s[0]}">${s[1]}</span>`;
}
function fmtDur(ms) {
  const m = Math.round(ms / 60e3);
  if (m < 60) return m + '분';
  if (m < 60 * 48) return (m / 60).toFixed(1) + '시간';
  return (m / 1440).toFixed(1) + '일';
}

// ── 상태 ─────────────────────────────────────────────────────────────
const AXH = 34, ROW = 30;
const S = {
  mode: 'track', zoom: 1, q: '', sel: null, arrows: 'sel',
  labelsOn: window.innerWidth > 700,
  collapsed: new Set(), expandedAll: false,
};
// 기본 접힘: 레인 그룹은 전부, 계층은 (큰 보드) 깊이1부터 / (작은 보드) 깊이2부터
function defaultCollapse() {
  const c = new Set();
  POSTS.forEach(p => { if (p.tr) c.add('T:' + p.tr); });
  c.add('T:(트랙 없음)');
  POSTS.forEach(p => { c.add('O:' + (p.ow || '(미배정)')); });
  const lim = M.large ? 1 : 2;
  POSTS.forEach(p => { if (kidsOf.has(p.id) && p.d >= lim) c.add('H:' + p.id); });
  return c;
}
S.collapsed = defaultCollapse();
if (!S.labelsOn) document.body.classList.add('labels-off');

// ── 행 목록 만들기 (모드 = 묶음 방식일 뿐) ───────────────────────────
function laneGroups(keyf, pfx) {
  const groups = new Map();
  POSTS.forEach(p => { const k = keyf(p);
    if (!groups.has(k)) groups.set(k, []); groups.get(k).push(p); });
  return [...groups.entries()].map(([k, items]) => {
    const ss = items.map(p => p._s).filter(x => x != null);
    const ee = items.map(p => p._e).filter(x => x != null);
    return { k, key: pfx + k, items, s: ss.length ? Math.min(...ss) : null,
             e: ee.length ? Math.max(...ee) : null,
             done: items.filter(p => p.st === 'DONE').length };
  }).sort((a, b) => (a.s ?? Infinity) - (b.s ?? Infinity) || (a.k < b.k ? -1 : 1));
}
function buildRows() {
  const q = S.q.trim().toLowerCase();
  if (q) {
    const hit = POSTS.filter(p =>
      (p.id + ' ' + p.t + ' ' + p.ow + ' ' + p.tr).toLowerCase().includes(q));
    return hit.slice(0, 800).map(p => ({ p, depth: 0 }));
  }
  if (S.mode === 'hier') {
    const out = [];
    const walk = (p, depth) => {
      const kids = kidsOf.get(p.id) || [];
      const key = 'H:' + p.id;
      const coll = kids.length > 0 && S.collapsed.has(key);
      out.push({ p, depth, kids: kids.length, collapsed: coll, key });
      if (kids.length && !coll) kids.forEach(k => walk(k, depth + 1));
    };
    rootsArr.forEach(r => walk(r, 0));
    return out;
  }
  const lane = S.mode === 'track'
    ? laneGroups(p => p.tr || '(트랙 없음)', 'T:')
    : laneGroups(p => p.ow || '(미배정)', 'O:');
  const out = [];
  lane.forEach(g => {
    out.push({ group: g, key: g.key, collapsed: S.collapsed.has(g.key) });
    if (!S.collapsed.has(g.key))
      [...g.items].sort((a, b) => (a._s ?? Infinity) - (b._s ?? Infinity)
        || (a.id < b.id ? -1 : 1)).forEach(p => out.push({ p, depth: 1 }));
  });
  return out;
}

// ── 그리기 (보이는 행만) ─────────────────────────────────────────────
const $ = id => document.getElementById(id);
const gscroll = $('gscroll'), gcanvas = $('gcanvas'), grows = $('grows');
let rows = [], rowIdx = new Map();
function labW() {
  return S.labelsOn ? (window.innerWidth > 700 ? 250 : 150) : 0;
}
function chartW() {
  const base = Math.max(gscroll.clientWidth - labW() - 20, 320);
  return base * S.zoom;
}
function xOf(t) { return labW() + (t - T0) / SPAN * chartW(); }

function tickStep(pxPerMs) {
  const steps = [60e3, 300e3, 900e3, 1800e3, 3600e3, 3 * 3600e3, 6 * 3600e3,
                 12 * 3600e3, 86400e3, 2 * 86400e3, 7 * 86400e3, 30 * 86400e3];
  for (const s of steps) if (s * pxPerMs >= 88) return s;
  return steps[steps.length - 1];
}
function layout() {
  rows = buildRows();
  rowIdx = new Map();
  rows.forEach((r, i) => { if (r.p && r.p.id) rowIdx.set(r.p.id, i); });
  gcanvas.style.width = (labW() + chartW()) + 'px';
  gcanvas.style.height = (AXH + rows.length * ROW) + 'px';
  document.documentElement.style.setProperty('--labw', labW() + 'px');
  render();
}
function render() {
  const sl = gscroll.scrollLeft, st = gscroll.scrollTop;
  const vw = gscroll.clientWidth, vh = gscroll.clientHeight;
  // 축 눈금 + 세로 격자 (보이는 범위만)
  const pxPerMs = chartW() / SPAN;
  const step = tickStep(pxPerMs);
  const tA = T0 + Math.max(0, (sl - labW() - 200) / pxPerMs);
  const tB = T0 + (sl + vw + 200) / pxPerMs;
  let ticks = '', glines = '';
  const fmt = step >= 86400e3 ? d => `${d.getMonth() + 1}-${d.getDate()}`
    : step >= 3600e3 ? d => `${d.getMonth() + 1}-${d.getDate()} ${String(d.getHours()).padStart(2,'0')}시`
    : d => `${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`;
  for (let t = Math.ceil((tA - T0) / step) * step + T0; t <= Math.min(tB, T1 + step); t += step) {
    const x = xOf(t);
    if (x < labW() + 34) continue; // 라벨 열 밑에 반쯤 가려지는 눈금은 생략
    ticks += `<div class="tick" style="left:${x}px">${fmt(new Date(t))}</div>`;
    glines += `<div class="gline" style="left:${x}px"></div>`;
  }
  $('gticks').innerHTML = ticks;
  $('ggrid').innerHTML = glines;
  $('gcorner').textContent = `${rows.length}행 · ${M.generated}`;
  // 지금 선
  const anyTaken = POSTS.some(p => p.st === 'TAKEN');
  $('gnow').hidden = !anyTaken;
  if (anyTaken) $('gnow').style.left = xOf(NOW) + 'px';
  // 사슬(선택 강조)
  let chainSet = null;
  if (S.sel) {
    chainSet = new Set([S.sel]);
    const wu = i => { (byId.get(i)?.af || []).forEach(a => {
      if (byId.has(a) && !chainSet.has(a)) { chainSet.add(a); wu(a); } }); };
    const wd = i => { (depOf.get(i) || []).forEach(x => {
      if (!chainSet.has(x)) { chainSet.add(x); wd(x); } }); };
    wu(S.sel); wd(S.sel);
  }
  // 보이는 행만 렌더
  const i0 = Math.max(0, Math.floor((st - AXH) / ROW) - 4);
  const i1 = Math.min(rows.length, Math.ceil((st + vh - AXH) / ROW) + 4);
  let hrows = '';
  for (let i = i0; i < i1; i++) {
    const r = rows[i], y = AXH + i * ROW;
    const even = i % 2 ? ' even' : '';
    if (r.group) {
      const g = r.group;
      const caret = r.collapsed ? '▸' : '▾';
      let bar = '';
      if (g.s != null) {
        const x = xOf(g.s), w = Math.max(xOf(g.e) - x, 3);
        const cls = g.done === g.items.length ? 'done' : 'taken';
        bar = `<div class="bar group rollup ${cls}" data-k="${esc(r.key)}"
          style="left:${x}px;width:${w}px"></div>
          <span class="bt" style="left:${x + w + 6}px">${g.done}/${g.items.length}건</span>`;
      }
      hrows += `<div class="row${even}" style="top:${y}px" data-k="${esc(r.key)}">
        <div class="lab"><span class="caret">${caret}</span>${tbadge(g.k)} <b>${esc(g.k)}</b>
        <span class="meta">${g.done}/${g.items.length}</span></div>${bar}</div>`;
      continue;
    }
    const p = r.p;
    const selCls = S.sel === p.id ? ' selrow' : (chainSet && !chainSet.has(p.id) ? ' dim' : '');
    const pad = 6 + r.depth * 14;
    const caret = r.kids ? `<span class="caret">${r.collapsed ? '▸' : '▾'}</span>` : '';
    const nm = (p.id ? p.id + ' ' : '') + p.t;
    const sub = p.sub && p.sub[0] > 1 ? ` <span class="meta">${p.sub[1]}/${p.sub[0]}</span>` : '';
    const lab = `<div class="lab" style="padding-left:${pad}px" data-id="${esc(p.id)}"
      ${r.kids ? `data-k="H:${esc(p.id)}"` : ''}>${caret}${sic(p)}
      <span class="pid">${esc(p.id)}</span> ${esc(p.t)}${sub}</div>`;
    let cell = '';
    if (p._s != null) {
      const x = xOf(p._s), w = Math.max(xOf(p._e) - x, 3);
      const cls = p.st === 'DONE' ? 'done' : 'taken';
      const grp = (r.kids || (S.mode === 'hier' && kidsOf.has(p.id))) ? ' group' : '';
      cell = `<div class="bar ${cls}${grp}" data-id="${esc(p.id)}"
        style="left:${x}px;width:${w}px"></div>
        <span class="bt" style="left:${x + 4}px">${esc(nm)}</span>`;
    } else {
      const ends = p.af.map(a => byId.get(a)?._e).filter(x => x != null);
      const x = xOf(ends.length ? Math.max(...ends) : NOW);
      const cls = p.rd ? ' ready' : '';
      const word = p.rd ? '집기 가능' : '대기';
      cell = `<div class="ghost${cls}" data-id="${esc(p.id)}"
        style="left:${x}px">${word} · ${esc(nm)}</div>`;
    }
    hrows += `<div class="row${even}${selCls}" style="top:${y}px">${lab}${cell}</div>`;
  }
  grows.innerHTML = hrows;
  renderArrows(chainSet, i0, i1);
}
function renderArrows(chainSet, i0, i1) {
  const svg = $('garrows');
  svg.setAttribute('width', labW() + chartW());
  svg.setAttribute('height', AXH + rows.length * ROW);
  svg.style.width = (labW() + chartW()) + 'px';
  svg.style.height = (AXH + rows.length * ROW) + 'px';
  let edges = [];
  if (S.arrows === 'sel' && S.sel && chainSet) {
    chainSet.forEach(id => { (byId.get(id)?.af || []).forEach(a => {
      if (chainSet.has(a)) edges.push([a, id]); }); });
  } else if (S.arrows === 'all') {
    POSTS.forEach(p => p.af.forEach(a => {
      if (byId.has(a)) edges.push([a, p.id]); }));
    if (edges.length > 900) edges = edges.slice(0, 900);
  }
  let out = '';
  for (const [a, b] of edges) {
    const ia = rowIdx.get(a), ib = rowIdx.get(b);
    const pa = byId.get(a), pb = byId.get(b);
    if (ia == null || ib == null || pa._e == null || pb._s == null) continue;
    const x1 = xOf(pa._e), y1 = AXH + ia * ROW + ROW / 2;
    const x2 = xOf(pb._s), y2 = AXH + ib * ROW + ROW / 2;
    const mx = x1 + 7;
    if (x2 >= x1 + 16)
      out += `<path d="M ${x1} ${y1} H ${mx} V ${y2} H ${x2 - 7}"/>
        <polygon points="${x2},${y2} ${x2 - 7},${y2 - 3.6} ${x2 - 7},${y2 + 3.6}"/>`;
    else
      out += `<path d="M ${x1} ${y1} H ${mx} V ${y2} H ${x2 + 7}"/>
        <polygon points="${x2},${y2} ${x2 + 7},${y2 - 3.6} ${x2 + 7},${y2 + 3.6}"/>`;
  }
  svg.innerHTML = out;
}

// ── 상호작용 ─────────────────────────────────────────────────────────
gscroll.addEventListener('scroll', () => requestAnimationFrame(render));
window.addEventListener('resize', () => requestAnimationFrame(layout));
gcanvas.addEventListener('click', e => {
  const k = e.target.closest('[data-k]');
  const idEl = e.target.closest('[data-id]');
  if (idEl && idEl.dataset.id && !(e.target.closest('.lab') && k)) {
    select(idEl.dataset.id); return;
  }
  if (k) { toggleKey(k.dataset.k); return; }
});
function toggleKey(key) {
  if (S.collapsed.has(key)) S.collapsed.delete(key); else S.collapsed.add(key);
  layout();
}
function select(id) {
  if (!id || S.sel === id) { S.sel = null; $('panel').hidden = true; render(); return; }
  S.sel = id; showPanel(id); render();
}
function showPanel(id) {
  const p = byId.get(id); if (!p) return;
  const word = p.st === 'DONE' ? 'DONE(완료)' : p.st === 'TAKEN' ? 'TAKEN(진행)'
    : p.rd ? 'OPEN — 집기 가능' : 'OPEN(대기)';
  const dur = p._s != null ? `${p.s} → ${p.f || '진행 중'}`
    + (p._e != null ? ` <span class="meta">(${fmtDur(p._e - p._s)})</span>` : '') : '아직 시작 안 함';
  const dls = p.dl.map(d =>
    `<a class="deliv" href="${esc(M.rootRel + '/' + d)}">${esc(d)}</a>`).join('<br>') || '—';
  const depBtn = a => `<button class="dep" data-sel="${esc(a)}">${esc(a)}</button>`;
  const ups = p.af.filter(a => byId.has(a)).map(depBtn).join('') || '—';
  const dns = (depOf.get(id) || []).map(depBtn).join('') || '—';
  $('panel').innerHTML = `
    <button class="x" title="닫기">✕</button>
    <h3>${sic(p)} <span class="pid">${esc(p.id)}</span>
      <a href="${esc(M.boardRel + '/' + p.fi)}">${esc(p.t)}</a></h3>
    <dl>
      <dt>상태</dt><dd>${esc(word)}</dd>
      <dt>트랙</dt><dd>${p.tr ? tbadge(p.tr) + ' ' + esc(p.tr) : '—'}</dd>
      <dt>담당</dt><dd>${esc(p.ow || '—')}</dd>
      <dt>기간</dt><dd>${dur}</dd>
      <dt>산출물</dt><dd>${dls}</dd>
      <dt>선행</dt><dd>${ups}</dd>
      <dt>후행</dt><dd>${dns}</dd>
      ${p.v ? `<dt>검증</dt><dd>${esc(p.v.replace(/^검증:\s*/, ''))}</dd>` : ''}
    </dl>`;
  $('panel').hidden = false;
}
document.getElementById('panel').addEventListener('click', e => {
  if (e.target.classList.contains('x')) { S.sel = null; $('panel').hidden = true; render(); }
  const b = e.target.closest('[data-sel]');
  if (b) { select(b.dataset.sel); scrollToRow(b.dataset.sel); }
});
function scrollToRow(id) {
  const i = rowIdx.get(id);
  if (i == null) return;
  gscroll.scrollTop = Math.max(0, AXH + i * ROW - gscroll.clientHeight / 2);
  const p = byId.get(id);
  if (p && p._s != null)
    gscroll.scrollLeft = Math.max(0, xOf(p._s) - labW() - 60);
}
// 모드·검색·토글
$('modes').addEventListener('click', e => {
  const b = e.target.closest('button[data-m]'); if (!b) return;
  S.mode = b.dataset.m;
  document.querySelectorAll('#modes button').forEach(x =>
    x.classList.toggle('on', x === b));
  layout();
});
$('q').addEventListener('input', () => { S.q = $('q').value; layout(); });
$('lt').addEventListener('click', () => {
  S.labelsOn = !S.labelsOn;
  document.body.classList.toggle('labels-off', !S.labelsOn);
  layout();
});
$('ar').addEventListener('click', () => {
  S.arrows = S.arrows === 'sel' ? 'all' : S.arrows === 'all' ? 'off' : 'sel';
  $('ar').textContent = '화살표: ' + (S.arrows === 'sel' ? '선택' : S.arrows === 'all' ? '전체' : '끄기');
  render();
});
$('xp').addEventListener('click', () => {
  S.expandedAll = !S.expandedAll;
  $('xp').textContent = S.expandedAll ? '접힘' : '펼침';
  S.collapsed = S.expandedAll ? new Set() : defaultCollapse();
  layout();
});
// 줌: 버튼·ctrl+휠·핀치 — 화면 중심(또는 커서)을 고정점으로
function zoomAt(factor, cx) {
  const old = chartW();
  S.zoom = Math.min(Math.max(S.zoom * factor, 1), 400);
  const nw = chartW();
  const px = gscroll.scrollLeft + cx - labW();
  gscroll.scrollLeft += px * (nw / old - 1);
  layout();
}
$('zi').addEventListener('click', () => zoomAt(1.6, gscroll.clientWidth / 2));
$('zo').addEventListener('click', () => zoomAt(1 / 1.6, gscroll.clientWidth / 2));
$('zf').addEventListener('click', () => { S.zoom = 1; layout(); });
gscroll.addEventListener('wheel', e => {
  if (!e.ctrlKey) return;
  e.preventDefault();
  zoomAt(e.deltaY < 0 ? 1.25 : 0.8, e.clientX - gscroll.getBoundingClientRect().left);
}, { passive: false });
let pinch = null;
gscroll.addEventListener('touchstart', e => {
  if (e.touches.length === 2)
    pinch = Math.hypot(e.touches[0].clientX - e.touches[1].clientX,
                       e.touches[0].clientY - e.touches[1].clientY);
});
gscroll.addEventListener('touchmove', e => {
  if (pinch && e.touches.length === 2) {
    e.preventDefault();
    const d = Math.hypot(e.touches[0].clientX - e.touches[1].clientX,
                         e.touches[0].clientY - e.touches[1].clientY);
    const cx = (e.touches[0].clientX + e.touches[1].clientX) / 2
      - gscroll.getBoundingClientRect().left;
    zoomAt(d / pinch, cx); pinch = d;
  }
}, { passive: false });
gscroll.addEventListener('touchend', () => { pinch = null; });

// ── 머리 요약·경고·아래 섹션 (자료에서 그때 만든다) ──────────────────
(function head() {
  const c = M.counts;
  const rd = M.ready.length
    ? `<span class="stat"><span class="sic ready">◍</span> 집기 가능 <b>${M.ready.length}</b></span>` : '';
  $('summary').innerHTML = `
    <span class="stat">게시글 <b>${POSTS.length}</b></span>
    <span class="stat"><span class="sic open">○</span> OPEN <b>${c.OPEN || 0}</b></span>
    <span class="stat"><span class="sic taken">◐</span> TAKEN <b>${c.TAKEN || 0}</b></span>
    <span class="stat"><span class="sic done">●</span> DONE <b>${c.DONE || 0}</b></span>
    <span class="meta">${esc(M.state)}</span>`;
  if (M.warnings.length) {
    const w = $('warnbox');
    w.hidden = false;
    w.innerHTML = `<summary>취합 순서 경고 ${M.warnings.length}건 (규칙 4절)</summary>
      <ul>${M.warnings.slice(0, 80).map(x => `<li>${esc(x)}</li>`).join('')}
      ${M.warnings.length > 80 ? `<li>… 외 ${M.warnings.length - 80}건</li>` : ''}</ul>`;
    if (M.warnings.length <= 6) w.open = true;
  }
  $('foot').innerHTML = `이 페이지는 <code>python3 tools/build_board_view.py
    ${esc(M.boardArg)}</code>가 보드의 게시글에서 생성한다 (${esc(M.generated)}).
    규칙은 <a href="${esc(M.rootRel)}/RULES.md">RULES.md</a> 참고.`;
})();
function postLine(p) {
  const own = p.ow ? ` <span class="meta">담당: ${esc(p.ow)}</span>` : '';
  const sub = p.sub && p.sub[0] > 1 ? ` <span class="meta">${p.sub[1]}/${p.sub[0]}</span>` : '';
  return `${sic(p)} <span class="pid">${esc(p.id)}</span> ${p.tr ? tbadge(p.tr) : ''}
    <a href="${esc(M.boardRel + '/' + p.fi)}">${esc(p.t)}</a>${sub}${own}`;
}
function wbsTree(p, depth) {
  const kids = kidsOf.get(p.id) || [];
  if (!kids.length) return `<div class="node">${postLine(p)}</div>`;
  return `<details${depth < 2 ? ' open' : ''}><summary>${postLine(p)}</summary>
    <div class="kids">${kids.map(k => wbsTree(k, depth + 1)).join('')}</div></details>`;
}
function pbsTree(p, depth) {
  const links = p.st === 'DONE' && p.dl.length
    ? p.dl.map(d => `<a class="deliv" href="${esc(M.rootRel + '/' + d)}">${esc(d)}</a>`).join(' · ')
    : '<span class="meta">(산출물 아직 없음)</span>';
  const line = `<span class="pid">${esc(p.id)}</span> ${links}
    <span class="meta">← ${esc(p.t)}</span>`;
  const kids = kidsOf.get(p.id) || [];
  if (!kids.length) return `<div class="node">${line}</div>`;
  return `<details${depth < 2 ? ' open' : ''}><summary>${line}</summary>
    <div class="kids">${kids.map(k => pbsTree(k, depth + 1)).join('')}</div></details>`;
}
function sumTable(keyf, name) {
  const rowsM = new Map();
  POSTS.forEach(p => { const k = keyf(p);
    if (!rowsM.has(k)) rowsM.set(k, { OPEN: 0, TAKEN: 0, DONE: 0 });
    rowsM.get(k)[p.st]++; });
  if (rowsM.size > 40) return '';
  const trs = [...rowsM.entries()].sort((a, b) => a[0] < b[0] ? -1 : 1).map(([k, r]) => {
    const n = r.OPEN + r.TAKEN + r.DONE, pct = n ? Math.floor(r.DONE * 100 / n) : 0;
    return `<tr><td>${esc(String(k))}</td><td>${n}</td><td>${r.OPEN}</td>
      <td>${r.TAKEN}</td><td>${r.DONE}</td>
      <td><span class="pbar"><div style="width:${pct}%"></div></span> ${pct}%</td></tr>`;
  }).join('');
  return `<table class="lvl"><tr><th>${name}</th><th>게시글</th><th>OPEN</th>
    <th>TAKEN</th><th>DONE</th><th>진행률</th></tr>${trs}</table>`;
}
function buildSection(sec) {
  if (sec === 'lvl')
    return sumTable(p => 'L' + p.d, '레벨') + sumTable(p => p.tr || '-', 'track');
  if (sec === 'wbs')
    return `<div class="tree">${rootsArr.map(r => wbsTree(r, 0)).join('')}</div>`;
  if (sec === 'pbs')
    return `<div class="tree">${rootsArr.map(r => pbsTree(r, 0)).join('')}</div>`;
  if (sec === 'comp') {
    const comp = new Map();
    POSTS.forEach(p => { if (p.st !== 'DONE') return;
      p.dl.forEach(d => { if (!comp.has(d)) comp.set(d, []);
        comp.get(d).push([p.f, p.id]); }); });
    const dirs = new Map();
    [...comp.entries()].sort().forEach(([path, hits]) => {
      hits.sort();
      const ids = hits.slice(0, 8).map(h => h[1]).join(', ')
        + (hits.length > 8 ? ` 외 ${hits.length - 8}건` : '');
      const li = `<li><a class="deliv" href="${esc(M.rootRel + '/' + path)}">${esc(path)}</a>
        <span class="meta">← Work ${esc(ids)} · 마지막 갱신 ${esc(hits[hits.length - 1][0])}</span></li>`;
      const dir = path.includes('/') ? path.slice(0, path.lastIndexOf('/')) : '.';
      if (!dirs.has(dir)) dirs.set(dir, []); dirs.get(dir).push(li);
    });
    const note = `<p class="meta">같은 파일을 여러 Work가 갱신해도 한 번만 나타난다 —
      일부만 갱신한 Work는 이 목록을 바꾸지 않을 수 있다.</p>`;
    if (!M.large || dirs.size <= 2)
      return `<ul class="flat">${[...dirs.values()].flat().join('')}</ul>` + note;
    return [...dirs.entries()].sort().map(([d, lis]) =>
      `<details class="sec"><summary><span class="deliv">${esc(d)}/</span>
        <span class="meta">${lis.length}개 파일</span></summary>
        <ul class="flat">${lis.join('')}</ul></details>`).join('') + note;
  }
  if (sec === 'tl') {
    const done = POSTS.filter(p => p.st === 'DONE' && p.dl.length)
      .sort((a, b) => (a.f + a.id) < (b.f + b.id) ? -1 : 1);
    const li = p => `<li><span class="pid">${esc(p.id)}</span>
      ${p.dl.map(d => `<a class="deliv" href="${esc(M.rootRel + '/' + d)}">${esc(d)}</a>`).join(' · ')}
      <span class="meta">← ${esc(p.t)} (${esc(p.f)})</span></li>`;
    if (!M.large) return `<ul class="flat">${done.map(li).join('')}</ul>`;
    const g = new Map();
    done.forEach(p => { const k = p.tr || '-';
      if (!g.has(k)) g.set(k, []); g.get(k).push(p); });
    return [...g.entries()].sort().map(([k, ps]) =>
      `<details class="sec"><summary>${esc(k)} <span class="meta">${ps.length}건
        (마지막 ${esc(ps[ps.length - 1].f)})</span></summary>
        <ul class="flat">${ps.map(li).join('')}</ul></details>`).join('');
  }
  return '';
}
document.querySelectorAll('details.top[data-sec]').forEach(d => {
  d.addEventListener('toggle', () => {
    if (d.open && !d.dataset.built) {
      d.querySelector('div').innerHTML = buildSection(d.dataset.sec);
      d.dataset.built = '1';
    }
  });
});

layout();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
