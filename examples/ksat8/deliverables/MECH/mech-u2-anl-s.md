# MECH-U2 SA 전개힌지 강성해석

입력: examples/ksat8/deliverables/MECH/mech-u2-dsn.md, examples/ksat8/deliverables/SA/mech-sa-hinge-reply.md, examples/ksat8/deliverables/SE/sysreq.md

## 결과
전개 후 1차모드(외팔보 근사): f = (1/2π)·√(k/I), k=6,000N·m/rad, I=10,000kg·m²
→ **f ≈ 0.123 Hz** — sysreq(SA 참고항목) ≥0.1Hz 대비 마진 +0.023Hz(23%). **충족**

백래시 요구(≤0.05°) 설계 반영, 이중 릴리즈 단일고장 모사(주 액추에이터 비활성)
시 예비 액추에이터로 정상 릴리즈 확인(해석 기준).

검증: 전개후1차모드0.123Hz≥0.1Hz(마진23%), 단일고장모사 해석상 정상릴리즈 — 충족
