---
id: AOCS-U1-DSN
title: 요 스티어링 제어계 설계
status: DONE
parent: M-AOCS
source: -
owner: AOCS-U1-DSN-01
deliverable: examples/ksat7/deliverables/AOCS/u1-yaw-steering-design.md
after: -
track: AOCS
started: 2026-08-27 01:50:56
finished: 2026-08-27 01:51:51
---

M-AOCS(SAR 지향 0.02°, 요 스티어링 ±4°)를 쪼개려면 SAR 지구자전 보상용 요
스티어링 제어법칙(제어대역폭·게인·센서/액추에이터 배분)을 먼저 설계해야
뒤이은 해석·검토·수락시험 유닛의 판정 기준이 정해진다. AOCS 팀 리드가 자기
지평에서 첫 설계로 발행한다. SAR 안테나가 강체가 아니라 전개형 구조이므로
제어대역이 안테나 1차모드를 침범하지 않는지 STR 확인이 필요하다(→REQ-AOCS-STR).
산출물: examples/ksat7/deliverables/AOCS/u1-yaw-steering-design.md — 지향오차
RSS 배분, 요 스티어링 프로파일, 제어대역폭 목표, 센서·액추에이터 1차 사이징.
검증: RSS배분0.0197°≤0.02°(마진1.5%), 요±4.0°, 안정도목표0.0026°≤0.003°/s
