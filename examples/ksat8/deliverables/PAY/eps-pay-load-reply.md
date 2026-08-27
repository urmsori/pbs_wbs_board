# REQ-EPS-PAY-부하 회신 — 채널별 부하 프로파일

입력: examples/ksat8/deliverables/PAY/u1-dsn.md, examples/ksat8/board/REQ-EPS-PAY-부하.md

1) 채널 구성별 DC 소모: TWTA(EPC포함) 310W/채널 + 수신기·스위치매트릭스 배분
   118W/채널 = **428W/채널**(24채널 소계 10,272W) + 공통전자(스위치매트릭스
   공통부·텔레메트리·예비계열 대기) 728W = **합계 11,000W**(sysreq/EPS확약 정합).
2) 정상상태 전류(100V 기준): 428W÷100V = **4.28A/채널**. 기동(inrush): TWTA
   EPC 소프트스타트 전제 상승시간≥10ms(EPS 확약 반영) 기준 첨두 ≤3배(≤12.8A,
   10ms 이내).
3) 스위칭 빈도: 정상운용 시 24채널 상시 ON(재구성 없음). 예비 TWTA 4기는
   냉대기(전원 OFF, 히터만 소electrification 20W)이며 고장 시에만 전환 —
   빈도 낮음(임무 중 예상 0~수회).

검증: 428W/채널×24+728W=11,000W(EPS확약11kW 정합), inrush≤3배·10ms이내(EPS 소프트스타트 전제 충족)
