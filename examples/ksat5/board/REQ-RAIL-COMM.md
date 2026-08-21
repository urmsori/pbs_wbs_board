---
id: REQ-RAIL-COMM
title: 송신 펄스 프로파일 재확인 (공유 레일 동시부하 검토용)
status: TAKEN
parent: RISK-RAIL
owner: COMM-DSN
deliverable: -
after: -
track: COMM
started: 2026-08-21 07:36:45
finished: -
---

EPS-DSN의 필요: 액추에이터 레일(8.4V) 동시부하 예산을 정하려면
icd-eps-comm-power.md의 송신 첨두(EOD 0.74A)가 **언제, 얼마나 자주,
얼마나 오래** 발생하는지가 필요하다 — 궤도당 송신 횟수·지속시간(기존
자료는 "궤도당 ≈4분, duty cycle 4.2%"만 명시), 실제 패킷 단위 온/오프
펄스 폭(수백ms~수s), 지상국 교신 중 위성 자세(슬루 필요 여부)를 COMM
팀이 직접 확인해 알려주기 바란다. bus-voltage-check.md §4가 이미
"분기 퓨즈/차단기 정격 미확정"을 명시한 상태이므로, 이 값으로 AOCS
슬루 첨두와의 동시 발생 최악 조건을 판정한다.
산출물: COMM 팀이 남기는 송신 펄스 시간 프로파일 확인 문서(경로는 COMM 팀이 정함).
