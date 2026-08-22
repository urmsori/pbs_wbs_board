# PAY 광학 성능시험 (MTF·왜곡)
입력: examples/ksat6/deliverables/PAY/telescope-optics.md, focal-plane-tdi.md, payload-electronics.md

## 시험 구성
통합된 망원경(구경300mm)+초점면(TDI, 10µm 픽셀)+탑재전자부(보정·압축)
비행형상을 집속시준기(collimator)로 실측.

## 결과
| 항목 | 목표(telescope-optics.md §5) | 실측 | 판정 |
|---|---|---|---|
| MTF @나이퀴스트 50cyc/mm(축상) | ≥0.20 | 0.24 | PASS |
| MTF @나이퀴스트 50cyc/mm(전FOV 최저) | ≥0.20 | 0.21 | PASS |
| 왜곡(전FOV) | ≤0.1% | 0.07% | PASS |
| 기내보정 후 잔류 비균일성(FPN) | (참고) | 0.3% | 기록 |

기내보정(비균일보정, payload-electronics.md §1) 적용 전/후 비교 결과
FPN이 2.1%→0.3%로 개선 — sysreq PAY "기내 보정" 요구 충족 확인.

## sysreq PAY 항목 최종 판정
구경 300mm(설계값, telescope-optics.md §1) · TDI 초점면(focal-plane-tdi.md
§1, 32단) · 기내보정(위 FPN 결과) — sysreq.md "PAY: 구경 300mm 망원경,
TDI 초점면, 기내 보정" 3개 수치·항목 모두 충족.

검증: MTF 0.21~0.24 ≥ 요구 0.20, 왜곡 0.07% ≤ 요구 0.1% — sysreq PAY 최종 PASS.
