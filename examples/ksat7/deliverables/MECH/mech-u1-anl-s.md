# MECH-U1 SAR 2단 전개기구 구조/동역학 해석

입력: examples/ksat7/deliverables/MECH/mech-u1-dsn.md, examples/ksat7/deliverables/SE/sysreq.md
(전개충격≤40g), REQ-MECH-PAY(회신 미수신 — 잠정 관성 4.2kg·m² 가정 사용)

## 결과
- 전개 동역학 시뮬레이션(잠정 관성 4.2kg·m² 기준): 종단 각속도 3.1 rad/s, 오버센터 잠금 착지 시
  구조 피크 가속도 **34.5g** — sysreq 전개충격≤40g 대비 마진 5.5g(13.8%). **판정: 충족**
- 단일고장 해석: 릴리즈 액추에이터 1계열 고장 시에도 병렬 계열로 전개 완료 확인(FMEA 단일고장점 없음).
  sysreq 단일고장 허용 **충족**.
- 민감도: 안테나 관성이 가정 대비 +15% 증가 시 착지 충격 38.9g까지 상승 — 여전히 40g 이내이나 마진
  축소. REQ-MECH-PAY 실측치 수신 시 댐퍼 계수 재조정 필요(리스크로 기록).
