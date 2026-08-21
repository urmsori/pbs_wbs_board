---
id: 024
title: 규칙 개정 v2.6 — 산출물 파일 존재 검사 (없는 파일로 DONE 금지)
status: DONE
parent: 000
owner: claude
deliverable: tools/post.py, tools/build_board_view.py, RULES.md
after: 023
track: -
started: 2026-08-21 04:26:00
finished: 2026-08-21 04:14:11
---

K-SAT 4 EM 통합시험(E-AIT-1)의 실발견: STR 게시글 14건이 **디스크에 없는
파일**을 deliverable로 적고 DONE 상태였다(오탈자 경로·템플릿 잔여 텍스트).
"경로가 없으면 DONE이 아니다"(4절)는 규칙이 있었지만 도구가 **문자열만 보고
파일 존재를 검사하지 않아** 위반이 통과됐다. NCR-01로 소급 보완했으나,
같은 사고는 도구가 막는 것이 맞다.

산출물: tools/post.py — done 시 deliverable의 각 경로가 실제로 존재하는지
검사(없으면 거부), tools/build_board_view.py — DONE 게시글의 산출물 파일이
없으면 경고. RULES.md v2.6(4절 한 줄).
검증: 없는 경로 done 거부·실존 경로 통과·뷰 경고를 시험으로 확인, K-SAT 4 보드 경고 0 확인
