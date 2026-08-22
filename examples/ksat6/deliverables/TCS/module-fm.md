# TCS 열제어 비행모델 인도
입력: examples/ksat6/deliverables/TCS/thermal-analysis.md, examples/ksat6/deliverables/TCS/mli-kit.md, examples/ksat6/deliverables/TCS/heater-thermistor.md, examples/ksat6/deliverables/TCS/radiator.md, examples/ksat6/deliverables/TCS/tvac-test.md, examples/ksat6/deliverables/EPS/heater-channel-confirmation.md, examples/ksat6/deliverables/TCS/pay-thermal-confirmation.md

## 구성
MLI(전면 도포, 개구부 최소화) + 히터 3채널(H1 배터리10W/H2 추진탱크8W/H3
광학부4W) + 서미스터 11점 + 라디에이터(-Z, 0.20㎡ OSR). 열진공(TVAC) 4사이클
실측으로 검증.

## sysreq.md TCS 행 수치 판정
| 항목 | sysreq 요구 | 실측(tvac-test.md) | 판정 |
|---|---|---|---|
| 전 유닛 작동온도 | -20~+50°C | 고온 +40°C / 저온 -17°C(구조체) 등 전 유닛 범위 내 | 충족 |
| 배터리 온도 | 0~+30°C | 고온 +25°C / 저온 +1°C | 충족 |
| 히터 예산 | ≤25W | 실측 합계 21.7W(사이클 최대 동시점등) | 충족(마진 3.3W) |

## 인터페이스 이행 기록
- REQ-TCS-EPS(EPS): DONE — 히터 4채널 배전 EPS 확인 완료(증설 없이 수용,
  heater-channel-confirmation.md), heater-thermistor.md에 반영.
- REQ-TCS-PAY(PAY): DONE — 광학부 온도 안정성(구배≤2°C, 변동≤±0.5°C) 요구를
  PAY-01에 전달, PAY 팀이 독자 산출과 일치함을 확인해 수용
  (examples/ksat6/deliverables/PAY/tcs-thermal-confirm.md).
- 수신 REQ: PAY 팀이 보낸 REQ-PAY-TCS(초점면 온도 안정성 요구)는 DONE으로
  처리 완료(pay-thermal-confirmation.md).

검증: sysreq.md TCS 행(-20~+50°C, 배터리0~+30°C, 히터≤25W) 전 항목 TVAC 실측
충족. EPS·PAY 인터페이스 모두 상대 팀 확인 완료.
