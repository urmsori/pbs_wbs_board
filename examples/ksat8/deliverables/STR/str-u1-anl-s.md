# STR-U1 중앙 실린더 구조해석

입력: examples/ksat8/deliverables/STR/str-u1-dsn.md, examples/ksat8/deliverables/SE/sysreq.md (1차모드≥30Hz), examples/ksat8/deliverables/PROP/str-prop-tank-reply.md, examples/ksat8/deliverables/SA/str-sa-load-reply.md, examples/ksat8/deliverables/PAY/str-pay-mount-reply.md

## 유한요소 모델
집중질량: 이원추진제 탱크 1,363kg(하부데크), SA 2윙 360kg(측판), PAY 중계기 156.6kg
(상판)+STR-U2 패널 구조 잠정104kg(상판/측판), 구조자체 244kg.

## 결과
- 1차 굽힘모드(횡): **33.6 Hz** — sysreq ≥30Hz 대비 마진 +3.6Hz(12%). **충족**
- 트러니언 장착점 국부모드: 62.1Hz ≥ PROP 요구 60Hz. **충족**
- 준정적 설계하중(PROP 회신 축8.5g/횡4.5g) 여유(MS): 중앙튜브 MS=+0.22,
  트러니언보강링 MS=+0.15, SA마운트 MS=+0.31(모두 양수). **충족**

## 질량
244kg (DSN 대비 변경 없음) — 목표≤260kg 대비 마진16kg.
