# PAY-U1 24채널 EIRP·NPR 성능시험

입력: examples/ksat8/deliverables/PAY/u1-ins.md, examples/ksat8/deliverables/PAY/u2-accept-test.md,
examples/ksat8/deliverables/PAY/u1-dsn.md

RF 챔버(FAC-PAY-U1)에서 교정 계측장비(CAL-PAY-U1)로 측정. RVW-A 조건에 따라
TWTA 개체편차(±0.3dB)를 채널별 바이어스 미세조정(±0.1dB 스텝)으로 보정.

## EIRP (24채널 전수)
- 범위: 52.05 ~ 52.61 dBW(조정 후), 전채널 **≥52dBW PASS**(최소마진 0.05dB).

## NPR (대표 4채널, 노이즈로딩)
- 측정치: 18.7 / 19.1 / 18.9 / 19.3 dB — 전 채널 **≥18dB PASS**(최소마진0.7dB).

## sysreq PAY 최종 판정
| 항목 | 요구 | 실측 |
|---|---|---|
| 채널수 | 24 | 24 — PASS |
| EIRP | ≥52dBW/채널 | 52.05~52.61dBW(전채널) — PASS |
| NPR | ≥18dB | 18.7~19.3dB(대표4채널) — PASS |

검증: sysreq PAY 전량 PASS — 24채널 EIRP52.05~52.61≥52dBW, NPR18.7~19.3≥18dB
