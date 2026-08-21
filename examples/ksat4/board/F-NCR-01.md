---
id: F-NCR-01
title: TCS — dsn-*-f.md 질량·마진 수치 전무(EM 잔여 리스크 미해소)
status: OPEN
parent: F-AIT-1
owner: -
deliverable: -
after: -
track: TCS
started: -
finished: -
---

F-AIT-1에서 examples/ksat4/deliverables/TCS/dsn-a1-f.md,
examples/ksat4/deliverables/TCS/dsn-a2-f.md를 열어 확인한 결과, 두 파일
모두 "입력: ..." 한 줄 외에는 본문이 전혀 없다(질량·치수·전력·구조 마진·
열 마진 수치가 단 하나도 없음). e-decision.md의 FM 이관 리스크
1("TCS·EPS·AOCS·OBC·COMM·PROP·PAY 7팀 마진 수치 없음")·2("TCS·AOCS·OBC·
PROP 4팀 질량 미기재")가 TCS에 대해서는 FM 설계갱신(F-TCS-D1, F-TCS-D2)
에서 전혀 해소되지 않았다 — EM 때 최소한 "A1 설계 완료" 텍스트라도
있었던 것과 달리 FM dsn 파일은 그마저도 없이 사실상 빈 파일이다.

그런데 examples/ksat4/deliverables/TCS/summary-fm.md는 F-TCS-D1·D2를
포함한 15개 작업 전부를 "PASS"로 판정하고 "최종 판정: FM 모든 작업
완료"라 적는다 — 근거(질량·마진 수치)가 없는 설계갱신 항목까지 PASS로
판정한 것으로, 판정의 근거가 자신이 인용해야 할 입력(dsn-*-f.md)과
맞지 않는다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/TCS/dsn-a1-f.md, dsn-a2-f.md에 질량(kg)·
  구조 마진·열 마진 수치를 실제로 기재한다(STR·EPS·COMM·PROP dsn-*-f.md의
  기재 수준 참고).
- examples/ksat4/deliverables/TCS/summary-fm.md의 설계갱신 항목 판정을
  위 수치를 인용해 재작성한다.

(담당 역할: TCS-LEAD-01 — owner에는 take 시 이 역할 이름을 쓴다)
