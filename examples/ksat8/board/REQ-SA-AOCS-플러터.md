---
id: REQ-SA-AOCS-플러터
title: 지향 제어 대역과 SA 모드 간섭 요구
status: DONE
parent: M-SA
source: SA-U1-DSN
owner: AOCS-DSN-01
deliverable: examples/ksat8/deliverables/AOCS/sa-interference-reply.md
after: -
track: AOCS
started: 2026-08-27 03:53:08
finished: 2026-08-27 03:53:08
---

2윙 대형 태양전지판(SA-U1-DSN)이 전개 후 1차모드 ≥0.1Hz(sysreq)를 만족해도,
AOCS 지향 제어 대역폭과 겹치면 패널 플러터가 지향 안정도 0.05°(sysreq)를
저해할 수 있다. 확인 요청:
1) AOCS 자세제어 루프 대역폭(Hz, 3dB 컷오프) 및 모멘텀 휠 스위칭 주파수
2) SA 1차모드가 피해야 할 금지대역(Hz 범위)과 최소 이격 마진(배수 또는 Hz)
3) SA 구동(전개/추적 구동장치) 동작이 AOCS 외란 예산(N·m)에 미치는 허용
   한계
산출물: AOCS 팀이 정하는 경로(예: examples/ksat8/deliverables/AOCS/)에
위 3항목을 수치로 명시해 달라. 무응답 시 AOCS 대역폭을 0.1Hz 미만으로
가정하고 SA 1차모드 0.1Hz와의 이격 마진 부족 리스크를 설계 문서에 기록한다.
검증: AOCS 대역폭·SA 금지대역·외란 허용한계 회신
검증: 대역폭0.02Hz 회신, SA모드 이격6.0배 충족, SADA외란배분0.08N·m≥0.05N·m
