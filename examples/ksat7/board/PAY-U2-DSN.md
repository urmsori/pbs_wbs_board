---
id: PAY-U2-DSN
title: 송수신기·펄스발생기 설계
status: DONE
parent: M-PAY
source: -
owner: PAY-U2-DSN-01
deliverable: examples/ksat7/deliverables/PAY/u2-transceiver-design.md
after: -
track: PAY
started: 2026-08-27 01:51:04
finished: 2026-08-27 01:51:52
---

M-PAY를 쪼개려면 안테나 개구(PAY-U1-DSN)에 급전하는 송수신기·펄스발생기의
파형(첨두전력·펄스폭·PRF·듀티)과 NESZ 예산을 먼저 확정해야 제작·시험 유닛과
타 트랙(EPS 전력파형 확약, HAR 대전류 배선, TCS 열관리) 인터페이스가 정해진다.
sysreq 첨두 펄스 1.8kW·최대 90s/궤도, NESZ≤-19dB를 배분한다.
산출물: examples/ksat7/deliverables/PAY/u2-transceiver-design.md — 파형 정의,
전력계통 요구(EPS), 배선 요구(HAR), 열손실 요구(TCS), NESZ 예산표.
검증: 첨두DC1.8kW·듀티6%·버스트90s/궤도 정합, NESZ설계목표-20dB(마진1dB)
