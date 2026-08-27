---
id: AOCS-U1-DSN
title: 안테나 지향 제어계 설계
status: DONE
parent: M-AOCS
source: -
owner: AOCS-DSN-01
deliverable: examples/ksat8/deliverables/AOCS/u1-dsn.md
after: -
track: AOCS
started: 2026-08-27 03:52:34
finished: 2026-08-27 03:52:34
---

M-AOCS(안테나 지향 0.05° 3σ, 모멘텀 휠+이온추력기 언로딩) 인도를 위해 지향오차
예산·제어대역폭·센서/휠 1차 사이징을 먼저 설계해야 뒤이은 해석·검토·수락시험
유닛의 판정 기준이 정해진다. SA 1차모드(REQ-AOCS-SA-모드 회신)와 PROP 언로딩
인터페이스(REQ-AOCS-PROP-언로딩 회신)를 반영한다. STR 정렬 기준(REQ-AOCS-STR-정렬)은
8x20초 회신 대기 초과로 잠정치 사용 — 정식 회신 도착 시 정정.
검증: 지향오차 RSS 배분 ≤0.05°, 제어대역폭이 SA 1차모드 대비 5배 이상 이격
검증: 지향오차RSS 123.1arcsec(0.0342°)≤0.05°(마진31.6%), 대역폭0.02Hz(SA모드대비6.0배 이격) — STR정렬 잠정치(정정예정)
