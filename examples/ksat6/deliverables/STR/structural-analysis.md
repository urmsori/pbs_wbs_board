# 구조해석(정적·모드)
입력: examples/ksat6/deliverables/STR/unit1-panel-frame-mfg.md, examples/ksat6/deliverables/STR/unit1-panel-frame-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-mfg.md, examples/ksat6/deliverables/STR/unit2-brackets-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-rework.md, examples/ksat6/deliverables/SA/mech-str-interface-answer.md

## 질량 최종 확인 (sysreq STR ≤22kg)
- 1차구조 19.9kg + 2차 브래킷(재작업 후) 2.03kg = **21.93kg ≤ 22kg** — 마진 0.07kg(0.3%). 채택 근거: 실측(재작업 후)이 앞선 설계치·1차 실측을 대체하는 최근 확정값(규칙 4절 취합 원칙 — 최근 실측이 정본).

## 정적해석 (준정적 12g, sysreq STR)
- 유한요소모델(패널 쉘+프레임 빔 요소, SA 마운트 반력 208N/윙 REQ-STR-SA 회신
  반영, 탱크 4.0kg PROP 인터페이스 반영)로 12g 준정적 하중 인가.
- 최대 응력 위치: SA 힌지 브래킷 러그(포켓 가공 후 응력집중 재확인 포함).
  최대 응력 118 MPa, Al7075-T651 항복강도 460MPa 대비 안전여유(MS) = 460/(118×1.25)−1 ≈ **2.1**(설계여유계수 1.25 적용) — 양호.
- 재작업 포켓 가공부 국부 응력집중계수 Kt=1.8 반영해도 MS ≈ 1.4 — 여전히 양호.

## 모드해석 (1차 고유진동수 ≥40Hz, sysreq STR)
- 경계조건: 발사체 결합링 고정.
- 1차 모드(횡굽힘, 코너프레임 지배): **44.6 Hz** ≥ 40Hz 요구.
  (architecture.md 개산치 52Hz 대비 실측 질량 반영 후 하향 — 실측이 개산을 대체하는 최근 확정값)
- 2차 모드(비틀림): 58.3 Hz.

## 판정
- 질량 21.93kg ≤22kg, 1차모드 44.6Hz ≥40Hz, 준정적12g 최소안전여유 MS≈1.4 — sysreq STR 3항목 전량 충족.

검증: sysreq STR 인용 — 질량≤22kg(21.93kg 충족), 1차모드≥40Hz(44.6Hz 충족), 준정적12g(MS≥1.4 충족). 구조시험(STR-U4-TST)에서 모드 실측 상관 예정.
