---
id: EPS-02
title: PCDU 설계
status: DONE
parent: M-EPS
source: -
owner: EPS-DSN-02
deliverable: examples/ksat6/deliverables/EPS/pcdu-design.md
after: EPS-01
track: EPS
started: 2026-08-22 01:23:14
finished: 2026-08-22 01:23:30
---

EPS-01 전력예산·아키텍처에서 정한 서브시스템별 첨두전류를 바탕으로 PCDU
배전채널(스위치·퓨즈·커넥터)과 배터리 충방전 관리 임계값을 확정해야 배터리팩
설계(EPS-03)와 다른 트랙의 배전 인터페이스 질의(REQ-*-EPS)에 답할 수 있다.
산출물: examples/ksat6/deliverables/EPS/pcdu-design.md — 채널별 전류정격표·
커넥터 사양·배터리 관리 임계값.
검증: sysreq 모선28V±4V 범위서 전 채널 전류정격 산출, 주버스퓨즈10A(마진1.5배) 확정
