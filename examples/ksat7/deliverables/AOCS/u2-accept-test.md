# AOCS-U2 센서·반작용휠 수락시험
입력: examples/ksat7/deliverables/AOCS/u2-ins.md, examples/ksat7/deliverables/CAL/aocs-u2-cal.md, examples/ksat7/deliverables/AOCS/u1-yaw-steering-design.md

| 장비 | 배분 예산 | 실측치 | 판정 |
|---|---|---|---|
| 별추적기 측정정확도 | ≤0.0035° | 0.0031° | PASS |
| 자이로 전파오차 | ≤0.0040° | 0.0036° | PASS |
| 반작용휠(4기 각각) 최대토크 | ≥0.10 N·m | 0.112 N·m(최소) | PASS |
| 반작용휠(4기 각각) 모멘텀저장 | ≥12 N·m·s | 12.6 N·m·s(최소) | PASS |
| 마그네토커(3축) 자기모멘트 | ≥20 A·m² | 20.8 A·m²(최소) | PASS |

판정: 전 항목 PASS, AOCS-U1-DSN 배분치 충족 확인. HIL 시험(AOCS-U1-TST) 입력으로 사용.
