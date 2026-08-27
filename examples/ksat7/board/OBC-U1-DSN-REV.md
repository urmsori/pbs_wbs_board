---
id: OBC-U1-DSN-REV
title: OBC 저장부 기록대역폭·SpW 채널 정정(PAY 실회신 반영)
status: DONE
parent: M-OBC
source: REQ-OBC-PAY
owner: OBC-DSN-01
deliverable: examples/ksat7/deliverables/OBC/obc-storage-design.md
after: -
track: OBC
started: 2026-08-27 01:58:07
finished: 2026-08-27 01:58:29
---

OBC-U1-DSN(obc-storage-design.md)은 PAY 회신 대기 중 기록대역폭 1.2Gbps·
SpW 2채널을 잠정 설계했으나, PAY 실회신(REQ-OBC-PAY,
examples/ksat7/deliverables/PAY/obc-datarate-reply.md)은 스팟모드 순간 첨두
3.2Gbps·SpW 4채널(PAY 입력용)을 요구한다. 잠정 가정이 실제 요구에 못
미쳐 저장부 설계를 정정해야 한다(규칙 4절 재작업 — DONE인 OBC-U1-DSN은
되돌리지 않고 이 정정 게시글로 고친다).
검증: 기록대역폭 3.6Gbps≥첨두3.2Gbps(마진12.5%), SpW 5채널 확정
