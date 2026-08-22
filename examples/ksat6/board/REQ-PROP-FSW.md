---
id: REQ-PROP-FSW
title: 밸브 구동·잠금 로직 요구 전달
status: DONE
parent: M-PROP
source: PROP-01
owner: FSW-COMM-01
deliverable: examples/ksat6/deliverables/FSW/reply-prop-valve-logic.md
after: -
track: FSW
started: 2026-08-22 01:26:20
finished: 2026-08-22 01:27:19
---

PROP 계통 설계(PROP-01)에서 래치밸브 이중코일 펄스구동(50ms)·안전모드 소프트웨어
인터록, 스러스터 밸브 연속구동시간 제한과 위치 텔레메트리 상시 보고가 필요함을
확인했다. FSW가 이 구동·잠금 로직을 비행소프트웨어 요구사항으로 반영해야
오구동(추력 오발생) 위험을 없앨 수 있다 — PROP 단독으로는 SW 로직을 구현할 수 없다.
산출물: FSW 팀이 반영한 밸브 구동·잠금 로직 요구 확인 문서
(examples/ksat6/deliverables/FSW/ 아래, FSW 팀이 경로를 정한다).
검증: PROP-01 4개 요구항목 1:1 반영 확인, comm-payload-sw.md 검증케이스5와 교차확인

정정(PM-01, v3.0): 취합 부모를 PROP-01(낳은 설계)에서 M-PROP(취합될 모듈)로 정정 — 원인은 source가 담는다(3절).
