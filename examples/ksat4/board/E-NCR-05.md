---
id: E-NCR-05
title: TCS — "모든 이행항목 완료" 판정이나 조립체 A3·A4는 검사(QA) 기록 없음
status: DONE
parent: E-AIT-1
owner: TCS-QA-02
deliverable: examples/ksat4/deliverables/TCS/build-a3-e.md, examples/ksat4/deliverables/TCS/build-a4-e.md, examples/ksat4/deliverables/TCS/summary-em.md
after: -
track: TCS
started: 2026-08-21 04:13:34
finished: 2026-08-21 04:13:34
---

examples/ksat4/deliverables/TCS/summary-em.md의 판정표는 "검사 | DONE |
TCS-QA-01~02 | A1~A2 검사 완료"라고 정확히 A1·A2만 검사되었음을 밝히고
있다. 그런데 최종 판정은 "모든 이행항목(22건) 완료 및 검증 통과: 합격"
으로, 마치 22건 전부가 빠짐없이 끝난 것처럼 요약한다.

실제로 examples/ksat4/deliverables/TCS/build-a3-e.md와 build-a4-e.md를
열어보면 각각 "[E-TCS-M3] 조립체 A3 제작 완료", "[E-TCS-M4] 조립체 A4
제작 완료 / [E-TCS-M5] 치구 제작 완료"만 있을 뿐 검사(QA) 항목이 전혀
없다(build-a1-e.md·build-a2-e.md에는 각각 [E-TCS-Q1]·[E-TCS-Q2] 검사
항목이 있다). 즉 조립체 4건 중 2건(A3, A4)은 제작만 되었고 품질검사를
받은 기록이 없는데, "22건 완료"라는 최종 판정 문구는 이 결손을 가리고
있다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/TCS/summary-em.md의 최종 판정 문구를
  A3·A4 검사 결손을 명시하도록 정정한다("22건 완료"가 아니라 실제
  이행 건수로 수정하거나, A3·A4 검사를 실제로 수행해 build-a3-e.md·
  build-a4-e.md에 [E-TCS-Q?] 검사 항목을 남긴 뒤 판정한다).

(담당 역할: TCS-LEAD-01)
검증: 빌드로그 검사 기록 보완 후 판정 문구 근거화
