---
id: PAY-CORR-02
title: twta-heat-layout.md 입력 경로 정정 요청 (AUDIT-2 결함)
status: DONE
parent: AUDIT-2
source: AUDIT-2
owner: PAY-IF-01
deliverable: examples/ksat8/deliverables/PAY/corr-02-record.md
after: -
track: PAY
started: 2026-08-27 04:15:55
finished: 2026-08-27 04:15:55
---

감사(AUDIT-2)에서 REQ-TCS-PAY-발열 회신
(examples/ksat8/deliverables/PAY/twta-heat-layout.md)의 "입력:"이
examples/ksat8/deliverables/TCS/pay-thermal-capability.md를 인용함을 발견했다.
이 파일은 별도 요청(REQ-PAY-TCS-방열, parent: M-PAY)의 회신으로,
REQ-TCS-PAY-발열(parent: M-TCS)의 취합 사슬 위에 있지 않다 — AUDIT-1과 동일
유형의 "보이지 않는 종속"이다(규칙 4절 v3.2). 수치 자체(채널당210W≤262W,
24채널5.04kW≤6.3kW)는 모순 없으나 기록 절차 정정이 필요하다.
요청: twta-heat-layout.md의 "입력:"에서 해당 경로를 제거하거나, PAY가 TCS에
정식 요청을 올려 회신을 받은 뒤 그 회신 경로로 대체해 달라. AUDIT-1과 동일
원인자(PAY-DSN-01)의 반복 패턴이므로 향후 양방향 ICD 처리 시 반대쪽 사슬
회신을 정식 요청 없이 재사용하지 않도록 유의해 달라.
산출물 제안: examples/ksat8/deliverables/PAY/twta-heat-layout.md(갱신).
검증: "입력:" 경로 전건 적법(자기팀/after/자기사슬회신/source/보드) 확인
검증: twta-heat-layout.md 입력줄 재확인 — 부적법 경로 제거 완료(선행조치), 2건 전부 적법
