# X-band 송신기 설계
입력: examples/ksat6/deliverables/COMM/link-budget.md, examples/ksat6/deliverables/OBC/reply-comm-downlink-interface.md, examples/ksat6/deliverables/EPS/comm-xtx-power-allowance.md

## 사양
| 항목 | 값 |
|---|---|
| RF 출력 | 10 W (40dBm), SSPA, 효율 30% |
| 변조 | QPSK + LDPC(또는 rate-1/2 컨볼루션+RS(223,255) 연접) |
| 데이터율 | 150 Mbps |
| 데이터 입력 인터페이스 | SpaceWire 1채널(물리 200Mbps), OBC I/O보드 SpW#와 직결(REQ-COMM-OBC 회신) |
| 입력 버퍼 | 64 Mbit(8MB) — OBC 권고치 그대로 채택, 150Mbps×0.4s≈60Mbit 버스트 흡수 |
| 프레이밍 | CCSDS AOS 가상채널 VC0(HK)/VC1(영상), RS(223,255) 부호화는 송신기 내부 수행 |
| 핸드셰이크 | OBC "TX_READY"→송신기 ACK, 종료 "TX_END"+프레임카운트 확인(OBC 회신 그대로 채택) |
| DC 입력 전력(첨두) | 40 W (33.3W SSPA + 5W 모뎀/여자기 + 1.7W 여유) = tx-load-response.md와 일치 |
| 첨두전류(28V) | 1.43 A |
| 질량 | 1.8 kg |

## EPS 허용치 대비 확인
- EPS 허용(REQ-COMM-EPS 회신): 첨두 70W/4A, duty 제약 없음(퓨즈 열정격 내).
- 본 설계 사용치: 첨두 40W/1.43A, duty 약 4%.
- **여유: 전력 30W(43%), 전류 2.57A — 충분한 마진.**

## 데이터 처리량 대비 확인
- OBC 회신 SpW 물리속도 200Mbps > 요구 150Mbps, 여유 50Mbps(33%).
- 버퍼 64Mbit이 150Mbps 버스트 0.4초 분(60Mbit)을 초과 — 여유 4Mbit(6.7%),
  **빠듯하다(정직하게 기록)**. 다운링크 프레임 손실 방지를 위해 OBC 판독
  버스트를 0.35초 이하로 낮추도록 후속 협의 권고(현재 설계로는 규정 마진
  없이 운용).

검증: EPS 허용치(70W/4A) 대비 사용치(40W/1.43A) 여유 확인, OBC 버퍼(64Mbit)
대비 버스트 소요(60Mbit) 여유가 6.7%로 빠듯함을 그대로 기록.
