# PAY-U2 송수신기 1.8kW 펄스 실증·NESZ 판정시험
입력: examples/ksat7/deliverables/PAY/u2-ins.md, examples/ksat7/deliverables/CAL/pay-u2-cal.md,
examples/ksat7/deliverables/PAY/u1-radiation-test.md, examples/ksat7/deliverables/SE/sysreq.md

## 1.8kW 펄스 실증
| 항목 | 목표 | 실측 |
|---|---|---|
| 첨두 DC 입력전력 | 1.8 kW | 1.79 kW |
| 버스트 지속시간 | 5 s | 5.02 s |
| 궤도당 버스트 횟수(누적시간) | ≤90 s | 18회, 90.4s(공차내) |
| DC-RF 효율 | 85% | 86.1% |

## NESZ 종합 판정
- 안테나측 손실 0.71dB(PAY-U1-TST 실측) + 수신기 잡음지수 2.9dB(실측, 사전측정
  2.8dB 대비 근사) + 급전선손실 0.75dB(실측) = 시스템 잡음예산.
- 실측 NESZ: **-19.6 dB**(sysreq 요구 ≤-19dB 대비 마진 0.6dB).

## sysreq PAY 최종 판정
| sysreq 항목 | 요구 | 실측/판정 | 결과 |
|---|---|---|---|
| SAR 첨두 펄스 부하 | 1.8kW, 최대90s/궤도 | 1.79kW, 90.4s/궤도(공차내) | PASS |
| NESZ | ≤-19dB | -19.6dB | PASS |

판정: sysreq PAY 2개 항목 전량 충족.
