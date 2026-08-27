# HAR-U1 형상관리 배포 기록 (대전류 펄스 배선, 조건부)

입력: examples/ksat7/deliverables/HAR/u1-design.md, u1-thermal-analysis.md,
u1-drawing-check.md, u1-review-board.md

## 배포 대상
- 도면 세트: HAR-U1-DWG-001 (배선 경로도), HAR-U1-DWG-002 (커넥터 정합표),
  HAR-U1-DWG-003 (실드·접지 상세)
- 판정 근거: HAR-U1-RB-01 "설계 확정(조건부)" — 전압강하 0.85~1.70%, 최고온도 65.5°C,
  이중화 구조 모두 sysreq/PAY 요구 충족

## 배포
- 베이스라인 ID: HAR-U1-BL-001
- 개정: Rev A (조건부 배포)
- 배포일: 2026-08-27
- 배포처: PUR(구매) — 자재(AWG10 케이블, 전원 커넥터, 편조 실드 슬리브) 구매 근거로 사용
- **조건부 사항**: EPS 배전 커넥터 정격이 잠정(p/n PCDU-PWR-J4 정합 대향 커넥터 가정) 상태.
  EPS 확정 정격 도착 시 개정관리로 Rev B 반영 필요 — module-fm.md 리스크 항목으로 승계.

## 형상관리 처리
1. 도면 3매 번호·개정기호 부여 확인(중복 없음)
2. RB 판정 문서(u1-review-board.md)와 조건부 사항 대사 — EPS 커넥터 정격 미확정 상태 확인
3. 조건부 베이스라인 등록, 구매(PUR) 처리 가능 상태로 전환(리스크 오픈 유지)

검증: RB 판정 대비 도면 3매 및 조건부 사항(EPS 커넥터 정격 잠정) 일치 확인, 조건부 배포 완료.
