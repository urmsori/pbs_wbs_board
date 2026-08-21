# STR EM 모듈 인수 시험 결과
입력: examples/ksat5/deliverables/STR/module-em.md,
      examples/ksat5/deliverables/SUPPORT/need-jig-str.md

AIT-RX-STR(AIT-TST)의 STR EM 모듈 인수 시험 기록. NEED-JIG-STR가
산출한 10종 정합 지그(JIG-01~10)로 module-em.md의 끼워맞춤 검사
8개 항목(STR-05 자체 검사)을 독립 재확인한다.

## 1. 시험 구성
- 지그: JIG-01(EPS 태양전지판)~JIG-10(COMM 안테나) 10종, mounting-
  interfaces.md 체결 패턴에 1:1 대응.
- 특히 JIG-03(EPS 배터리 브래킷)은 module-em.md에서 "잠정 합격"으로
  이월된 유일 항목의 최종 재확인용으로 별도 표시된 지그.

## 2. 재확인 결과
| 대상 | module-em.md 판정 | AIT 독립 재확인(지그) | 결과 |
|---|---|---|---|
| EPS 태양전지판(M2.5×4) | 합격 | JIG-01 정합 | 일치 |
| EPS PCU(PC/104 피치) | 합격 | JIG-02 정합 | 일치 |
| EPS 배터리(M3×4, 잠정 합격) | 잠정 합격 | JIG-03 정합(최종 발자국 95×90×20mm 기준) | **일치 — 잠정 판정 최종 확정** |
| AOCS 리액션휠/마그네토토커 | 합격 | JIG-04/05 정합 | 일치 |
| AOCS 스타트래커/자이로/태양센서 | 합격 | JIG-06/07/08 정합 | 일치 |
| COMM 트랜시버/안테나 | 합격 | JIG-09/10 정합 | 일치 |

## 3. 질량 확인
구조체 실측 2.97kg ≤ 배분 3.00kg (module-em.md 수치 재확인, 계량 결과 동일).

## 4. 판정
8개 끼워맞춤 항목 전건 지그 정합 확인. 특히 module-em.md에서
미결로 이월된 EPS 배터리 브래킷(잠정 합격) 항목이 JIG-03으로 최종
발자국 기준 정합 확인되어 미결 사항 해소. STR EM 모듈 인수 **합격**.

검증: 10종 지그 전건 정합 확인, JIG-03으로 EPS 배터리 브래킷 잠정
판정을 최종 확정, 구조체 질량 2.97kg≤3.00kg 재확인.
