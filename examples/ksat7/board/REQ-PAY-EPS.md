---
id: REQ-PAY-EPS
title: 1.8kW 펄스 전력 공급 확약(파형 합의) 요청
status: DONE
parent: M-PAY
source: PAY-U2-DSN
owner: EPS-U1-DSN-01
deliverable: examples/ksat7/deliverables/EPS/pay-pulse-confirmation.md
after: -
track: EPS
started: 2026-08-27 01:56:45
finished: 2026-08-27 01:57:26
---

송수신기·펄스발생기 설계(PAY-U2-DSN)가 정한 파형(첨두 DC 1.8kW, 버스트 5s×최대
18회/궤도, 듀티 6%, 상승/하강 <1ms 트래피조이드)을 모선(50V±5V)이 실제로 공급할 수
있는지 EPS 확약이 필요하다. sysreq EPS 항목의 슈퍼커패시터/배터리 하이브리드가
이 버스트 구조를 DoD ≤30% 이내에서 반복 방전할 수 있는지 확인 바란다.
산출물: EPS 팀이 남기는 문서 — 파형 수용 확약(가능/조건부/불가), 조건부라면 버스트
구조 제약(최대 버스트 길이·간격), 모선 전압 강하(펄스 중) 예측치.
검증: 5s×18회/궤도, 듀티6%, DoD≤30% 조건에서 공급 가능 확약 회신
검증: 5s×18회/궤도 파형 조건부(간격≥20s) 공급 가능, 전압강하-3.6%(규격내)
