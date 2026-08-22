# 별추적기(STT) 수락시험
입력: examples/ksat6/deliverables/AOCS/pointing-budget.md

## 수락 기준 vs 실측
| 항목 | 배분 예산 | 실측(수락시험) | 판정 |
|---|---|---|---|
| 측정정확도(3σ, 교차보어사이트) | 0.003° | 0.0025° | PASS |
| 갱신율 | (모드 설계 입력) | 5 Hz | PASS |
| 전력(평균/첨두) | 6W/8W(pointing-budget §5) | 5.6W/7.8W | PASS |

단일 유닛(항성센서 헤드+전자부) 광시야각(FOV 20°×20°) 구성, 이중화 없음 —
sysreq 지향 0.05° 예산의 정확도 항목(pointing-budget.md §1)은 이 실측치로
갱신 없이 유지 가능(마진 확대).

검증: 실측 0.0025° ≤ 배분 0.003° — pointing-budget.md §1 배분 대비 PASS.
