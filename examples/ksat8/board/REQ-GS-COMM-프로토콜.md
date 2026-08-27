---
id: REQ-GS-COMM-프로토콜
title: TT&C 주파수·변조·레인징 계획 요청
status: DONE
parent: M-GS
source: M-GS
owner: COMM-DSN-01
deliverable: examples/ksat8/deliverables/COMM/REQ-GS-COMM-프로토콜-reply.md
after: -
track: COMM
started: 2026-08-27 03:53:58
finished: 2026-08-27 03:53:59
---

관제소 적합성 판정(안테나 대역·복조기·레인징 장비 선정)과 IOT 30일 계획(가시
윈도우별 TT&C 시나리오)을 세우려면 COMM이 정하는 TT&C 링크의 실제 값이
먼저 필요하다. 같은 에이전트가 COMM·GS 두 역할을 겸하더라도 이 정보는
COMM 설계(COMM-U1)의 산출물이므로 정식 요청으로 받는다(v3.2).

무엇을 알려달라: (1) 상향/하향 주파수 대역과 채널(가능하면 정확한 MHz),
(2) TC/TM 변조 방식과 부호율, (3) 레인징 방식(톤/PN)과 코히런트 턴어라운드
비, (4) 안테나 EIRP·G/T 예상치(관제소 링크버짓용).

회신 산출물 경로 제안: examples/ksat8/deliverables/COMM/REQ-GS-COMM-프로토콜-reply.md
검증: 주파수/변조/레인징/EIRP 잠정치 회신
