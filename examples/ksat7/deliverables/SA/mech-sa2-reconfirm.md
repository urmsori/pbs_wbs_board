# SA 패널 질량·관성 재확인 (REQ-MECH-SA2, MECH 힌지 rev.2 대응)

입력: examples/ksat7/board/REQ-MECH-SA2.md, examples/ksat7/deliverables/SA/mech-sa-interface-reply.md,
examples/ksat7/deliverables/SA/panel-mfg.md, examples/ksat7/deliverables/SA/panel-inspection.md

## 재확인
패널은 이미 인도(SA-U1-MFG/INS/TST DONE) 완료된 비행모델로, rev.2 힌지 재설계
착수 이후 패널측 설계·제작 변경 없음. 기존 REQ-MECH-SA 회신치를 그대로 재확인한다.
- 질량: **7.6kg/윙** (변경 없음)
- 관성(힌지축 기준): **10.1 kg·m²** (변경 없음)

## 힌지강성 증대(8000→25,000 N·m/rad)에 대한 판단
힌지강성이 3배 이상 증가하면 전개 잠금 시 임펄스가 다소 커지나, 패널측
관성(10.1kg·m²)과 기존 점성 로터리 댐퍼(설계목표 ≤35g, sysreq 예산 ≤40g,
SA-U1-ANL-S 마진 반영)로 흡수 가능한 범위로 판단된다 — 단, 정량적 전개충격
재해석은 MECH 측 rev.2 몫이며 본 회신은 패널측 입력치(질량·관성) 불변만 확인한다.

검증: 질량7.6kg/윙·관성10.1kg·m² 최신 설계와 일치(변경없음) 재확인, 힌지강성25,000N·m/rad 증대는 기존 댐퍼·전개충격예산(≤40g) 내 흡수 가능 판단(정량 재해석은 MECH 몫)
