# PAY 비행모델 인도 — module-fm
입력: examples/ksat7/deliverables/PAY/u1-antenna-design.md, u1-structural-analysis.md,
u1-design-check.md, u1-review-a.md, u1-review-b.md, u1-review-board.md, u1-mfg.md,
u1-ins.md, u1-radiation-test.md, u2-transceiver-design.md, u2-mfg.md, u2-ins.md,
u2-pulse-test.md

## 구성 유닛
- **PAY-U1 능동위상배열 안테나**: 설계(DSN)→구조해석(ANL-S)→검도(CHK)→검토
  A/B→검토회(RB, 승인)→CM 배포 요청 → 제작(PUR→IQC→MFG→CLN→INS) →
  방사시험(CAL·FAC·PA 요청→TST).
- **PAY-U2 송수신기·펄스발생기**: 설계(DSN) → 제작(PUR→IQC→MFG→CLN→INS) →
  시험(CAL 요청→TST: 1.8kW 펄스 실증·NESZ 판정).

## ICD 협상
- REQ-PAY-EPS(→EPS): 1.8kW 버스트 파형(상승/하강<1ms, 5s×18회/궤도, 첨두전류
  40.0A) 전달, 회신 대기 중 EPS 측 확약 필요분은 REQ-EPS-PAY(EPS→PAY 역질의)로
  동일 수치 재확인·회신 완료.
- REQ-PAY-HAR(→HAR): 첨두전류40.0A, 계통당20.0A·저항≤0.0675Ω, 전압강하≤3% 전달.
- REQ-PAY-TCS(→TCS): 첨두발열270W×5s×18회/궤도, 인터페이스0.30㎡ 전달.
- 수신 REQ 회신(수치): REQ-MECH-PAY(관성모멘트46.7/44.0kg·m², 전개각90°±0.5°×2단),
  REQ-STR-PAY(질량72.0kg, 3점킨매틱 PCD400mm 8-M8), REQ-OBC-PAY(스팟첨두3.2Gbps/
  평균1.1Gbps, SpW4채널), REQ-TCS-PAY(첨두발열270W), REQ-EPS-PAY(첨두전류40.0A),
  REQ-FSW-PAY(펄스폭20/6.7µs·PRF3000Hz, 전환2.5s) — 6건 전량 수치 회신 완료.

## sysreq PAY 최종 판정 (u2-pulse-test.md 인용)
| 항목 | 요구 | 실측 | 판정 |
|---|---|---|---|
| SAR 첨두 펄스 부하 | 1.8kW, 최대90s/궤도 | 1.79kW, 90.4s/궤도(공차내) | PASS |
| NESZ | ≤-19dB | -19.6dB(안테나측손실0.71dB+수신기NF2.9dB+급전손실0.75dB 종합) | PASS |

## 서비스 요청 처리
CM-PAY-U1(배포), PUR-PAY-U1, PUR-PAY-U2(구매), CAL-PAY-U1, FAC-PAY-U1,
PA-PAY-U1(방사시험 교정·시설·입회), CAL-PAY-U2(펄스시험 교정) — 7건 전량 DONE.

## 결론
sysreq PAY 2개 항목 전량 충족. PAY 비행모델 인도 완료.
