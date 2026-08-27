# COMM-U1 TT&C 트랜스폰더 형상관리 배포 기록

입력: examples/ksat8/deliverables/COMM/comm-u1-baseline.md (REQ-COMM-CM-형상관리
요청 게시글이 지정한 대상 산출물 — COMM-RB-01 baseline 승인)

## 배포 대상
- Baseline: 주파수 2087.5MHz(상향)/2255.5MHz(하향), PN레인징+240/221,
  SSPA 2W정격, 상시150W/피크220W, 1553B 이중버스(OBC IF)
- 판정 근거: COMM-RB-01 승인 — RVW1(RF, 조건부)·RVW2(전력/열/IF, 무조건)
  종합

## 배포
- 베이스라인 ID: COMM-U1-BL-001
- 개정: Rev A(조건부 최초 배포)
- 배포일: 2026-08-27
- 배포처: PUR(부품 구매, REQ-COMM-PUR-부품), TST(RF시험) 대기 — 이 기준선을
  입력으로 사용
- 승계 리스크(NCR-COMM-01, RB 판정문서에서 그대로 승계): 안테나 배치·이득
  (3dBi, LGA×2)은 STR 미회신에 따른 잠정 가정. REQ-COMM-STR-안테나 정식
  회신 도착 시 링크버짓 재계산·baseline 갱신 필요(RF 링크마진 ≥6dB로
  안테나 이득 ±3dB 변동에도 마진 유지 가능하므로 제작·시험 진행에는
  지장 없음).

## 형상관리 처리
1. RB 판정 문서(comm-u1-baseline.md) 대비 배포 대상 대사 — 일치
2. 베이스라인 등록 완료, 구매·시험 단계 처리 가능 상태로 전환

검증: RB 판정 대비 배포 대상 일치 확인, 베이스라인 COMM-U1-BL-001 등록
(안테나 배치 NCR-COMM-01 승계).
