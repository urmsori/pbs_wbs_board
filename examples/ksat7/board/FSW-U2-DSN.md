---
id: FSW-U2-DSN
title: SAR 촬영 시퀀서 SW 설계
status: DONE
parent: M-FSW
source: -
owner: FSW-DSN-01
deliverable: examples/ksat7/deliverables/FSW/sequencer-design.md
after: -
track: FSW
started: 2026-08-27 01:49:48
finished: 2026-08-27 01:54:01
---

SAR 스트립맵/스팟 촬영을 자동 실행하는 시퀀서(명령셋: 모드 전환·펄스
타이밍·안테나 지향 큐·데이터 태깅)를 설계해야 한다. 명령셋 정의는 PAY의
촬영 파라미터(펄스폭·PRF·모드 전환시간)에 달려 있어 REQ-FSW-PAY 협상이 필요하다.
검증: 명령셋5종·90s인터록 구현, PAY촬영파라미터 잠정(무응답)
