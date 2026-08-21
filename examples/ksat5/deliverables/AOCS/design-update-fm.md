# FM 설계갱신 (EM 결과·리스크 반영)
입력: examples/ksat5/deliverables/AOCS/module-test-report.md,
      examples/ksat5/deliverables/AOCS/rail-profile.md,
      examples/ksat5/deliverables/AOCS/sensor-mounting-design.md

## 1. EM 시험 결과 반영
- 자세결정오차 0.14°/제어오차 0.28°(module-test-report.md) — 배분 대비
  여유(0.01°/0.02°)가 작음. FM에서는 EKF 게인·PD 게인을 미세조정해
  여유를 각 0.02°로 확대(목표: 결정 0.13°, 제어 0.28° 유지).
- 장착 사양(정렬·강성)은 EM에서 STR 회신치(≤0.015°/≥150 Hz 스타트래커,
  ≤0.02°/≥120 Hz 자이로, sensor-mounting-design.md)를 그대로 승계 —
  FM 도면 변경 없음.

## 2. RISK-RAIL 리스크 반영 (SW 스케줄링 강화)
rail-profile.md에서 회신한 "AOS 직전 확보 슬루 ≥10 s guard band" 규칙을
FM 온보드 SW 스케줄러에 하드 제약으로 반영한다:
- 확보 슬루 시작시각 = AOS 예정시각 − (예상 슬루시간 + 10 s 여유) 로
  자동 계산·고정(EM에서는 권고치였으나 FM에서는 스케줄러 강제 조건화)
- 지터로 여유가 5 s 미만으로 줄어들 경우 확보 슬루를 즉시 취소하고
  다음 궤도로 이월(동시부하 최악조건 발생 자체를 원천 차단)

## 3. 변경 요약
| 항목 | EM | FM |
|---|---|---|
| EKF/PD 게인 | 초기치 | 미세조정(여유 확대) |
| 장착 정렬·강성 | STR 회신치 | 동일(승계) |
| 확보 슬루 guard band | 권고 10 s | SW 강제 조건(미달 시 슬루 취소) |

검증: 변경 항목이 module-test-report.md 실측 여유(0.01°/0.02°)를
확대하는 방향임을 확인, guard band 강제화가 rail-profile.md 최악조건
(스케줄 지터 겹침)을 SW 레벨에서 차단함을 확인.
