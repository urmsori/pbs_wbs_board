---
id: REQ-OBC-PAY-TM
title: 중계기 TM 점수 요청
status: DONE
parent: M-OBC
source: OBC-U1-DSN
owner: PAY-IF-02
deliverable: examples/ksat8/deliverables/PAY/obc-tm-reply.md
after: -
track: PAY
started: 2026-08-27 03:55:49
finished: 2026-08-27 03:55:49
---

왜: OBC의 TM 8,000점 예산 중 중계기(PAY) 몫을 확정하려면 채널당 TM 점수와
갱신 주기를 알아야 레지스터 맵·수집 스케줄을 짤 수 있다.

무엇을 알려달라: (1) 채널(24개)당 TM 점수 개수, (2) TM 종류별 갱신 주기
(고속/저속), (3) 이산/아날로그 비율(레지스터 폭 산정용).

회신 산출물 경로 제안: examples/ksat8/deliverables/PAY/obc-tm-reply.md
검증: 총400점(15점×24+40) 회신, 갱신주기 1Hz/0.1Hz
