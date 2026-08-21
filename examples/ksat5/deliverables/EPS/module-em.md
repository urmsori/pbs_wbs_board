# EPS EM 모듈 인도 문서 (M-EPS)

입력: examples/ksat5/deliverables/EPS/power-generation.md,
examples/ksat5/deliverables/EPS/power-conditioning.md,
examples/ksat5/deliverables/EPS/battery-sizing.md,
examples/ksat5/deliverables/EPS/test-plan.md,
examples/ksat5/deliverables/EPS/icd-str-eps.md,
examples/ksat5/deliverables/EPS/icd-comm-eps.md

SE-01의 인도 요청(M-EPS)에 대한 EPS 팀 최종 통합 문서. EPS-01~04
(발생계·조절계·배터리·시험계획) 산출물을 모듈 단위로 통합한다.

## 1. 모듈 구성 요약
| 서브시스템 | 산출물 | 핵심 결과 |
|---|---|---|
| 전력 발생계 | power-generation.md | 몸체 2면+전개 날개 2매, EOL 궤도평균 발생 ≈20.6W (요구 ≥20W 충족) |
| 전력조절계(PCU) | power-conditioning.md | S3R+BDR, 1차버스 8.4V(EOD 6.8V)/5V/3.3V/액추에이터 레일 4계통, 보호회로 포함 |
| 배터리 | battery-sizing.md | 2S1P 18650(3.4Ah), 팩 에너지 ≈25.8Wh, 식 구간 DoD ≈22%, 첨두전류 여유 확인 |
| 시험계획 | test-plan.md | 발생·레귤레이션·부하스텝·보호회로·액추에이터레일 5개 시험 항목·기준 |

## 2. 질량 예산 (확정, ICD-STR-EPS 갱신 반영)
| 항목 | 질량(kg) |
|---|---|
| 태양전지판(장착부 포함) | 0.80 |
| PCU | 0.15 |
| 배터리(확정: 2S1P, battery-sizing.md) | 0.22 |
| 하니스 여유 | 0.10 |
| **EPS 모듈 총질량** | **1.27** |
| EPS 배분(sysreq) | 3.0 |
| 여유 | 1.73 |

배터리 질량이 잠정치(0.25kg, ICD-STR-EPS)에서 확정치(0.22kg)로
갱신됐다 — STR 팀에는 필요 시 소폭 하향 갱신으로 재확인 가능(마진
방향이므로 STR 설계 변경 불필요).

## 3. 인터페이스 확정 사항
- **ICD-STR-EPS**: 태양전지판/PCU 장착 발자국·홀 패턴·질량 확정 회신
  완료(icd-str-eps.md). 배터리 잠정치는 위 2항 확정치로 대체.
- **ICD-COMM-EPS**: 초기 설계(5V 레일 공용) 검토 결과 송신 엣지에서
  레일 정격 20% 초과가 확인되어 COMM PA를 액추에이터 레일(8.4V)로
  이설하도록 권고했고, COMM 회신(rev.2, icd-eps-comm-power.md)에서
  반영을 확인했다. 이에 따라 5V 레일은 로직단 부하만 지므로 여유
  문제는 해소된 것으로 판단한다.
- **ICD-EPS-COMM / ICD-EPS-AOCS**: 배터리 용량 산정에 필요한 부하
  프로파일을 COMM·AOCS로부터 회신받아 battery-sizing.md에 반영 완료.

## 4. 발생 전력 요구 충족 확인
EOL 궤도평균 발생 ≈20.6W ≥ sysreq 요구 20W (power-generation.md).
BOL 피크 발생 ≈101W로 션트 레귤레이터(정격 120W) 여유 내.

## 5. 잔여 리스크 / 후속 조치(EPS 범위 밖)
- COMM 링크마진(EOD 6.8V 조건, 0.3dB)에 대한 재확인은 COMM-04
  담당으로, EPS 배터리 전압 범위(6.8~8.4V) 자체는 본 설계와 일치하여
  EPS 측 조치 불필요.
- OBC 5V 부하는 가정치(0.4A)로 설계됐으므로, OBC 확정치 도착 시
  power-conditioning.md·battery-sizing.md 마진 재확인 권장.

검증: 4개 내부 Work(EPS-01~04)와 2건의 대외 ICD 회신이 모두 정합됨을 확인 — 발생(20.6W≥20W), 질량(1.27kg≤3.0kg), 배터리(DoD 22%≤25~30% 한도), 인터페이스(STR/COMM 확정 회신 반영)로 EM 모듈 인도 기준 충족.
