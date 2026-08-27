# TCS-U1 형상관리 배포 기록 (FM 도면·해석서, 조건부)

입력: examples/ksat7/deliverables/TCS/unit1-review-board.md, unit1-thermal-design.md,
unit1-thermal-analysis.md, unit1-structural-analysis.md, unit1-drawing-check.md

## 배포 대상
- 도면·해석서 세트: TCS-U1-DWG-001 (히트파이프 배치도), TCS-U1-DWG-002 (라디에이터
  구조도), 열해석서(unit1-thermal-analysis.md), 구조해석서(unit1-structural-analysis.md)
- 판정 근거: TCS-RB-01 "조건부 승인 — 제작 착수 가능(FM 진행)". BOL 기준 전 항목
  sysreq 충족(고온+42°C·저온-12°C·배터리+8°C, 여유3°C)

## 배포
- 베이스라인 ID: TCS-U1-BL-001
- 개정: Rev A (조건부 배포)
- 배포일: 2026-08-27
- 배포처: PUR(구매), MFG(제작) 대기 — 이 기준선을 입력으로 사용
- **조건부 사항 승계**:
  1. EOL 열화 리스크 — TCS-TST-01(TVAC)에서 저온케이스 극단치(코팅 열화 α 최대 가정)
     재확인을 시험 판정 기준에 추가 필요
  2. 히트파이프 단일고장(90W>80W정격) 리스크 — FM 형상은 수용(Accept)하되 리스크
     등록부 기록, 차기 블록 정격 상향(90W/식) 검토 권고
  두 사항 모두 module-fm.md 리스크로 승계 기록 필요

## 형상관리 처리
1. RB 판정 문서와 도면·해석 산출물 목록 대사 — 일치
2. 조건부 사항 2건 확인
3. 조건부 베이스라인 등록, 구매·제작 단계 처리 가능 상태로 전환

검증: RB 판정 대비 산출물 목록 및 조건부 사항 2건(TVAC 재확인, 단일고장 리스크 수용)
일치 확인, 조건부 배포 완료.
