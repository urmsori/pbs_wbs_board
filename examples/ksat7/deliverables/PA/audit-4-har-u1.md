# PA 표본감사 4 — HAR-U1 배선검사·PA입회기록 수치 대조

입력: examples/ksat7/deliverables/HAR/u1-inspection.md, examples/ksat7/deliverables/PA/har-u1-inspection-witness.md,
examples/ksat7/deliverables/HAR/u1-thermal-analysis.md, examples/ksat7/deliverables/HAR/module-fm.md

## 감사 대상
HAR-U1 배선 검사(HAR-U1-INS-01, u1-inspection.md)의 실측 전압강하 수치가, 그 검사에
입회한 PA 입회 기록(har-u1-inspection-witness.md, PA-HAR-U1 산출물)에 정확히 반영됐는지
대조한다.

## 대조 항목
| 항목 | u1-inspection.md (실측, HAR팀 작성) | har-u1-inspection-witness.md (PA 입회기록) | 일치 |
|---|---|---|---|
| 정상운전 전압강하 | 0.86~0.87% (계통1/2 개별) | 0.85~1.70% (u1-thermal-analysis.md **설계 예측치**
  인용) | **불일치** |
| 단일고장 전압강하 | 1.72% (계통1 단독 전량부담) | 상동(범위 상한 1.70%로 뭉뚱그려 기재) | **불일치** |
| 도통·절연저항 | 도통 정상 2/2, 절연저항 245/238MΩ(≥100MΩ) | "도통 정상", "절연저항 규정치
  이상"으로 정성 기재 — 수치 자체는 미기재이나 모순은 아님 | 정성적 일치 |
| 판정(합격 여부) | 합격 (3% 이내) | 합격 (3% 이내) | 예(결론은 동일) |

## 감사 결과
**결함 발견(경미).** PA-HAR-U1(har-u1-inspection-witness.md)이 실측치(0.86~0.87%,
1.72%) 대신 설계 단계 예측치(u1-thermal-analysis.md의 0.85~1.70%)를 그대로 인용해
"실측 결과 확인"이라고 기재했다. 두 수치가 근접해(0.01~0.02%p 차이) 합격/불합격
판정에는 영향이 없으나, 입회 기록이 실측 문서(u1-inspection.md)가 작성되기 전
설계치를 실측치처럼 서술한 것은 기록 정확성 원칙(4절 "기록의 정본")에 위배된다.
원인은 PA(서비스 부서) 자신의 기재 오류다 — HAR팀 산출물(u1-inspection.md)은
정확하다.

## 조치
원인이 PA 자신의 산출물이므로 PA track으로 수정 요청(PA-HAR-U1-CORR-01, source=본
감사 AUDIT-4)을 발행하고, 즉시 PA 역할로 집어 실측치로 정정한다.

검증: 4개 항목 대조 중 전압강하 실측치 표기 1건 불일치(설계예측치 오기재) 발견,
판정 결론 자체는 무영향 — 감사 완료, 결함 1건 발견 및 수정 요청 발행.
