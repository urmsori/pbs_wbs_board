---
id: EPS-01
title: EPS 전력예산·아키텍처 설계
status: DONE
parent: M-EPS
source: -
owner: EPS-DSN-01
deliverable: examples/ksat6/deliverables/EPS/power-budget.md
after: -
track: EPS
started: 2026-08-22 01:19:36
finished: 2026-08-22 01:21:52
---

M-EPS 인도를 위해 먼저 모선 아키텍처(28V±4V 조절모선, PCDU 직접에너지전달)와
서브시스템별 전력 할당표를 정해야 PCDU·배터리 용량을 뒤이어 설계할 수 있다.
산출물: examples/ksat6/deliverables/EPS/power-budget.md — 서브시스템별 평균/첨두
할당과 배터리 용량 산출 근거.
검증: sysreq EPS 항목(28V±4V·155W·DoD≤25%) 인용 판정, 평균111W/첨두151W ≤155W(충족, AOCS·COMM·PAY 3건은 가정치로 EPS-04 재검증 예정)
