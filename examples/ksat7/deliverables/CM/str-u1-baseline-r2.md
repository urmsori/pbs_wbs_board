# STR-U1 형상관리 재배포 기록 (베이스라인 rev.2, NCR 대응)

입력: examples/ksat7/deliverables/STR/str-u1-r2-anl.md, str-u1-tst-sine.md,
examples/ksat7/deliverables/CM/str-u1-baseline.md(rev.1)

## 배포 대상 (개정)
- 도면: STR-U1-DWG-001~005 rev.2 — 상판·중앙튜브 리브 추가, 3점 킨매틱 인터페이스
  (PCD400mm, 8-M8, 로컬강성 65N/µm)로 개정
- 판정 근거: STR-U1-R2-ANL 예측 — 1차모드 36.8Hz(요구≥35Hz 대비 마진 +1.8Hz, 5.1%),
  준정적10g MS 전부 양수(최소 +0.15), 질량 44.5kg(≤45kg, 마진 0.5kg)

## 배포
- 베이스라인 ID: STR-U1-BL-001
- 개정: **Rev B** (rev.1의 1차모드 NCR/RED에 대한 보강 재설계 반영)
- 배포일: 2026-08-27
- 배포처: PUR(rev.2 자재 구매), MFG(개조 제작, STR-U1-R2-MFG) 대기
- 승계 상태: 본 배포는 **해석 예측 기반**(36.8Hz)이며, STR-U1-R2-TST 실측 확정 전까지는
  module-fm.md의 NCR/RED 오픈 상태를 유지한다 — 실측 완료 후 STR 팀이 module-fm.md를
  갱신할 때 Rev B 실측 확정치로 종결 예정.

## 형상관리 처리
1. rev.2 해석 문서(str-u1-r2-anl.md)와 개정 도면 목록 대사 — 리브 추가·인터페이스
   PCD400/8-M8 반영 확인
2. rev.1 대비 개정 이력 기록(Rev A→Rev B), 베이스라인 ID는 유지하고 개정기호만 갱신
3. 재배포 완료, 제작 단계 처리 가능 상태로 전환

검증: rev.2 해석(36.8Hz≥35Hz, MS+0.15, 44.5kg≤45kg) 대비 개정 도면 반영 확인,
베이스라인 STR-U1-BL-001 Rev B 재배포 완료(실측 확정은 R2-TST 대기).
