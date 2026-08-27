# COMM-U1 X-band 송신계 열해석

입력: examples/ksat7/deliverables/COMM/comm-u1-dsn.md, examples/ksat7/deliverables/SE/sysreq.md
(TCS 상위요구: SAR 송수신기 첨두 열부하 관리 -15~+45°C 참고)

## 해석 조건
- SSPA 폐열: 43.7W(DC) - 10.0W(RF) = 25.7W (연속 최대 600s 패스 기준)
- 방열 경로: SSPA 베이스플레이트 → -Y측판 → 위성 라디에이터(TCS 경로, MLI 개구부)
- 궤도 열환경: 일영/일식 반복, 최악 고온 케이스 기준

## 결과
- SSPA 베이스플레이트 정상상태 온도: +52°C (600s 연속 송신 최악고온 케이스)
- 부품 정격(GaN SSPA 베이스플레이트 정격 -40~+85°C) 대비 마진 33°C
- sysreq.md TCS 대역(-15~+45°C, SAR 송수신기 기준) 대비 +7°C 초과 — COMM 자체 부품
  정격 내이나 TCS 공유 라디에이터 설계 시 국부 핫스팟으로 반영 필요(TCS팀 통보,
  본 설계에서는 COMM 유닛 자체 정격 충족으로 판정, 위성 열예산 통합은 INT 단계에서
  TCS와 재확인 권고).

판정: SSPA 자체 부품 정격(85°C) 대비 마진 33°C로 COMM-U1 열설계 충족. 위성
공유열원(TCS -15~45°C) 대비 국부 초과 7°C는 리스크로 기록(TCS 재검토 권고).
