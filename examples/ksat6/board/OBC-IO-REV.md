---
id: OBC-IO-REV
title: I/O보드 SpW 채널 배정 정정(PAY 실회신 반영)
status: TAKEN
parent: M-OBC
source: REQ-OBC-PAY
owner: OBC-IO-01
deliverable: -
after: -
track: OBC
started: 2026-08-22 01:28:12
finished: -
---

OBC-IO(io-board.md)는 PAY 회신 대기 중 SpW 채널을 "영상용 2채널"로 잠정
배정했으나, PAY의 실제 회신(REQ-OBC-PAY,
examples/ksat6/deliverables/PAY/obc-datarate-reply.md)은 "영상 1링크(≥150Mbps
여유)+명령/상태 1링크(분리)" 구성을 요청했다. 잠정 가정과 실측 요구의
구성이 달라 io-board.md의 채널 배정표를 갱신해야 한다(규칙 4절 재작업 —
DONE인 OBC-IO는 되돌리지 않고 이 정정 게시글로 고친다).
산출물: examples/ksat6/deliverables/OBC/io-board.md 갱신(SpW 채널 용도 정정).
