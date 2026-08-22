# EPS 비행모델 인도 (K-SAT 6)
입력: examples/ksat6/deliverables/EPS/power-budget.md, pcdu-design.md, battery-pack.md, integration-test.md

## 구성
- 아키텍처: 28V±4V(24~32V) 조절모선, PCDU DET+순차스위칭.
- PCDU: 채널별 전류정격(주버스 퓨즈 10A), 배터리 관리 임계값(충전종지33.6V·로드셰딩27.2V·안전모드26.4V).
- 배터리: 8S3P 18650 Li-ion, 293.8Wh(BOL)/235.0Wh(EOL).

## sysreq 최종 판정 (인용: "EPS: 모선 28V±4V, 부하 155W, 일식 35분 배터리 심방전 ≤25%")
| 항목 | 요구 | 실측/산출 | 판정 |
|---|---|---|---|
| 모선전압 | 28V±4V(24~32V) | 27.6~28.9V(전 시나리오) | 충족 |
| 부하(평균) | ≤155W | 91.4W(마진41%) | 충족 |
| 부하(첨두 시나리오) | ≤155W | 131W(마진24W) | 충족 |
| DoD(일식35분) | ≤25% | BOL16.6% / EOL20.8% | 충족 |

## 이력
EPS-01(전력예산·아키텍처)→EPS-02(PCDU)·EPS-03(배터리팩) 병렬→EPS-04(통합시험,
AOCS/COMM/PAY 실측 회신 반영) 순으로 진행. 타 트랙 질의 5건(REQ-COMM-EPS,
REQ-FSW-EPS, REQ-HAR-EPS, REQ-TCS-EPS, REQ-AOCS-EPS) 회신 완료.

검증: sysreq EPS 3항목 전량 실측 기반 충족(위 표), 예산 초과 없이 인도.
