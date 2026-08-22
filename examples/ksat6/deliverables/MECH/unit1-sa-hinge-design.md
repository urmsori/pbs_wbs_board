# SA 전개힌지 쌍 설계
입력: examples/ksat6/deliverables/MECH/interface-sa.md, examples/ksat6/deliverables/SA/mech-str-interface-answer.md, examples/ksat6/deliverables/STR/unit2-brackets-design.md

## 요구사항 인용 (sysreq.md MECH)
- 전개 충격 ≤50g
- 단일고장 허용(single fault tolerance)

## 힌지 구성
- 윙당 2개 힌지(내측·외측), 각 힌지 **이중 토션스프링**(주+보조, 각 50%
  토크 분담) — 스프링 1개 파손 시에도 나머지로 전개 완료 가능(단일고장 허용 충족).
- 잠금: 정전개 완료 시 캠 래치, 래치 토크 0.6 Nm(interface-sa.md 인용).
- 힌지 강성(래치 후, 잠금 상태): 45 Nm/rad(interface-sa.md 예비치 확정 채택)
  → 전개 후 1차모드 ≈0.87Hz ≥ sysreq SA 0.8Hz(참고 인용, MECH 인도물은 아니나
  인터페이스 정합 확인).

## 전개 충격 저감 설계 (sysreq MECH ≤50g)
- 종단 감쇠: 점성 로터리 댐퍼(엔드스톱 직전 90°구간 감쇠 작동), 전개
  각속도를 목표 ≤10°/s(SA 회신 인용)로 제한.
- 운동에너지: 윙 관성 1.51kg·m² × (0.175rad/s)² /2 ≈ 0.023 J → 댐퍼로 종단
  0.05초 내 흡수 설계, 래치 충격 가속도 개산 **≤35g**(설계 목표, sysreq
  50g 대비 마진 30%) — 상세 값은 MECH-U4-TST 기능시험에서 실측 확인.

## 단일고장 허용 대책 요약
- 스프링 이중화(주+보조), 래치 캠 이중 접촉면, 힌지 베어링 계열 2조 병렬.

검증: sysreq MECH 인용 — 단일고장 허용(스프링 이중화로 충족), 전개충격≤50g(설계목표 35g, 실측은 MECH-U4-TST에서 확정).
