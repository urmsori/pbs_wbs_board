# 통신(COMM) 비행모델 인도
입력: examples/ksat6/deliverables/COMM/link-budget.md, examples/ksat6/deliverables/COMM/sband-transceiver.md, examples/ksat6/deliverables/COMM/xband-transmitter.md, examples/ksat6/deliverables/COMM/antenna.md, examples/ksat6/deliverables/COMM/rf-integration-test.md, examples/ksat6/deliverables/COMM/tx-load-response.md

## sysreq.md 판정 (COMM 자기 항목)
> COMM: S-band TT&C 상향 64kbps/하향 2Mbps, X-band 150Mbps.

| 항목 | 요구 | 실측/설계 결과 | 판정 |
|---|---|---|---|
| S-band 상향 64kbps | 64kbps | 실측 마진 +29.0dB | **충족(여유 큼)** |
| S-band 하향 2Mbps | 2Mbps | 실측 마진 **+0.94dB** | **충족하나 마진 1dB 미만 — 빠듯함을 그대로 기록** |
| X-band 150Mbps | 150Mbps | 실측 마진 +5.96dB, 10초 무오류 시연 | **충족(양호)** |

## 구성
1. 링크버짓(link-budget.md) — S/X-band EIRP·G/T·마진 산출.
2. S-band 트랜시버(sband-transceiver.md) — Tx 2W, 상시부하 8W.
3. X-band 송신기(xband-transmitter.md) — RF 10W, 첨두 40W/1.43A/duty~4%.
4. 안테나(antenna.md) — S-band 2기(3dBi, 130° 빔폭) · X-band 1기(15dBi, ±11° 빔폭).
5. RF 통합시험(rf-integration-test.md) — 실측 마진 재확인.

## 발행/수신 REQ 요약
- 발행(COMM→타 트랙): REQ-COMM-OBC(데이터 인터페이스, OBC 회신 SpW/64Mbit/AOS),
  REQ-COMM-STR(장착·FOV, STR 회신 좌표·이격 확인), REQ-COMM-EPS(첨두전력,
  EPS 회신 70W/4A 여유) — 3건 모두 DONE.
- 수신(타 트랙→COMM): REQ-EPS-COMM(송신 첨두전류·duty 질의) — 40W/1.43A/약4%로
  회신, EPS 가정치(55W/8%)보다 낮게 나와 EPS 예산 갱신 여지 통보. DONE.

## 남은 위험(정직 기록, 잠정 가정 아님 — 실측 기반)
- **S-band 하향 마진 1dB 미만(+0.94dB)**: 앙각 15° 이상에서만 신뢰
  운용(G-OPSPROC 절차 반영됨). 후속 개선 과제: 위성 안테나 이득 +2dB 또는
  지상국 G/T 상향.
- **X-band 데이터 버퍼 여유 6.7%(빠듯)**: OBC 판독 버스트 시간 단축 협의를
  후속 과제로 남김(현재는 시험상 무오류였으나 정상운용 중 모니터링 권고).

검증: 위 표의 각 항목이 sysreq.md 자기 항목을 인용해 판정되었고, 마진이
부족한 두 항목(S-band 하향, 버퍼 여유)을 숨기지 않고 명시했다.
