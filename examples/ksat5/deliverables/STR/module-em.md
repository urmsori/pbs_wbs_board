# STR EM 모듈 인도 문서
입력: examples/ksat5/deliverables/STR/primary-structure-design.md,
examples/ksat5/deliverables/STR/mounting-interfaces.md,
examples/ksat5/deliverables/STR/structural-analysis.md,
examples/ksat5/deliverables/STR/fabrication-record.md,
examples/ksat5/deliverables/STR/icd-aocs-str.md,
examples/ksat5/deliverables/STR/icd-comm-str.md,
examples/ksat5/deliverables/EPS/icd-str-eps.md,
examples/ksat5/deliverables/AOCS/icd-str-aocs-mass-footprint.md,
examples/ksat5/deliverables/COMM/icd-str-comm-footprint.md

## 끼워맞춤 검사 (STR-05)
실물 구조체(STR-04)에 각 팀 인터페이스 치구/도면 치수를 대조해 검사.

| 대상 | 검사 항목 | 결과 |
|---|---|---|
| EPS 태양전지판 몸체 패널(2면) | M2.5×4 홀 위치·피치 | 합격(도면 대비 공차 이내) |
| EPS PCU 스탠드오프 | 90.17×96.13mm PC/104 피치 | 합격 |
| EPS 배터리 예약 브래킷 | M3×4(잠정 발자국) | 잠정 합격 — EPS-03 최종 확정 후 재확인 필요 |
| AOCS 리액션휠×3, 마그네토토커×3 | 직교 3축 브래킷 위치 | 합격 |
| AOCS 스타트래커 장착면 | 평면도 5μm, PCD50 홀 | 합격(icd-aocs-str.md 정렬 공약 이행 확인) |
| AOCS 자이로/태양센서 | PCD30, PCD14 홀 패턴 | 합격 |
| COMM 트랜시버 보드 | M3 82×88mm 대각피치 | 합격 |
| COMM 안테나 4조 | -Z 패널 대칭 배치, 돌출 ≤8mm | 합격 |

## 구조체 최종 질량
| 항목 | 질량(kg) |
|---|---|
| 구조체(실측, STR-04) | 2.97 |
| STR 배분(sysreq) | 3.00 |
| 여유 | 0.03 |

## 강도·진동 여유 요약
전체 1차 모드 185 Hz, 임계 부재 최소 안전여유 MS=+4.0(structural-analysis.md).
국부 모드 요구(스타트래커 ≥150Hz, 자이로 ≥120Hz) 모두 충족.

## 미결 사항 (통합 단계로 이관)
- EPS 배터리 최종 발자국/질량(EPS-03 완료 후 갱신 예정) — 큰 변경
  가능성은 낮음(EPS 회신 잠정 여유 1.70kg).

## 검증
끼워맞춤 검사 8개 항목 중 7개 확정 합격, 1개(EPS 배터리) 잠정 합격으로
기록. 구조체 실측 질량 2.97kg ≤ STR 배분 3.00kg 확인. 강도·진동
해석(structural-analysis.md) 결과 모두 요구 충족 확인.
