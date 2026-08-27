# COMM-U1 X-band 800Mbps 송신계(DVB-S2) 설계

입력: examples/ksat7/deliverables/SE/sysreq.md, REQ-COMM-OBC(→OBC/comm-interface-spec.md),
REQ-COMM-STR(→STR/comm-antenna-mount-spec.md), REQ-COMM-EPS(→EPS/comm-tx-power-budget.md)

## 1. 판정 대상 (sysreq.md 인용)
- 데이터: **X-band 800 Mbps**, 원시 2TB 저장 → 본 설계가 만족해야 할 수치.
- 모선 50V±5V, SAR 첨두 펄스 부하 1.8kW 최대 90s/궤도(EPS 상호배제 고려).
- STR 1차구조 ≤45kg, 1차모드 ≥35Hz(SAR 안테나 장착 상태).

## 2. ICD 협상 결과 (REQ-COMM-OBC/STR/EPS 회신 완료 — 폴링 중 3건 모두 회신 도착)
- **OBC**: SpaceWire 다운링크 전용 1채널 850Mbps 보장(하향 800Mbps 대비 마진 6.25%),
  재생 elastic 버퍼 256Mbit, 언더런 마진 ≥15%. (GS 접촉시간 8분은 OBC측 잠정 가정 —
  GS-U1-OPS에서 실측 접촉시간 확정 필요.)
- **STR**: 장착면 -Y측판(지구지향 인접), 질량배정 3.0kg, 지구지향 시야 ±70°(SAR/SA
  가림 없음), 4점 M8 볼트 PCD150mm, 장착부 국부강성 1차모드 기여 <0.1Hz(무시 가능).
- **EPS**: 송신 채널 첨두 DC 60W 배정(지속시간 제한 없음, 교신패스 최대 600s 연속),
  SAR 펄스와 동시 운용 허용(급전 경로 분리, 단 정상모선 총부하 540W EOL 이내),
  모선 리플 ≤200mVpp, 부하스텝 과도 ≤±2%/5ms.

## 3. 송신계 구성
DVB-S2 변조기 → X-band 업컨버터(8.1GHz) → SSPA(GaN, 효율 28%) → 도파관 →
고이득 안테나(18dBi, -Y측판 장착, STR PCD150 M8×4).

- 변조: DVB-S2, 32APSK, 부호율 5/6, 스펙트럼효율 4.43 bit/symbol, roll-off 0.05
- 심볼레이트 = 800Mbps / 4.43 ≈ **180.6 Msps** → 점유대역 ≈189.6MHz
- RF 출력(HPA): **10.0 W (40.0 dBm)**
- DC 소모: SSPA 35.7W(효율28%) + 변조기/업컨버터/드라이버 8.0W = **43.7W**
  → EPS 배정 60W 대비 마진 16.3W(27%), STR 질량배정 3.0kg 내 안테나 확정.

## 4. 링크버짓 (예측)
| 항목 | 값 |
|---|---|
| TX RF 출력 | 10.0 dBW |
| TX 안테나 이득 | 18.0 dBi |
| EIRP | 28.0 dBW |
| 최악 슬랜트레인지(550km, 앙각10° 마스크) | 1816 km |
| 자유공간손실(8.1GHz) | -175.8 dB |
| 대기/지향/편파 손실 | -2.0 dB |
| 수신 EIRP | -149.8 dBW |
| GS G/T (13m급) | 28.5 dB/K |
| 볼츠만상수 | -228.6 dBW/K/Hz |
| **C/N0** | **107.3 dBHz** |
| 데이터레이트 800Mbps (10log₁₀) | 89.0 dBHz |
| 요구 Eb/No(32APSK 5/6, BER1e-7)+구현손실1.0dB | 9.4 dB |
| 요구 C/N0 | 98.4 dBHz |
| **예측 링크 마진** | **+8.9 dB** |

판정: sysreq.md X-band 800Mbps 요건을 32APSK 5/6·180.6Msps로 예측 충족(마진 +8.9dB).
실측 마진은 COMM-U1-TST에서 정직 기록(예측 대비 하향 가능성 있음 — PA 백오프, 실제
지향오차 등 미반영 요소).

## 5. 확정 인터페이스
- OBC↔변조기: SpW 850Mbps 채널, 256Mbit 버퍼(OBC 회신 그대로 채택)
- STR 장착: -Y측판, 3.0kg, 4×M8 PCD150mm(STR 회신 그대로 채택)
- EPS 급전: 50V 버스, 첨두 43.7W(배정 60W 이내, 마진 16.3W)

검증: sysreq X-band 800Mbps → 32APSK 5/6 180.6Msps로 예측 충족(마진 +8.9dB), 3개
ICD(OBC/STR/EPS) 전부 실회신 수치 반영, DC 43.7W<배정60W, 안테나 3.0kg=배정3.0kg.
