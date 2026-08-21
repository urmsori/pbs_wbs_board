---
id: 018
title: 규칙 개정 v2.0 — 대용량 보드 뷰 (2,000건 이상)
status: DONE
parent: 000
owner: claude
deliverable: RULES.md, tools/build_board_view.py
after: 017
track: -
started: 2026-08-21 01:17
finished: 2026-08-21 01:27
---

불편: 실제 위성 개발 규모의 보드(게시글 2,000건 이상, 5레벨)를 지금 뷰로
열면 WBS가 한 화면에 수천 줄로 펼쳐지고, Gantt는 수천 행 SVG 하나가 되어
아무것도 읽을 수 없다. 큰 보드에서는 요약이 기본이고 상세는 접혀 있어야
한다.

산출물: RULES.md v2.0(5절 대용량 뷰 규정), tools/build_board_view.py —
게시글 100건 초과 보드에서: 레벨×상태 요약표와 트랙 요약표, 접히는
WBS/PBS 트리(부모마다 하위 진행률 n/m), 요약 Gantt(레벨 2까지) +
서브트리별 상세 Gantt(접힘), 디렉토리로 묶인 PBS Product 구성, 트랙별로
묶인 시간 순 목록, "집기 가능" 목록의 상한 표시.
검증: 게시글 2,190건의 satellite-full 보드로 실측 — 생성 0.21초, HTML 1.1MB.
접힌 WBS가 화면에서 ~30줄로 요약되고, 요약 Gantt(레벨 2)와 서브트리별 상세
Gantt 24개(접힘), 레벨×상태·트랙 요약표, 집기 가능 48건 상한 표시를 스크린샷
으로 확인. 형제 위상 정렬로 행 순서가 EM→QM→FM 시간 논리를 따름을 확인.
작은 보드 2개(규칙·satellite)는 기존과 동일하게 렌더링된다.
