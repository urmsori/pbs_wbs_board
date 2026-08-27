---
id: REQ-STR-PROP-탱크
title: 이원추진제 탱크 질량·장착 요청 (STR→PROP)
status: DONE
parent: M-STR
source: STR-U1-DSN
owner: PROP-DSN-01
deliverable: examples/ksat8/deliverables/PROP/str-prop-tank-reply.md
after: -
track: PROP
started: 2026-08-27 03:49:52
finished: 2026-08-27 03:50:29
---

왜: STR-U1(중앙 실린더) 주하중 경로와 1차모드를 설계하려면 실린더 하부
데크에 얹히는 이원추진제 탱크의 질량·장착 방식을 알아야 트러니언/스커트
마운트 국부강성과 발사 축하중 여유를 정할 수 있다.
요청: (1) 산화제·연료 탱크 각 습식/건식 질량(kg), (2) 탱크 장착 방식(트러니언
점수·위치 또는 스커트 마운트) 및 요구 국부강성, (3) 발사 시 탱크가 구조체에
전달하는 축/횡 하중(g 또는 N, 준정적+동적).
회신 산출물 제안: examples/ksat8/deliverables/PROP/str-prop-tank-reply.md
검증: 회신치를 STR-U1 1차모드·질량 예산(≤380kg, 1차모드≥30Hz) 해석에 반영
검증: 탱크 습식질량 1,363kg, 트러니언 장착 국부강성 60Hz, 축8.5g/횡4.5g 하중 회신(예비)
