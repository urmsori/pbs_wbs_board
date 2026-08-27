---
id: REQ-FSW-AOCS
title: "[FSW→AOCS] 요 스티어링 제어 인터페이스(주기·신호) 확정 요청"
status: DONE
parent: M-FSW
source: FSW-U1-DSN
owner: AOCS-U1-DSN-01
deliverable: examples/ksat7/deliverables/AOCS/fsw-interface-reply.md
after: -
track: AOCS
started: 2026-08-27 01:54:40
finished: 2026-08-27 01:55:02
---

비행SW 코어(FSW-U1-DSN)가 sysreq.md 지향 0.02°(3σ)·요 스티어링 ±4°·안정도
0.003°/s를 관리하려면 AOCS와의 제어 인터페이스(제어주기 Hz, 요 스티어링
명령/피드백 신호 목록 — 형식·갱신주기·단위)를 합의해야 한다.
산출물: AOCS 팀이 제어주기(Hz)와 요 스티어링 신호 목록(이름·형식·주기·단위)을
회신 문서로 남긴다. FSW는 이를 입력으로 코어 제어루프 인터페이스를 확정한다.
검증: 제어주기·신호목록 회신, sysreq 안정도 0.003°/s 배분과 정합 확인
검증: 제어주기10Hz(대역폭0.79Hz의12.7배), 신호5종 회신
