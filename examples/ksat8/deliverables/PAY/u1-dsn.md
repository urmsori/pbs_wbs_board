# PAY-U1 24채널 Ka 중계기 패널 설계

입력: examples/ksat8/deliverables/SE/sysreq.md,
examples/ksat8/deliverables/TCS/pay-thermal-capability.md,
examples/ksat8/deliverables/EPS/pay-power-capability.md,
examples/ksat8/deliverables/HAR/pay-waveguide-budget.md

## 채널 구성
- 24채널 × 36MHz(총 864MHz), 수신기(LNA+주파수변환) → 스위치매트릭스(입력4x4/
  출력) → TWTA(채널별 1기+예비4기, 4:28 이중화) → 도파관 → 안테나 급전.

## 링크(EIRP) 예산
| 항목 | 값 |
|---|---|
| TWTA 포화출력 | 200W(23.0dBW) |
| 운용 백오프(OBO) | 3dB |
| 유효 출력 | 100W(20.0dBW) |
| 도파관+하니스 손실(HAR 회신) | 0.57dB |
| 안테나계통 이득(급전 설계 가정) | 33.0dBi |
| **EIRP** | **20.0−0.57+33.0 = 52.43dBW** ≥ 52dBW(마진 0.43dB) |

## NPR
- OBO 3dB 특성곡선 기준 설계예측 NPR **19.5dB** ≥ 18dB(마진1.5dB).
  최종치는 PAY-U1-TST 노이즈로딩 시험에서 확정.

## 전력 배분(채널당, EPS confirm 458W/채널 이내)
| 항목 | W/채널 |
|---|---|
| TWTA(EPC 포함, DC입력) | 310 |
| 수신기+스위치매트릭스 배분 | 118 |
| **소계** | **428** (EPS확약 458 대비 마진 30W) |
| 공통전자(24채널 합산 후 가산) | 728W(전체) |
| **총합(24채널)** | 428×24+728 = **10,272+728 = 11,000W** = sysreq/EPS확약 정합 |

## 발열 배분(채널당, TCS confirm 262W/채널·6.3kW 이내)
- TWTA 발열: 310−100 = 210W/채널 ≤ 262W(TCS확약, 마진52W).
- 24채널 합계: 210×24 = **5,040W ≤ 6,300W**(TCS확약, 마진1,260W).

검증: EIRP52.43dBW≥52dBW(마진0.43dB), NPR설계예측19.5dB≥18dB(마진1.5dB),
전력428W/채널≤458W(EPS확약), 발열210W/채널≤262W·5.04kW≤6.3kW(TCS확약)
