---
id: E-NCR-03
title: AOCS — summary-em.md 판정이 board 실제 상태와 모순(낡은 판정)
status: DONE
parent: E-AIT-1
owner: AOCS-LEAD-01
deliverable: examples/ksat4/deliverables/AOCS/summary-em.md
after: -
track: AOCS
started: 2026-08-21 04:13:34
finished: 2026-08-21 04:13:34
---

examples/ksat4/deliverables/AOCS/summary-em.md는 시험 항목을 "진행중"으로
기재한다: "시험 | 진행중 | 시험 수행 중(E-AOCS-T2 진행중, E-AOCS-T3 대기)"
및 최종 판정 "조건부 합격 - ... 시험 완료 대기중".

그러나 board를 실제로 대조하면 E-AOCS-T2(자세제어 기능시험 수행)와
E-AOCS-T3(자세제어 시험 보고)는 둘 다 status: DONE이고 finished:
2026-08-21 04:03:36으로, summary-em.md를 최종 취합한 E-AOCS-L1의
finished 시각(2026-08-21 04:03:36)과 같은 시각에 이미 완료되어 있다.
즉 summary-em.md 본문은 자신이 인용하는 두 게시글이 이미 끝난 뒤에도
"진행중"·"대기"라는 낡은 문구를 그대로 두고 있어, "조건부 합격"이라는
최종 판정의 근거가 실제 완료 상태와 어긋난다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/AOCS/summary-em.md의 판정표·최종 판정을
  E-AOCS-T2·T3 완료 상태에 맞춰 재작성한다(시험이 실제로 끝났다면
  결과를 반영해 판정하고, 여전히 조건부일 근거가 있다면 그 근거를
  구체적으로 적는다 — "대기중"이라는 표현은 board 상태와 맞지 않는다).

(담당 역할: AOCS-LEAD-01)
검증: board 상태(T2·T3 DONE)와 대조해 판정 갱신
