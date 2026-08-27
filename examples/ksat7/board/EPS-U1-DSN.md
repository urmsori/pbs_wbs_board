---
id: EPS-U1-DSN
title: PCDU·펄스전력부(슈퍼캡 하이브리드) 설계
status: DONE
parent: M-EPS
source: -
owner: EPS-U1-DSN-01
deliverable: examples/ksat7/deliverables/EPS/pcdu-pulse-design.md
after: -
track: EPS
started: 2026-08-27 01:50:21
finished: 2026-08-27 01:55:31
---

M-EPS 인도를 위해 SAR 첨두 1.8kW 버스트(sysreq: 최대90s/궤도)를 배터리 DoD≤30%
이내로 흡수하려면 PCDU를 슈퍼커패시터·배터리 하이브리드 방전 회로로 설계해야
한다. 모선 50V±5V 조절, 슈퍼캡뱅크가 버스트 첨두를 분담하고 배터리는 완만한
방전으로 DoD를 억제하는 구조. PAY 실제 펄스 파형·듀티(REQ-EPS-PAY)와 PROP
홀추력기 300W 운전 프로파일(REQ-EPS-PROP, 동시부하 여부)이 필요해 협상한다.
검증: 모선50V±5V·1.8kW/90s 버스트 하이브리드 아키텍처 확정, PROP 동시부하 배제, PAY 파형 잠정치(리스크 기록)
