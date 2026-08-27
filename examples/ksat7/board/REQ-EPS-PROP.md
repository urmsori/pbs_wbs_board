---
id: REQ-EPS-PROP
title: 홀추력기 300W 운전 프로파일 요청
status: DONE
parent: M-EPS
source: EPS-U1-DSN
owner: PROP-DSN-01
deliverable: examples/ksat7/deliverables/PROP/thruster-operating-profile.md
after: -
track: PROP
started: 2026-08-27 01:52:48
finished: 2026-08-27 01:53:15
---

PCDU 전력예산에서 홀추력기(300W급, Δv25m/s)가 SAR 촬영 버스트(1.8kW/90s)와
동시에 구동되는지 확인해야 한다 — 동시 구동 시 모선 순간부하가 2.1kW를 넘어
50V±5V 조절 범위와 DoD≤30% 여유를 재검토해야 한다. 확인 요청:
1) 궤도당 추력 운전 시간(분)과 듀티, 정상상태 전류(A)
2) SAR 촬영 시간대(궤도상 위치)와 추력 운전 시간대의 중첩 여부(동시운용 정책)
3) 기동 중 전력 램프업/다운 특성(초 단위)
산출물: PROP 팀이 정하는 경로(예: examples/ksat7/deliverables/PROP/)에 위 3항목을
수치로 명시해 달라. 무응답 시 "SAR 촬영과 전기추진은 상호 배타 운용"으로 잠정 가정한다.
검증: SAR-추력 상호배타 운용, 300W/1.0A 정상상태, 램프 3s 확정
