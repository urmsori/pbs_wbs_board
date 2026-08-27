# AOCS-U1 폐루프(HIL) 시험
입력: examples/ksat7/deliverables/AOCS/u2-accept-test.md, examples/ksat7/deliverables/CAL/aocs-u1-cal.md,
examples/ksat7/deliverables/AOCS/u1-review-board.md, examples/ksat7/deliverables/SE/sysreq.md

## HIL 구성
실측 센서(별추적기0.0031°·자이로0.0036°)·반작용휠(토크0.112N·m·모멘텀12.6N·m·s
최소치)을 대입한 폐루프 시뮬레이션 + 실물 자세기준 시뮬레이터.

## 실측 결과
| sysreq 항목 | 요구 | 실측 |
|---|---|---|
| 지향정확도 | 0.02°(3σ) | 0.0183°(3σ) |
| 요 스티어링 | ±4° | ±4.0°(프로파일 추종오차 0.02° 이내) |
| 안정도(노출시간 중) | 0.003°/s | 0.00251°/s |

## sysreq AOCS 최종 판정
지향정확도 0.0183°≤0.02°(마진8.5%), 요 스티어링 ±4.0° 정합, 안정도
0.00251°≤0.003°/s(마진16.3%). 3개 항목 전량 충족.
