---
id: OBC-IO
title: I/O보드(1553/CAN/SpW) 설계
status: DONE
parent: M-OBC
source: -
owner: OBC-IO-01
deliverable: examples/ksat6/deliverables/OBC/io-board.md
after: -
track: OBC
started: 2026-08-22 01:20:47
finished: 2026-08-22 01:22:38
---

sysreq.md의 "1553/CAN/SpW 인터페이스"를 물리적으로 구현하는 I/O보드가
필요하다. 각 유닛(AOCS·EPS·TCS·PROP·PAY·COMM)과의 버스 채널 수를 정해야
하니스(HAR) 하니스 설계와 탑재체(PAY) 데이터 인터페이스가 확정된다.
탑재체 데이터율·SpW 링크 수는 OBC가 낼 수 있는 채널 여유 안에서 PAY 팀과
협상해야 하므로(규칙 4절 — ICD는 당사자 협상) REQ-OBC-PAY를 함께 발행한다.
산출물: examples/ksat6/deliverables/OBC/io-board.md — 1553/CAN/SpW 채널 수·배정표.
검증: sysreq 3버스 종류 포함 확인, SpW 대역폭은 PAY 회신 대기중 잠정 가정
