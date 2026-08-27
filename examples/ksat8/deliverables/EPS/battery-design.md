# 배터리팩 설계(축약) — EPS-U2

입력: examples/ksat8/deliverables/SE/sysreq.md, examples/ksat8/deliverables/EPS/pcu-distribution-design.md

## 구성
- Li-ion 셀(3.6V 공칭, 40Ah급) 8S3P 구성: 공칭 28.8V(범위 23.2~33.6V),
  용량 120Ah.
- BOL 나명판 에너지: 28.8V×120Ah = **3,456 Wh**.
- 이클립스 방전 한도: DoD ≤70%(15년 수명, 사이클수명 확보) → usable
  ≈2,419 Wh ≈ **2.4 kWh**(sysreq 정합).
- BDR(배터리 방전 레귤레이터, 부스트)이 배터리단(23.2~33.6V)을 100V±2V
  버스로 승압, BCR(충전 레귤레이터)이 태양광 잉여전력으로 충전.

## 이클립스 부하 반영
- 이클립스 중 필수 부하: COMM 150W(상시, REQ-COMM-EPS-전력 회신) + TCS
  히터 우선순위 채널(H1 배터리40W·H2 추진배관60W·H3 밸브30W, 총 130W,
  eps-heater-budget.md 1~3순위) + 하우스키핑(AOCS/OBC 등, 잠정 300W) ≈
  580W. 최대 이클립스 지속시간(GEO 춘추분 최대 ≈72분) 기준 소요 에너지
  ≈580W×1.2h≈696Wh ≪ usable 2,419Wh(여유 3.5배) — PAY/EP는 이클립스 중
  미운용(ep-power-commitment.md 정합) 전제.

검증: 8S3P 28.8V/120Ah, usable 2,419Wh(DoD70%)≈2.4kWh(sysreq 정합),
이클립스 필수부하 696Wh≪usable 여유3.5배
