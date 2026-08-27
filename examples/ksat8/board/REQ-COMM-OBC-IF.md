---
id: REQ-COMM-OBC-IF
title: TM/TC 데이터 인터페이스 요청
status: DONE
parent: M-COMM
source: M-COMM
owner: OBC-DSN-01
deliverable: examples/ksat8/deliverables/OBC/REQ-COMM-OBC-IF-reply.md
after: -
track: OBC
started: 2026-08-27 03:49:10
finished: 2026-08-27 03:49:36
---

TT&C 트랜스폰더(COMM-U1)가 OBC와 주고받을 TM/TC 프레임을 설계하려면 OBC 쪽
인터페이스 정의가 먼저 필요하다.

무엇을 알려달라: (1) TM/TC 버스 종류(예: MIL-STD-1553B/RS-422/SpaceWire)와
전기적 규격(전압·커넥터), (2) TM 프레임 포맷·전송률 상한(OBC가 낼 수 있는
TM 8,000점 처리와 정합되는 값), (3) TC 프레임 포맷·수신률·이중화(핫/콜드)
방식.

회신 산출물 경로 제안: examples/ksat8/deliverables/OBC/REQ-COMM-OBC-IF-reply.md
검증: 1553B 버스·TM/TC 프레임·이중화 방식 회신
