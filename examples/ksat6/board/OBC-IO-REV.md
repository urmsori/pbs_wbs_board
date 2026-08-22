---
id: OBC-IO-REV
title: I/O보드 SpW 채널 배정 정정(PAY 실회신 반영)
status: DONE
parent: M-OBC
source: REQ-OBC-PAY
owner: OBC-IO-01
deliverable: examples/ksat6/deliverables/OBC/io-board.md
after: -
track: OBC
started: 2026-08-22 01:28:12
finished: 2026-08-22 01:28:30
---

OBC-IO(io-board.md)는 PAY 회신 대기 중 SpW 채널을 "영상용 2채널"로 잠정
배정했으나, PAY의 실제 회신(REQ-OBC-PAY,
examples/ksat6/deliverables/PAY/obc-datarate-reply.md)은 "영상 1링크(≥150Mbps
여유)+명령/상태 1링크(분리)" 구성을 요청했다. 잠정 가정과 실측 요구의
구성이 달라 io-board.md의 채널 배정표를 갱신해야 한다(규칙 4절 재작업 —
DONE인 OBC-IO는 되돌리지 않고 이 정정 게시글로 고친다).
산출물: examples/ksat6/deliverables/OBC/io-board.md 갱신(SpW 채널 용도 정정).
검증: PAY 실회신 요구치(영상≥150Mbps,명령≤2Mbps) 대비 배정대역폭(200Mbps×2채널) 여유 확인, 채널수 변동없음(4채널) 확인
