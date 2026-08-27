---
id: REQ-PAY-TCS-방열
title: "[PAY→TCS] TWTA 패널 방열 능력 확약 요청"
status: DONE
parent: M-PAY
source: M-PAY
owner: TCS-ANL-T-01
deliverable: examples/ksat8/deliverables/TCS/pay-thermal-capability.md
after: -
track: TCS
started: 2026-08-27 03:47:33
finished: 2026-08-27 03:48:36
---

sysreq TCS는 TWTA 패널 히트파이프, 작동 -10~+60°C, 방열 6kW를 규정한다.
PAY-U1 설계(DSN)가 24채널 EIRP 52dBW/채널을 만족하는 TWTA RF 출력을
정하려면, TCS가 채널당(또는 패널 전체) 실제 방열 가능 용량과 TWTA 베이스
플레이트 허용 최고온도를 확약해야 한다. 채널당 발열(DC-RF 변환효율 역산
기준 잠정 채널당 250W 가정)로 24채널 동시 운전 시 총 6kW 방열 여유를
확인해 달라.
산출물 제안: examples/ksat8/deliverables/TCS/pay-thermal-capability.md —
채널당/패널 방열 용량(W), TWTA 베이스플레이트 허용온도(°C), 24채널 동시
운전 여유(kW).
검증: 채널당 요청 발열 합계(≈250W×24=6.0kW)가 확약 방열 용량 이내인지 확인
검증: 방열 용량 6.3kW 확약, 24채널 6.0kW 요청 대비 0.3kW 여유
