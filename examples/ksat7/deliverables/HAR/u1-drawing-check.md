# HAR-U1 대전류 펄스 배선 도면 검도

입력: examples/ksat7/deliverables/HAR/u1-design.md, examples/ksat7/deliverables/HAR/u1-thermal-analysis.md, examples/ksat7/deliverables/HAR/pay-req-reply.md

## 검도 항목
1. 전압강도 계산(u1-design.md): AWG10, 왕복6m, R=0.01917Ω, 36A(50V기준)
   시 1.38% — 계산식·단위 일치 확인, 이상 없음.
2. 줄열 해석(u1-thermal-analysis.md): 도체 최고온도 65.5°C ≤ 절연정격
   200°C — 확인, 이상 없음.
3. PAY REQ 대조(pay-req-reply.md): 계통당 20.0A·저항상한 0.0675Ω 조건에서
   전압강하 0.85%, 단일계통 40.0A 부담시 1.70% — 모두 3% 이내, 여유 충분.
4. 커넥터 핀맵: 잠정 EPS 가정(4핀, 극당 2핀 병렬 20A/핀) — REQ-HAR-EPS
   회신 미도착 상태이므로 **조건부 승인**, 확정 커넥터 정격 도착 시 재검토
   필요(리스크로 module-fm.md 기록).
5. 접지/차폐: 편조 실드 SPG 접지 — HAR-U2 INS EMC 차폐 검사로 최종 검증
   예정.

## 판정
계산·해석 정합, PAY 요구 대조 만족. EPS 커넥터 정격만 잠정 상태로 검도
통과(조건부) — RVW 단계로 송부.
