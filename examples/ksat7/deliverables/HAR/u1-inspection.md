# HAR-U1 대전류 펄스 배선 검사 (도통·절연·전압강하 @펄스)

입력: examples/ksat7/deliverables/HAR/u1-cleaning.md, examples/ksat7/deliverables/EPS/distribution-connector-spec.md, examples/ksat7/deliverables/PA/har-u1-inspection-witness.md, examples/ksat7/deliverables/HAR/pay-req-reply.md

PA 입회 하에(PA-HAR-U1, har-u1-inspection-witness.md) 검사 수행.

## EPS 확정 데이터 대조
REQ-HAR-EPS 회신(distribution-connector-spec.md): 모선 45~55V, SAR 펄스
전용 채널 연속정격 45A/서지 90A(≤90s), 전압강하 3% 예산 = 왕복 케이블저항
**≤41.7mΩ**. 본 설계 저항(계통당 19.17mΩ 계산치)은 예산의 46% — 여유
확인.

## 도통시험 (2식)
| 계통 | 결과 |
|---|---|
| 계통1 | 도통 정상(단선 없음) |
| 계통2 | 도통 정상(단선 없음) |

## 절연저항시험 (@500VDC, 판정기준 ≥100MΩ)
| 계통 | 측정치 |
|---|---|
| 계통1 | 245 MΩ |
| 계통2 | 238 MΩ |
합격(기준 100MΩ 대비 2배 이상).

## 펄스 시 전압강하 실측
| 계통 | 실측 저항(왕복) | 시험전류 | 전압강하 | 최저모선전압 대비 |
|---|---|---|---|---|
| 계통1 단독 | 19.3 mΩ | 20.0A(PAY 이중화 정상) | 0.386V | 0.386/45=**0.86%** |
| 계통2 단독 | 19.5 mΩ | 20.0A(PAY 이중화 정상) | 0.390V | 0.390/45=**0.87%** |
| 계통1 단독 전량부담 | 19.3 mΩ | 40.0A(단일계통 고장 가정) | 0.772V | 0.772/45=**1.72%** |

EPS 저항예산(41.7mΩ) 대비도 계통당 19.3~19.5mΩ로 54% 여유.

## 판정 (sysreq.md HAR: 전압강하 ≤3% @펄스)
정상운전(0.86~0.87%)·단일고장 시나리오(1.72%) 모두 **3% 이내 — 합격**.
도통·절연저항 전 항목 합격. EMC 차폐 정량 검사는 HAR-U2-INS-01(EMC 차폐
전용 검사)에서 수행하며, 본 유닛은 동일 편조 실드 SPG 접지 적용(설계
동일).

PA 입회 결과: No Finding(har-u1-inspection-witness.md).
