---
id: HAR-D1
title: 주버스 하니스 설계(라우팅·핀맵 취합)
status: DONE
parent: M-HAR
source: -
owner: HAR-DSN-01
deliverable: examples/ksat6/deliverables/HAR/unit1-main-bus.md
after: -
track: HAR
started: 2026-08-22 01:20:11
finished: 2026-08-22 01:24:42
---

전 유닛을 잇는 주버스 하니스(전원·신호)를 설계하려면 OBC 커넥터·핀맵과 EPS
배전 출력 커넥터·전류 정격을 알아야 한다 — 하니스는 남의 핀맵 없이는 설계할
수 없다. 이 Work를 시작하면서 그 두 정보를 REQ-HAR-OBC, REQ-HAR-EPS로 즉시
요청한다(당사자 간 ICD 협상, 규칙 4절).
산출물: examples/ksat6/deliverables/HAR/unit1-main-bus.md — 라우팅도·핀맵
취합·전압강하 예산 배분.
검증: 전압강하 계산 최대1.10%(COMM-X)<=2%, OBC/EPS 핀맵·전류정격 회신 반영
