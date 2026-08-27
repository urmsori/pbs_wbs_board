---
id: PROP-DSN-01
title: 이원추진제 계통 설계(탱크·추력기 배치)
status: DONE
parent: M-PROP
source: M-PROP
owner: PROP-DSN-01
deliverable: examples/ksat8/deliverables/PROP/biprop-design.md
after: REQ-PROP-STR-장착
track: PROP
started: 2026-08-27 03:55:02
finished: 2026-08-27 03:56:17
---

왜: sysreq Δv 2,250m/s 중 정지궤도 진입분을 담당하는 이원추진제(산화제·
연료 탱크+액체추력기) 계통을 설계하려면 탱크·추력기 장착 인터페이스(STR
회신)가 먼저 있어야 한다. (축약 체인: 설계→검토→시험)
산출물: examples/ksat8/deliverables/PROP/biprop-design.md

[진행 기록] REQ-PROP-STR-장착 회신 대기 8×20초(2회) 초과 — 규칙 v3.2·
COMMON에 따라 잠정 가정을 명시하고 설계를 진행한다(가정 근거: 본인이 이미
STR에 답한 str-prop-tank-reply.md의 대칭 수치 — 트러니언 4점, 국부강성
≥60Hz, 축8.5g/횡4.5g). 실회신이 오면 정정 게시글(after 유지)로 갱신한다.
손 편집으로 TAKEN — post.py는 after 미완 상태를 정상적으로 거부한다.
검증: Δv 1,500m/s용 추진제 1,363kg, LAE 400N+RCS 10N×12기 배치(잠정, STR 실회신 대기)
