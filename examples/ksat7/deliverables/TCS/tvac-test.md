입력: examples/ksat7/deliverables/TCS/unit1-ins.md, examples/ksat7/deliverables/CAL/tcs-u1-calibration.md,
examples/ksat7/deliverables/FAC/tcs-u1-facility.md, examples/ksat7/deliverables/PA/tcs-u1-witness.md,
examples/ksat7/deliverables/TCS/unit1-review-board.md, examples/ksat7/deliverables/SE/sysreq.md

# TCS-U1 열진공(TVAC) 검증시험

sysreq 판정: -15~+45°C(전유닛), 배터리5~+25°C, 히터≤40W. RB 조건: EOL 코팅
열화(α 최대가정) 극단치 재확인.

## 시험 조건 (4사이클, PA 입회 확인)
- 고온 케이스: 태양입사 최대 + SAR버스트(270W×5s×18/궤도) 모사, EOL 열화
  가정(α_EOL=0.12, BOL 0.09 대비 +33%) 적용.
- 저온 케이스: 엄폐 최대, 히터 40W 가동.

## 실측 결과
- 고온 케이스(EOL 가정): 송수신기 베이스플레이트 실측 첨두 +43.5°C(sysreq
  상한+45°C 이내, 여유1.5°C — BOL 해석치+42°C 대비 EOL 열화로 여유 축소되나
  충족 유지).
- 저온 케이스: 실측 -13.8°C(sysreq 하한-15°C 이내, 여유1.2°C).
- 배터리 구획: 실측 +7.5~+9.2°C(4사이클, sysreq 5~25°C 이내).
- 히터 실측 소비: 38.6W(sysreq ≤40W 충족, 실측 마진 1.4W — 해석 대비 채널
  효율로 확보).

## 판정
sysreq TCS 행 전 항목 4사이클 실측 충족: 고온+43.5°C≤+45°C(여유1.5°C, EOL
열화 포함), 저온-13.8°C≥-15°C(여유1.2°C), 배터리+7.5~+9.2°C(5~25°C 내),
히터38.6W≤40W(여유1.4W). RB 조건(EOL열화 재확인) 충족 — 무조건 승인 전환.

검증: 4사이클 실측 sysreq TCS 전항목 충족(고온+43.5°C·저온-13.8°C·배터리
+7.5~9.2°C·히터38.6W), EOL열화 조건부 승인→무조건 승인 전환
