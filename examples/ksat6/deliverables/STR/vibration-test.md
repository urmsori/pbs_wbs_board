# 구조시험(정현·랜덤 진동)
입력: examples/ksat6/deliverables/STR/structural-analysis.md, examples/ksat6/deliverables/STR/unit1-panel-frame-inspection.md, examples/ksat6/deliverables/STR/unit2-brackets-inspection.md

## 시험 조건
- 정현진동(sine burst): 준정적 12g 등가, 5~100Hz 스윕(sysreq STR 12g 인용).
- 랜덤진동: 발사환경 스펙트럼(20~2000Hz, 전체 RMS 8.2 grms), 3축 각 1분.

## 결과 — 공진탐색(모드 상관)
| 항목 | 해석(STR-U3-ANL) | 시험 실측 |
|---|---|---|
| 1차 모드 | 44.6 Hz | 43.1 Hz (해석 대비 −3.4%, 상관 양호) |
| 2차 모드 | 58.3 Hz | 57.0 Hz |

- 정현진동 12g 등가 인가 후 잔류 변형·균열 없음(육안·타각검사).
- 랜덤진동 후 재공진탐색: 1차모드 42.9Hz(시험 전 43.1Hz 대비 0.5% 이내 변화 — 구조 건전성 확인).

## 판정
- 1차모드 실측 43.1Hz ≥ sysreq STR 40Hz 요구 충족.
- 준정적 12g 등가 정현시험 후 손상 없음 — sysreq STR 12g 요구 충족.

검증: sysreq STR 인용 — 1차모드≥40Hz(실측43.1Hz 충족), 준정적12g(정현시험 후 손상없음, 충족). 해석-시험 상관 오차 3.4% 이내.
