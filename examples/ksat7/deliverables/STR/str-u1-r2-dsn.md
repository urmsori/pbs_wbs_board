# STR-U1 rev.2 보강 재설계 (NCR 대응)

입력: examples/ksat7/deliverables/STR/str-u1-tst-sine.md(NCR, 실측30.4Hz), str-u1-anl-s2.md(권고),
examples/ksat7/deliverables/PAY/str-interface-reply.md(REQ-STR-PAY 회신 — 확정 인터페이스)

## 변경 사항
1. 상판 국부 리브 4개소 추가(안테나 장착점 주변), 중앙튜브 벽두께 +0.4mm(적층 2겹 추가).
2. 안테나 장착 인터페이스를 PAY 실확정 사양으로 전면 재설계: **3점 킨매틱 마운트, PCD400mm
   8-M8, 로컬강성 65N/µm 확보**(요구 ≥50N/µm 대비 마진 30%) — 기존 4점 PCD500/M10 잠정
   브래킷은 폐기.
3. 안테나 하중 반영: 전개반력 850N(PAY 회신)을 인터페이스 설계 하중으로 채택.

## 질량 영향
보강분 +3.2kg(리브+튜브 적층), 인터페이스 브래킷 재설계 STR-U2 쪽에서 별도 처리(질량 변동은
STR-U2-R2-MFG에서 반영). STR-U1 자체 질량: 41.3kg(rev.1 실측) + 3.2kg = **44.5kg**
— sysreq ≤45kg 대비 마진 0.5kg(타이트, rev.2 특기사항).

## 다음 단계
STR-U1-R2-ANL로 1차모드 재해석(목표 ≥35Hz 예측 확보) 후 CM 재배포.
