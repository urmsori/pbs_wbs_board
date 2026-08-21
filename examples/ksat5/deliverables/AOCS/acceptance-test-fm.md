# FM 모듈 수락시험 결과
입력: examples/ksat5/deliverables/AOCS/calibration-report-fm.md,
      examples/ksat5/deliverables/AOCS/design-update-fm.md,
      examples/ksat5/deliverables/AOCS/icd-eps-aocs-power-profile.md,
      examples/ksat5/deliverables/AOCS/rail-profile.md

EM 인수 치구·인터페이스(module-test-report.md heritage)를 사용한
모듈 단위 벤치 수락시험. 최종 위성구조체 장착 후 검증은 INT2 범위.

## 시험 항목 및 결과
| 항목 | 절차 | 결과 |
|---|---|---|
| 모드 전이 | 전 모드(SAFE/DETUMBLE/NOMINAL/MOMENTUM-DUMP) 강제 천이 | 정상, EM과 동일 |
| 자세결정오차 | calibration-report-fm.md 교정치 반영 EKF 구동 | 0.13° (설계 목표 0.13° 부합, EM 0.14° 대비 개선) |
| 자세제어오차 | 조정 PD 게인 적용 | 0.27° (설계 목표 0.28° 이내) |
| 종합 지향오차 | RSS(결정+제어+정렬여유 0.35°) | 0.45° (SYS-REQ 0.5° 이내, EM 0.47° 대비 개선) |
| 확보 슬루 guard band 강제 로직 | AOS 예정시각 대비 여유 5~10 s 시나리오 주입 | 여유<5s 시 슬루 자동 취소·이월 정상 동작 확인 |
| 소비전력 | NOMINAL 30분 연속 / 슬루 60 s 첨두 | 평균 2.9 W, 첨두 8.7 W(icd-eps-aocs-power-profile.md 이내) |

## 판정
전 항목 SYS-REQ·설계 목표 이내로 합격. FM-AOCS-01에서 갱신한 SW
guard band 강제 로직이 최악조건(RISK-RAIL 동시부하)을 실제로 차단함을
확인.

검증: 종합 지향오차 0.45° ≤ SYS-REQ 0.5°, guard band 강제 로직 정상
동작(여유<5s 시 슬루 취소) 확인.
