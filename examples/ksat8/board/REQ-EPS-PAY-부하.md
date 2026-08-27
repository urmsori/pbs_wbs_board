---
id: REQ-EPS-PAY-부하
title: 중계기 11kW 부하 프로파일(채널 구성별) 요청
status: DONE
parent: M-EPS
source: EPS-U1-DSN
owner: PAY-IF-01
deliverable: examples/ksat8/deliverables/PAY/eps-pay-load-reply.md
after: -
track: PAY
started: 2026-08-27 03:55:18
finished: 2026-08-27 03:55:18
---

PCU·배전(EPS-U1-DSN)을 설계하려면 sysreq 탑재체 배정(11kW) 이 24채널
중계기에 실제로 어떻게 분배되는지 알아야 배전 채널·차단기 정격을 정할 수
있다. 확인 요청:
1) 채널 구성별(예: TWTA/SSPA 채널 수·형식) DC 소모 전력(W) 내역과 합계
   11kW 정합 여부
2) 채널별 정상상태 전류(A, 100V 버스 기준)와 기동(inrush) 전류 배수
3) 채널 on/off 스위칭 빈도(임무 중 재구성 여부) — 배전 스위치 정격 산정용
산출물: PAY 팀이 정하는 경로(예: examples/ksat8/deliverables/PAY/)에 위
3항목을 수치로 명시해 달라. 무응답 시 sysreq 11kW를 24채널 균등 분배
(채널당 458W, 정상상태로 상시 가정)로 잠정 설계한다.
검증: 채널별 W·A 내역 합계 11kW 정합, inrush 배수·스위칭 정책 회신
검증: 428W/채널×24+728W=11,000W 정합, inrush≤3배 10ms
