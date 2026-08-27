---
id: FSW-U1-DSN-REV
title: 비행SW 코어 요 스티어링 제어주기·신호 정정(AOCS 실회신 반영)
status: DONE
parent: M-FSW
source: REQ-FSW-AOCS
owner: FSW-DSN-01
deliverable: examples/ksat7/deliverables/FSW/core-design.md
after: -
track: FSW
started: 2026-08-27 01:58:46
finished: 2026-08-27 01:59:29
---

FSW-U1-DSN(core-design.md)은 AOCS 회신 대기 중 제어주기 20Hz(잠정)를
가정했으나, AOCS 실회신(REQ-FSW-AOCS,
examples/ksat7/deliverables/AOCS/fsw-interface-reply.md)은 제어주기 10Hz와
5종 신호 목록(YAW_STEER_CMD·ATT_FB·RATE_FB·RWA_TORQUE_CMD·MODE_STATUS)을
확정했다. 잠정치와 달라 코어 제어루프 설계를 정정해야 한다(규칙 4절
재작업 — DONE인 FSW-U1-DSN은 되돌리지 않고 이 정정 게시글로 고친다).
검증: 제어주기 10Hz·신호5종 확정 반영
