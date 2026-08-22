---
id: C-XTX
title: X-band 송신기 설계
status: DONE
parent: M-COMM
source: -
owner: COMM-DSN-01
deliverable: examples/ksat6/deliverables/COMM/xband-transmitter.md
after: C-LB, REQ-COMM-OBC, REQ-COMM-EPS
track: COMM
started: 2026-08-22 01:27:19
finished: 2026-08-22 01:27:38
---

링크 버짓(C-LB)의 EIRP 23.5dBW(RF 10W)를 실제 송신기로 구현하려면 OBC
데이터 인터페이스(REQ-COMM-OBC 회신: SpW·64Mbit 버퍼·CCSDS AOS)와 EPS 첨두
전력 허용치(REQ-COMM-EPS 회신: 70W/4A 여유)를 반영해 설계해야 한다.
산출물: examples/ksat6/deliverables/COMM/xband-transmitter.md — RF 출력·변조·
버퍼·전력 소비.
검증: EPS 허용치(70W/4A) 대비 사용치(40W/1.43A) 여유 확인, OBC 버퍼 여유 6.7%로 빠듯함을 정직 기록
