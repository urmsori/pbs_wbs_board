---
id: FIX-AOCS-U1-STR정렬반영
title: STR 정렬 기준 정식 회신 반영 — 지향오차 예산 정정
status: DONE
parent: M-AOCS
source: REQ-AOCS-STR-정렬
owner: AOCS-DSN-01
deliverable: examples/ksat8/deliverables/AOCS/u1-dsn.md
after: REQ-AOCS-STR-정렬
track: AOCS
started: 2026-08-27 04:04:28
finished: 2026-08-27 04:04:28
---

AOCS-U1-DSN은 STR 정렬 회신 대기 8×20초 초과로 정렬오차 50arcsec(잠정)를
사용했다(AOCS-U1-RVW-A 조건부 승인 사유). REQ-AOCS-STR-정렬 정식 회신
(정렬큐브 수직도10·열드리프트5, 안테나 보어사이트 열드리프트18 arcsec/궤도)이
도착했으므로 지향오차 예산을 정정한다.
검증: 정렬오차 실측 반영 RSS가 여전히 0.05°(180arcsec) 이내인지 재확인
검증: 정정 RSS114.5arcsec(0.0318°)≤0.05°(마진36.4%로 개선), BASELINE 유지
