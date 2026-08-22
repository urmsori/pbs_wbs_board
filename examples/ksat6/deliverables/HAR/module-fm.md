# HAR 비행모델 인도 — 전 유닛 하니스

입력: examples/ksat6/deliverables/HAR/unit1-main-bus.md,
examples/ksat6/deliverables/HAR/unit2-deployment.md

## 구성
- **유닛1(주버스 하니스)**: PCDU 배전 → OBC/AOCS/COMM-S/COMM-X/PAY/TCS 히터
  전원선 + OBC 1553B/CAN/SpW×4 신호선. OBC·EPS ICD 회신
  (connector-pinmap.md, distribution-connector-spec.md) 반영.
- **유닛2(전개부 하니스)**: SA 2윙 HDRM·안테나 액추에이터 전원선, 힌지
  센서·리미트스위치 신호선. 굽힘반경·전개 충격 설계 반영.

## sysreq.md HAR 항목 판정 요약
| 항목 | 기준 | 유닛1 실측 | 유닛2 실측 | 판정 |
|---|---|---|---|---|
| 전원선 전압강하 | ≤2% | 최대 1.07%(COMM-X) | 1.11%(HDRM) | 충족 |
| EMC 차폐(실드 접지연속성) | 낮을수록 양호(<0.1Ω 사내기준) | 0.03Ω | 0.05Ω | 충족 |
| 절연저항 | ≥100MΩ | 최저 280MΩ | -(유닛2는 도통·차폐 중심 검사) | 충족 |
| 도통 | 100% | 100% | 100% | 충족 |

## 유닛 체인 이력
1. 하니스 설계(라우팅·핀맵 취합) — HAR-D1, HAR-D2
2. 전원 하니스 제작 — HAR-P1, HAR-P2
3. 신호 하니스 제작 — HAR-S1, HAR-S2
4. 도통·절연·EMC 차폐 검사 — HAR-I1, HAR-I2

## 수신 ICD
- REQ-HAR-OBC → OBC 커넥터·핀맵(connector-pinmap.md) 반영, 유닛1 설계 확정.
- REQ-HAR-EPS → EPS 배전 채널 전류정격(distribution-connector-spec.md)
  반영, 유닛1 전압강하 계산 근거.

## 잔여 리스크
- 전개부(유닛2) 힌지 굽힘 관련 MECH 측 문의가 늦게 들어올 수 있음 —
  발생 시 별도 REQ로 접수해 유닛2 산출물을 갱신(재작업, 규칙 4절)한다.
  이 인도 시점까지 수신된 문의 없음.

검증: sysreq.md HAR 항목(전압강하 ≤2%, EMC 차폐) 유닛1·유닛2 전 채널
실측 충족 — unit1-main-bus.md, unit2-deployment.md의 검사 절 참조.
