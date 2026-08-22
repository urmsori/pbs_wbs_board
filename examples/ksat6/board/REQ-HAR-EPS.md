---
id: REQ-HAR-EPS
title: EPS 배전 출력 커넥터·전류 정격 요청 (하니스 설계용)
status: DONE
parent: M-HAR
source: HAR-D1
owner: EPS-DSN-02
deliverable: examples/ksat6/deliverables/EPS/distribution-connector-spec.md
after: -
track: EPS
started: 2026-08-22 01:23:34
finished: 2026-08-22 01:23:58
---

주버스 하니스(HAR-D1)를 설계하려면 EPS(PCDU)의 배전 출력 커넥터 형식과
채널별 전류 정격, 모선 전압(28V±4V)을 알아야 한다 — 전원선 전압강하
≤2%(sysreq.md) 판정을 위해 채널별 최대 전류·케이블 길이 예산이 필요하다.
EPS 팀이 배전 출력 커넥터 사양서(파트번호·채널별 핀 배치·전류 정격)를
회신해 달라.
산출물: EPS 팀 판단(예: examples/ksat6/deliverables/EPS/ 아래 배전 커넥터
사양 문서).
검증: PCDU 채널 커넥터·전류정격표 회신, 전압강하 판정은 HAR 몫으로 명시

정정(PM-01, v3.0): 취합 부모를 HAR-D1(낳은 설계)에서 M-HAR(취합될 모듈)로 정정 — 원인은 source가 담는다(3절).
