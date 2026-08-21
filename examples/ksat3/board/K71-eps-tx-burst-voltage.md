---
id: K71
title: 송신 버스트(12W·10s) 시 버스 전압 유지 확인
status: OPEN
parent: K30
owner: -
deliverable: -
after: -
track: EPS
started: -
finished: -
---

COMM 송신 버스트 시 피크 소비전력 12 W(최대 10초)로 잡았다. sysreq의
"송신 버스트 최대 10초, 이때 버스 전압 ≥7.0 V 유지" 요구와 직결되는
교차 요구로, EPS 쪽에서 이 부하 조건에서 버스 전압 ≥7.0 V 유지가
가능한지 확인이 필요하다(배터리 내부저항·레귤레이터 응답 등 고려).
산출물: examples/ksat3/deliverables/eps-to-comm.md — 12 W·10초 버스트 부하
조건에서의 버스 전압 유지 가능 여부(확인/불가 시 대안)를 명시한 문서.
