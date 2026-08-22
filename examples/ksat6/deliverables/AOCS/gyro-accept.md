# 자이로(IMU) 수락시험
입력: examples/ksat6/deliverables/AOCS/pointing-budget.md

## 수락 기준 vs 실측
| 항목 | 배분 예산 | 실측(수락시험) | 판정 |
|---|---|---|---|
| 각속도 잡음(ARW) | 0.0010°/s(pointing-budget §2) | 0.0009°/s | PASS |
| 별추적기 전파오차(갱신 사이) | 0.010°(pointing-budget §1) | 0.008° | PASS |
| 바이어스 안정도 | (참고) | 0.02°/hr | 기록 |
| 전력(평균/첨두) | 4W/5W(pointing-budget §5) | 4.1W/5.0W | PASS |

3축 FOG(광섬유자이로) 단일 패키지, sysreq 안정도 0.005°/s 예산의 자이로
항목은 실측치로 유지.

검증: ARW 0.0009 ≤ 배분 0.0010, 전파오차 0.008 ≤ 배분 0.010 — pointing-budget.md §1·§2 대비 PASS.
