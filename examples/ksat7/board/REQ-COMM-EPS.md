---
id: REQ-COMM-EPS
title: 송신 첨두 전력 허용 요청
status: DONE
parent: M-COMM
source: COMM-U1-DSN
owner: EPS-U1-DSN-01
deliverable: examples/ksat7/deliverables/EPS/comm-tx-power-budget.md
after: -
track: EPS
started: 2026-08-27 01:56:45
finished: 2026-08-27 01:57:26
---

COMM-U1 HPA는 800Mbps 하향 중 첨두 DC 소모가 발생한다. sysreq.md 상
모선 50V±5V, SAR 첨두 펄스 부하 1.8kW(최대 90s/궤도)와 겹치지 않는지,
COMM 송신 첨두전력으로 얼마까지 배정 가능한지 확인이 필요하다.
요청:
1) COMM 송신 채널에 배정 가능한 첨두 DC 전력(W)과 지속시간 제한
2) SAR 펄스 부하와의 동시 발생 금지/허용 여부(버스 예산 상호배제)
3) 모선 전압 50V±5V 리플·과도 규격(HPA 전원단 설계용)
산출물 제안: examples/ksat7/deliverables/EPS/comm-tx-power-budget.md
검증: COMM 첨두60W 배정, 모선리플200mVpp·과도±2%/5ms 회신
