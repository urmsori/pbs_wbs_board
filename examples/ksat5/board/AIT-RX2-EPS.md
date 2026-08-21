---
id: AIT-RX2-EPS
title: EPS FM 모듈 인수 검사
status: DONE
parent: INT2
owner: AIT-QA-01
deliverable: examples/ksat5/deliverables/AIT/rx2-eps.md
after: -
track: AIT
started: 2026-08-21 07:45:37
finished: 2026-08-21 07:46:35
---

AIT-01의 필요: 인도된 EPS FM 모듈(module-fm.md)을 인수 검사한다.
EPS/module-fm.md §1 EM 승계 리스크표에서 액추에이터 레일 동시부하가
rail-budget.md·burn-in-fm.md로 종결됐음을 확인해야 하고, PCU 백플레인
커넥터·배터리 커넥터는 EM과 동일(신규 커넥터 변경 언급 없음)하므로
EM 하니스(NEED-HAR-EPS)·EM SW(NEED-SW-EPS) 재사용 가능성을 확인하며
착수한다.
산출물: examples/ksat5/deliverables/AIT/rx2-eps.md
검증: EM하니스/SW 재사용, 4레일 텔레메트리 기준이내, 퓨즈정격 실물대조 일치, 동시부하 실모듈재현은 INT2-TST 이월
