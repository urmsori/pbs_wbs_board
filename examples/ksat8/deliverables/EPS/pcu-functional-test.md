# PCU·배전유닛 기능·부하시험

입력: examples/ksat8/deliverables/EPS/pcu-inspection.md, examples/ksat8/deliverables/CAL/eps-u1-cal.md,
examples/ksat8/deliverables/FAC/eps-u1-fac.md, examples/ksat8/deliverables/PA/eps-u1-pa.md

교정된 전자부하 뱅크·DAQ(CAL-EPS-U1)로 0~15kW 전 채널(PAY24+EP2+COMM1+
히터6) 부하를 단계적으로 인가, 100V±2V 조절 성능과 PAY 채널 인러시
대응성을 실측. PA 입회 완료.

## 결과
| 항목 | 요구 | 실측 | 결과 |
|---|---|---|---|
| 버스전압 조절 | 100V±2V | 98.4~101.7V(0~15kW 전 구간) | 충족 |
| 전 채널 합계부하 | ≤15,000W | 14,420W 정상부하 인가 확인 | 충족 |
| PAY 채널 인러시 | LCL(8A) i²t 트립 없이 통과 | 12.6A 첨두·9ms, 트립 없음 | 충족(RB 조건 해소) |
| EP 동시 2채널 | 3,000W | 3,010W 실측 | 충족 |

RB 조건부 승인의 조건(인러시 실측)이 위 결과로 해소됨.

검증: 100V±2V(98.4~101.7V) 전구간 유지, PAY인러시 12.6A/9ms 트립없음(RB조건 해소), EP 3,010W 실측
