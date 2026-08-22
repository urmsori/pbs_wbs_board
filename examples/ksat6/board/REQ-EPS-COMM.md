---
id: REQ-EPS-COMM
title: COMM 송신 첨두전류·듀티 요청
status: DONE
parent: M-EPS
source: EPS-01
owner: COMM-IF-01
deliverable: examples/ksat6/deliverables/COMM/tx-load-response.md
after: -
track: COMM
started: 2026-08-22 01:23:21
finished: 2026-08-22 01:23:41
---

EPS 전력예산(EPS-01)에서 X-band 150Mbps 다운링크 송신 구간의 첨두 전류와
듀티를 알아야 PCDU 스위치·퓨즈 정격과 배터리 방전 심도를 계산할 수 있다.
예산상 가정치(첨두 55W/듀티 8%)를 검증받아야 한다.
산출물: COMM 팀이 정하는 경로에 S-band TT&C 상시부하(W)와 X-band 송신 시
첨두전류(A, 28V 기준)·듀티(%)·1궤도당 송신 총 시간(분)을 명시해 달라.
검증: EPS 가정치(55W/8%)보다 낮은 실계산치(40W/1.43A/약4%)로 회신, 60GB/일·150Mbps·98.8분 궤도주기로 duty 환산

정정(PM-01, v3.0): 취합 부모를 EPS-01(낳은 설계)에서 M-EPS(취합될 모듈)로 정정 — 원인은 source가 담는다(3절).
