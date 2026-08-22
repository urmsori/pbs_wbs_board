# 전개 기능시험(중력보상)
입력: examples/ksat6/deliverables/MECH/unit1-sa-hinge-inspection.md, examples/ksat6/deliverables/MECH/unit2-hdrm-inspection.md, examples/ksat6/deliverables/MECH/unit3-antenna-deploy-inspection.md, examples/ksat6/deliverables/MECH/unit1-sa-hinge-design.md, examples/ksat6/deliverables/MECH/unit2-hdrm-design.md, examples/ksat6/deliverables/MECH/unit3-antenna-deploy-design.md

## 시험 조건
- 중력보상: SA 윙 2축 에어베어링 지그, X-band 안테나 와이어 서스펜션.
- 상온(20°C), 3회 반복 전개(윙 2개·안테나 1개 각 3회 = 9회).

## 결과 — 전개 충격 (가속도계, 래치/방출 순간 피크, sysreq MECH ≤50g)
| 기구 | 설계목표 | 시험 실측(3회 평균 피크) |
|---|---|---|
| SA 힌지 래치(윙1) | ≤35g | 31.2 g |
| SA 힌지 래치(윙2) | ≤35g | 32.8 g |
| HDRM NEA 방출 | ≤20g | 17.5 g |
| X-band 안테나 래치 | ≤15g | 12.9 g |

전 항목 sysreq MECH 50g 대비 큰 마진으로 충족(최대 실측 32.8g < 50g).

## 결과 — 단일고장 모의 (sysreq MECH 단일고장 허용)
- SA 힌지: 보조스프링 인위 차단 후 주스프링 단독 전개 — 3/3 성공, 전개시간 8.2초(정상 대비 +1.1초, 규격 이내).
- HDRM: 주 NEA 인위 차단 후 예비 NEA 단독 방출 — 3/3 성공.
- X-band 안테나: 보조스프링 차단 후 주스프링 단독 전개 — 3/3 성공.

## 전개 시간·완전전개각 확인
- SA 윙 자유전개각 179.4→179.6°(3회 평균), X-band 89.6→89.8°(3회 평균) — 설계 공차 이내 유지.

검증: sysreq MECH 인용 — 전개충격≤50g(실측 최대32.8g 충족), 단일고장허용(3개 기구 전량 단독계열 3/3 성공 실증).
