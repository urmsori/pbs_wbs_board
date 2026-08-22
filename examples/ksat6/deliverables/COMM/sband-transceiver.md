# S-band 트랜시버 설계
입력: examples/ksat6/deliverables/COMM/link-budget.md

## 사양
| 항목 | 값 |
|---|---|
| 주파수 | 하향 2.2GHz / 상향 2.1GHz (S-band TT&C) |
| 하향 데이터율 | 2 Mbps (텔레메트리, QPSK) |
| 상향 데이터율 | 64 kbps (명령, BPSK) |
| 송신 RF 출력 | 2 W (33dBm), 송신단 손실 1.0dB → 링크버짓 EIRP 산출과 일치 |
| 수신감도 | −108 dBm (Eb/N0 6dB 기준 64kbps에서 요구 C/N 만족) |
| 채널부호화 | 하향 rate-1/2 컨볼루션+RS 연접(또는 동등 LDPC), 상향 rate-1/2 컨볼루션 |
| 질량 | 1.2 kg |
| 소비전력 | 대기(수신 전용) 5W, 송신 시 첨두 15W(28V 기준 0.54A), 정상 상시부하 8W(tx-load-response.md와 일치) |
| 인터페이스 | OBC와 RS-422(명령/텔레메트리 저속 채널), 커맨드 검증은 FSW-COMM이 처리 |

## 근거
- Tx 출력 2W는 링크버짓 EIRP(5.0dBW=Pt(3dBW)-손실(1dB)+안테나이득(3dBi))의 Pt=3dBW=2W와 정합.
- 대기 5W+송신 시 증분 10W → 상시부하 8W는 송신 duty가 낮은 TT&C 특성상 대기~송신 가중평균으로 근사.

검증: 링크버짓의 EIRP 역산치(Pt=3dBW)와 본 설계 Tx 출력(33dBm=3dBW) 일치 확인.
