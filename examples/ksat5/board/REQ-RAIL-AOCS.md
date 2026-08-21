---
id: REQ-RAIL-AOCS
title: 슬루 첨두 시간 프로파일 재확인 (공유 레일 동시부하 검토용)
status: DONE
parent: RISK-RAIL
owner: AOCS-DSN
deliverable: examples/ksat5/deliverables/AOCS/rail-profile.md
after: -
track: AOCS
started: 2026-08-21 07:33:41
finished: 2026-08-21 07:34:00
---

EPS-DSN의 필요: 액추에이터 레일(8.4V) 동시부하 예산을 정하려면
icd-eps-aocs-power-profile.md의 슬루 첨두(EOD 1.34A)가 **언제,
얼마나 자주, 얼마나 오래** 발생하는지가 필요하다 — 궤도당 슬루 횟수,
1회당 지속시간(현재 자료는 "최대 60s"만 명시), 지상국 교신 시간대와의
겹침 가능성(교신 중 자세 유지가 슬루를 요구하는지)을 AOCS 팀이 직접
확인해 알려주기 바란다. 이 값으로 AOCS 첨두와 COMM 송신 펄스가 실제로
겹칠 확률/최악 조건을 판정한다.
산출물: AOCS 팀이 남기는 슬루 시간 프로파일 확인 문서(경로는 AOCS 팀이 정함).
검증: 궤도당 첨두 누적시간(최악 360s/통상 80s)이 시험·ICD 산정치와 정합함을 확인
