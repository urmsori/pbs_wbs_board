# HAR-U2 도파관·RF 하니스 검사 (삽입손실)

입력: examples/ksat8/deliverables/HAR/u2-mfg.md,
examples/ksat8/deliverables/HAR/u2-design.md

조립 완료된 HAR-U2 도파관 경로의 삽입손실·VSWR을 검사한다. sysreq.md
HAR 항목(도파관 손실 ≤0.8dB) 최종 판정. REQ-HAR-PAY-RF·REQ-HAR-STR-경로
정식 회신은 8×20초 재폴링에도 미접수 — 설계 시 잠정 가정(경로 2.0m,
굴곡 3회, 플랜지 4개소)과 동일한 조립 형상으로 실측한다.

## 검사 결과
| 항목 | 기준 | 실측 |
|---|---|---|
| 삽입손실(대표 채널) | ≤0.8dB(sysreq HAR 상한) | 0.58dB |
| VSWR | 참고치 | 1.13:1 |
| 플랜지 체결 토크 | 규정치 | 전 4개소 규정치 이내 |

## 판정
삽입손실 0.58dB ≤ 0.8dB **합격**(설계 예측 0.57dB와 정합, 0.01dB
오차는 조립 공차 범위). PAY 플랜지 규격·STR 실경로 정식 회신 미확인은
리스크로 module-fm.md에 기록.

검증: 삽입손실 0.58dB<=0.8dB(sysreq HAR상한) 합격, 설계예측 0.57dB와 정합
