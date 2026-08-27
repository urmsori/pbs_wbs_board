# INT-TST-4 통합시험4 — 환경·열(TWTA 6kW 방열 통합 확인)

입력: examples/ksat8/deliverables/AIT/rx-2.md,
examples/ksat8/deliverables/TCS/module-fm.md, examples/ksat8/deliverables/PAY/module-fm.md

## 시험 구성
통합 본체 형상(TWTA 24기 실장, 인접 EPS/COMM/HAR 열원 포함)을 열진공
챔버에 투입해 TCS 패널(히트파이프 매립) 단위 TVAC 결과가 통합
형상에서도 유지되는지 재확인.

## 결과
| 항목 | TCS 모듈시험(패널단위) | 통합시험(위성 전체) | 판정 |
|---|---|---|---|
| 발열부하 | 5.04kW(채널당210W×24, 확정치) | 5.04kW+인접열원(EPS/COMM 발열 0.3kW) = 5.34kW | 방열용량6.3kW 대비 마진0.96kW(15%) — PASS |
| 고온 | +52°C | +54°C(인접열원 영향 +2°C) | 요구 상한+60°C 이내 — PASS |
| 저온(히터보정 후) | -9°C | -8°C(통합 열저항 소폭 감소) | 요구 하한-10°C 이내 — PASS |
| 이클립스 히터 200W | H1~H6 우선순위 | 우선순위 그대로 재현, 정상 동작 | PASS |

인접 서브시스템 열간섭을 반영해도 sysreq TCS 요구(방열6kW·작동범위
-10~+60°C)를 마진 내로 충족 — 통합 형상에서 TWTA 6kW 방열 성능 확정.

검증: 통합 열부하5.34kW≤6.3kW(마진15%), 온도범위-8~+54°C(요구
-10~+60°C 이내) — TCS 모듈시험 결과가 통합 형상에서도 유효함을 확인
