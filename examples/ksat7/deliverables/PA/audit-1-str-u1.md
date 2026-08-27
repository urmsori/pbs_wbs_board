# PA 표본감사 1 — STR-U1 정현진동시험(1차모드 NCR) 기록 대조

입력: examples/ksat7/board/STR-U1-TST-SINE.md, examples/ksat7/deliverables/STR/str-u1-tst-sine.md,
examples/ksat7/deliverables/STR/str-u1-anl-s2.md, examples/ksat7/deliverables/STR/module-fm.md,
examples/ksat7/board/M-STR.md

## 감사 대상
STR-U1 정현진동시험(STR-U1-TST-SINE)에서 발생한 1차모드 미충족(NCR/RED)이 module-fm.md
(모듈 인도 요약)까지 정직하게, 수치 일관되게 승계되었는지 대조한다.

## 대조 항목
| 항목 | STR-U1-TST-SINE 게시글/산출물 | module-fm.md | 일치 |
|---|---|---|---|
| 산출물 파일 존재 | str-u1-tst-sine.md 존재 확인 | 동일 파일 인용 | 예 |
| "입력:" 명시 | str-u1-ins.md, str-u1-cal-cert.md, str-u1-fac-booking.md,
  str-u1-witness.md, str-u1-anl-s2.md 명시 | — | 예 |
| 검증 한 줄 | 게시글 본문 "검증: 실측1차모드30.4Hz<35Hz — 미충족(NCR/RED)..." | — | 예 |
| ANL-S2 예측치 | 약 29.5Hz | 29.5Hz 인용 | 예 |
| 실측 1차모드 | 30.4Hz(ANL-S2 대비 3% 이내 일치) | 30.4Hz 인용 | 예 |
| 판정 | 미충족(NCR/RED), rev.2 이관 | 미충족(NCR/RED), rev.2 이관 | 예 |
| 질량 | (별도 게시글) 41.3kg | 41.3kg 인용, sysreq 충족 판정 | 예 |
| 준정적10g | 손상無 | 손상無, 충족 | 예 |

## 감사 결과
**결함 없음.** STR-U1의 1차모드 미충족은 은폐되지 않고 STR-U1-TST-SINE 게시글의
검증 줄, str-u1-tst-sine.md 산출물, module-fm.md, M-STR 게시글 검증 줄까지 4곳
모두에서 동일 수치(30.4Hz)로 일관되게 기록되었다. sysreq 3항목 중 2항목 충족·
1항목 미충족(오픈 NCR)이라는 판정도 각 문서에서 동일하게 인용된다. 산출물 파일이
실제로 존재하며 입력이 명시되어 있다. **불시 감사는 이 경우 결함이 아니라 정상
경로(재작업/NCR 관리)가 정직하게 작동하고 있음을 확인했다.**

검증: 4개 문서(게시글·산출물·module-fm·M-STR) 간 1차모드 수치(30.4Hz) 및 판정
(NCR/RED) 전건 일치 확인, 산출물 실재·입력 명시 확인 — 감사 완료, 결함 없음.
