# 전기추진(이온추력기) 계통 설계
입력: examples/ksat8/deliverables/SE/sysreq.md, examples/ksat8/deliverables/EPS/ep-power-commitment.md,
examples/ksat8/deliverables/AOCS/unloading-thrust-req.md, examples/ksat8/deliverables/PROP/eps-load-profile.md,
examples/ksat8/deliverables/PROP/aocs-unloading-interface.md, examples/ksat8/deliverables/PROP/biprop-design.md

## Δv·추진제 산정
- 담당 Δv: 750 m/s(GEO 유지 N/S+E/W + 모멘텀 언로딩, sysreq 명시치).
- 이온추력기 Isp 1,600s, 잔여 질량(3,500kg - 이원추진제 1,363kg = 2,137kg)
  기준 로켓방정식 산정: 제논 추진제 **≈100kg**.

## 추력기·전력(EPS 확약 2,000W 반영)
- 4기(2for2 이중화, 남/북 패널 각 2기), 채널당 입력전력 1,000W, 정상추력
  ≈70mN, 최대 2채널 동시 2,000W(EPS 확약 상한과 정확히 일치).
- 캔팅각 ±20°, 최소펄스 50ms, 1일 최대 점화 6시간(EPS windows).

## 모멘텀 언로딩 정합성(AOCS 확정 회신 반영)
- AOCS 요구: 축당 트리거 20N·m·s, 정렬허용 ≤1.0°.
- 소요시간 = 20N·m·s ÷ 0.079N·m(캔팅 20° 피치성분, 70mN 기준) ≈ 253초(4.2분)
  ≪ 세션 예산 10~20분 — 여유 충분.
- 캔팅 브래킷 공차를 ≤1.0°로 설계 반영(AOCS 요구 수용).
- 연간 언로딩 26회(AOCS 추정) 기준 연간 추가 점화시간 ≈110분 — 750m/s
  Δv 예산에 이미 포함된 마진으로 흡수(제논 100kg 산정에 언로딩분 포함
  가정).

## 제논 탱크
- 고압탱크 1기(150bar), 습식 ≈100kg+건식 25kg=125kg, 중앙실린더 축상 장착.

검증: 채널당 1,000W·70mN이 EPS 확약(2,000W 상한) 및 AOCS 요구(정렬 1.0°,
253초≪세션예산) 모두 충족
