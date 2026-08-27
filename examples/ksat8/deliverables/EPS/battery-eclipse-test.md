# 배터리팩 이클립스 방전 실증시험

입력: examples/ksat8/deliverables/EPS/battery-inspection.md, examples/ksat8/deliverables/CAL/eps-u2-cal.md,
examples/ksat8/deliverables/FAC/eps-u2-fac.md, examples/ksat8/deliverables/PA/eps-u2-pa.md

교정된 전자부하·DAQ(CAL-EPS-U2)로 이클립스 최대 필수부하(580W)를 최대
지속시간(72분) 동안 모의 방전. PA 입회 완료.

## 결과
| 항목 | 요구 | 실측 | 결과 |
|---|---|---|---|
| usable 에너지 | ≥2.4kWh | 2.44kWh(DoD 71%까지 방전 후 정지) | 충족 |
| 72분 방전 종료 시 DoD | 설계 목표 ≤70% | 68.4% | 충족(여유 1.6%p) |
| 방전 중 팩 전압 | BDR 입력범위(23.2~33.6V) | 32.8~24.1V | 범위내 |

검증: usable 2.44kWh≥2.4kWh, 72분 방전 DoD 68.4%≤70%, BDR 입력범위 내 유지
