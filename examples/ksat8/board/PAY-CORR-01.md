---
id: PAY-CORR-01
title: waveguide-route-spec.md 입력 경로 정정 요청 (AUDIT-1 결함)
status: DONE
parent: AUDIT-1
source: AUDIT-1
owner: PAY-IF-01
deliverable: examples/ksat8/deliverables/PAY/corr-01-record.md
after: -
track: PAY
started: 2026-08-27 04:15:55
finished: 2026-08-27 04:15:55
---

감사(AUDIT-1)에서 REQ-HAR-PAY-RF 회신
(examples/ksat8/deliverables/PAY/waveguide-route-spec.md)의 "입력:"이
examples/ksat8/deliverables/HAR/pay-waveguide-budget.md를 인용함을 발견했다.
이 파일은 별도 요청(REQ-PAY-HAR-도파관, parent: M-PAY)의 회신으로, REQ-HAR-PAY-RF
(parent: M-HAR)의 취합 사슬 위에 있지 않다 — 정식 요청 경로 없이 인접 사슬의
정보를 재사용한 "보이지 않는 종속"이다(규칙 4절 v3.2). 수치 자체(WR-42,
28포트, 손실배분 0.8dB)는 HAR 실측(0.57dB)과 모순되지 않으나 기록 절차 정정이
필요하다.
요청: waveguide-route-spec.md의 "입력:"에서 해당 경로를 제거하거나, PAY가 HAR에
정식 요청을 올려 회신을 받은 뒤 그 회신 경로로 대체해 달라.
산출물 제안: examples/ksat8/deliverables/PAY/waveguide-route-spec.md(갱신).
검증: "입력:" 경로 전건 적법(자기팀/after/자기사슬회신/source/보드) 확인
검증: waveguide-route-spec.md 입력줄 재확인 — 부적법 경로 제거 완료(선행조치), 2건 전부 적법
