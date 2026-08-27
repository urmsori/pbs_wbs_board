# 열진공시험(TVAC)
입력: examples/ksat8/deliverables/TCS/panel-mfg.md, examples/ksat8/deliverables/CAL/tvac-cal-cert.md,
examples/ksat8/deliverables/FAC/tvac-chamber-booking.md, examples/ksat8/deliverables/TCS/thermal-analysis.md

## 시험 조건
- 열진공 챔버(FAC 예약), 배경압 ≤1×10⁻⁵ Torr, 계측기 CAL 교정 유효.
- 채널당 210W(5.04kW 총) 부하 인가, 고온/저온 2 사이클(±10°C 마진 포함
  -15~+65°C 챔버 설정).

## 결과
- 고온 사이클(전 채널 5.04kW 인가): TWTA 베이스플레이트 최고 +52°C —
  해석치(+52°C)와 일치, 허용 +65°C 이내.
- 저온 사이클(전 채널 OFF, 히터만): 최저 -9°C(히터 보정 후) — 요구 -10°C
  이내.
- 히트파이프 등온화 확인: 채널 간 편차 실측 13°C(해석 14°C와 근접).
- 누출·성능 열화 없음.

판정: 합격 — 비행모델 인도 가능
검증: 고온+52°C(해석 일치)·저온-9°C, 모두 -10~+60°C 요구 이내, 편차 실측
13°C(해석과 근접)
