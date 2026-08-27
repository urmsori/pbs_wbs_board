# AOCS-U1 폐루프(HIL) 시험

입력: examples/ksat8/deliverables/AOCS/u2-accept-test.md, examples/ksat8/deliverables/AOCS/u1-dsn.md

수락된 실제 센서·휠(AOCS-U2-TST)을 HIL에 넣고 CM-AOCS-U1 기준선 제어법칙
(대역폭0.02Hz)으로 폐루프 지향정확도 측정:
- 정착 후 지향오차(3σ): **0.0305°**(109.8arcsec) — 설계예측(0.0318°) 대비
  실측이 더 우수(센서 실측치가 배분보다 여유 있었음).
- SA 모드(0.12Hz) 여기 없음 확인(스펙트럼 -40dB 이하).

sysreq AOCS 판정: 지향 0.0305° ≤ 0.05° — **PASS**(마진 39%).

검증: sysreq AOCS 지향 0.0305°≤0.05°(마진39%) PASS
