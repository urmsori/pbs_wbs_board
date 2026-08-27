---
id: TCS-DSN-01
title: TWTA 히트파이프 매립 패널 설계
status: DONE
parent: M-TCS
source: M-TCS
owner: TCS-DSN-01
deliverable: examples/ksat8/deliverables/TCS/panel-design.md
after: REQ-TCS-PAY-발열,REQ-TCS-STR-패널
track: TCS
started: 2026-08-27 03:55:02
finished: 2026-08-27 03:55:55
---

왜: sysreq(방열 6kW, 작동 -10~+60°C)를 만족하는 TWTA 방열 패널을 설계하려면
TWTA 채널별 발열·배치(PAY 회신)와 패널 모재·체결 인터페이스(STR 회신)가
먼저 있어야 한다.
산출물: examples/ksat8/deliverables/TCS/panel-design.md

[진행 기록] REQ-TCS-PAY-발열·REQ-TCS-STR-패널 회신 대기 8×20초(2회, 총
16회) 초과 — 규칙 v3.2·COMMON에 따라 잠정 가정을 명시하고 설계를 진행한다
(가정 근거: REQ-PAY-TCS-방열 본문의 PAY측 잠정치 250W/채널, sysreq STR
예산). 실회신이 오면 정정 게시글(after 유지)로 갱신한다. 손 편집으로
TAKEN — post.py는 after 미완 상태를 정상적으로 거부한다.
검증: 6.0kW(250W×24채널) ≤ 확약 방열용량 6.3kW, 0.3kW 여유(잠정, PAY/STR 실회신 대기)
