---
id: INT2-TST
title: FM 통합시험(동시부하 재현·링크마진 통합확인)
status: DONE
parent: INT2
owner: AIT-TST-01
deliverable: examples/ksat5/deliverables/AIT/integration-test-fm.md
after: NEED-FM-DUALLOAD, AIT-RX2-STR, AIT-RX2-EPS, AIT-RX2-AOCS, AIT-RX2-COMM
track: AIT
started: 2026-08-21 07:46:49
finished: 2026-08-21 07:47:25
---

AIT-01의 필요: 4개 FM 모듈이 모두 인수 검사를 통과했으니, 위성구조체에
통합한 상태에서 두 승계 리스크(RISK-RAIL, RISK-LINK)의 실제 통합
조건 재현·확인 및 운용 제약 채택을 마무리한다. NEED-FM-DUALLOAD(이중
부하 리그)가 도착했으므로 이를 입력으로 AOCS-COMM 동시부하(2.08A,
≤5s)를 실모듈로 재현한다.
산출물: examples/ksat5/deliverables/AIT/integration-test-fm.md
검증: 동시부하 실모듈재현(레일6.83V유지,퓨즈미동작), 링크마진 통합확인7.8dB, 운용제약4건 채택
