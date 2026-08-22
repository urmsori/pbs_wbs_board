# OBC → PAY 회신: 대용량 저장·전송 대역 확인

입력: examples/ksat6/deliverables/OBC/io-board.md, examples/ksat6/deliverables/OBC/mem-board.md

REQ-PAY-OBC(PAY-01, TDI 초점면 원시 180~230Mbps → 압축 후 100~115Mbps) 회신.

## SpW 지속 처리율 여유
- io-board.md 배정: 탑재체 영상용 SpW 2채널, 채널당 물리 대역폭 200Mbps.
- 압축 후 실제 필요 처리율(100~115Mbps)은 SpW 1채널 여유(200Mbps) 안에 충분히
  들어온다. 2채널 배정은 이중화/버스트 여유용으로 유지 → **처리 가능**.

## 128GB 중 탑재체 영상버퍼 할당량
- mem-board.md 배분표: 탑재체 영상 버퍼 **118 GB** 확정.
- 압축 후 평균 115Mbps 기준 일일 저장량: 115Mbps × 86400s / 8 ≈ 1,242 GB/일
  발생 가능량이지만, 실제 촬영시간(궤도당 관측 가능 시간 제한)을 고려한
  일일 하향 목표 60GB(sysreq)에 맞춰 촬영 스케줄이 운용되므로, 118GB 버퍼는
  약 2일치 하향 지연을 흡수 가능 → **확답: 여유 충분**.

검증: SpW 채널 여유(200Mbps>115Mbps), 버퍼 118GB가 일일 60GB 목표 대비 약 2일치 여유임을 계산 확인.
