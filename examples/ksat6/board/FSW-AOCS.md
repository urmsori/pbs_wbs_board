---
id: FSW-AOCS
title: 자세제어 SW
status: DONE
parent: M-FSW
source: -
owner: FSW-AOCS-01
deliverable: examples/ksat6/deliverables/FSW/aocs-sw.md
after: FSW-ARCH
track: FSW
started: 2026-08-22 01:21:51
finished: 2026-08-22 01:28:01
---

아키텍처가 정한 제어주기·태스크 틀 안에서 지향 0.05°(3σ)·안정도
0.005°/s(sysreq AOCS)를 만족하는 자세제어 SW를 구현해야 한다. 제어
알고리즘의 입출력(센서·액추에이터 신호, 제어주기)은 AOCS 하드웨어 팀과
협상해야 정해지므로(규칙 4절 ICD 당사자 협상) REQ-FSW-AOCS를 함께 발행한다.
산출물: examples/ksat6/deliverables/FSW/aocs-sw.md — 제어 루프 구조, 처리시간, 검증 케이스.
검증: AOCS 회신(20Hz,신호목록) 반영 확인, 7개 검증케이스 정의, 처리시간 3.1ms<50ms 확인
