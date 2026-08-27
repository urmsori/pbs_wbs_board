# PA 표본감사 2 — MECH-U1 전개시험 기록 대조

입력: examples/ksat7/board/MECH-U1-TST.md, examples/ksat7/deliverables/MECH/mech-u1-tst.md,
examples/ksat7/deliverables/MECH/module-fm.md

## 감사 대상
MECH-U1 전개시험(MECH-U1-TST) 실측 결과가 module-fm.md에 정확히 승계되었는지 대조한다.

## 대조 항목
| 항목 | MECH-U1-TST 게시글/산출물 | module-fm.md | 일치 |
|---|---|---|---|
| 산출물 파일 존재 | mech-u1-tst.md 존재 확인 | 동일 파일 계열 인용 | 예 |
| "입력:" 명시 | mech-u1-ins.md, mech-u1-fac-booking.md, mech-u1-anl-s2.md 명시 | — | 예 |
| 검증 한 줄 | 게시글 본문 "검증: 실측전개충격37.1g≤40g, 단일고장허용 — 충족" | — | 예 |
| 전개충격 실측 | 37.1g(3회 평균, 재현성 37.1±0.6g) | 37.1g 인용, 마진2.9g(7.3%) | 예 |
| ANL-S2 예측치 | 36.4g | (오픈리스크 항목에 36.4g 언급 없음 — 34.5g/36.4g/37.1g 3단계 값이
  모두 module-fm.md 표에 순서대로 인용됨) | 예 |
| 단일고장 허용 | 릴리즈 1계열 강제비활성, 병렬계열 정상전개 확인 | 단일고장 허용 실측 확인, 충족 | 예 |
| FAC 서비스 연계 | after: FAC-MECH-U1 | "CM/PUR/FAC 서비스 요청 전건 처리 완료" | 예 |

## 감사 결과
**결함 없음.** 전개충격 실측치(37.1g)가 잠정설계(34.5g)→재해석(36.4g)→실측(37.1g)의
3단계 수치 이력과 함께 module-fm.md에 정확히 인용되고, 마진(2.9g, 7.3%)도 일치한다.
게시글 검증 줄과 산출물 판정이 동일하며, 산출물 파일이 실제로 존재한다. FAC 서비스
요청(FAC-MECH-U1)이 after로 정상 종속되어 있다.

검증: 3단계 수치 이력(34.5→36.4→37.1g) 및 마진(7.3%) 일치, 산출물 실재·입력 명시
확인 — 감사 완료, 결함 없음.
