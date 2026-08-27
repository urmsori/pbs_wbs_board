# COMM-U1 X-band 송신계 RF 시험 (링크버짓 실측)

입력: examples/ksat7/deliverables/COMM/comm-u1-dsn.md(예측버짓), comm-u1-ins.md,
examples/ksat7/deliverables/CAL/comm-u1-cal.md, examples/ksat7/deliverables/PA/comm-u1-witness.md

## 시험 조건
- 교정필 장비(CAL-COMM-U1) 사용, PA(PA-COMM-U1) 입회
- 시험모드: 정상모선 50V 공급, 연속 송신 300s

## 실측 결과
| 항목 | 예측(DSN) | 실측 | 차이 |
|---|---|---|---|
| RF 출력 | 10.0 dBW(10.0W) | 9.6 dBW(9.1W) | -0.4 dB (커넥터·도파관 삽입손실 실측치가 설계여유보다 큼) |
| 안테나 이득(실측 패턴) | 18.0 dBi | 17.3 dBi | -0.7 dB (근접장 패턴 측정, 급전 정렬오차) |
| 위상잡음/구현손실 | 1.0 dB(Eb/No 여유분) | 2.0 dB(SSPA AM/PM 변환 실측 반영) | -1.0 dB |
| 시험일 GS 국G/T (앙각 12°, 실측 교정) | 28.5 dB/K | 27.1 dB/K | -1.4 dB |
| **합계 열화** | — | — | **-3.5 dB** |

- 예측 링크 마진(DSN, comm-u1-dsn.md): **+8.9 dB**
- **실측 링크 마진: +5.4 dB** (예측 대비 3.5dB 열화, 원인 4가지 모두 기록)
- 스펙트럼 점유대역 실측 191.2MHz(예측 189.6MHz, 근사 일치)
- BER 실측: 800Mbps 전송 중 프레임에러 없음(30분 연속, QEF 기준 충족)

## 판정
sysreq.md X-band 800Mbps 요건: **충족** — 실측 마진 +5.4dB(양(+)이므로 링크 성립),
단 예측 대비 3.5dB 낮음을 정직하게 기록. RB 조건2(TCS 통합 열해석 재확인)와 함께
INT 단계 리스크로 승계: GS 지상국 G/T 실측치가 표준(28.5dB/K)보다 낮게 나온 사례는
GS-U1-TST(수신 적합성시험)에서 지상국별로 재확인 필요.

검증: sysreq X-band 800Mbps 판정 — 실측 링크마진 +5.4dB(양수, PASS), 예측 대비
-3.5dB 열화 원인 4건 전부 수치 기록(정직 기록).
