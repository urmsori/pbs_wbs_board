---
id: OBC-U1-DSN
title: OBC 프로세서보드·2TB 저장부 상세설계
status: DONE
parent: M-OBC
source: -
owner: OBC-DSN-01
deliverable: examples/ksat7/deliverables/OBC/obc-storage-design.md
after: -
track: OBC
started: 2026-08-27 01:49:29
finished: 2026-08-27 01:53:34
---

sysreq OBC(처리여유≥50%, 원시 2TB, SpW/CAN)를 만족하는 CDH 프로세서보드와
2TB 대용량 저장장치(레코더)를 상세설계해야 제작에 넘길 수 있다. 저장 경로의
쓰기대역폭은 PAY의 SAR 원시데이터율에 달려 있어 REQ-OBC-PAY 협상이 필요하다.
검증: 처리여유52%, 저장2.0TB, PAY데이터율 잠정(무응답 기록)
