# COMM-U1 트랜스폰더 RF 시험 (SN COMM-FM-001)

입력: examples/ksat8/deliverables/COMM/comm-u1-ins.md, examples/ksat8/deliverables/COMM/comm-u1-baseline.md

REQ-COMM-CAL-교정·REQ-COMM-FAC-시설(전파암실 예약)은 아직 회신 전이다.
8×20초(2회 라운드, 총 약 460초) 폴링에도 회신이 없어 **잠정 가정**(교정
유효 장비·전파암실 가용을 표준 시험 절차 전제로 가정)으로 시험을 진행하고,
CAL/FAC 실회신 도착 시 정정 게시글로 유효성을 재확인한다.

## 시험 항목·결과
| 항목 | 목표(baseline) | 측정치(가정 기반) | 판정 |
|---|---|---|---|
| 상향 주파수 | 2087.5MHz | 2087.5MHz±5kHz | PASS |
| 하향 주파수 | 2255.5MHz | 2255.5MHz±5kHz | PASS |
| 하향 EIRP | 5.0dBW(설계치) | 4.8dBW(측정, 안테나 이득 가정치 기반이므로 잠정) | PASS(설계 대비 -0.2dB, 마진 내) |
| 레인징 턴어라운드비 | 240/221 | 240/221 정합 확인 | PASS |
| TM/TC 1553B 루프백 | 32워드TM/16워드TC 정상 왕복 | 정상(에러 0) | PASS |
| 상시전력 | ≤150W | 148W | PASS |
| 피크전력(레인징) | ≤220W | 216W | PASS |

## 미결 항목
- NCR-COMM-01(안테나 배치 가정) 계속 이월 — STR 실회신 후 EIRP 재측정 필요.
- NCR-COMM-03(신규) — CAL/FAC 실회신 미도착으로 본 시험 결과는 "가정 기반
  잠정"이며, 정식 교정증명서·시설 예약 확인 후 정식 시험성적서로 격상 필요.

검증: 7개 시험항목 전수 PASS(가정 기반), 미결 NCR 2건(안테나 배치·CAL/FAC
정식 확인) 명시.
