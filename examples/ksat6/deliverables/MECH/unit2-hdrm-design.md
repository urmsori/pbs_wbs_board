# 홀드다운·릴리즈(HDRM) 설계
입력: examples/ksat6/deliverables/SA/mech-str-interface-answer.md, examples/ksat6/deliverables/STR/unit2-brackets-design.md

## 요구사항 인용 (sysreq.md MECH)
- 전개 충격 ≤50g, 단일고장 허용

## 구속 설계
- 윙당 2점 홀드다운(내측·외측), 각 점 케이블 커터 방식 **이중 화약 커터**
  (단일고장 허용) + 예비 열선(비화약) 백업 방출 경로.
- 구속력: 준정적 12g 마운트 반력 208N/윙(REQ-STR-SA 인용) 대비 설계 예압
  하중 320N/점(마진 확보, 2점 분산 시 각 160N 분담 + 마진).

## 방출 충격 저감
- 화약 커터 대신 저충격 비화약(NEA, Non-Explosive Actuator) 채택 —
  발화식 대비 충격 스펙트럼 저감(설계 목표 방출 순간 가속도 ≤20g,
  전개 전체 과정 종단 충격은 MECH-U1 힌지 댐퍼가 지배 ≤35g).
- NEA 이중화(주+예비, 각 독립 구동회로) — 단일고장 허용.

검증: sysreq MECH 인용 — 단일고장허용(NEA 이중화+비화약 백업 충족), 전개충격≤50g(NEA 방출순간 설계목표20g<50g, 실측은 MECH-U4-TST).
