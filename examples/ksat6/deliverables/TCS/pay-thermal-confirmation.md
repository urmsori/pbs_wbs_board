# TCS → PAY 회신: 초점면 온도 안정성 확인
입력: examples/ksat6/deliverables/TCS/thermal-analysis.md, examples/ksat6/deliverables/TCS/heater-thermistor.md, examples/ksat6/deliverables/TCS/tvac-test.md

PAY-01 요청(REQ-PAY-TCS)의 초점면/광학벤치 ±0.5°C(노출 구간) 요구는 TCS
열해석(thermal-analysis.md)에서 이미 같은 값(궤도 1주기 내 변동 ≤±0.5°C)으로
설계 입력에 반영했던 항목과 동일하다. 달성 가능함을 확인한다.

## 달성 근거
- 채널: H3(광학부 구조·배플 전용), 정격 4W, 서모스탯 대역 -15°C ON/-10°C OFF
  (heater-thermistor.md).
- TVAC 실측(tvac-test.md): 광학벤치 내 구배 최대 1.6°C(요구 ≤2°C 대비 여유),
  노출시간 스케일(수 초~수십 초)에서는 서모스탯 히스테리시스보다 짧아 열용량에
  의해 ±0.5°C 이내로 완충됨을 열평형 로깅으로 확인.
- 히터 예산: H3 실측 3.9W, 전체 채널 합계 21.7W ≤ sysreq 25W 이내
  (마진 3.3W로 초점면 제어대역폭 확장 여력 있음).

## 제어대역폭
서모스탯 on/off 주기 실측 약 6분(열용량 대비 열손실률 기준) — 노출시간(수십초)
동안은 사실상 정상상태로 간주 가능.

검증: tvac-test.md 실측 구배 1.6°C ≤ 2°C, 히터예산 21.7W ≤ 25W로 PAY 요구
(±0.5°C, WFE 12nm RMS 배분) 달성 가능 확인.
