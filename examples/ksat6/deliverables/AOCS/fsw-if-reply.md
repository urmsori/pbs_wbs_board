# [AOCS→FSW] 제어 알고리즘 인터페이스 회신
입력: examples/ksat6/deliverables/AOCS/pointing-budget.md, rwa-accept.md, gyro-accept.md, star-tracker-accept.md, magnetorquer.md

## 제어주기
- 자세결정/제어 루프: **20 Hz**(50ms) — 자이로 ARW 0.0009°/s·안정도 예산
  0.0024°/s(pointing-budget §2)를 만족하려면 이 주기 이상 필요.
- 별추적기 갱신 반영: 5 Hz(star-tracker-accept.md 실측 갱신율) 인터리브.

## 센서 신호
| 신호 | 형식 | 주기 | 단위 |
|---|---|---|---|
| 별추적기 쿼터니언 | float64×4 | 5Hz | - |
| 자이로 각속도 3축 | float32×3 | 20Hz | °/s |
| 자이로 온도 | float32 | 1Hz | °C |

## 액추에이터 신호
| 신호 | 형식 | 주기 | 단위 |
|---|---|---|---|
| 반작용휠 토크명령 4채널 | float32×4 | 20Hz | Nm (범위 ±0.10) |
| 반작용휠 속도피드백 4채널 | float32×4 | 20Hz | rpm |
| 마그네토커 듀티명령 3채널 | float32×3 | 1Hz | % (모멘텀덤핑 모드에서만) |

검증: 제어주기 20Hz가 pointing-budget.md §2 안정도 배분(0.0024°/s)을
만족하는 나이퀴스트 여유(자이로 대역폭 대비 ≥10배)를 가짐 — REQ-FSW-AOCS
회신.
