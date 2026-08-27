# 전력(EPS) 비행모델 인도 — module-fm

입력: examples/ksat8/deliverables/SE/sysreq.md, EPS-U1(100V PCU·배전) 전체 체인,
EPS-U2(배터리팩) 전체 체인, REQ-EPS-PAY-부하/REQ-EPS-PROP-부하/REQ-EPS-TCS-히터(발신)
및 REQ-COMM/HAR/PAY/PROP-EPS(수신), REQ-FSW-EPS-TMTC(수신) 회신

## 구성
- EPS-U1: 100V PCU·배전유닛(S3R+BDR/BCR DET 아키텍처) — 설계 풀체인
  (DSN→ANL-S·ANL-T→CHK→RVW-A/B→RB→CM) + 제작 체인(PUR→IQC→MFG→CLN→INS)
  + 시험(CAL·FAC·PA→TST: 0~15kW 기능·부하시험).
- EPS-U2: 배터리팩(Li-ion 8S3P, 28.8V/120Ah) — 축약 설계 체인(DSN→CHK→RB)
  + 제작 체인(PUR→IQC→MFG→CLN→INS) + 시험(CAL·FAC·PA→TST: 이클립스
  방전 실증).

## sysreq 판정 (examples/ksat8/deliverables/SE/sysreq.md 「EPS」 행 인용)
"EPS: 100V 버스, 15kW 배전, 배터리 이클립스 2.4kWh."

| 항목 | 요구 | 실측/판정 | 결과 |
|---|---|---|---|
| 버스전압 | 100V±2V | 98.4~101.7V(0~15kW 전구간, EPS-U1-TST) | 충족 |
| 배전용량 | 15kW | 채널구성 14,420W 인가 실증(PAY11,000+EP3,000+ COMM220+히터200+HK) | 충족 |
| 이클립스 배터리 | 2.4kWh | usable 2.44kWh, 72분 방전 DoD68.4%(EPS-U2-TST) | 충족 |

EPS-U1-RB(검토회) 조건부 승인의 조건(PAY 인러시 12.8A/10ms LCL 트립여유
실측)은 EPS-U1-TST(9ms 트립없음)로 해소됨.

## ICD 협상 결과 요약
- REQ-EPS-PAY-부하(발신)/REQ-PAY-EPS-전력(수신): 채널당 428W·합계11,000W
  정합, 인러시≤3배·10ms, 확약용량11kW로 상호 확정.
- REQ-EPS-PROP-부하(발신)/REQ-PROP-EPS-전력(수신): 이온추력기 2채널
  동시점화 3.0kW(당초 확약 2.0kW에서 정정 상향), 1일≤2시간, PAY와
  동시운용 허용(13.42kW≤15kW).
- REQ-EPS-TCS-히터(발신): 6채널 비균등 200W(H1~H6), 이클립스 우선순위
  H1(배터리)>H2(추진배관)>H3(밸브) 반영.
- REQ-COMM-EPS-전력(수신): 상시150W·피크220W 배정, 리플≤100mVpp.
- REQ-HAR-EPS-배전(수신): 채널별 LCL정격·100V절연 이격(1.5/2.0mm) 회신.
- REQ-FSW-EPS-TMTC(수신): TM≈76점·TC36개·배터리관리 파라미터 회신.

## 잠정/리스크
없음 — 설계 단계 잠정 가정(PAY 균등부하, PROP 상호배제, TCS 균등배분)은
전량 실회신 또는 실측으로 해소·정정됨(정정 이력: pcu-distribution-design.md,
ep-power-commitment.md 「정정」 항).

검증: sysreq EPS 3항목(100V±2V·15kW배전·이클립스2.4kWh) 전량 실측 기반
충족, ICD 6건(3발신+3수신) 회신 완료
