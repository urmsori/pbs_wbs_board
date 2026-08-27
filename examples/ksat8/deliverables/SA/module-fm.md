# 태양전지판(SA) 비행모델 인도 — module-fm

입력: examples/ksat8/deliverables/SE/sysreq.md, SA-U1(2윙 대형 패널) 전체 체인,
REQ-SA-MECH-힌지/REQ-SA-AOCS-플러터(발신) 및 REQ-AOCS-SA-모드/REQ-MECH-SA-힌지/
REQ-STR-SA-하중(수신) 회신

## 구성
- SA-U1: 2윙 대형 태양전지판(트리플정션 GaAs 셀, 윙당 26.6㎡) — 축약
  설계 체인(DSN→ANL-S→CHK→RB, RVW·ANL-T 생략) + 제작 체인(PUR→IQC→MFG→
  CLN→INS) + 플래시시험(CAL→TST).

## sysreq 판정 (examples/ksat8/deliverables/SE/sysreq.md 「SA」 행 인용)
"SA: EOL 16kW, 전개 후 1차모드 ≥0.1Hz."

| 항목 | 요구 | 실측/판정 | 결과 |
|---|---|---|---|
| EOL 출력 | ≥16,000 W | 16,120 W(플래시시험, 마진0.75%) | 충족 |
| 전개 후 1차모드 | ≥0.1 Hz | 0.118 Hz(SA-U1-ANL-S, MECH 실측 힌지강성 6,080N·m/rad 반영) | 충족 |

SA-U1-RB(검토회) 조건부 승인의 조건(MECH 힌지강성 실회신 시 1차모드
재검증)은 위 재해석(0.118Hz)으로 해소됨.

## ICD 협상 결과 요약
- REQ-SA-MECH-힌지(발신)/REQ-MECH-SA-힌지(수신): 힌지강성 6,080N·m/rad
  (잠정6,000 대비+1.3%), 백래시0.04°≤0.05°, 6점M8 PCD150mm 볼트패턴,
  이중릴리즈로 단일고장 허용 확보 — 상호 확정.
- REQ-SA-AOCS-플러터(발신)/REQ-AOCS-SA-모드(수신): AOCS 제어대역폭
  0.02Hz, SA 1차모드 이격 6.0배(요구5배 이상) 충족, SADA 외란 배분
  0.08N·m≥설계치0.05N·m(스텝) — 노치필터 불요로 상호 확정.
- REQ-STR-SA-하중(수신): 질량180kg/윙, 전개반력2,500N·모멘트3,000N·m,
  4점M10 마운트 회신 완료(STR-U1 측판 마운트 설계 입력 제공).

## 잠정/리스크
없음 — 설계 단계 잠정 가정(힌지강성6,000N·m/rad)은 MECH 실회신
(6,080N·m/rad)으로 정정·재검증 완료(panel-design.md 「정정」 항,
panel-review-board.md 「조건 해소」 항). EOL 마진이 0.75%로 낮아 궤도상
성능 추이는 GS 관제 데이터로 추적 권고(운용 단계 관찰 항목).

검증: sysreq SA 2항목(EOL16kW·1차모드≥0.1Hz) 전량 실측/실회신 기반 충족,
ICD 3건(2발신+1수신, 총 3건 회신) 완료
