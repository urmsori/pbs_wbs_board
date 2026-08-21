---
id: F-NCR-04
title: PAY — dsn-*-f.md 질량 수치 EM 대비 퇴행 + summary-fm.md 26.8kg 근거 없음
status: OPEN
parent: F-AIT-1
owner: -
deliverable: -
after: -
track: PAY
started: -
finished: -
---

F-AIT-1에서 examples/ksat4/deliverables/PAY/dsn-a1-f.md,
examples/ksat4/deliverables/PAY/dsn-a2-f.md를 열어 확인한 결과, "A1(또는
A2) 설계 완료"라는 한 줄뿐이고 질량·치수·전력·구조 마진·열 마진 수치가
전혀 없다. EM 단계의 같은 파일(dsn-a1-e.md·dsn-a2-e.md)에는 "질량:
2.5 kg / 치수: 300mm×200mm×100mm / 전력: 50W"가 실제로 적혀 있었다 —
FM 설계갱신(F-PAY-D1, F-PAY-D2)에서 수치가 새로 없어진 것으로, EM
잔여 리스크가 해소되기는커녕 **퇴행**했다. 구조/열 마진 수치는 EM
때도 없었고 FM에서도 여전히 없다(e-decision.md 리스크 1의 PAY 항목
미해소).

한편 examples/ksat4/deliverables/PAY/summary-fm.md는 "질량 26.8/28kg"
(배분 28 kg 대비 95.7% 사용, 8개 서브시스템 중 배분 대비 가장 여유가
적은 수치)이라고 적지만, PAY 디렉토리의 dsn-a1-f.md·dsn-a2-f.md·
parts-f.md·build-a1~a4-f.md·cfg-f.md 어디에도 26.8이라는 숫자나 그
근거가 되는 부품별/조립체별 질량 내역이 없다 — 배분 여유가 가장 적은
수치인데도 출처를 추적할 수 없는 판정이다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/PAY/dsn-a1-f.md, dsn-a2-f.md에 질량(kg)·
  치수·전력·구조 마진·열 마진 수치를 실제로 기재한다(최소 EM 수준
  복원, 마진은 신규 기재).
- examples/ksat4/deliverables/PAY/summary-fm.md의 "26.8/28kg"이 어느
  산출물(부품별/조립체별 질량 합산)에서 나온 수치인지 근거를 추가하거나,
  근거 파일을 새로 작성해 인용한다.

(담당 역할: PAY-LEAD-01 — owner에는 take 시 이 역할 이름을 쓴다)
