# EPS FM 모듈 인도 문서 (M2-EPS)

입력: examples/ksat5/deliverables/EPS/design-update-fm.md,
examples/ksat5/deliverables/EPS/build-record-fm.md,
examples/ksat5/deliverables/EPS/acceptance-inspection-fm.md,
examples/ksat5/deliverables/EPS/burn-in-fm.md,
examples/ksat5/deliverables/EPS/rail-budget.md

SE-01의 FM 인도 요청(M2-EPS)에 대한 EPS 팀 최종 통합 문서. 사람 단위
분해(EPS-F01 설계갱신/EPS-DSN → EPS-F02 제작/EPS-MFG → EPS-F03
수락검사/EPS-QA → EPS-F04 번인시험/EPS-TST → 본 문서/EPS-LEAD)
결과를 통합한다.

## 1. EM 승계 리스크 종결 확인
| 리스크 | EM 상태(integration-report.md) | FM 종결 근거 |
|---|---|---|
| 액추에이터 레일 동시부하(2.08A) | 미검토(신규 발견, 이월) | RISK-RAIL(rail-budget.md)에서 3자 협상으로 분기 2.0A/1.25A + 상위 3.0A 완속 퓨즈 확정, design-update-fm.md 반영, burn-in-fm.md 실물 시험으로 실증 — **종결** |
| COMM EOD 링크마진 0dB | 요구 충족·여유 없음(이월) | COMM 소관(RISK-LINK, link-margin-fix.md로 COMM이 별도 해결) — EPS 범위 밖, 본 인도에 영향 없음 |

## 2. 모듈 상태 요약
| 항목 | FM 확정치 | 근거 |
|---|---|---|
| 발생 전력 | EOL 궤도평균 ≈20.6W(EM과 동일, 변경 없음) | design-update-fm.md §1 |
| 배터리 | 2S1P 18650, 실측 3.41/3.38Ah | acceptance-inspection-fm.md §2 |
| 질량 | 1.27kg(EM 확정치 유지, 퓨즈 추가분 무시 가능) | design-update-fm.md §4 |
| 분기 퓨즈 | AOCS 2.0A / COMM 1.25A / 상위공용 3.0A(완속) | rail-budget.md, 실물 검사·시험 전 단계 확인 |
| 수락검사 | 합격(불일치 없음) | acceptance-inspection-fm.md |
| 번인시험 | 합격(초기고장 없음, 공유레일 4시나리오 전건 통과) | burn-in-fm.md |

## 3. 운용 인터페이스 노트 (AIT/AOCS 전달용)
design-update-fm.md §3의 운용 제약(AOS guard band 15s 상향, 비필수
슬루의 교신 시간대 스케줄링 금지, 초기 궤도 운용 중 레일 전류
텔레메트리 모니터링)은 EPS 하드웨어 조치가 아니므로 이 인도로
종결되지 않는다 — AIT/AOCS가 FM 운용 절차에 반영해야 하는 잔여
항목으로 명시해 인계한다.

## 4. 종합 판정
EPS FM 모듈은 설계갱신·제작·수락검사·번인시험을 모두 통과했고, EM
승계 리스크 중 EPS 소관인 액추에이터 레일 동시부하는 하드웨어(퓨즈
정격)와 실물 시험으로 종결했다. 운용 절차 항목(§3)은 AIT/AOCS로
인계하는 조건부 사항으로 정직하게 명시한다.

검증: EPS-F01~04 전건 DONE 확인, EM 대비 발생/질량 불변 확인, rail-budget 정격의 실물 시험 실증(burn-in-fm.md) 확인, 미종결 운용 항목은 인계 사항으로 별도 명시.
