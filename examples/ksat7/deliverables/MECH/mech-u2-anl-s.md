# MECH-U2 SA 전개힌지 구조/동역학 해석

입력: examples/ksat7/deliverables/MECH/mech-u2-dsn.md, examples/ksat7/deliverables/SE/sysreq.md
(전개 후 1차모드≥0.5Hz, 전개충격≤40g)

- 힌지강성 8000N·m/rad 기준 전개 후(3윙 전개상태) 1차모드 **0.62Hz** — sysreq ≥0.5Hz 대비
  마진 0.12Hz(24%). **판정: 충족**
- 전개충격(잠정 관성 2.5kg·m² 가정) **31g** — sysreq ≤40g 대비 마진 9g. **판정: 충족**
- 단일고장: 기계식 오버센터 잠금 + 화약 백업 릴리즈 이중화 확인, 단일고장점 없음.
- REQ-MECH-SA(패널 질량·관성 실측) 회신 수신 시 재검증 필요(리스크 오픈).
