---
id: 015
title: 규칙 개정 v1.7 — 읽기 전용 집기 가능 조회와 시각 정합 검사
status: DONE
parent: 000
owner: claude
deliverable: RULES.md, tools/build_board_view.py
after: 014
track: -
started: 2026-08-21 01:02
finished: 2026-08-21 01:04
---

웨이브 2 에이전트들의 불편 보고. (1) agent-ait: "집기 가능" 표시가 뷰에
있어도 병렬 운용에서는 뷰 갱신이 취합자 몫이라, 웨이브 중간에 집는
에이전트는 결국 after 게시글 파일들을 하나씩 열어 확인해야 했다 — 뷰 파일을
쓰지 않는 가벼운 조회 명령이 필요하다. (2) agent-eps: 시각을 손으로 옮겨
적다 보니 오기입 여지가 있다 — 도구가 started ≤ finished를 검사해 주면
좋겠다. (3) 웨이브 2에서 RULES.md 버전 줄이 이력과 어긋난 채 배포된 사고의
재발 방지 — 버전 줄과 이력의 최신 항목이 다르면 도구가 경고한다.

산출물: RULES.md v1.7, --ready 옵션과 시각·버전 검사가 추가된
tools/build_board_view.py.
검증: --ready가 파일을 쓰지 않고 목록만 출력함을 확인(집기 가능 0건이면 빈
출력). started>finished인 게시글과 버전 줄 불일치(9.9로 바꿔 재현)가 각각
경고로 잡히고, 정상 상태에서는 경고가 없음을 확인.
