---
id: F-NCR-02
title: AOCS — dsn-*-f.md 질량·마진 수치 부재 + summary-fm.md 근거 없는 판정
status: DONE
parent: F-AIT-1
owner: AOCS-DSN-01
deliverable: examples/ksat4/deliverables/AOCS/dsn-a1-f.md, examples/ksat4/deliverables/AOCS/dsn-a2-f.md, examples/ksat4/deliverables/AOCS/summary-fm.md
after: -
track: AOCS
started: 2026-08-21 04:28:25
finished: 2026-08-21 04:28:25
---

F-AIT-1에서 examples/ksat4/deliverables/AOCS/dsn-a1-f.md,
examples/ksat4/deliverables/AOCS/dsn-a2-f.md를 열어 확인한 결과, 두 파일
모두 "A1(또는 A2) 설계 완료 — 작업 완료"라는 한 줄뿐이고 질량·구조 마진·
열 마진 수치가 없다. e-decision.md의 FM 이관 리스크(AOCS는 질량·마진
모두 미기재 대상)가 FM 설계갱신(F-AOCS-D1, F-AOCS-D2)에서 전혀
해소되지 않았다.

게다가 examples/ksat4/deliverables/AOCS/summary-fm.md는 입력으로
icd.md·dsn-a1-f.md·dsn-a2-f.md(수치 없는 파일들)만 인용하면서
"처리 완료: 15건, 미해결: 0건"이라고만 적어 15건이 무엇인지 나열하지
않고, 최종 판정도 "FM 단계 완료 — **EM 단계 진입 가능**"이라 적혀 있다
— FM을 마쳤는데 EM 단계로 진입한다는 것은 단계 순서가 거꾸로이며, 다른
서브시스템(STR·EPS·COMM 등)의 summary-fm.md가 "PM 이관 승인"·"다음
통합 단계로 진행 가능"이라 적는 것과도 어긋난다. 판정 문구 자체가
자신이 인용한 입력과도, 다른 서브시스템의 판정 형식과도 근거 없이
어긋난 사례다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/AOCS/dsn-a1-f.md, dsn-a2-f.md에 질량(kg)·
  구조 마진·열 마진 수치를 실제로 기재한다.
- examples/ksat4/deliverables/AOCS/summary-fm.md의 "15건"을 실제
  작업 목록으로 나열하고, "EM 단계 진입 가능"이라는 판정 문구를
  올바른 다음 단계 표현으로 정정한다.

(담당 역할: AOCS-LEAD-01 — owner에는 take 시 이 역할 이름을 쓴다)
검증: 질량 합이 배분 이내·마진 수치 기재를 확인
