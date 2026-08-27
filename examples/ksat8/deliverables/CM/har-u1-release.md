# HAR-U1 100V 전력 하니스 형상관리 배포 기록

입력: examples/ksat8/deliverables/HAR/u1-design.md,
examples/ksat8/deliverables/HAR/u1-thermal-analysis.md,
examples/ksat8/deliverables/HAR/u1-electrical-analysis.md,
examples/ksat8/deliverables/HAR/u1-drawing-check.md,
examples/ksat8/deliverables/HAR/u1-review-a.md,
examples/ksat8/deliverables/HAR/u1-review-b.md,
examples/ksat8/deliverables/HAR/u1-review-board.md
(전건 CM-HAR-U1 요청 게시글이 지정한 대상 산출물)

## 배포 대상
- 도면 세트: HAR-U1-DWG-001(100V 전력 하니스 배선도)
- 판정 근거: HAR-U1-RB-01 확정(조건부) — 전압강하 주버스 0.23%/분기
  0.77% ≤ 내부기준 1%, 절연 이격 3mm(도체간)/4mm(대지간) EPS 요구 상회

## 배포
- 베이스라인 ID: HAR-U1-BL-001
- 개정: Rev A(조건부 최초 배포)
- 배포일: 2026-08-27
- 배포처: PUR(자재 구매, PUR-HAR-U1), MFG(제작) 대기 — 이 기준선을 입력으로 사용
- 승계 리스크(RB-01 조건 그대로 승계): ① 커넥터 p/n 잠정(PCU-PWR-J1) →
  PUR 발주 시 정식 MIL-DTL-38999 III p/n 반영 필요 ② OBC 모니터링
  인터페이스·STR 라우팅 잠정 가정 — 정식 회신 접수 시 재확인 필요

## 형상관리 처리
1. RB-01 판정 문서와 설계·해석·검도·검토 산출물 7건 목록 대사 — 일치
2. 베이스라인 등록 완료, 구매 단계 처리 가능 상태로 전환. 커넥터 p/n
   조건은 PUR-HAR-U1 요청 처리 시 정식 p/n(MIL-DTL-38999 시리즈 III)으로
   대체함을 발주 근거에 명시하도록 PUR 측에 조건 전달.

검증: RB-01 판정 대비 산출물 7건 목록 일치 확인, 베이스라인 HAR-U1-BL-001
등록(조건부, 커넥터 p/n 승계 리스크 명시).
