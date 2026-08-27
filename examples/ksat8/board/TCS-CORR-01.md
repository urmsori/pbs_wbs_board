---
id: TCS-CORR-01
title: TWTA 채널 발열 실측 반영 정정(PAY 확정 회신)
status: DONE
parent: M-TCS
source: REQ-TCS-PAY-발열
owner: TCS-DSN-01
deliverable: examples/ksat8/deliverables/TCS/panel-design.md,examples/ksat8/deliverables/TCS/thermal-analysis.md
after: REQ-TCS-PAY-발열
track: TCS
started: 2026-08-27 03:58:59
finished: 2026-08-27 03:59:32
---

왜: panel-design.md·thermal-analysis.md는 PAY 확정 회신 전 250W/채널(6.0kW)로
잠정 가정했다. PAY 확정 회신(twta-heat-layout.md)은 채널당 210W·총
5,040W·배치 4열×3행(패널당 12채널)+예비 4기(모서리, 히터 5W/기)를 준다 —
반영해 정정한다(규칙 4절 "재작업은 정상 경로").
산출물: examples/ksat8/deliverables/TCS/panel-design.md(갱신),
examples/ksat8/deliverables/TCS/thermal-analysis.md(갱신)
검증: PAY 확정치(210W/채널,5.04kW) 반영, 방열마진 0.3→1.26kW(20%)로 확대
