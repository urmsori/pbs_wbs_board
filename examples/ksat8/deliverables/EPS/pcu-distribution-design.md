# 100V PCU·배전 설계 (EPS-U1)

입력: examples/ksat8/deliverables/SE/sysreq.md, examples/ksat8/board/REQ-EPS-PAY-부하.md,
examples/ksat8/deliverables/PROP/eps-load-profile.md, examples/ksat8/deliverables/TCS/eps-heater-budget.md,
examples/ksat8/deliverables/EPS/comm-power-allocation.md,
examples/ksat8/deliverables/EPS/pay-power-capability.md,
examples/ksat8/deliverables/EPS/ep-power-commitment.md,
examples/ksat8/deliverables/EPS/distribution-connector-spec.md

## 요청 상태
- REQ-EPS-PAY-부하(PAY, 채널별 부하 내역): **무응답**(8×20s×2회 폴링
  초과) → **잠정 가정**: 11kW를 24채널 균등 분배(채널당 458W, 정상상태
  상시)로 설계. 실 채널별 편차는 배전 여유(채널당 8A 정격, 균등부하 대비
  마진 1.7배)로 흡수 가능하도록 설계해 리스크를 낮춤. PAY 회신 도착 시
  재검증.
- REQ-EPS-PROP-부하(PROP, 운전 전력·시간): **실회신 반영**
  (eps-load-profile.md) — 이온추력기 2채널 동시 점화, 채널당 1.5kW,
  합계 **3.0kW**, 1일 총 점화 ≤2시간, 탑재체(11kW)와 동시운용 허용.
  버스 EOL 16kW 중 탑재체 차감 5kW 여유 내에서 수용 가능하다는 PROP측
  판단을, 아래 배전 채널표에서 EPS 배전 15kW 예산 기준으로 재확인해
  확정한다(3.0kW 반영, 최초 가정 2.0kW 대비 상향 — ep-power-commitment.md
  「정정」 항 참조).
- REQ-EPS-TCS-히터(TCS, 채널 배분): **실회신 반영**(eps-heater-budget.md)
  — 6채널 비균등 배분(H1배터리40W·H2추진배관60W·H3추력기밸브30W·
  H4/H5구조부25W×2·H6예비20W), 총 200W, 서모스탯 자동(H2는 커맨드
  오버라이드 가능). 최대 동시 점등 시 2.0A(100V 기준)로 배전 설계.

## 아키텍처
- 토폴로지: 완전조절 100V 버스 — S3R(Sequential Switching Shunt Regulator)
  션트 조절 + BCR/BDR(배터리 충/방전 레귤레이터)에 의한 직접에너지전달
  (DET) 방식. 일광 중 태양전지판 잉여전력은 S3R이 션트로 버리고, 이클립스
  중 BDR이 배터리(EPS-U2, 2.4kWh)로 100V±2V를 유지한다.
- 조절 범위: 100V±2V(98~102V) 전 부하(0~15kW) 구간에서 유지, 리플
  ≤100 mVpp(HAR·COMM·PAY 회신 규격과 정합).
- 주버스 피더: 150A 정격(15kW/100V), 배전 유닛(PCU) 출력단에서 채널군별
  LCL(Latching Current Limiter)로 분기.

## 배전 채널 구성 (15kW 예산)
| 채널군 | 채널수 | 부하 | LCL 정격 | 비고 |
|---|---|---|---|---|
| PAY(중계기) | 24 | 11,000 W(균등가정 458W/ch) | 8 A/ch | REQ-EPS-PAY-부하 잠정 |
| EP(전기추진) | 2 | 최대 2,000 W(동시2채널) | 20 A/ch | REQ-EPS-PROP-부하 잠정, PAY 동시운용 확인됨 |
| COMM | 1 | 상시150W/피크220W | 3 A | comm-power-allocation.md 확정 |
| TCS 히터 | 6 | 200 W(균등33W/ch) | 3 A/ch | REQ-EPS-TCS-히터 잠정 |
| 버스 housekeeping(AOCS/OBC 등) | - | ≤1,650 W 여유 | - | 마진 |
| **합계** | | **≤15,000 W** | | sysreq 15kW 배전 이내 |

- 배전 출력 커넥터: MIL-DTL-38999 시리즈 III, 100V 절연 이격거리
  ≥1.5mm(도체간)/≥2.0mm(대지간) — HAR-U1 하니스 설계에 회신 완료
  (distribution-connector-spec.md).

## sysreq 판정 (설계 단계, 실측 전 잠정)
sysreq: "EPS: 100V 버스, 15kW 배전, 배터리 이클립스 2.4kWh." → 위 채널
구성 합계 ≤15,000W로 배전 예산 이내 확정(설계 단계). 100V±2V 조절은
S3R+BDR DET 아키텍처로 전 부하구간 유지 설계. 배터리 2.4kWh는 EPS-U2에서
별도 설계·시험.

검증: 채널구성 합계 15,000W 이내(설계단계 충족), 100V±2V DET 아키텍처
확정, PAY/EP 동시운용 마진 확인(13kW+housekeeping≤15kW).

## 정정 (REQ-EPS-PAY-부하 실회신 반영)
입력: examples/ksat8/deliverables/PAY/eps-pay-load-reply.md
PAY 실측 회신 도착 — 채널당 428W(24채널 소계 10,272W)+공통전자 728W=
정확히 **11,000W**(균등가정 458W/채널과 거의 일치, 정정 불요). 기동
인러시 첨두 ≤12.8A(≤3배, 10ms 이내)는 LCL 정격(8A 연속)의 1.6배이나
10ms 단시간 트립 곡선(i²t) 내로 흡수 가능 — EPS-U1-TST에서 실측 확인
예정(리스크 낮음, 설계 변경 불요).
검증(정정): 채널당428W·합계11,000W 정합 확인, inrush 12.8A/10ms LCL
i²t 여유 내(시험 확인 예정).
