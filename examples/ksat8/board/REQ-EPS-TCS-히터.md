---
id: REQ-EPS-TCS-히터
title: 히터 예산 요구 (채널 배전) 요청
status: DONE
parent: M-EPS
source: EPS-U1-DSN
owner: TCS-DSN-01
deliverable: examples/ksat8/deliverables/TCS/eps-heater-budget.md
after: -
track: TCS
started: 2026-08-27 03:47:33
finished: 2026-08-27 03:48:36
---

PCU·배전(EPS-U1-DSN)이 TCS 히터(배터리·추진 배관·구조부 등)를 배전하려면
채널별 전력 예산이 필요하다. 확인 요청:
1) 히터 채널 수와 채널별 정격 전력(W), 총합
2) 채널별 온-오프 제어 방식(서모스탯 자동 vs 커맨드) 및 최대 동시 점등
   시나리오(합산 전류 산정용)
3) 이클립스 중(배터리 2.4kWh 방전 구간) 필수 히터 채널과 우선순위
산출물: TCS 팀이 정하는 경로(예: examples/ksat8/deliverables/TCS/)에 위
3항목을 수치로 명시해 달라. 무응답 시 총 히터 예산 200W(6채널 균등 33W,
전 채널 서모스탯 자동)로 잠정 설계한다.
검증: 채널 수·정격·총합 회신, 이클립스 필수 채널 우선순위 확정
검증: 히터 6채널 200W 정격·이클립스 우선순위 회신
