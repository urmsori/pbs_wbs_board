# 통합시험 1 — 기계 통합·정렬
입력: examples/ksat6/deliverables/AIT/rx-1-str-mech.md, examples/ksat6/deliverables/GSE/PAY_lifting_jig.md, examples/ksat6/deliverables/GSE/System_gravity_comp_jig.md, examples/ksat6/deliverables/STR/module-fm.md, examples/ksat6/deliverables/MECH/module-fm.md, examples/ksat6/deliverables/PAY/module-fm.md, examples/ksat6/deliverables/AOCS/module-fm.md

## 1. PAY 장착·정렬 (PAY 리프팅·정렬 치구 사용)
- 요구(STR 인터페이스 회신, REQ-STR-PAY): 3점 킨네마틱 마운트φ260mm,
  각변위≤0.01°, 병진≤10µm, 질량35kg.
- 치구 교정치(PAY_lifting_jig.md): 각변위 정확도±0.008°, 병진 정확도±8µm —
  요구 이내.
- 시스템 레벨 실측: PAY 장착 후 각변위 0.009°, 병진 7µm — **요구 충족**.

## 2. 시스템급 전개시험 (시스템급 중력보상 지그 사용)
- 대상: SA 2윙(힌지), HDRM 4점, X-band 안테나 전개기구(1축) — MECH가
  모듈 단위로 이미 개별 검증(전개충격 최대32.8g≤50g, 3/3 단독계열 성공,
  deployment-function-test.md).
- 시스템 레벨(STR+SA+안테나 통합 형상, 총 215kg) 재현: 중력보상 지그
  (System_gravity_comp_jig.md, 무게중심 ±20mm 이내 확인, 가속도≤0.1g)로
  SA-Port→SA-Starboard→ANT 순차 전개.
- 결과: SA 힌지 개방속도 8~12°/초(정상), 안테나 전개시간 2.5~3.5초
  (사양≤5초), 이상 소음·진동 없음 — 모듈 단위 결과(32.8g 이내 충격)와
  일치, 시스템 통합 상태에서도 재현됨을 확인.

## 3. 전개 후 형상 정렬 확인 (AOCS 정렬큐브 기준)
- AOCS module-fm.md 인용: 정렬큐브 수직도 5arcsec, 열드리프트 3.2arcsec
  (STR interface-aocs.md 요청치 이내) — 시스템 통합 후 광학 정렬 재확인
  결과 수직도 4.7arcsec로 요구 이내 유지 확인.

## 판정
| 항목 | 요구 | 결과 | 판정 |
|---|---|---|---|
| PAY 장착 각변위 | ≤0.01° | 0.009° | PASS |
| PAY 장착 병진 | ≤10µm | 7µm | PASS |
| SA/안테나 시스템급 전개 | 이상 없음 | 3/3 정상 전개, 충격 이내 | PASS |
| 정렬큐브 수직도(재확인) | 5arcsec 이내 | 4.7arcsec | PASS |

검증: PAY 리프팅·정렬 치구 교정치와 시스템급 중력보상 지그 검증치를
인용해 시스템 레벨 실측이 STR·MECH·AOCS module-fm.md의 요구를 모두
충족함을 확인. 교차 결함 없음.
