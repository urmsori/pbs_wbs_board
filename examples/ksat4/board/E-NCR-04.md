---
id: E-NCR-04
title: OBC — summary-em.md의 "미실시/진행중" 조건이 자신이 인용한 입력과 모순
status: DONE
parent: E-AIT-1
owner: OBC-LEAD-01
deliverable: examples/ksat4/deliverables/OBC/summary-em.md
after: -
track: OBC
started: 2026-08-21 04:13:34
finished: 2026-08-21 04:13:34
---

examples/ksat4/deliverables/OBC/summary-em.md는 "A3 조립체"·"A4 조립체"의
시험 열을 "-"(미실시)로, "부품 인증"을 "조건부"로 표시하고 최종 판정을
"조건부 합격 - A3·A4는 시험 미실시로 조건부 처리하며, 부품 인증이
진행 중"이라 적는다.

그런데 summary-em.md가 스스로 입력으로 지정한
examples/ksat4/deliverables/OBC/test-em.md는 "[E-OBC-T1] 시험 절차 완료
— [E-OBC-T2] 시험 수행 완료 — [E-OBC-T3] 시험 보고 완료"라고만 적혀 있어
A3·A4를 미실시로 구분하는 근거가 없고, parts-e.md도 "[E-OBC-P1][E-OBC-P2]
부품 구매 완료"라고만 되어 있어 "부품 인증 진행 중"이라는 조건과 맞는
서술이 없다. board를 대조해도 E-OBC-D3·D4·M3·M4·Q1·Q2·T1·T2·T3가 전부
status: DONE이다. 즉 summary-em.md의 "조건부" 판정을 뒷받침할 근거가
자신이 인용한 산출물에도, board 상태에도 없다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/OBC/summary-em.md의 판정표·최종 판정을
  재작성한다: "미실시"·"진행중"으로 남길 근거가 실제로 있다면 그
  근거(예: A3·A4 시험 결과가 test-em.md에 없는 이유)를 test-em.md에도
  함께 남기고, 근거가 없다면 board 상태(전부 DONE)에 맞춰 판정을
  올바르게 정정한다.

(담당 역할: OBC-LEAD-01)
검증: 입력 파일·board 대조로 조건 철회 근거 확인
