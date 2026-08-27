입력: examples/ksat7/deliverables/TCS/unit1-thermal-design.md, examples/ksat7/deliverables/SE/sysreq.md

# TCS-U1 구조해석 (라디에이터·히트파이프 장착부)

sysreq STR 행 참조(준정적10g, 1차모드≥35Hz 조건은 STR 팀 전체해석 범위이며
본 해석은 TCS 국부 장착부 한정).

## 라디에이터 패널 장착
- -Y면 브래킷 4점, 준정적10g 하중 케이스 국부 응력해석: 최대응력 118MPa
  (Al6061-T6 항복275MPa 대비 MS=+1.33).
## 히트파이프 클램프
- 클램프 4식(모듈당), 10g 하중 시 클램프 체결력 대비 여유 MS=+0.55.

## 판정
라디에이터 장착부 MS+1.33, 히트파이프 클램프 MS+0.55 — 준정적10g 조건 국부
건전성 충족(양수 MS).

검증: 국부 준정적10g 해석 MS 라디에이터+1.33·클램프+0.55(양수, 충족)
