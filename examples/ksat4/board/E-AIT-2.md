---
id: E-AIT-2
title: EM 기능 통합 시험
status: DONE
parent: E-PHASE
owner: AIT-02
deliverable: examples/ksat4/deliverables/support/ait-e.md
after: E-AIT-1, E-NCR-01, E-NCR-02, E-NCR-03, E-NCR-04, E-NCR-05
track: AIT
started: 2026-08-21 04:11:43
finished: 2026-08-21 04:16:15
---

서브시스템 산출물 전체의 정합을 실제로 대조한다. 불일치는 NCR
게시글로 올린다(발견되는 필요).
산출물: examples/ksat4/deliverables/support/ait-e.md
(담당 역할: AIT-02 — owner에는 take 시 이 역할 이름을 쓴다)

## 대기 (AIT-02)

E-AIT-1(전기 통합)에서 실제 대조로 NCR 5건(E-NCR-01~05, 대상: STR·
COMM·AOCS·OBC·TCS)을 발견해 게시했다. 모두 아직 status: OPEN이라
서브시스템 팀의 수정이 끝나지 않았다 — 위 다섯 건을 이 게시글의
`after`에 추가해 수정 완료(DONE)를 기다린다. 기능 통합 검사는 아직
수행하지 않았고, 다섯 NCR이 모두 DONE되어야 재개한다. 이 게시글은
TAKEN 상태로 유지한다.
검증: NCR 5건 status DONE 확인 후 각 정정 산출물 원문 직접 대조(STR/COMM/AOCS/OBC/TCS), 8개 test-em.md·icd.md 기능·인터페이스 정합 재확인 — 잔여 리스크(4개 서브시스템 질량 미기재)는 ait-e.md에 기록
