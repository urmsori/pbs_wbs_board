# EPS FM 수락검사(Acceptance Inspection)

입력: examples/ksat5/deliverables/EPS/design-update-fm.md,
examples/ksat5/deliverables/EPS/build-record-fm.md

제작자(EPS-MFG)와 독립적으로 EPS-QA가 build-record-fm.md의 결과물을
design-update-fm.md(설계 기준선) 대비 재검사한다.

## 1. 퓨즈 정격 실물 확인 (독립 재검사)
| 항목 | 설계 기준(design-update-fm.md) | 실물 확인(QA 실측) | 판정 |
|---|---|---|---|
| AOCS 분기 퓨즈 | 2.0A 표준 블로우 | 2.0A 각인 확인, 저항 실측 정상 | 합격 |
| COMM 분기 퓨즈 | 1.25A 완속 | 1.25A 각인 확인, 완속형 마킹 확인 | 합격 |
| 상위 공용 퓨즈 | 3.0A 완속 | 3.0A 각인 확인, 완속형 마킹 확인 | 합격 |

## 2. 배터리 실측 대조
- 셀 용량 실측(build-record-fm.md): 3.41/3.38 Ah — battery-sizing.md
  선정 기준(3.4Ah 대표치) 대비 -0.6%~+0.3%, 설계 여유(DoD 22%) 내
  변동으로 재계산 불필요 판정.

## 3. 치수·체결 확인
- 태양전지판 발자국·체결 홀 패턴: icd-str-eps.md 확정치와 실물 대조,
  일치 확인.
- PCU 보드 외형·체결 홀: icd-str-eps.md 확정치(96×90×15mm, PC/104
  피치)와 실물 대조, 일치 확인.
- 육안 검사(제작자 자체 점검, build-record-fm.md §3)를 QA가 전 항목
  재확인 — 불일치 없음.

## 4. 서류 확인
- 부품 이력(로트/시리얼) 전 항목 기록 존재 확인.
- 연속성 시험 결과 기록 확인.

## 5. 종합 판정
**합격.** 설계 기준선(design-update-fm.md) 대비 불일치 발견 없음.
번인시험(EPS-F04) 진행 가능.

검증: 퓨즈 3종 정격 각인·기능 실측 대조 전 항목 일치, 배터리 용량 실측이 설계 여유 내 변동임을 확인, 치수·체결 실물 대조 일치, 부품이력·시험기록 서류 완비 확인 — 종합 합격 판정.
