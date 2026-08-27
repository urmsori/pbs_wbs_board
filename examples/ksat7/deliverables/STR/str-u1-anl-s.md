# STR-U1 1차구조체 구조해석

입력: examples/ksat7/deliverables/STR/str-u1-dsn.md, examples/ksat7/deliverables/SE/sysreq.md
(1차모드≥35Hz, 준정적10g), REQ-STR-PAY(회신 미수신 — 잠정 안테나 38kg·PCD500mm 4점 가정 사용)

## 유한요소 결과 (잠정 안테나 질량 가정 기반)
- SAR 안테나 장착 상태 1차 굽힘모드: **37.2 Hz** — sysreq 1차모드≥35Hz 대비 마진 +2.2Hz(6.3%). **판정: 충족**
- 준정적 10g 하중 케이스 최대 응력 여유(MS): 중앙 튜브 MS=+0.31, 상판 브래킷 MS=+0.18(모두 양수).
  sysreq 준정적10g 요구 **충족**.
- 민감도: 안테나 질량이 가정(38kg) 대비 +10% 증가 시 1차모드 35.9Hz까지 하락 — 여전히 35Hz 이상,
  REQ-STR-PAY 실측치 수신 시 재검증 필요(리스크로 기록).

## 질량
41.0kg (ANL 단계에서 DSN 대비 변경 없음) — sysreq ≤45kg 대비 마진 4.0kg. **판정: 충족**
