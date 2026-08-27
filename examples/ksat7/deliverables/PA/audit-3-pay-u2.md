# PA 표본감사 3 — PAY-U2 펄스 실증·NESZ 판정시험 기록 대조

입력: examples/ksat7/deliverables/PAY/u2-pulse-test.md, examples/ksat7/deliverables/PAY/u1-radiation-test.md,
examples/ksat7/deliverables/PAY/module-fm.md

## 감사 대상
PAY-U2 펄스 실증·NESZ 종합판정(u2-pulse-test.md)이 PAY-U1 방사시험 실측치를 정확히
인용해 종합했는지, module-fm.md까지 수치가 일관되게 승계됐는지 대조한다.

## 대조 항목
| 항목 | u1-radiation-test.md | u2-pulse-test.md | module-fm.md | 일치 |
|---|---|---|---|---|
| 안테나측 손실 | 0.71 dB(실측) | 0.71dB(PAY-U1-TST 실측, 인용) | — | 예 |
| 첨두DC입력 | — | 1.79kW(목표1.8kW) | 1.79kW 인용 | 예 |
| 버스트 누적시간 | — | 90.4s(공차내, 목표≤90s) | 90.4s(공차내) 인용 | 예 |
| NESZ | (안테나측 배분 -20dB 달성 확인) | -19.6dB(요구≤-19dB, 마진0.6dB) | -19.6dB 인용 | 예 |
| "입력:" 명시 | u1-ins.md, CAL/FAC/PA 서비스 산출물 3건 | u2-ins.md, pay-u2-cal.md,
  u1-radiation-test.md, sysreq.md | u1-*/u2-* 전체 목록 | 예 |
| 서비스 요청 처리 | CAL-PAY-U1, FAC-PAY-U1, PA-PAY-U1 DONE | CAL-PAY-U2 DONE | "7건 전량 DONE" 기재 | 예 |

## 감사 결과
**결함 없음.** PAY-U2-TST가 PAY-U1-TST 실측치(안테나측 손실 0.71dB)를 그대로 인용해
NESZ를 종합 계산했고(-19.6dB), 그 결과가 module-fm.md에 동일 수치로 재인용된다.
서비스 요청 처리 건수(CM 1·PUR 2·CAL 2·FAC 1·PA 1 = 7건)도 module-fm.md 기재와
실제 board 상 DONE 게시글 수가 일치한다(직접 대조: CM-PAY-U1, PUR-PAY-U1,
PUR-PAY-U2, CAL-PAY-U1, CAL-PAY-U2, FAC-PAY-U1, PA-PAY-U1 = 7건 DONE 확인).

검증: NESZ 계산 근거(안테나측손실0.71dB) 및 결과(-19.6dB) 3개 문서 간 일치, 서비스
요청 7건 DONE 카운트 실제 board와 일치 확인 — 감사 완료, 결함 없음.
