---
id: REQ-PROP-EPS-전력
title: 전기추진 전력 확약 요청
status: DONE
parent: M-PROP
source: PROP-DSN-02
owner: EPS-U1-DSN-01
deliverable: examples/ksat8/deliverables/EPS/ep-power-commitment.md
after: -
track: EPS
started: 2026-08-27 03:47:05
finished: 2026-08-27 03:47:12
---

왜: 이온추력기(전기추진)는 스테이션키핑·언로딩 기간에 큰 펄스 전력을 쓴다.
100V 버스에서 배정 가능한 전력·전압 리플 허용치를 확약받아야 PPU(전력처리
장치) 정격을 정할 수 있다.
요청: 전기추진에 배정 가능한 최대 전력(W)·동시 점화 채널 수, 버스 전압
리플 허용치, 스테이션키핑 windows(1일 점화 시간대), 배터리 방전 병행 여부.
회신 산출물 제안: examples/ksat8/deliverables/EPS/ep-power-commitment.md
검증: EP 2000W(2채널) 확약, PAY 동시운용 가능
