# MECH 전개기구 비행모델 인도 — module-fm
입력: examples/ksat6/deliverables/MECH/unit1-sa-hinge-design.md, examples/ksat6/deliverables/MECH/unit1-sa-hinge-mfg.md, examples/ksat6/deliverables/MECH/unit1-sa-hinge-inspection.md, examples/ksat6/deliverables/MECH/unit2-hdrm-design.md, examples/ksat6/deliverables/MECH/unit2-hdrm-mfg.md, examples/ksat6/deliverables/MECH/unit2-hdrm-inspection.md, examples/ksat6/deliverables/MECH/unit3-antenna-deploy-design.md, examples/ksat6/deliverables/MECH/unit3-antenna-deploy-mfg.md, examples/ksat6/deliverables/MECH/unit3-antenna-deploy-inspection.md, examples/ksat6/deliverables/MECH/deployment-function-test.md, examples/ksat6/deliverables/MECH/interface-sa.md

## 구성
- SA 전개힌지 쌍(윙당 2개×2윙), 홀드다운·릴리즈(HDRM, 4점), X-band 안테나
  전개기구(1축). 비행모델(FM) 단계 — 중력보상 전개 기능시험 완료.

## sysreq MECH 항목 최종 판정 (수치 인용)
| 항목 | 요구(sysreq.md) | 최종 실측/판정 | 근거 |
|---|---|---|---|
| 전개 충격 | ≤50 g | **최대 32.8 g**(SA 힌지 래치, 3개 기구 중 최대치) | deployment-function-test.md |
| 단일고장 허용 | 필요 | SA힌지(이중 토션스프링)·HDRM(이중 NEA)·안테나(이중 스프링) 3개 기구 전량 단독계열 3/3 전개 성공 실증 | deployment-function-test.md |

## 진행 경과 요약
- MECH-U1(SA 전개힌지: 설계·제작·검사) ∥ MECH-U2(HDRM: 설계·제작·검사) ∥
  MECH-U3(X-band 안테나 전개기구: 설계·제작·검사) → MECH-U4(전개 기능시험,
  중력보상, 3개 기구 통합) — 3개 유닛 전량 검사 합격 후 통합시험 순으로 진행.
- 외부 인터페이스 회신: SA(REQ-SA-MECH) 회신 완료 — 힌지 강성 목표
  45Nm/rad 채택(예비치 그대로 확정, 이후 재작업 없음).
- 잠정 가정 없음 — 필요했던 REQ-SA-MECH가 폴링 이전에 이미 회신되어 진행.

검증: sysreq MECH 2항목(전개충격≤50g, 단일고장허용) 전량 실측/시험으로 충족 확인.
