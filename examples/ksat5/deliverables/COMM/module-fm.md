# 통신(COMM) FM 모듈 인도 문서
입력: examples/ksat5/deliverables/COMM/design-update-fm.md,
examples/ksat5/deliverables/COMM/fabrication-record-fm.md,
examples/ksat5/deliverables/COMM/acceptance-inspection-fm.md,
examples/ksat5/deliverables/COMM/acceptance-test-fm.md,
examples/ksat5/deliverables/EPS/rail-budget.md

## 모듈 구성 (EM 대비 변경 요약)
1. UHF 트랜시버 FM 보드 — 회로·전원 아키텍처는 EM rev.2 승계
   (PA 액추에이터 레일 8.4V 직결, 로직단 5V 레일), 비행급 부품 등급 적용
2. UHF 디플로이어블 휩 안테나 4조 — 피드망 위상·임피던스 재조정
   (위상오차 ±1.6°, RISK-LINK 대응), 형상·장착 인터페이스는 EM과 동일
3. 질량 0.700 kg(트랜시버+안테나), 배분 1.20kg 이내(하네스·체결 포함)

## EM 승계 리스크 종결 현황
| 리스크 | EM 상태 | FM 종결 근거 |
|---|---|---|
| RISK-LINK(EOD 링크마진 0dB) | 여유 0dB | 안테나 피드망 재조정(link-margin-fix.md) → FM 수락시험(acceptance-test-fm.md) 챔버 실측 **EOD 마진 7.8dB**(목표7.5dB 상회, 요구≥6dB 충족)로 실측 검증 완료 |
| RISK-RAIL(액추에이터 레일 3자 동시부하) | 퓨즈 정격 미확정 | EPS 3자 협상(rail-budget.md) — COMM 분기 **1.25A 완속**, 상위 공용 **3.0A 완속**, 선택성 42% 확정. COMM 수락검사(acceptance-inspection-fm.md §3)에서 확정치 인용해 COMM측 하드웨어 적합 재확인, 수락시험(acceptance-test-fm.md §2)에서 정상상태 부하(0.74A, 여유41%) 실측 확인 |

두 승계 리스크 모두 하드웨어 조치 자체는 종결됐다.

## 인도 시점 잔여 사항 (정직 공개 — 종결 아님, 이월)
1. **AOCS-COMM 동시부하(2.08A, ≤5초) 재현시험**: COMM 단독 수락시험
   범위 밖으로 두었다(rail-budget.md가 정한 대로 AIT 통합시험에서
   공용 3.0A 퓨즈 조건으로 재현 예정) — COMM 모듈 인도 판정에는
   영향 없으나 AIT 판정 전까지 "실제 동시조건 통과"는 미확인 상태다.
2. **운용 제약 이행**: rail-budget.md §3의 AOS guard band 15s 상향,
   비필수 슬루 스케줄링 금지, 초기궤도운용 실측 모니터링은 COMM
   하드웨어가 아니라 AIT/운영 절차·AOCS 운용계획에 반영되어야
   한다 — COMM 모듈 자체 조치가 아님을 명시해 이월한다.
3. **비행 실측 최종 확인**: rail-budget.md도 명시하듯 AOCS·COMM의
   시간 프로파일은 지상 분석/시험 기반 1차 추정이며, 초기궤도운용
   실측으로 최종 확인될 사항이다.

## 산출물 목록 (본 FM 모듈을 구성하는 COMM 산출물)
- examples/ksat5/deliverables/COMM/design-update-fm.md
- examples/ksat5/deliverables/COMM/fabrication-record-fm.md
- examples/ksat5/deliverables/COMM/acceptance-inspection-fm.md
- examples/ksat5/deliverables/COMM/acceptance-test-fm.md
- (EM 승계: link-budget.md, transceiver-em.md, antenna-design.md,
  bus-voltage-check.md, link-margin-fix.md)

검증: 수락검사(전 항목 합격) + 수락시험(EOD 마진 7.8dB≥7.5dB 목표,
레일전류 여유 74%/41%, 질량 0.700kg 배분내) 전건 통과로 FM 모듈
인도 조건 충족 확인. 잔여 사항 3건은 AIT/운영 단계로 명시 이월(낙관
판정 없음).
