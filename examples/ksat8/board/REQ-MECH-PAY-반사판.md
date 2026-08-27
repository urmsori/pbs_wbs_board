---
id: REQ-MECH-PAY-반사판
title: 반사판 질량·관성·전개각 요청 (MECH→PAY)
status: DONE
parent: M-MECH
source: MECH-U1-DSN
owner: PAY-IF-03
deliverable: examples/ksat8/deliverables/PAY/mech-pay-reflector-reply.md
after: -
track: PAY
started: 2026-08-27 03:55:49
finished: 2026-08-27 03:55:49
---

왜: MECH-U1(반사판 전개기구) 힌지·구동 모터·토크스프링 용량을 정하려면
반사판(2.4m, 피드 포함)의 질량·힌지축 관성과 요구 전개각을 알아야 한다.
요청: (1) 반사판(피드 포함) 질량(kg), (2) 전개 힌지축 기준 관성모멘트(kg·m²),
(3) 요구 전개각(스토우드→전개, deg)과 지향 공차, (4) 전개 완료 후 잠금
예비하중 요구(N·m).
회신 산출물 제안: examples/ksat8/deliverables/PAY/mech-pay-reflector-reply.md
검증: 회신치를 MECH-U1 구동 토크·전개충격 해석(목표≤35g)에 반영
검증: 급전질량8.0kg/반사판(합계16kg), 관성0.05kg·m² 회신
