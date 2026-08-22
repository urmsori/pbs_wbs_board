# 2차 브래킷군 설계
입력: examples/ksat6/deliverables/STR/unit1-panel-frame-design.md, examples/ksat6/deliverables/STR/interface-aocs.md, examples/ksat6/deliverables/STR/interface-comm.md, examples/ksat6/deliverables/STR/interface-prop.md, examples/ksat6/deliverables/MECH/interface-sa.md

## 브래킷 목록 (인터페이스 회신 반영)
| 브래킷 | 장착 대상 | 위치 | 질량 |
|---|---|---|---|
| SA 힌지 브래킷 ×2 | SA 전개힌지 (MECH-U1) | ±X 코너프레임 | 0.6kg ×2 |
| X-band 안테나 브래킷 | X-band 안테나 | -Z(0,0,-450) | 0.3kg |
| S-band 안테나 브래킷 ×2 | S-band 안테나 | (0,±400,0) | 0.15kg ×2 |
| 탱크 마운트 브래킷 4점 | PROP 탱크 | Z=+50 크로스빔 | 0.8kg |
| 정렬큐브 아일랜드 | AOCS 큐브 | -Z 탑재체 데크 | 0.2kg |
| **합계** | | | **2.85 kg** |

## 질량 갱신
- 1차구조(unit1 실측) 19.9kg + 2차 브래킷 2.85kg = 22.75kg > sysreq 22kg 초과.
- 마진 확보를 위해 탱크 브래킷을 크로스빔 공용 설계로 변경, 브래킷 재질을
  Al7075→Al7075 박육화(리브 보강)로 0.8kg→0.55kg 절감 → 브래킷 합계 2.6kg,
  1차구조+2차 브래킷 = 19.9+2.6 = **22.5kg** — 여전히 sysreq 22kg 근소 초과.
  STR-U3-ANL(구조해석)에서 마진 재검증 필요(1차구조 실측 마진 활용 여부 판단).

검증: 2차 브래킷 경량화 반영 후 22.5kg — sysreq STR 22kg 대비 0.5kg 초과, STR-U3-ANL에서 최종 마진 판정 필요(내부 재작업 기록).
