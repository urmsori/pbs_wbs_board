---
id: NEED-HAR-EPS
title: EPS 인수 시험용 시험 하니스(PCU 백플레인·배터리 커넥터 대응)
status: DONE
parent: AIT-RX-EPS
owner: HAR-TECH-01
deliverable: examples/ksat5/deliverables/SUPPORT/need-har-eps.md
after: -
track: HAR
started: 2026-08-21 07:13:40
finished: 2026-08-21 07:15:01
---

AIT-TST의 필요: EPS EM 모듈을 EGSE에 연결해 시험하려는데, PCU와
배터리의 커넥터 규격이 서로 달라 이를 EGSE로 모을 시험 하니스가
없다. icd-str-eps.md(module-em.md §3 확정 인터페이스로 인용됨)를 읽고
확인한 구체 요구:

- PCU: 스택 배면 34핀 백플레인 헤더 1개 — 버스 전력 + 하위 레일
  (5V/3.3V/액추에이터 레일) 전부가 이 커넥터로 인출됨(icd-str-eps.md §2).
- 배터리 팩: 2핀 전력 + 온도센서 서미스터 1핀, 팩 상단 인출
  (icd-str-eps.md §3) — 배터리 대신 EGSE 가변전원(6.8~8.4V, EOD~공칭
  전 구간 재현)을 이 2핀 커넥터에 연결해야 함.

요청: PCU 34핀 백플레인 헤더 1채널(레일별 브레이크아웃 포함) + 배터리
모의용 2핀 전력·1핀 서미스터 채널을 갖춘 EPS EM 모듈 시험 하니스.
산출물: (지원 역할이 정함)
검증: PCU 34핀 백플레인(레일별 브레이크아웃)+배터리 2핀/1핀 서미스터가 요청과 일치, icd-str-eps.md 커넥터 규격 확인
