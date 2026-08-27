---
id: REQ-MECH-SA-힌지
title: SA 힌지 인터페이스 요청 (MECH→SA)
status: DONE
parent: M-MECH
source: MECH-U2-DSN
owner: SA-U1-DSN-01
deliverable: examples/ksat8/deliverables/SA/mech-sa-hinge-reply.md
after: -
track: SA
started: 2026-08-27 03:52:52
finished: 2026-08-27 03:52:52
---

왜: MECH-U2(SA 전개힌지) 스프링·댐퍼·래치 용량을 정하려면 SA 윙(2윙)의
질량·관성과 힌지 접속부 요구를 알아야 한다. 귀 팀이 올린 REQ-SA-MECH-힌지에는
본 요청과 별개로 회신한다(examples/ksat8/deliverables/MECH/sa-hinge-icd.md 참조 예정).
요청: (1) 윙당 패널 질량(kg)·힌지축 관성(kg·m²), (2) 힌지 접속부 요구 회전강성
범위(N·m/rad)와 백래시 허용치, (3) 힌지 장착 볼트 패턴/좌표.
회신 산출물 제안: examples/ksat8/deliverables/SA/mech-sa-hinge-reply.md
검증: 회신치를 MECH-U2 힌지강성·댐퍼 사이징에 반영, 전개 후 1차모드≥0.1Hz 해석과 정합
검증: 질량180kg/윙·관성10,000kg·m²·힌지강성목표6,000N·m/rad 회신
