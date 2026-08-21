---
id: 012
title: 규칙 개정 v1.4 — 프로젝트마다 보드 하나 (다중 보드)
status: DONE
parent: 000
owner: claude
deliverable: RULES.md, tools/build_board_view.py
after: 008
started: 2026-08-21 00:50
finished: 2026-08-21 00:52
---

불편: 인공위성 예시 프로젝트를 이 규칙으로 시작하려는데, 규칙이 Board를 이
저장소의 board/ 디렉토리 하나로 고정하고 있고(1절), 게시글 id도 3자리
일련번호로만 정하고 있어(3절) 두 번째 Product를 올릴 곳이 없다. 도구도
board/와 board.html 경로가 하드코딩되어 있다.

산출물: RULES.md v1.4(프로젝트마다 보드 디렉토리 하나, id는 보드 안에서
유일하면 되고 접두어 허용), 보드·출력 경로를 인자로 받고 링크를 출력 위치
기준으로 계산하는 tools/build_board_view.py.
검증: 인자 없이 실행하면 기존과 동일하게 board.html이 생성되고, 다른 위치의
보드 디렉토리를 인자로 주면 그 옆에 board.html이 생성되며 RULES.md 링크가
출력 위치 기준 상대 경로로 계산됨을 확인했다.
