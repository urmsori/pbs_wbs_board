---
id: REQ-FSW-AOCS
title: "[FSW→AOCS] 제어 알고리즘 인터페이스(제어주기·센서/액추에이터 신호) 요청"
status: DONE
parent: FSW-AOCS
source: FSW-AOCS
owner: AOCS-DSN-01
deliverable: examples/ksat6/deliverables/AOCS/fsw-if-reply.md
after: -
track: AOCS
started: 2026-08-22 01:25:41
finished: 2026-08-22 01:26:34
---

자세제어 SW(FSW-AOCS)가 sysreq.md의 지향 0.05°(3σ)·안정도 0.005°/s를
만족하려면 제어주기(Hz)와 입출력 신호 목록(센서: 스타트래커/자이로/태양센서
등, 액추에이터: 리액션휠/자기토커 등)의 데이터 형식·갱신주기를 AOCS
하드웨어 팀과 합의해야 한다.
산출물: AOCS 팀이 제어주기(Hz), 센서/액추에이터 신호 목록(이름·형식·주기·단위)을
회신 문서로 남긴다. FSW는 이를 입력으로 aocs-sw.md의 제어 루프를 확정한다.
검증: 제어주기20Hz·신호목록 회신, pointing-budget 안정도 배분과 정합
