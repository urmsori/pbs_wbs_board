---
id: 007
title: 규칙 개정 v1.2 — 취합 Work는 마지막에 끝난다, Gantt 종속성 화살표
status: DONE
parent: 000
owner: claude
deliverable: RULES.md
after: 006
started: 2026-08-21 00:29
finished: 2026-08-21 00:32
---

불편 두 가지. (1) 개정 006이 00:20에 끝났는데 루트 게시글 000의 finished가
00:06에 머물러, 최종 Work(규칙 자체)가 타임라인 중간에 있었다. 취합 Work는
자식보다 늦게 끝나야 최종 산출물이 시간상 항상 마지막에 온다. (2) Gantt에서
after 종속성이 "선행: NNN" 텍스트로만 보여 Work 간 선후 관계가 눈에 들어오지
않았다.

산출물: RULES.md v1.2(취합 마감 규칙, Gantt 종속성 표시 규칙),
tools/build_board_view.py(종속성 화살표, 취합 순서 검증), 갱신된
board.html·VALIDATION.md, 재취합된 board/000.
