# COMM-U1 X-band 송신계 장착부 구조해석

입력: examples/ksat7/deliverables/COMM/comm-u1-dsn.md, examples/ksat7/deliverables/STR/str-u1-dsn.md,
examples/ksat7/deliverables/STR/comm-antenna-mount-spec.md, examples/ksat7/deliverables/SE/sysreq.md

## 해석 조건
- 장착: -Y측판, 4×M8 PCD150mm, 유닛질량 3.0kg(안테나+HPA 브래킷 포함)
- 하중: 준정적 10g(sysreq.md STR 요건), 발사 랜덤진동 스펙트럼(STR 표준)

## 결과
- 브래킷 국부 1차모드: 118Hz(FEM), STR 회신치 "1차모드 기여 <0.1Hz 영향" 확인 —
  STR-U1 전체 1차모드(≥35Hz 목표)에 미치는 영향 무시 가능.
- 준정적 10g 하중 시 M8 볼트 최대응력 142MPa < 허용 320MPa(A286, 안전율 2.25).
- 브래킷 최대 처짐 0.08mm(강성 목표 <0.15mm 충족).

판정: sysreq.md 1차모드 ≥35Hz(SAR 안테나 장착 상태) 목표에 COMM-U1 장착부가
저해요인 아님(국부모드 118Hz≫35Hz, 응력 안전율 2.25). 제작 착수 가능.
