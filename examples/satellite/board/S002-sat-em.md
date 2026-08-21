---
id: S002
title: EM 형상 통합·기능시험
status: DONE
parent: S000
owner: agent-ait
deliverable: examples/satellite/deliverables/sat-em-report.md
after: S021,S031,S040
track: SAT
started: 2026-08-21 00:59:24
finished: 2026-08-21 01:00:09
---

모듈 EM급 산출물(EM EPS, EM AOCS, EM 트랜시버)을 전기적으로 통합해 기능을
검증하는 엔지니어링 모델 형상.
산출물: examples/satellite/deliverables/sat-em-report.md

검증: 선행 산출물 수치 대비 플랫새트 통합 실측을 대조 — 버스 소비 39.8 W ≤ 45 W(sysreq),
버스 전압 26.8~30.6 V가 EPS EM 범위(26.4~30.9 V, eps-em) 이내, 폐루프 지향 0.074° ≤ 0.1°(aocs-em 단독 0.071°와 정합), BER 3.5e-6 ≤ 1e-5(comm-em 3.2e-6과 동등) — 전 항목 합격 확인.
