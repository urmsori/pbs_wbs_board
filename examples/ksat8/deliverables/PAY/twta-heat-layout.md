# REQ-TCS-PAY-발열 회신 — TWTA 채널별 발열·배치

입력: examples/ksat8/deliverables/PAY/u1-dsn.md, examples/ksat8/deliverables/TCS/pay-thermal-capability.md,
examples/ksat8/board/REQ-TCS-PAY-발열.md

- 채널당 TWTA 발열: **210W**(DC입력310W−RF출력100W), TCS확약 262W/채널 이내
  (마진52W).
- 24채널 총 발열: **5,040W** ≤ TCS확약 6,300W(마진1,260W).
- 배치도: 남/북 패널 각 4열×3행(12채널), 예비 TWTA 4기는 각 패널 모서리
  2기씩 냉대기 배치(발열 거의 없음, 히터 5W/기).
- Duty/이중화: 24채널 상시 가동(100% duty), 예비 4기는 대기(발열 무시가능
  수준, 히터 20W 합산).

검증: 채널당210W≤262W(TCS확약), 24채널5.04kW≤6.3kW(마진1.26kW), 배치도 회신
