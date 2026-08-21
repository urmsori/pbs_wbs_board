#!/usr/bin/env python3
"""게시글 상태 전환 소도구 (규칙 v1.9, 3절).

에이전트들이 date 실행과 frontmatter 손 편집을 반복하다 오기입하는 불편을
없앤다. 시각은 초 단위로 자동 기록되고, 규칙 위반(선행 미완, 상태 순서
위반)은 거부된다. 손 편집도 여전히 유효하다 — 이 도구는 지름길일 뿐이다.

사용법:
  python3 tools/post.py take  <게시글.md> <owner>
  python3 tools/post.py done  <게시글.md> <산출물경로[,경로2...]> [검증 한 줄]
  python3 tools/post.py ready <보드 디렉토리>
"""
import datetime
import pathlib
import re
import sys


def field(text, key):
    m = re.search(rf"^{key}:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def set_field(text, key, value):
    return re.sub(rf"^{key}:.*$", f"{key}: {value}", text, count=1, flags=re.M)


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_by_id(board, pid):
    """게시글 파일명은 <id>-제목.md 이므로 글롭으로 후보를 좁히되,
    계층 id(QM-STR-BR)가 잎 id(QM-STR-BR-01)의 접두어일 수 있으므로
    frontmatter의 id가 정확히 일치하는 파일만 채택한다(v2.2)."""
    exact = board / f"{pid}.md"
    candidates = ([exact] if exact.exists() else []) + sorted(board.glob(f"{pid}-*.md"))
    for hit in candidates:
        if field(hit.read_text(encoding="utf-8"), "id") == pid:
            return hit
    return None


def take(path, owner):
    p = pathlib.Path(path)
    t = p.read_text(encoding="utf-8")
    if field(t, "status") != "OPEN":
        sys.exit(f"거부: {p.name}의 status가 OPEN이 아니다({field(t, 'status')}).")
    after = field(t, "after")
    if after and after != "-":
        for a in [x.strip() for x in after.split(",") if x.strip()]:
            dep = find_by_id(p.parent, a)
            if dep is None:
                sys.exit(f"거부: 선행 {a} 게시글을 찾을 수 없다.")
            if field(dep.read_text(encoding="utf-8"), "status") != "DONE":
                sys.exit(f"거부: 선행 {a}가 아직 DONE이 아니다.")
    t = set_field(t, "status", "TAKEN")
    t = set_field(t, "owner", owner)
    t = set_field(t, "started", now())
    p.write_text(t, encoding="utf-8")
    print(f"TAKEN {field(t, 'id')} (owner: {owner})")


def done(path, deliverable, verify=None):
    p = pathlib.Path(path)
    t = p.read_text(encoding="utf-8")
    if field(t, "status") != "TAKEN":
        sys.exit(f"거부: {p.name}의 status가 TAKEN이 아니다({field(t, 'status')}).")
    if not deliverable or deliverable == "-":
        sys.exit("거부: 산출물 경로가 없다 — 산출물 없는 Work는 없다(규칙 4절).")
    t = set_field(t, "status", "DONE")
    t = set_field(t, "deliverable", deliverable)
    t = set_field(t, "finished", now())
    if verify:
        t = t.rstrip() + f"\n검증: {verify}\n"
    p.write_text(t, encoding="utf-8")
    print(f"DONE {field(t, 'id')} → {deliverable}")


def ready(board):
    board = pathlib.Path(board)
    posts = {}
    for f in sorted(board.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        posts[field(t, "id")] = (field(t, "status"), field(t, "after"), field(t, "title"), field(t, "track"))
    try:
        for pid, (status, after, title, track) in posts.items():
            if status != "OPEN":
                continue
            deps = [] if after in ("", "-") else [x.strip() for x in after.split(",") if x.strip()]
            if all(posts.get(d, ("",))[0] == "DONE" for d in deps):
                print(f"{pid}\t{track}\t{title}")
    except BrokenPipeError:  # head 등으로 잘라 읽을 때 정상 종료
        sys.stderr.close()


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "take" and len(sys.argv) >= 4:
        take(sys.argv[2], sys.argv[3])
    elif cmd == "done" and len(sys.argv) >= 4:
        done(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    elif cmd == "ready":
        ready(sys.argv[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
