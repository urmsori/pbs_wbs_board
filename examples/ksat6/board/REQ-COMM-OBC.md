---
id: REQ-COMM-OBC
title: X-band 다운링크 데이터 인터페이스(버퍼·전송 프로토콜) 확정 요청
status: DONE
parent: C-LB
source: C-LB
owner: OBC-IO-01
deliverable: examples/ksat6/deliverables/OBC/reply-comm-downlink-interface.md
after: -
track: OBC
started: 2026-08-22 01:26:20
finished: 2026-08-22 01:26:51
---

링크 버짓(C-LB)에서 X-band 150Mbps 송신기(C-XTX)를 설계하려면 OBC 대용량
메모리에서 송신기로 데이터를 넘기는 물리 인터페이스와 전송 프로토콜을
확정해야 한다. OBC 팀에 요청한다.
산출물: OBC 팀이 남기는 문서 — 인터페이스 종류(예: SpaceWire)와 링크 속도,
버스트 다운링크에 필요한 송신기 측 버퍼 최소 깊이(Mbit), 프레이밍/전송
프로토콜(예: CCSDS AOS 가상채널), 다운링크 시작/정지 핸드셰이크 방식.
검증: SpW 채널배정·버퍼깊이 계산(150Mbps×0.4s≈60Mbit<64Mbit) 확인
