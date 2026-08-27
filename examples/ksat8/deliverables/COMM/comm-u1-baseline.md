# COMM-U1 설계검토회(RB) — Baseline 승인

입력: examples/ksat8/deliverables/COMM/comm-u1-review1.md, examples/ksat8/deliverables/COMM/comm-u1-review2.md

## 결정
설계검토 1(RF, 조건부)·2(전력/열/IF, 무조건)를 취합해 **baseline 승인**한다.

- 확정: 주파수 2087.5/2255.5MHz, PN레인징+240/221, SSPA 2W정격, 상시150W/
  피크220W(EPS 예산 내), 1553B 이중버스(OBC IF).
- 조건부 이월 항목(NCR-COMM-01): 안테나 배치·이득(3dBi, LGA×2)은 STR 미회신에
  따른 **잠정 가정**이다. REQ-COMM-STR-안테나 실회신 도착 시 링크버짓
  (comm-u1-linkbudget.md)을 재계산하고 정정 게시글로 baseline을 갱신한다.
  실회신 전까지는 이 잠정치로 제작·시험을 진행해도 무방하다고 판단(RF
  링크마진 여유 ≥6dB로 안테나 이득이 ±3dB 변동해도 마진 유지 가능하므로
  제작 착수를 막을 사유가 아님).

baseline을 CM에 등록 요청한다(REQ-COMM-CM-형상관리).

검증: 조건부 항목 1건(NCR-COMM-01, 안테나 배치)을 명시한 baseline 승인.
