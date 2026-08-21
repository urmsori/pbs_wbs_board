---
id: ICD-EPS-AOCS
title: AOCS 구동기 소비 전력 프로파일 요청
status: DONE
parent: EPS-03
owner: AOCS-DSN
deliverable: examples/ksat5/deliverables/AOCS/icd-eps-aocs-power-profile.md
after: -
track: AOCS
started: 2026-08-21 07:05:08
finished: 2026-08-21 07:05:39
---

EPS-BAT의 필요: 배터리 용량(방전 심도, 첨두 부하)을 산정하려면 자세제어
구동기(반작용휠·자기토커 등)의 실제 소비 전력 프로파일이 필요하다 —
정상 지향 유지 시 평균 소비 전력(W), 슬루/기동 시 첨두 소비 전력(W)과
지속시간, 버스 직결 액추에이터 레일(8.4V 공칭, 방전 말기 하한 약
6.8V) 동작 가능 전압 범위를 AOCS 팀이 직접 확인해 알려주기 바란다.
sysreq의 지향 정확도 ≤0.5° 요구를 만족하는 구동기 구성 기준으로
작성해 달라.
산출물: AOCS 팀이 남기는 구동기 전력 프로파일 문서(경로는 AOCS 팀이 정함).
검증: NOMINAL 3.2W/첨두 9.1W 산정치 정합, 6.8~8.4V 구간 동작 확인
