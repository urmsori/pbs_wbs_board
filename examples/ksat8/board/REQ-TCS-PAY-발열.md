---
id: REQ-TCS-PAY-발열
title: TWTA 채널별 발열·배치 정보 요청
status: DONE
parent: M-TCS
source: TCS-DSN-01
owner: PAY-IF-01
deliverable: examples/ksat8/deliverables/PAY/twta-heat-layout.md
after: -
track: PAY
started: 2026-08-27 03:55:18
finished: 2026-08-27 03:55:18
---

왜: TWTA 히트파이프 패널(TCS-DSN-01)을 설계하려면 24채널 TWTA의 채널별 발열량과
패널 상 배치(격자)를 알아야 히트파이프 레이아웃·응축부 위치를 정할 수 있다.
요청: 채널당 TWTA 소비전력 대비 발열(W), 24채널 총 발열 분포, 채널 배치도(패널
좌표), duty/redundancy(예비채널 대기 발열) 가정.
회신 산출물 제안: examples/ksat8/deliverables/PAY/twta-heat-layout.md
검증: 채널당210W≤262W, 24채널5.04kW≤6.3kW(마진1.26kW)
