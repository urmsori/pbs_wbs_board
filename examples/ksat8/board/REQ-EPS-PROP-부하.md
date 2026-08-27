---
id: REQ-EPS-PROP-부하
title: 전기추진 운전 전력·시간 요청
status: DONE
parent: M-EPS
source: EPS-U1-DSN
owner: PROP-DSN-02
deliverable: examples/ksat8/deliverables/PROP/eps-load-profile.md
after: -
track: PROP
started: 2026-08-27 03:47:33
finished: 2026-08-27 03:48:36
---

PCU·배전(EPS-U1-DSN)에서 15kW 예산 중 전기추진(이온추력기, GEO 유지
Δv 750m/s) 채널 정격과, 탑재체 11kW 부하와의 동시 구동 여부를 확인해야
버스 순시부하·배터리 이클립스 방전 여유를 판정할 수 있다. 확인 요청:
1) 추력기 정상상태 소모 전력(W)·전류(A, 100V 버스 기준)와 채널 수(이중화
   포함)
2) 궤도당(또는 유지운용 주기당) 운전 시간과 듀티(연속/간헐)
3) 탑재체(11kW) 동시 운용 정책(상호배제 여부) 및 기동 램프업/다운 특성
산출물: PROP 팀이 정하는 경로(예: examples/ksat8/deliverables/PROP/)에
위 3항목을 수치로 명시해 달라. 무응답 시 "탑재체 상시 운용, 전기추진은
유지운용 기간에만 별도 채널로 순차 구동(동시부하 배제)"로 잠정 가정한다.
검증: 추력기 W·A·운전시간 회신, 탑재체 동시부하 정책 확정
검증: 추력기 정상전력 1.5kW/채널·듀티·탑재체 동시운용 정책 회신(잠정)
