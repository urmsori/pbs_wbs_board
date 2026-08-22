# OBC → COMM 회신: X-band 다운링크 데이터 인터페이스

입력: examples/ksat6/deliverables/OBC/io-board.md, examples/ksat6/deliverables/OBC/mem-board.md

REQ-COMM-OBC(링크버짓 C-LB) 회신.

- 인터페이스: SpaceWire, io-board.md의 SpW 4채널 중 COMM(X-band) 송신 버퍼용
  1채널 전용 배정. 링크 속도: SpW 물리 200Mbps(X-band 150Mbps 하향 목표 대비 여유).
- 송신기 측 버퍼 최소 깊이: 64 Mbit(약 8MB) 권고 — OBC 대용량메모리(mem-board.md
  탑재체 영상버퍼 118GB)에서 벌크 판독 시 버스트 전송 흡수용.
- 프레이밍/전송 프로토콜: CCSDS AOS 가상채널(VC0=상태HK, VC1=영상 벌크),
  Reed-Solomon(223,255) 부호화는 송신기단에서 수행.
- 다운링크 시작/정지 핸드셰이크: OBC가 SpW 링크로 "TX_READY" 신호 후 송신기
  ACK, 종료 시 "TX_END" + 프레임카운트 일치 확인.

검증: SpW 채널 배정이 io-board.md 채널표와 일치, 버퍼 깊이가 150Mbps×수백ms 버스트를 흡수함을 계산 확인(150Mbps×0.4s≈60Mbit<64Mbit 여유).
