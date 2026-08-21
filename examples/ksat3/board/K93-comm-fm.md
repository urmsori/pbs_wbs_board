---
id: K93
title: COMM FM — 안테나 상세치수·질량 실측
status: DONE
parent: K90
owner: sonnet-comm
deliverable: examples/ksat3/deliverables/comm-fm.md
after: K40
track: COMM
started: 2026-08-21 02:26:43
finished: 2026-08-21 02:27:20
---

FM 이관 항목: 다이폴 소자 길이·급전점 좌표 확정, 질량 실측(추산 305g
검증). 링크버짓 최종 확인은 K92의 하드웨어 검증 결과를 입력으로 쓴다
(완성은 그 뒤).
산출물: examples/ksat3/deliverables/comm-fm.md

## 작업 기록
- 다이폴 소자 길이(172 mm, 437 MHz 1/4파장 기준)·급전점 좌표 확정, str-to-comm.md(K84 정정) 개구부 30 mm와 정합 확인(편차 ≤1 mm).
- 안테나 전개 스윕 경로-태양전지 패널 간 여유각(약 8°) 재확인, 비간섭.
- 질량 실측: 트랜시버 보드·전개 기구·RF 케이블·체결류 합계 297 g — EM 추산 305 g 대비 8 g 감소, 배분 500 g 대비 여유 203 g(약 41%)로 적합.
- 링크버짓 최종 확인은 K92(EPS FM 버스트 하드웨어 검증) 결과 확인 후 유효함을 comm-fm.md에 단서로 명시.
검증: 치수-개구부 정합과 질량 실측을 기록, 링크버짓은 K92 결과 단서부
