# STR-U1 정현진동시험

입력: examples/ksat7/deliverables/STR/str-u1-ins.md, examples/ksat7/deliverables/CAL/str-u1-cal-cert.md,
examples/ksat7/deliverables/FAC/str-u1-fac-booking.md, examples/ksat7/deliverables/PA/str-u1-witness.md,
examples/ksat7/deliverables/STR/str-u1-anl-s2.md(재검증 예측치 참조)

## 시험 조건
정현스윕 5~100Hz, 준정적10g 등가 레벨. SAR 안테나 질량모사체(72.0kg, PAY 실측 ICD 반영,
3점 킨매틱 PCD400mm 인터페이스)를 STR-U2 브래킷에 장착한 비행형상 대표 상태로 시험. PA 입회.

## 결과
실측 1차 굽힘모드 **30.4 Hz** — ANL-S2 예측(약29.5Hz)과 3% 이내 일치, 실측으로 확인.
sysreq STR "1차모드≥35Hz(SAR 안테나 장착 상태)" **미충족(부적합)** — 부족분 4.6Hz.
준정적10g 등가 레벨에서 구조 손상·영구변형 없음(건전성은 확인됨) — 강도 요구는 별도 충족.

## 판정
**NCR(부적합보고서) 대상 — RED.** 1차모드 요구 미충족은 구조 강성 보강(STR-U1-ANL-S2 권고:
상판·튜브 리브 보강, 인터페이스 로컬강성 확보) 후 재시험이 필요하다. 본 비행형상(rev.1)은
현재 상태로 sysreq 미충족이며, module-fm.md에 오픈 비적합으로 기록하고 rev.2 설계반복으로
이관한다. 워크맨십 스크리닝(TST-RANDOM)은 구조 손상 확인 목적으로 계속 진행한다.
