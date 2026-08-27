---
id: FSW-U1-DSN
title: 비행SW 코어 설계(스케줄러·안전모드·원격측정/명령)
status: DONE
parent: M-FSW
source: -
owner: FSW-DSN-01
deliverable: examples/ksat7/deliverables/FSW/core-design.md
after: -
track: FSW
started: 2026-08-27 01:49:47
finished: 2026-08-27 01:53:48
---

sysreq FSW(비행 관리 전 기능 + 안전모드)를 만족하는 비행SW 코어(태스크 스케줄러,
안전모드 진입/복귀 로직, TM/TC 처리, 요 스티어링 자세제어 인터페이스)를
설계해야 코드리뷰·검토회로 넘길 수 있다. 요 스티어링 제어 인터페이스는
AOCS와 REQ-FSW-AOCS로 협상해야 한다.
검증: 스케줄러12태스크·안전모드3조건·TM/TC구현, AOCS제어주기 잠정(무응답)
