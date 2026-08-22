---
id: REQ-EPS-AOCS
title: AOCS 부하 프로파일 요청(휠·센서 첨두·평균)
status: DONE
parent: EPS-01
source: EPS-01
owner: AOCS-DSN-01
deliverable: examples/ksat6/deliverables/AOCS/eps-load-reply.md
after: -
track: AOCS
started: 2026-08-22 01:25:41
finished: 2026-08-22 01:26:34
---

EPS 전력예산(EPS-01)에서 모선 부하 155W 이내 배분과 배터리 용량을 확정하려면
반작용휠 4기·자이로·별추적기·마그네토커의 실제 부하가 필요하다. 예산상
가정치(첨두 45W/평균 20W)를 검증받아야 EPS-04 통합시험에서 확정할 수 있다.
산출물: AOCS 팀이 정하는 경로(예: examples/ksat6/deliverables/AOCS/*.md)에
휠·센서 첨두전력(W)·평균전력(W)·모드별(초기포착/정상추적/모멘텀덤핑) 프로파일을
28V±4V 모선 기준으로 명시해 달라.
검증: 첨두38W(≤가정45W), 평균25.7W(가정20W대비+5.7W) 회신
