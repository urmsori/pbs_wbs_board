# SA 전개 인터페이스 확인 (최종)
입력: examples/ksat6/deliverables/SA/eol-margin-fix.md, examples/ksat6/deliverables/MECH/interface-sa.md

## 최종 정합
| 항목 | SA 최종치(SA-05) | MECH 제공치(REQ-SA-MECH 회신) | 판정 |
|---|---|---|---|
| 전개각 | 180°±1° | 180°±1° | 일치 |
| 볼트 패턴 | φ50mm M4×6(패널측) | M4×6 수용(φ50mm) | 정합 |
| 힌지축 관성모멘트 | 1.63 kg·m² | 설계 여유 1.51kg·m² 기준(구설계) 45Nm/rad 채택 | 최신치로 재확인 |
| 힌지 강성 | 요구 41.3 Nm/rad | 제공 ≥45 Nm/rad | 충족(마진 8.2%) |

## 1차모드 재계산 (최종 질량 반영)
- k=45 Nm/rad, I=1.63 kg·m² → ω=√(k/I)=√(45/1.63)=5.256 rad/s → f = ω/2π = **0.837 Hz**

## 판정 (sysreq 인용)
- sysreq "SA: ... 전개 후 1차모드 ≥0.8Hz" → 산출 0.837Hz ≥ 0.8Hz, **충족**(마진 4.6%).
- sysreq "SA: EOL 340W(수직입사)" → SA-05 최종 356.4W ≥ 340W, **충족**(마진 4.8%, 재확인).

검증: MECH 힌지강성(45Nm/rad, 취합 최근값 우선 원칙)과 SA-05 최종 관성(1.63kg·m²)으로 1차모드 0.837Hz 산출, sysreq 0.8Hz 요구 충족 확인. 힌지 재설계 불필요.
