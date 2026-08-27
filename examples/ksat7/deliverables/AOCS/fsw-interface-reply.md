# AOCS→FSW 회신: 요 스티어링 제어 인터페이스(주기·신호)
입력: examples/ksat7/deliverables/AOCS/u1-yaw-steering-design.md, examples/ksat7/deliverables/AOCS/u1-stability-analysis.md

## 제어주기
10 Hz(폐루프 대역폭 0.79Hz의 12.7배 — 디지털 제어 안정성 여유 확보).

## 요 스티어링 신호 목록
| 신호명 | 방향 | 형식 | 주기 | 단위 |
|---|---|---|---|---|
| YAW_STEER_CMD | FSW→AOCS | float32 | 10 Hz | deg |
| ATT_FB(쿼터니언) | AOCS→FSW | float32×4 | 10 Hz | - |
| RATE_FB | AOCS→FSW | float32×3 | 10 Hz | deg/s |
| RWA_TORQUE_CMD | AOCS→FSW(모니터) | float32×4 | 10 Hz | N·m |
| MODE_STATUS | AOCS→FSW | enum(ACQ/TRACK/DUMP/SAFE) | 1 Hz | - |

검증: 제어주기 10Hz는 안정도 배분 0.003°/s(설계목표 0.0026°/s)를 만족하는
샘플링 여유를 제공, sysreq 안정도 배분과 정합.
