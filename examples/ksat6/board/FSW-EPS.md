---
id: FSW-EPS
title: 전력·열 관리 SW
status: DONE
parent: M-FSW
source: -
owner: FSW-EPS-01
deliverable: examples/ksat6/deliverables/FSW/eps-thermal-sw.md
after: FSW-ARCH
track: FSW
started: 2026-08-22 01:21:51
finished: 2026-08-22 01:26:37
---

sysreq.md의 EPS(모선 28V±4V, 일식 35분 배터리 심방전 ≤25%)·TCS(히터 예산
≤25W) 요구를 지키려면 배터리 충전 종지·저전압 임계·히터 제어 로직이
필요하다. 배터리 관리 파라미터는 EPS 하드웨어 팀과 협상해야 정해지므로
REQ-FSW-EPS를 함께 발행한다.
산출물: examples/ksat6/deliverables/FSW/eps-thermal-sw.md — 배터리 관리 로직, 히터 제어 로직, 검증 케이스.
검증: EPS 회신 임계값 반영 확인, 5개 검증 케이스 정의, sysreq DoD≤25%·히터≤25W 판정 충족
