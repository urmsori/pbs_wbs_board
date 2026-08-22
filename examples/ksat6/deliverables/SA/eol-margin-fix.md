# SA EOL 마진 보완설계 (스트링 증설)
입력: examples/ksat6/deliverables/SA/flash-test.md, examples/ksat6/deliverables/SA/mech-str-interface-answer.md, examples/ksat6/deliverables/MECH/interface-sa.md

## 원인
- SA-01 설계는 EOL 열화계수(0.88)만 반영하고 셀 직렬저항·스트링 정합손실
  (2~3%)을 분리 반영하지 않아, 실측(SA-03) 대비 EOL 예측이 낙관적이었다.
  실측 BOL은 설계치와 정합(+0.4%)했으므로 결함은 설계 마진 산정 쪽에 있다.

## 보완: 윙당 10→11스트링 증설
- 셀수: 11스트링×19셀 = 209셀/wing (기존 190셀 대비 +10%)
- 폭 방향 증설(길이 1.6m 유지, 폭 0.38→0.418m) — **힌지 회전축 기준 연장길이(L=1.6m)는 불변**이라
  MECH 힌지 인터페이스(REQ-SA-MECH 회신, examples/ksat6/deliverables/MECH/interface-sa.md) 재협상 불필요.
- 윙당 질량: 기판(0.669m²×2.15) 1.44kg + 셀층(0.669×0.7) 0.47kg = **1.91 kg**(기존 1.74kg 대비 +9.8%)
- 힌지축 관성모멘트 재계산: I=(1/3)×1.91×1.6² = **1.63 kg·m²**(기존 1.51 대비 +7.9%, L 불변이라 증가폭이 질량 증가율보다 작음)
- 요구 힌지강성 k=I·ω²(ω=5.03rad/s) = 1.63×25.3 ≈ **41.3 Nm/rad** — MECH 설계목표(≥45Nm/rad, examples/ksat6/deliverables/MECH/interface-sa.md) 이내(마진 8.2%), **MECH 재설계 불필요**.

## EOL 재판정 (SA-03 실측 BOL/EOL 비율 0.880 적용)
- 신규 BOL(스케일링) = 368.2W × (209×2)/(190×2) = 368.2×1.10 = **405.0 W**
- 신규 EOL = 405.0 × 0.880 = **356.4 W**

## 판정 (sysreq 인용)
- sysreq "SA: EOL 340W(수직입사)" → 356.4W ≥ 340W, **충족**(마진 4.8%).
- sysreq "전개 후 1차모드 ≥0.8Hz" → 힌지강성 요구치 41.3Nm/rad ≤ MECH 목표 45Nm/rad 이내 유지, SA-04에서 최종 확인.

검증: SA-03 실측 BOL/EOL 비율(0.880)을 스트링수 비례 스케일링해 EOL 356.4W 산출, sysreq 340W 대비 마진 4.8%로 재판정 통과. MECH 힌지 인터페이스 재협상 불필요함을 확인.
