# 전력(EPS) 비행모델 인도 — module-fm

입력: examples/ksat7/deliverables/SE/sysreq.md, EPS-U1(PCDU·펄스전력부) 전체 체인,
EPS-U2(배터리팩) 전체 체인, REQ-EPS-PAY/REQ-EPS-PROP(발신) 및 REQ-PAY/PROP/COMM/HAR/TCS-EPS(수신) 회신

## 구성
- EPS-U1: PCDU·펄스전력부(슈퍼커패시터·배터리 하이브리드) — 설계 풀체인
  (DSN→ANL-S·ANL-T→CHK→RVW-A/B→RB→CM) + 제작 체인(PUR→IQC→MFG→CLN→INS).
- EPS-U2: 배터리팩(Li-ion 14S3P, 51.8V/777Wh BOL) — 제작 체인(PUR→IQC→MFG→CLN→INS)
  + 시험 체인(CAL·FAC·PA→TST: 1.8kW 펄스 방전 실증).

## sysreq 판정 (examples/ksat7/deliverables/SE/sysreq.md 「EPS」 행 인용)
"모선 50V±5V, SAR 펄스 1.8kW 버스트 대응(슈퍼커패시터/배터리 하이브리드), DoD ≤30%."

| 항목 | 요구 | 실측/판정 | 결과 |
|---|---|---|---|
| 모선전압 | 50V±5V(45~55V) | 버스트 중 46.4~53.8V (EPS-U2-TST) | 충족 |
| 펄스대응 | 1.8kW 버스트(최대90s/궤도, 5s×18회 실측파형) | 20궤도 반복 이상없음, 슈퍼캡 재충전 18.9s<간격20s | 충족 |
| DoD | ≤30% | 궤도당 최대27.3%, 평균24.8% | 충족 |

EPS-U1-RB(검토회) 조건부 승인의 조건(DoD 실측 재검증)은 EPS-U2-TST-01로
해소됨.

## ICD 협상 결과 요약
- REQ-EPS-PAY(발신) / REQ-PAY-EPS(수신): 실제 파형 5s×18회/궤도·듀티6%·
  상승/하강<1ms로 일치 확인, sysreq 원안(1.8kW/90s)과 총 버스트시간 정확히
  일치. 조건부 공급 확약(버스트 간격≥20s).
- REQ-EPS-PROP(발신) / REQ-PROP-EPS(수신): SAR-추력 상호배타 운용 확정,
  300W/1.0A 연속공급 EOL예산 내 확약.
- REQ-COMM-EPS(수신): 첨두60W 배정, SAR 동시운용 허용(별도 경로).
- REQ-HAR-EPS(수신): 펄스채널 45A연속/90A서지, 전압강하예산 41.7mΩ 회신.
- REQ-TCS-EPS(수신): 히터 40W 3채널 배전 가능 확인.

## 잠정/리스크
없음 — 모든 ICD 항목이 실측 또는 상대팀 회신으로 확정됨(설계 단계 잠정
가정치는 전량 실측·회신으로 해소).

검증: sysreq EPS 3항목(모선50V±5V·1.8kW버스트·DoD≤30%) 전량 실측 기반 충족, ICD 5건 회신 완료
