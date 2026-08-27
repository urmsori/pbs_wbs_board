입력: examples/ksat7/deliverables/TCS/unit1-thermal-design.md, examples/ksat7/deliverables/PAY/tcs-thermal-profile.md,
examples/ksat7/deliverables/SE/sysreq.md

# TCS-U1 열해석 (고온/저온 케이스)

sysreq 판정 기준: 전 유닛 -15~+45°C, 배터리 5~+25°C, 히터≤40W.

## 고온 케이스 (일조, SAR 촬영 궤도)
- 태양입사+지구적외선+SAR버스트(270W×5s×18/궤도) 최악 조합.
- 정상상태 라디에이터(0.35㎡, ε0.80/α0.09) 방열량 ≈ εσA(T_rad^4) 대비 입력열
  (버스 baseline 60W + SAR평균 4.2W등가 + 히터0W) 균형점 T_rad ≈ +38°C.
- 송수신기 베이스플레이트 첨두: 기저 +38°C + 버스트 상승 0.56°C×누적완충
  ≈ +42°C — sysreq 상한 +45°C 이내(여유 3°C).

## 저온 케이스 (엄폐, 비촬영)
- 태양입사 없음, 버스 baseline 최소 발열, 히터 40W 가동.
- 균형점 T_rad ≈ -12°C — sysreq 하한 -15°C 이내(여유 3°C).
- 배터리 구획(별도 MLI+히터 15W 채널): 균형점 +8°C — sysreq 배터리 5~+25°C
  이내(하한여유 3°C, 상한여유 17°C).

## 판정
고온 +42°C ≤ +45°C(여유3°C), 저온 -12°C ≥ -15°C(여유3°C), 배터리 +8°C(5~25°C
범위 내), 히터 40W≤40W(sysreq 상한, 여유0 — CHK·RVW 단계에서 마진 확보 여부
재검토 필요 플래그).

검증: sysreq TCS 행(-15~+45°C, 배터리5~25°C, 히터≤40W) 대비 고온+42°C·저온
-12°C·배터리+8°C 전항목 충족, 히터는 상한치 도달(마진0) — CHK 단계 확인 필요.
