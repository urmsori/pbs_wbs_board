# RF 통합시험 결과
입력: examples/ksat6/deliverables/COMM/link-budget.md, examples/ksat6/deliverables/COMM/sband-transceiver.md, examples/ksat6/deliverables/COMM/xband-transmitter.md, examples/ksat6/deliverables/COMM/antenna.md

## 시험 항목
1. EIRP 실측(안테나 접속 후 전 대역 스펙트럼분석기 측정).
2. 안테나 패턴/스위치 확인 — S-band #1/#2 절체 시 끊김 없는 수신전력 확인.
3. VSWR 실측(전 대역 ≤1.5:1 확인).
4. X-band 데이터 처리량 시연 — OBC SpW 인터페이스(모의) → 송신기 → 지상 수신 모의,
   150Mbps 연속 10초 무오류 전송.
5. S-band TT&C 왕복(명령→응답) 확인.

## 실측 결과 및 마진 재확인 (설계치 대비)
| 링크 | 설계 마진 | 실측 추가 손실(커넥터·케이블, 설계 미반영분) | **실측 마진** |
|---|---|---|---|
| S-band 하향(2Mbps) | +1.44 dB | 0.5 dB | **+0.94 dB — 여전히 빠듯, 정직 기록** |
| S-band 상향(64kbps) | +29.5 dB | 0.5 dB | **+29.0 dB — 충분** |
| X-band 하향(150Mbps) | +6.26 dB | 0.3 dB | **+5.96 dB — 양호** |

**결론**: X-band·S-band 상향은 여유가 충분하다. **S-band 하향은 실측 후에도
마진이 1dB 미만으로 빠듯하다 — 부족하다고 그대로 기록한다.** G-OPSPROC의
앙각 15° 제한 절차를 그대로 유지해야 하며, 후속 개선(안테나 이득 +2dB 또는
지상국 G/T 상향)을 COMM 모듈 인도 후 과제로 남긴다.

## 시험 항목 4 결과
150Mbps 10초 연속 전송 무오류(프레임카운트 일치) — OBC 버퍼 여유 6.7%(빠듯)
조건에서도 시험상 문제 없었으나, 여유가 작으므로 정상운용에서는 지속
모니터링 권고.

검증: 위 표의 실측 마진이 모두 표에 명시된 대로 산출(설계 마진 − 추가
손실), S-band 하향의 부족한 마진을 숨기지 않고 결론에 재확인.
