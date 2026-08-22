---
id: STR-U3-ANL
title: 구조해석(정적·모드)
status: DONE
parent: M-STR
source: -
owner: STR-ANL-01
deliverable: examples/ksat6/deliverables/STR/structural-analysis.md
after: STR-U1-MFG,STR-U2-MFG
track: STR
started: 2026-08-22 01:26:44
finished: 2026-08-22 01:27:31
---

제작·실측이 끝난 1차구조·2차 브래킷군의 실측 질량을 입력으로 정적(준정적12g)·
모드(1차 고유진동수) 해석을 수행해 sysreq STR 항목을 최종 판정해야 한다.
설계·제작과 다른 사람(해석)이 맡는다. unit2에서 남은 질량 초과(0.43kg)도
여기서 최종 판정한다.
산출물: examples/ksat6/deliverables/STR/structural-analysis.md — 정적/모드 해석 결과.
검증: sysreq STR 3항목 전량 충족: 질량21.93kg≤22kg, 1차모드44.6Hz≥40Hz, 준정적12g MS≈1.4
