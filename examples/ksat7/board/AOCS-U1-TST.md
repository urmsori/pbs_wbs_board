---
id: AOCS-U1-TST
title: AOCS 폐루프(HIL) 시험
status: DONE
parent: M-AOCS
source: -
owner: AOCS-U1-TST-01
deliverable: examples/ksat7/deliverables/AOCS/u1-hil-test.md
after: AOCS-U2-TST, CAL-AOCS-U1
track: AOCS
started: 2026-08-27 02:04:20
finished: 2026-08-27 02:04:20
---

수락시험을 마친 실제 센서·액추에이터(AOCS-U2-TST 실측치)를 하드웨어인루프
(HIL)에 넣고, 형상관리 기준선(CM-AOCS-U1) 제어법칙으로 폐루프 지향정확도·
요 스티어링·안정도를 검사자와 다른 사람(시험)이 검증해 sysreq AOCS 3개
항목을 최종 판정해야 한다.
산출물: examples/ksat7/deliverables/AOCS/u1-hil-test.md — 실측치·sysreq 판정.
검증: sysreq AOCS 판정: 지향0.0183≤0.02°, 요±4.0°, 안정도0.00251≤0.003°/s 전량 PASS
