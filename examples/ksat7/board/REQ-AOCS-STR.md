---
id: REQ-AOCS-STR
title: 센서 정렬 기준면·SAR 안테나 강성(제어대역) 요청
status: DONE
parent: M-AOCS
source: AOCS-U1-DSN
owner: STR-IF-01
deliverable: examples/ksat7/deliverables/STR/aocs-alignment-spec.md
after: -
track: STR
started: 2026-08-27 01:54:20
finished: 2026-08-27 01:54:44
---

요 스티어링 제어계 설계(AOCS-U1-DSN)에서 지향오차 예산 중 정렬오차에 0.0035°를
배분했고, 제어대역폭(0.8Hz)이 SAR 안테나(전개형) 1차모드와 5배 이상 이격되어야
제어-구조 연성이 없다고 판단했다(안테나 1차모드 ≥4.0Hz 필요). STR 팀에 두 가지를
요청한다: ① 별추적기·자이로 공통 정렬 기준면(정렬 큐브)의 면간 수직도와 열드리프트,
② SAR 안테나 장착 상태에서의 1차모드 여유(안테나 질량 72kg, PAY-U1-DSN 배분치 기준).
산출물: STR 팀이 남기는 문서 — 정렬 기준면 수직도(arcsec)·열드리프트(arcsec),
안테나 장착 상태 1차모드(Hz) 실측/해석치.
검증: 수직도·열드리프트가 정렬오차 배분 0.0035°(12.6arcsec) 이내, 1차모드 ≥4.0Hz 회신
검증: 수직도7.3arcsec합계≤12.6, 1차모드37.2Hz(잠정)>>4.0Hz최소치
