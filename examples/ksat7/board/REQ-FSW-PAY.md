---
id: REQ-FSW-PAY
title: "[FSW→PAY] SAR 촬영 시퀀서 명령셋·촬영 파라미터 확정 요청"
status: DONE
parent: M-FSW
source: FSW-U2-DSN
owner: PAY-OPS-01
deliverable: examples/ksat7/deliverables/PAY/fsw-sequencer-reply.md
after: -
track: PAY
started: 2026-08-27 01:54:40
finished: 2026-08-27 01:55:02
---

SAR 촬영 시퀀서(FSW-U2-DSN)의 명령셋(모드 전환·펄스 타이밍·안테나 지향 큐)을
확정하려면 PAY의 촬영 파라미터(스트립맵/스팟 모드별 펄스폭·PRF·모드 전환
소요시간·첨두 펄스부하 90s/궤도 내 운용 제약)를 알아야 한다.
산출물: PAY 팀이 모드별 펄스폭·PRF·모드 전환시간·펄스부하 운용 제약을
회신 문서로 남긴다. FSW는 이를 입력으로 시퀀서 명령셋을 확정한다.
검증: 회신 파라미터 기준 시퀀서 명령셋이 sysreq PAY 펄스 1.8kW/90s 제약 준수 확인
검증: 펄스폭20/6.7µs·PRF3000Hz, 전환2.5s, 버스트제약5s×18회/궤도 회신
