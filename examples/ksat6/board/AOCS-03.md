---
id: AOCS-03
title: 자이로(IMU) 수락
status: DONE
parent: M-AOCS
source: -
owner: AOCS-IMU-01
deliverable: examples/ksat6/deliverables/AOCS/gyro-accept.md
after: AOCS-01
track: AOCS
started: 2026-08-22 01:24:38
finished: 2026-08-22 01:25:18
---

지향오차·안정도 예산(AOCS-01)에서 자이로(IMU)에 배분된 각속도 잡음(ARW)·
전파오차 예산을 만족하는 장비를 수령·수락시험해야 한다. 예산 배분이
먼저 확정되어야(after=AOCS-01) 수락 판정 기준이 정해진다.
산출물: examples/ksat6/deliverables/AOCS/gyro-accept.md — ARW·바이어스 안정도
실측치, 배분 예산 대비 판정.
검증: ARW 0.0009 ≤ 0.0010, 전파오차 0.008 ≤ 0.010 PASS
