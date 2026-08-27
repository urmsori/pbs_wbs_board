---
id: REQ-AOCS-STR-정렬
title: "[AOCS→STR] 센서·안테나 정렬 기준면 요청"
status: DONE
parent: M-AOCS
source: M-AOCS
owner: STR-DSN-01
deliverable: examples/ksat8/deliverables/STR/aocs-alignment-spec.md
after: -
track: STR
started: 2026-08-27 04:02:52
finished: 2026-08-27 04:02:52
---

sysreq 안테나 지향 0.05°(3σ)를 지향오차 예산(정렬오차·센서오차·제어오차·구조
열변형)으로 배분하려면 AOCS-U1 설계(DSN) 착수 전에 STR의 정렬 기준을 알아야
한다. 별추적기·자이로 공통 정렬 큐브의 면간 수직도·열드리프트(arcsec), 그리고
Ka 안테나 2기의 구조체 대비 장착 정렬(보어사이트) 안정도·열드리프트를 요청한다.
산출물 제안: examples/ksat8/deliverables/STR/aocs-alignment-spec.md — 정렬
기준면 수직도(arcsec)·열드리프트(arcsec/궤도), 안테나 보어사이트 정렬 안정도.
검증: 회신치를 지향오차 예산 중 정렬항에 배분해 RSS 합이 0.05°(180arcsec) 이내인지 확인
검증: 정렬큐브 수직도10arcsec·열드리프트5arcsec/궤도, 안테나 열드리프트18arcsec/궤도 회신
