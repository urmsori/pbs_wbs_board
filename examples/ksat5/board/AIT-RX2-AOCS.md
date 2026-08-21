---
id: AIT-RX2-AOCS
title: AOCS FM 모듈 인수 검사
status: DONE
parent: INT2
owner: AIT-TST-01
deliverable: examples/ksat5/deliverables/AIT/rx2-aocs.md
after: -
track: AIT
started: 2026-08-21 07:45:37
finished: 2026-08-21 07:46:35
---

AIT-01의 필요: 인도된 AOCS FM 모듈(module-fm.md)을 인수 검사한다.
AOCS/module-fm.md §1~3: EKF/PD 게인 미세조정과 guard band SW 강제
로직만 갱신됐고 커넥터·인출면 변경 언급이 없으므로 EM 하니스(NEED-
HAR-AOCS)·EM SW(NEED-SW-AOCS) 재사용 가능성을 확인하며, 종합
지향오차(0.45°) 재현과 guard band 로직 동작을 독립 재확인한다.
산출물: examples/ksat5/deliverables/AIT/rx2-aocs.md
검증: EM하니스/SW 재사용, 모드전이 전건통과, 지향오차0.45도 일치, guardband로직 재현
