---
id: RISK-RAIL
title: 액추에이터 레일 3자 동시부하 예산·분기 퓨즈 정격 확정
status: DONE
parent: INT2
owner: EPS-DSN
deliverable: examples/ksat5/deliverables/EPS/rail-budget.md
after: -
track: EPS
started: 2026-08-21 07:33:10
finished: 2026-08-21 07:38:52
---

(담당 역할: EPS-DSN)

AIT의 필요: EM 통합시험(integration-report.md §3)에서 8.4V 액추에이터
레일을 AOCS 구동기(슬루 첨두 1.34A, EOD)와 COMM PA(송신 첨두 0.74A,
EOD)가 동일 물리 레일로 공유함을 확인했다. 각 팀 ICD(icd-eps-aocs-
power-profile.md, icd-eps-comm-power.md)는 자기 부하만 독립 산정했고,
동시 최악 부하(≈2.08A, EOD 6.8V)를 어느 팀도 검토하지 않았다 — COMM
자신의 bus-voltage-check.md §4도 "분기 퓨즈/차단기 정격 미확정"을
이미 명시한 상태다.

요청: EPS 주관으로 AOCS·COMM과 3자 협상해 액추에이터 레일 동시부하
예산을 확정하고, 분기 퓨즈/차단기 정격을 정하라.
산출물: examples/ksat5/deliverables/EPS/rail-budget.md
검증: AOCS/COMM 회신 대조로 2.08A/≤5s 최악조건 확정, 분기2.0A·1.25A/상위공용3.0A 퓨즈 정격이 83%이하 여유로 통과, 선택성 67%/42%≤80% 확인, 운용제약(guard band 확대·스케줄 금지·궤도실측) 병행 권고
