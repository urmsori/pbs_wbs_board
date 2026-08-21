---
id: NEED-FM-DUALLOAD
title: AOCS-COMM 동시부하(2.08A, ≤5s) 재현시험용 이중부하 시험 리그
status: DONE
parent: INT2
owner: GSE-01
deliverable: examples/ksat5/deliverables/GSE/NEED-FM-DUALLOAD_deliverable.md
after: -
track: GSE
started: 2026-08-21 07:45:16
finished: 2026-08-21 07:45:16
---

AIT-01의 필요: FM 통합시험에서 RISK-RAIL이 정한 동시 최악조건(2.08A,
≤5s)을 **실제 AOCS FM 모듈 + COMM FM 모듈을 동시에 공유 액추에이터
레일에 걸어** 재현해야 하는데, EM 단계 장비(NEED-HAR-AOCS, NEED-HAR-
COMM, NEED-SW-AOCS, NEED-SW-EPS)는 전부 모듈 1개씩 EGSE에 개별 연결·
단독 시험하도록 만들어졌다 — 두 모듈을 같은 급전선에 동시에 물리고
공용 3.0A 완속 퓨즈 앞단 레일 전압을 시간 동기로 기록하는 리그가 없다.

근거(읽고 확인):
- rail-budget.md §1: 동시 최악부하 2.08A는 AOCS 슬루(1.34A)와 COMM
  송신(0.74A)이 겹치는 조건이며, 판정 자체가 "궤도당 최대 5초"로
  시간 한정된 시나리오다 — 두 모듈이 실제로 동시에 구동돼야 재현된다.
- COMM/module-fm.md §"인도 시점 잔여 사항" 1항: "AOCS-COMM 동시부하
  (2.08A, ≤5초) 재현시험... COMM 단독 수락시험 범위 밖... AIT 통합
  시험에서 공용 3.0A 퓨즈 조건으로 재현 예정" — COMM 스스로 AIT로
  이월을 명시.
- EPS/burn-in-fm.md §3은 "동시(최악 재현) 2.08A, 5s" 시나리오를
  이미 시험했지만, **전자부하(EGSE 시뮬레이터)로 AOCS+COMM 전류를
  흉내 낸 EPS 자체 벤치 시험**이지 실제 AOCS FM·COMM FM 하드웨어를
  물린 것이 아니다 — EPS 소관 정격 실증으로는 유효하나, AIT가 확인해야
  할 "실제 두 모듈 통합 상태에서의 재현"을 대신하지 않는다.

요청: 공용 급전선(PCU~분기점, 3.0A 완속 퓨즈 포함)에 AOCS FM 분기
(2.0A)와 COMM FM 분기(1.25A, 완속)를 동시에 연결하고, AOCS 슬루
트리거(need-sw-aocs.md 재사용)와 COMM 송신 트리거(need-sw-eps.md의
load_step_actuator_comm_pulse.py 파형을 실제 COMM 트리거로 대체)를
동기 발동시켜, 레일 전압(6.8V 하한 유지 여부)·분기별 전류·퓨즈
동작 여부를 시간 동기로 기록하는 이중부하 시험 리그.
산출물: examples/ksat5/deliverables/GSE/dualload-rig-fm.md
검증: AOCS 분기(2.0A)+COMM 분기(1.25A) 동시 인가 시 상위 3.0A 퓨즈
앞단 레일 전압을 5초 이상 연속 기록할 수 있음을 확인, 트리거 동기
오차가 재현 조건(±5s 이내 중첩)에 지장 없음을 확인.
검증: GSE 장비 구성, 교정, 통신 확인 완료
