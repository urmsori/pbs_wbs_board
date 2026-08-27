---
id: HAR-U1-DSN-01
title: 100V 전력 하니스 설계
status: DONE
parent: M-HAR
source: -
owner: HAR-DSN-01
deliverable: examples/ksat8/deliverables/HAR/u1-design.md
after: -
track: HAR
started: 2026-08-27 03:42:32
finished: 2026-08-27 03:47:02
---

M-HAR 인도를 위해 sysreq(100V 절연·대전류)를 만족하는 100V 배전 하니스
(모선-PCU/PCDU-부하 간 전력·모니터링 신호 배선)를 설계해야 한다. EPS
배전 커넥터·채널 정격(REQ-HAR-EPS-배전), 전력계통 모니터링 신호가
연결되는 OBC 커넥터·핀맵(REQ-HAR-OBC-핀맵), 라우팅 경로·구조 관통부
(REQ-HAR-STR-경로)가 채널 배분·배선 굵기·경로 확정에 필요해 먼저 요청한다.
검증: 100V 절연 설계 여유, 채널별 전압강하 예측치 산출.
검증: 전압강하 예측 0.77%<=1%(내부기준), 잠정가정 사용(EPS/OBC/STR 8x20s 타임아웃)
