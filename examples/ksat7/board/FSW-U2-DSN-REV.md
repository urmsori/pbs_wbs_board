---
id: FSW-U2-DSN-REV
title: SAR 촬영 시퀀서 인터록 로직 정정(PAY 실회신 반영)
status: DONE
parent: M-FSW
source: REQ-FSW-PAY
owner: FSW-DSN-01
deliverable: examples/ksat7/deliverables/FSW/sequencer-design.md
after: -
track: FSW
started: 2026-08-27 01:58:46
finished: 2026-08-27 01:59:29
---

FSW-U2-DSN(sequencer-design.md)은 PAY 회신 대기 중 명령셋 파라미터를
placeholder로 남기고 "90s 누적시 자동정지"라는 단순 인터록만 설계했으나,
PAY 실회신(REQ-FSW-PAY,
examples/ksat7/deliverables/PAY/fsw-sequencer-reply.md)은 버스트 최대
5s·궤도당 최대 18회(누적≤90s)·버스트 간 최소간격 300s라는 더 정교한
운용 제약을 요구한다. 단순 누적 인터록으로는 버스트당 상한·간격 제약을
누락하므로 로직을 정정해야 한다(규칙 4절 재작업).
검증: 4중 인터록(5s버스트·18회·300s간격·90s누적) 확정 반영
