---
id: REQ-AOCS-EPS
title: 반작용휠 첨두 전류 허용
status: DONE
parent: AOCS-01
source: AOCS-01
owner: EPS-DSN-02
deliverable: examples/ksat6/deliverables/EPS/aocs-wheel-current-allowance.md
after: -
track: EPS
started: 2026-08-22 01:25:24
finished: 2026-08-22 01:25:36
---

지향 예산·모드 설계(AOCS-01)의 1차 사이징에서 반작용휠 4기는 모멘텀덤핑·
급기동 시 기당 최대토크 구간에서 순간 첨두전류를 끈다. 이 첨두를 PCDU
반작용휠 채널이 트립 없이 받아줄 수 있는지 EPS 팀에 확인받아야 최종
사이징(AOCS-04)을 확정할 수 있다.
산출물: EPS 팀이 정하는 경로에 반작용휠 채널당 허용 첨두전류(A)·허용 지속
시간(ms)·전류제한(current-limit) 문턱값을 명시해 달라. AOCS 설계값(기당
순간 첨두 약 0.6A, 인러시 ≤1.2A/5ms, 28V±4V 모선 기준)을 참고치로 제공한다.
검증: PCDU AOCS채널 4A 연속/6A·20ms 서지허용으로 AOCS 인러시 4.8A/5ms 트립없이 수용 확인
