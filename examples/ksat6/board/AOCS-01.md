---
id: AOCS-01
title: 지향 예산·모드 설계
status: DONE
parent: M-AOCS
source: -
owner: AOCS-DSN-01
deliverable: examples/ksat6/deliverables/AOCS/pointing-budget.md
after: -
track: AOCS
started: 2026-08-22 01:23:50
finished: 2026-08-22 01:24:33
---

M-AOCS(자세제어 비행모델 인도)를 쪼개려면 sysreq(지향 0.05°/0.005°/s)를 개별
센서·액추에이터 오차로 배분하는 지향 오차 예산과 임무 모드(획득·정상추적·
모멘텀덤핑·안전모드)를 먼저 정해야 나머지 유닛(별추적기·자이로·반작용휠·
마그네토커·HIL시험)의 개별 수락 기준이 정해진다. AOCS 팀 리드가 자기
지평에서 첫 설계로 발행한다.
산출물: examples/ksat6/deliverables/AOCS/pointing-budget.md — 지향오차 RSS
배분표, 안정도 배분표, 임무모드 정의, 반작용휠/마그네토커 1차 사이징.
검증: RSS 배분 0.031°/0.0024°/s ≤ sysreq 0.05°/0.005°/s, 마진 38%/52%
