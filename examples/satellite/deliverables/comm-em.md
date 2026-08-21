# COMM EM S-band 트랜시버 검증 (Work S040)

SYS-REQ v1(S001)의 COMM 배분 요구(상향 64 kbps, 하향 S-band ≥ 2 Mbps,
링크마진 ≥ 3 dB, 질량 5 kg)에 대해 EM 트랜시버로 링크버짓과 변복조를 검증했다.

## 링크버짓 (550 km, 앙각 10°, 지상국 G/T 20 dB/K)

| 링크 | 데이터율 | 변조 | EIRP | 요구 Eb/N0 | 계산 마진 | 요구 마진 | 판정 |
|---|---|---|---|---|---|---|---|
| 하향 S-band | 2 Mbps | OQPSK | 9.0 dBW | 9.6 dB | 4.8 dB | ≥ 3 dB | PASS |
| 상향 S-band | 64 kbps | BPSK | 지상 43 dBW | 10.6 dB | 12.3 dB | ≥ 3 dB | PASS |

## 변복조 시험 (EM 벤치, 채널 시뮬레이터 경유)

| 항목 | 조건 | 요구 | 실측 | 판정 |
|---|---|---|---|---|
| 하향 BER | 2 Mbps, Eb/N0 9.6 dB | ≤ 1e-5 | 3.2e-6 | PASS |
| 상향 커맨드 수신 | 64 kbps, -110 dBm | 무오류 복호 | 10,000 프레임 무오류 | PASS |
| 도플러 추적 | ±55 kHz 스윕 | 락 유지 | 락 유지 확인 | PASS |
| EM 질량 | 실측 | ≤ 5 kg (배분) | 4.6 kg | PASS |

검증: EM 벤치에서 링크버짓 계산과 변복조 BER 시험을 수행, 전 항목 SYS-REQ 대비 PASS 확인.
