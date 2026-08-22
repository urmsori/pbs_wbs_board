---
id: AOCS-06
title: AOCS 폐루프(HIL) 시험
status: DONE
parent: M-AOCS
source: -
owner: AOCS-HIL-01
deliverable: examples/ksat6/deliverables/AOCS/hil-test.md
after: AOCS-02, AOCS-03, AOCS-04, AOCS-05
track: AOCS
started: 2026-08-22 01:25:24
finished: 2026-08-22 01:27:07
---

개별 수락(별추적기·자이로·반작용휠·마그네토커)이 모두 끝나야 그 실측
장비 모델을 넣어 AOCS 하드웨어인루프(HIL) 폐루프 시험으로 sysreq 지향
0.05°(3σ)·안정도 0.005°/s(노출시간 중) 충족을 검증할 수 있다. 비행 SW
(FSW-AOCS) 통합 검증은 별도로 INT 단계에서 수행하며, 이 시험은 대표
제어법칙 모델로 AOCS 하드웨어 체인 자체를 검증한다.
산출물: examples/ksat6/deliverables/AOCS/hil-test.md — 폐루프 지향정확도·
안정도 실측 결과, sysreq 판정.
검증: 실측 0.034°/0.0028°/s ≤ 0.05°/0.005°/s PASS
