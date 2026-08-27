# AOCS-U1 형상관리 배포 기록 (요 스티어링 제어계)

입력: examples/ksat7/deliverables/AOCS/u1-review-board.md, u1-yaw-steering-design.md,
u1-stability-analysis.md, u1-design-check.md

## 배포 대상
- 제어법칙 문서: AOCS-U1-DWG-CTRL-001 (제어법칙·게인표)
- 센서/액추에이터 배분표: AOCS-U1-DWG-ALLOC-001 (별추적기·자이로·반작용휠·마그네토커 배분)
- 판정 근거: AOCS-U1-RB 승인 — 정렬오차 배분 0.0035°(12.6arcsec) 대비 STR 실측 합
  7.3arcsec 충족, 안테나 1차모드 조건 해소로 승인

## 배포
- 베이스라인 ID: AOCS-U1-BL-001
- 개정: Rev A (최초 배포)
- 배포일: 2026-08-27
- 배포처: PUR(AOCS-U2 장비 구매), TST(HIL 시험) 대기 — 이 기준선을 입력으로 사용
- 승계 리스크: STR 판정기준(35Hz) 최종 충족 여부는 STR track ANL-S 재해석(REQ-STR-PAY
  질량 72kg 반영)에서 별도 확정 예정 — AOCS 설계 승인과는 별개 사안으로 module-fm.md에 기록

## 형상관리 처리
1. RB 판정 문서와 설계·해석·검도 산출물 목록 대사 — 일치
2. 베이스라인 등록 완료, 구매·시험 단계 처리 가능 상태로 전환

검증: RB 판정 대비 산출물 목록 일치 확인, 베이스라인 AOCS-U1-BL-001 등록.
