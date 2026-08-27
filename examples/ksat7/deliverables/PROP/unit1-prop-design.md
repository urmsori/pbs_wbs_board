입력: examples/ksat7/deliverables/SE/sysreq.md, examples/ksat7/deliverables/STR/prop-mounting-icd.md,
examples/ksat7/deliverables/PROP/thruster-operating-profile.md,
examples/ksat7/board/REQ-PROP-EPS.md(잠정 — EPS 회신 대기)

# PROP-U1 홀추력기 시스템 개념설계

sysreq PROP 행: Δv 25m/s, 홀추력기 300W급, 제논 예산.

## 추진제 예산
- Isp 1,500s, 300W급 홀추력기(방전전압 300V·전류 1.0A, thruster-operating-profile
  회신치와 정합), 위성질량 ≈280kg(마진 반영) 가정.
- 소요 추진제질량 mp = m0(1-exp(-Δv/(Isp·g0))) = 280×(1-exp(-25/14,710)) ≈ 0.48kg.
- 설계 마진 30% 적용 → 제논 예산 0.62kg. 탱크 용량 2L급, 충전압 150bar(상온) 선정
  (여유 포함 시 최대 탑재 가능량 ≈1.1kg > 0.62kg 소요, 여유율 77%).

## 장착 배치 (STR 확정, REQ-PROP-STR 회신)
- 추력기: 하판 -Z면 (0,0,-420mm), 추력방향 질량중심 관통, 4점 M6 볼트 PCD120mm.
- 제논탱크: 중앙튜브 하단 스트랩 마운트. 준정적10g 하중 MS=+0.22(양수, 충족),
  1차모드 37.2Hz(≥35Hz sysreq STR 충족, SAR 안테나 장착 상태 포함 해석치).

## 배관·전력 인터페이스
- 제논 배관: 탱크→압력조절기→추력기, 래치밸브 이중화(단일고장 허용).
- 전력: 300W(300V/1.0A), 운전 프로파일은 thruster-operating-profile.md 확정
  (캠페인당 90분, SAR-추력 상호배타 운용). EPS 300W 연속 공급 확약은
  REQ-PROP-EPS 회신 대기 — 잠정으로 모선 전력예산(EOL 620W 공급/540W 소비)
  내 캠페인 궤도(SAR 미촬영)에서 공급 가능하다고 가정.

## 판정(설계 단계)
Δv 25m/s 대비 제논 예산 0.62kg(탑재여유 77%), 장착부 구조 여유 확보(STR 확인).
전력 확약은 잠정 — REQ-PROP-EPS 확정 후 갱신. 정량 열해석은 PROP-ANL-T-01에서 수행.

검증(설계 단계): 제논예산 0.62kg≤탑재1.1kg(여유77%), 장착 MS+0.22·37.2Hz≥35Hz(STR),
전력 300W(잠정, EPS 회신 대기).
