# REQ-AIT-HAR-플랜지실측 회신 — HAR-U2 도파관 실측 플랜지·어댑터 조치

입력: examples/ksat8/board/REQ-AIT-HAR-플랜지실측.md,
examples/ksat8/deliverables/AIT/int-tst-1.md,
examples/ksat8/deliverables/HAR/u2-pay-reconcile.md,
examples/ksat8/deliverables/HAR/u2-design.md

## HAR-U2 도파관 실측 플랜지 목록 (제작 형상)
- HAR-U2 제작 플랜지: WR-28 상당(UBR-320 계열), 4개소(양단 2 + 중간
  분기 2) — u2-pay-reconcile.md에서 PAY 정식 규격(WR-42)과 불일치
  예고했던 그 4개소와 동일.
- PAY 수신단: WR-42(Ka-band) 포트, 28포트 중 본 경로 대응 채널.
- 불일치 성격: 내경·볼트홀 패턴 상이로 직접 체결 불가(INT-TST-1 실측
  확인).

## 어댑터 조치 타당성 확인
INT-TST-1이 WR-28↔WR-42 변환 어댑터 4개소를 현장 제작·삽입, 볼트토크
규정치 준수로 정상 체결을 확인했다. HAR 측 검토:
- 어댑터 삽입에 따른 추가 손실 0.04dB/개소(순증 1개소 기준)를 더해도
  총 도파관 손실 0.62dB ≤ sysreq HAR 상한 0.8dB(마진 0.18dB) — 전기
  성능 기준 **타당**.
- 어댑터는 기존 4개 플랜지 접속점을 대체하는 방식으로 삽입되어 굴곡·
  경로장 등 나머지 설계 요소(u2-design.md)는 변경 없음.
- **HAR 측 판정: 어댑터 조치 타당, 재설계 불요.**

## 하니스 도면 반영 계획
- HAR-U2 도파관 도면(u2-design.md 계열)에 어댑터 4개소(WR-28↔WR-42
  변환, 개소당 삽입손실 0.04dB)를 형상 변경으로 추가 반영한다.
- 손실 예산표를 기존 0.58dB(HAR 실측) → **0.62dB(어댑터 포함 통합
  실측치)**로 갱신하고, sysreq 상한 0.8dB 대비 마진을 0.23dB→0.18dB로
  수정 기록한다.
- u2-pay-reconcile.md의 "물리적 정합 미확인" 리스크 항목을 INT-TST-1
  실물 확인·조치·재검증 완료 근거로 **CLOSED** 갱신한다.
- 형상관리(CM) 반영은 축약체인 특성상 통합(INT) 단계 형상변경으로
  처리하며, 다음 도면 개정 시 어댑터 부품을 정식 BOM에 편입한다.

## 판정
어댑터 조치 타당, 도파관 손실 0.62dB ≤ 0.8dB 충족. 리스크 CLOSED.

검증: 어댑터4개소 조치 타당성 확인, 손실0.62dB<=0.8dB(마진0.18dB),
도면 반영계획 수립 — HAR module-fm.md 이관 리스크 1항 CLOSED
