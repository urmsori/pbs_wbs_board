# MECH-U1 전개시험

입력: examples/ksat7/deliverables/MECH/mech-u1-ins.md, examples/ksat7/deliverables/FAC/mech-u1-fac-booking.md,
examples/ksat7/deliverables/MECH/mech-u1-anl-s2.md(재검증 예측치 참조)

## 시험 조건
중력보상(에어베어링) 전개시험, SAR 패널 질량모사체(루트35.0kg/팁33.0kg, PAY 실측 ICD 반영)
장착, 재조정 댐퍼(MECH-U1-ANL-S2 조치 반영) 적용 상태로 1단→2단 순차 전개 3회 반복.

## 결과
전개시간 1단 8.2s/2단 7.9s, 전개각 90.0°±0.3°(공차내), 잠금 착지충격 실측 **37.1g**(3회
평균) — sysreq MECH 전개충격≤40g 대비 마진 2.9g(7.3%). ANL-S2 예측(36.4g)과 2% 이내 일치.
**판정: 충족.** 3회 반복 재현성 양호(37.1±0.6g). 단일고장 모사(릴리즈 1계열 강제 비활성)
1회 수행 — 병렬 계열로 정상 전개 확인, 단일고장 허용 **충족**.
