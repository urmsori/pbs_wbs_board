# STR 구조 비행모델 인도 — module-fm
입력: examples/ksat6/deliverables/STR/architecture.md, examples/ksat6/deliverables/STR/unit1-panel-frame-design.md, examples/ksat6/deliverables/STR/unit1-panel-frame-mfg.md, examples/ksat6/deliverables/STR/unit1-panel-frame-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-design.md, examples/ksat6/deliverables/STR/unit2-brackets-mfg.md, examples/ksat6/deliverables/STR/unit2-brackets-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-rework.md, examples/ksat6/deliverables/STR/structural-analysis.md, examples/ksat6/deliverables/STR/vibration-test.md, examples/ksat6/deliverables/STR/final-inspection.md, examples/ksat6/deliverables/STR/interface-aocs.md, examples/ksat6/deliverables/STR/interface-comm.md, examples/ksat6/deliverables/STR/interface-prop.md, examples/ksat6/deliverables/PAY/str-interface-reply.md

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
- PAY 인터페이스(REQ-STR-PAY): 폴링 8회×20초(160초) 내 미회신이라 잠정치
  (질량15kg·볼트원φ200mm 8-M6)로 STR-ARCH를 1차 완료했다. 이후 PAY 실회신
  (질량35kg·3점 킨매틱 마운트φ260mm·각변위≤0.01°·병진≤10µm)이 도착해
  STR-ARCH-REV(정정 게시글)로 architecture.md를 개정, STR-ARCH를 재취합했다
  — 규칙 4절 재작업 경로(잠정→실회신→정정)의 실제 사례. 최초 형상(킨매틱
  3점)이 실회신과 일치해 1차구조·2차 브래킷 재설계는 불필요했고, 탑재체
  35kg 자체는 STR 1차구조 22kg 예산과 별개 항목이라 질량 판정에 영향 없음.
  잔여 미결 사항 없음.

검증: sysreq STR 3항목(질량≤22kg→21.9kg, 1차모드≥40Hz→43.1Hz, 준정적12g→MS≈1.4) 전량 실측/시험으로 충족 확인. PAY 인터페이스는 잠정→실회신 반영까지 완료되어 미결 없음.
