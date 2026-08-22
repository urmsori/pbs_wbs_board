# SA 비행모델 인도 (K-SAT 6)
입력: examples/ksat6/deliverables/SA/cell-string-layup.md, panel-substrate.md, flash-test.md, eol-margin-fix.md, deployment-interface-check.md

## 구성
- 2윙 전개형 GaAs 3접합 셀 태양전지판, 윙당 11스트링×19셀(증설 후), 힌지 완전
  전개 180°±1°(MECH 인터페이스 정합).

## sysreq 최종 판정 (인용: "SA: EOL 340W(수직입사), 전개 후 1차모드 ≥0.8Hz")
| 항목 | 요구 | 산출/실측 | 판정 |
|---|---|---|---|
| EOL 전력(수직입사) | ≥340W | 356.4W(마진4.8%) | 충족 |
| 전개 후 1차모드 | ≥0.8Hz | 0.837Hz(마진4.6%) | 충족 |

## 이력·재작업 기록
SA-01(셀 스트링 레이업)→SA-02(패널기판 2윙 제작)→SA-03(전기성능시험/플래시)
에서 EOL 324.0W로 sysreq 340W 대비 4.7% 미달 발견(설계 시 정합손실 미반영,
원인은 자기 설계). SA-05(스트링 10→11 증설)로 보완, EOL 356.4W로 재판정
통과. SA-04(전개 인터페이스 확인)에서 MECH 힌지강성(45Nm/rad, REQ-SA-MECH
회신)과 결합해 1차모드 0.837Hz로 최종 검증. 타 트랙(STR/MECH) 질의 2건
(REQ-MECH-SA, REQ-STR-SA) 회신 완료.

검증: sysreq SA 2항목 전량 충족(위 표), 재작업(SA-03 미달→SA-05 보완→SA-04 재확인) 왕복 기록 완료.
