---
id: REQ-COMM-EPS
title: X-band 송신 첨두전력 허용치 확인 요청
status: DONE
parent: C-LB
source: C-LB
owner: EPS-DSN-02
deliverable: examples/ksat6/deliverables/EPS/comm-xtx-power-allowance.md
after: -
track: EPS
started: 2026-08-22 01:23:34
finished: 2026-08-22 01:23:58
---

링크 버짓(C-LB)에서 X-band 송신기(C-XTX)의 RF 출력(잠정 10W)을 정하려면
모선이 허용하는 첨두 송신 부하 상한(28V 버스 기준 첨두전류·듀티)을 EPS
전력예산과 맞춰봐야 한다. EPS 팀에 요청한다.
산출물: EPS 팀이 남기는 문서 — X-band 송신 구간(첨두)에 배정 가능한 전력
상한(W)과 28V 버스 기준 허용 첨두전류(A), PCDU 스위치/퓨즈 정격상 duty
제약(있다면).
검증: PCDU X-band채널 70W/4A 여유 확인, duty10% 가정 하 제약없음
