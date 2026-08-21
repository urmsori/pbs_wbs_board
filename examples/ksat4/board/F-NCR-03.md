---
id: F-NCR-03
title: OBC — dsn-*-f.md가 "예정"(TBD)뿐인데 summary-fm.md는 완료로 판정
status: OPEN
parent: F-AIT-1
owner: -
deliverable: -
after: -
track: OBC
started: -
finished: -
---

F-AIT-1에서 examples/ksat4/deliverables/OBC/dsn-a1-f.md,
examples/ksat4/deliverables/OBC/dsn-a2-f.md를 열어 확인한 결과, 질량(kg)·
치수(mm)·전력(W)·구조마진(%)·열마진(%) 다섯 항목이 전부 "예정"(TBD
placeholder)으로만 적혀 있어 실제 수치가 하나도 없다. e-decision.md의
FM 이관 리스크(OBC는 질량·마진 모두 미기재 대상)가 FM 설계갱신
(F-OBC-D1, F-OBC-D2)에서 전혀 해소되지 않았다 — 오히려 "예정"이라는
표현은 아직 값이 결정되지 않았음을 스스로 명시하고 있다.

그런데 examples/ksat4/deliverables/OBC/summary-fm.md는 "A1 설계갱신"·
"A2 설계갱신" 항목을 모두 "✓ 완료"로 표시한다 — 자신이 인용해야 할
설계 산출물(dsn-a1-f.md·dsn-a2-f.md)이 수치를 "예정"으로 남겨 둔
상태와 정면으로 모순된다. 또한 summary-fm.md에는 다른 7개
서브시스템과 달리 최종 "판정: 합격/APPROVED" 같은 결론 문장 자체가
없어 판정 근거를 확인할 수 없다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/OBC/dsn-a1-f.md, dsn-a2-f.md의 "예정"
  항목을 실제 질량·치수·전력·구조마진·열마진 수치로 채운다.
- examples/ksat4/deliverables/OBC/summary-fm.md에 위 수치를 인용한
  설계갱신 판정과, 서브시스템 전체에 대한 최종 판정 문장을 추가한다.

(담당 역할: OBC-LEAD-01 — owner에는 take 시 이 역할 이름을 쓴다)
