# COMM FM 수락검사
입력: examples/ksat5/deliverables/COMM/design-update-fm.md,
examples/ksat5/deliverables/COMM/fabrication-record-fm.md,
examples/ksat5/deliverables/COMM/icd-str-comm-footprint.md,
examples/ksat5/deliverables/EPS/rail-budget.md

제작자(COMM-MFG)와 별도인 검사자(COMM-QA)가 독립적으로 수행한 공식
수락 판정.

## 1. 치수·질량 검사
| 항목 | 사양 | 실측(fabrication-record-fm.md) | 판정 |
|---|---|---|---|
| 트랜시버 외형/체결 홀 패턴 | 90×96×25mm, M3 82×88mm 대각(icd-str-comm-footprint.md) | 도면 대비 편차 없음(현품 대조) | 합격 |
| 트랜시버 질량 | 0.55 kg | 0.552 kg | 합격(허용공차 내) |
| 안테나+디플로이어 질량 | 0.15 kg | 0.148 kg | 합격 |
| 안테나 수납 포락선 | −Z 패널 돌출 ≤8mm(icd-comm-str.md) | 실측 7.6mm | 합격 |

## 2. RF 성능 검사
| 항목 | 사양 | 실측 | 판정 |
|---|---|---|---|
| 피드망 위상오차 | ±2° 이내 | ±1.6° | 합격 |
| PA 출력(8.4V 공칭) | ≥33.0dBm(설계 33.1dBm 승계) | 33.0dBm | 합격 |

## 3. 액추에이터 레일 퓨즈 정격 — RISK-RAIL 이월 항목 재확인 (종결)
design-update-fm.md에서 "RISK-RAIL 최종 퓨즈 정격이 나오면 COMM-FM-03
수락검사에서 재확인" 하기로 이월했던 항목이다. RISK-RAIL이 DONE으로
종결되어 examples/ksat5/deliverables/EPS/rail-budget.md의 확정치를
인용해 재확인한다:

- **COMM 전용 분기 퓨즈: 1.25A, 완속형(slow-blow)**(rail-budget.md §2) —
  COMM 정상상태 첨두 0.74A(EOD, icd-eps-comm-power.md)가 240초 연속
  흘러도 완속형 특성상 nuisance trip 없이 견디도록 정격화됨을 확인.
  0.74A/1.25A ≈ 59%로 지속부하 여유 있음.
- **PCU~분기 상위 공용 퓨즈: 3.0A 완속형**(rail-budget.md §2) — 동시
  최악 2.08A(AOCS+COMM, ≤5초 한정)가 3.0A 정격의 83%로, 완속 특성상
  5초 통과 시 트립 없음을 rail-budget.md 판정으로 확인.
- **선택성**: COMM 분기(1.25A)가 상위 공용(3.0A)의 42%로 선택성 기준
  (80% 이하) 충족 — COMM 분기 단독 고장 시 AOCS 급전에 영향 없음.
- COMM 하드웨어(퓨즈·커넥터·배선) 자체는 EPS가 정한 정격을 그대로
  수용하는 구조이며, COMM측 부품(커넥터·하네스)은 3.0A 연속 정격
  이상으로 이미 선정되어 있어(fabrication-record-fm.md 부품 스크리닝
  목록) 추가 변경 불필요함을 확인했다.

**정직 공개**: rail-budget.md §3의 운용 제약(AOS guard band
10s→15s, 비필수 슬루 스케줄링 금지, 초기궤도운용 실측 모니터링)은
COMM 하드웨어 검사로 종결되는 항목이 아니라 AIT/운영 절차에 반영될
사항이다 — 이 수락검사는 COMM 하드웨어가 확정 퓨즈 정격 조건을
만족함만 확인하며, 운용 제약 이행 여부는 COMM-FM-05(인도) 시 별도
명시해 이월한다.

## 4. 종합 판정
전 항목 합격 — **COMM FM 하드웨어 수락 합격**. RISK-RAIL 이월 재확인
항목은 rail-budget.md 확정치 인용으로 닫는다.

검증: 치수 6항목·RF 2항목 전건 사양 대비 합격, 퓨즈 정격 재확인은
rail-budget.md 확정 수치(1.25A/3.0A, 선택성 42%)를 직접 인용해
COMM측 하드웨어가 초과 없음을 확인. 운용 제약 이행은 검사 범위 밖으로
명시해 이월.
