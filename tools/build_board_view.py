#!/usr/bin/env python3
"""board/의 게시글을 취합해 WBS/PBS 현황 페이지(board.html)를 만든다.

PBS WBS Board 규칙 5절의 도구. 표준 라이브러리만 사용한다.
사용법: python3 tools/build_board_view.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOARD = ROOT / "board"
OUT = ROOT / "board.html"

STATUS_LABEL = {"OPEN": "OPEN", "TAKEN": "TAKEN", "DONE": "DONE"}


def parse_post(path):
    post = {
        "id": "",
        "title": path.stem,
        "status": "OPEN",
        "parent": "-",
        "owner": "-",
        "deliverable": "-",
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
    return posts, roots, children


def esc(s):
    return html.escape(s, quote=True)


def wbs_node(post, children):
    status = post["status"].upper()
    badge = f'<span class="badge {status.lower()}">{esc(STATUS_LABEL.get(status, status))}</span>'
    owner = f' <span class="meta">담당: {esc(post["owner"])}</span>' if post["owner"] != "-" else ""
    line = (
        f'{badge} <span class="pid">{esc(post["id"])}</span> '
        f'<a href="board/{esc(post["file"])}">{esc(post["title"])}</a>{owner}'
    )
    kids = "".join(wbs_node(c, children) for c in children.get(post["id"], []))
    return f"<li>{line}{f'<ul>{kids}</ul>' if kids else ''}</li>"


def pbs_node(post, children):
    status = post["status"].upper()
    if status == "DONE" and post["deliverable"] != "-":
        item = (
            f'<span class="pid">{esc(post["id"])}</span> '
            f'<a class="deliv" href="{esc(post["deliverable"])}">{esc(post["deliverable"])}</a> '
            f'<span class="meta">← {esc(post["title"])}</span>'
        )
    else:
        item = (
            f'<span class="pid">{esc(post["id"])}</span> '
            f'<span class="pending">(산출물 아직 없음)</span> '
            f'<span class="meta">← {esc(post["title"])}</span>'
        )
    kids = "".join(pbs_node(c, children) for c in children.get(post["id"], []))
    return f"<li>{item}{f'<ul>{kids}</ul>' if kids else ''}</li>"


def main():
    posts, roots, children = load_posts()
    counts = {"OPEN": 0, "TAKEN": 0, "DONE": 0}
    for p in posts:
        counts[p["status"].upper()] = counts.get(p["status"].upper(), 0) + 1
    finished = counts.get("OPEN", 0) == 0 and roots and all(
        r["status"].upper() == "DONE" for r in roots
    )
    state_line = (
        "프로젝트 완료: OPEN 게시글이 없고 루트 게시글이 DONE이다."
        if finished
        else "진행 중: OPEN 게시글을 집어 계속한다."
    )

    wbs = "".join(wbs_node(r, children) for r in roots)
    pbs = "".join(pbs_node(r, children) for r in roots)
    timeline = "".join(
        f'<li><span class="pid">{esc(p["id"])}</span> '
        f'<a class="deliv" href="{esc(p["deliverable"])}">{esc(p["deliverable"])}</a> '
        f'<span class="meta">← {esc(p["title"])}</span></li>'
        for p in posts
        if p["status"].upper() == "DONE" and p["deliverable"] != "-"
    )

    page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PBS WBS Board</title>
<style>
  body {{ font-family: system-ui, sans-serif; margin: 2rem auto; max-width: 60rem;
         padding: 0 1rem; color: #1a1a1a; background: #fff; line-height: 1.6; }}
  h1 {{ font-size: 1.5rem; }} h2 {{ font-size: 1.15rem; margin-top: 2rem;
       border-bottom: 1px solid #ddd; padding-bottom: .3rem; }}
  ul {{ list-style: none; padding-left: 1.2rem; border-left: 1px solid #e5e5e5; }}
  li {{ margin: .35rem 0; }}
  .badge {{ display: inline-block; font-size: .7rem; font-weight: 700;
            padding: .1rem .45rem; border-radius: .6rem; vertical-align: middle; }}
  .badge.open  {{ background: #fde8e8; color: #b42318; }}
  .badge.taken {{ background: #fef4e6; color: #b25e09; }}
  .badge.done  {{ background: #e6f4ea; color: #1e7e34; }}
  .pid {{ color: #888; font-family: monospace; }}
  .meta {{ color: #888; font-size: .85rem; }}
  .pending {{ color: #aaa; }}
  .deliv {{ font-family: monospace; }}
  .summary {{ background: #f6f8fa; border: 1px solid #e5e5e5; border-radius: .5rem;
              padding: .8rem 1rem; }}
  a {{ color: #0b57d0; text-decoration: none; }} a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<h1>PBS WBS Board</h1>
<p class="summary">게시글 {len(posts)}건 —
  <span class="badge open">OPEN</span> {counts.get("OPEN", 0)} ·
  <span class="badge taken">TAKEN</span> {counts.get("TAKEN", 0)} ·
  <span class="badge done">DONE</span> {counts.get("DONE", 0)}<br>
  {esc(state_line)}</p>

<h2>WBS — Work 분해 트리</h2>
<ul>{wbs}</ul>

<h2>PBS — 산출물 분해 트리 (구조로 취합)</h2>
<ul>{pbs}</ul>

<h2>산출물 시간 순 목록 (id 순으로 취합)</h2>
<ul>{timeline}</ul>

<p class="meta">이 페이지는 <code>python3 tools/build_board_view.py</code>가
board/의 게시글에서 생성한다. 규칙은 <a href="RULES.md">RULES.md</a> 참고.</p>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf-8")
    print(f"{OUT.name}: 게시글 {len(posts)}건 취합 완료 — {state_line}")


if __name__ == "__main__":
    main()
