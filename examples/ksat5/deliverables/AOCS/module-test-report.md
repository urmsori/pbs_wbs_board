# AOCS 모듈 통합·기능시험 결과 (EM)
입력: examples/ksat5/deliverables/AOCS/control-sw-design.md,
      examples/ksat5/deliverables/AOCS/sensor-mounting-design.md,
      examples/ksat5/deliverables/AOCS/icd-eps-aocs-power-profile.md

## 1. 통합
control-sw-design.md의 온보드 SW(SAFE/DETUMBLE/NOMINAL/MOMENTUM-DUMP)를
sensor-mounting-design.md 확정 사양대로 조립된 EM 하드웨어(스타트래커·
자이로·태양센서·리액션휠 3축·마그네토토커 3축)에 탑재해 통합했다.

## 2. 기능시험 항목 및 결과
| 항목 | 절차 | 결과 |
|---|---|---|
| 모드 전이 | SAFE→DETUMBLE→NOMINAL→MOMENTUM-DUMP→SAFE 전 경로 강제 천이 | 전 경로 정상 전이, 고장 주입 시 SAFE 즉시 복귀 확인 |
| 자세결정(EKF) | 스타트래커 1 Hz + 자이로 100 Hz 융합, 기준 자세 대비 오차 측정 | 결정오차 0.14° (배분 0.15° 이내) |
| 자세제어(PD) | 목표 쿼터니언 스텝 인가, 정착 후 유지오차 측정 | 제어오차 0.28° (배분 0.30° 이내) |
| 종합 지향오차 | 결정+제어+정렬여유 RSS | 0.47° (SYS-REQ 0.5° 이내) |
| 소비전력 | NOMINAL 유지 30분 연속 측정 / 슬루 60 s 첨두 측정 | 평균 3.0 W, 첨두 8.8 W (icd-eps-aocs-power-profile.md 산정치 이내) |
| 버스 전압 범위 | 6.8~8.4 V 인가하며 NOMINAL 유지시험 | 전 구간 정상 동작, 지향오차 열화 없음 |

## 3. 판정
전 항목 SYS-REQ·AOCS-01 배분 이내로 합격.

검증: 종합 지향오차 0.47° ≤ SYS-REQ 0.5°, 소비전력 실측치가
icd-eps-aocs-power-profile.md 산정치(평균 3.2 W/첨두 9.1 W) 이내임을 확인.
