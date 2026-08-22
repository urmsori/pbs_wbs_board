# STR 구조 비행모델 인도 — module-fm
입력: examples/ksat6/deliverables/STR/architecture.md, examples/ksat6/deliverables/STR/unit1-panel-frame-design.md, examples/ksat6/deliverables/STR/unit1-panel-frame-mfg.md, examples/ksat6/deliverables/STR/unit1-panel-frame-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-design.md, examples/ksat6/deliverables/STR/unit2-brackets-mfg.md, examples/ksat6/deliverables/STR/unit2-brackets-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-rework.md, examples/ksat6/deliverables/STR/structural-analysis.md, examples/ksat6/deliverables/STR/vibration-test.md, examples/ksat6/deliverables/STR/final-inspection.md, examples/ksat6/deliverables/STR/interface-aocs.md, examples/ksat6/deliverables/STR/interface-comm.md, examples/ksat6/deliverables/STR/interface-prop.md

## 구성
- 1차구조(6면 샌드위치 패널 + 코너프레임 4본 + 발사체 결합링), 2차 브래킷군
  (SA 힌지·안테나·탱크·정렬큐브 장착). 비행모델(FM) 단계 — 진동시험·최종검사 완료.

## sysreq STR 항목 최종 판정 (수치 인용)
| 항목 | 요구(sysreq.md) | 최종 실측/판정 | 근거 |
|---|---|---|---|
| 질량 | ≤22 kg | **21.9 kg** | final-inspection.md(시험 후 최종 실측) |
| 1차 고유진동수 | ≥40 Hz | **43.1 Hz**(시험 실측, 해석 44.6Hz와 상관오차 3.4%) | vibration-test.md |
| 준정적 하중 | 12 g | 정현진동 12g 등가 인가 후 손상 없음, 해석 최소안전여유 MS≈1.4 | vibration-test.md, structural-analysis.md |

## 진행 경과 요약
- 구조 아키텍처(STR-ARCH) → 1차구조(unit1: 설계·제작·검사) ∥ 2차 브래킷(unit2:
  설계·제작·검사) → 질량 초과(22.43kg) 발견 → 경량화 재작업(STR-U2-REWORK,
  21.93kg) → 구조해석(STR-U3-ANL, sysreq 3항목 방향성 확인) → 구조시험
  (STR-U4-TST, 정현·랜덤 진동) → 최종검사(STR-U5-INS).
- 외부 인터페이스 회신: SA(REQ-STR-SA·REQ-MECH-SA), AOCS(REQ-AOCS-STR),
  COMM(REQ-COMM-STR), PROP(REQ-PROP-STR) — 전량 회신 완료.
- 잠정 가정: PAY 인터페이스(REQ-STR-PAY)는 폴링 8회×20초(160초) 내 미회신 —
  탑재체 질량15kg·볼트원φ200mm 8-M6·정렬허용0.01°를 잠정치로 architecture.md에
  반영해 진행. PAY 회신 도착 시 재작업 필요 여부 재확인 필요(미결).

검증: sysreq STR 3항목(질량≤22kg, 1차모드≥40Hz, 준정적12g) 전량 실측/시험으로 충족 확인. PAY 인터페이스만 잠정 가정 표기.
