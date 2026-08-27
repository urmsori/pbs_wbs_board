# HAR 모듈 비행모델 인도 요약

입력: examples/ksat7/deliverables/HAR/u1-*.md, u2-*.md, examples/ksat7/deliverables/SE/sysreq.md

## sysreq.md HAR 항목 대비 판정
> HAR: 대전류 펄스 배선(전압강하 ≤3% @펄스), EMC 차폐.

| 판정 항목 | 기준 | 실측/결과 | 판정 |
|---|---|---|---|
| 대전류 펄스 배선 전압강하 | ≤3% @펄스 | 정상운전 0.86~0.87%, 단일계통 전량부담(단일고장) 1.72% (u1-inspection.md, PA 입회) | 충족 |
| EMC 차폐 | 차폐 확보 | 접지본딩 6.5mΩ≤10mΩ, 실드연속성 0.03Ω, 개별실드 절연 전건 확인 (u2-inspection.md) | 충족 |

## 유닛별 요약

### HAR-U1 대전류 펄스 배선 (SAR 1.8kW)
설계 풀체인: DSN→ANL-T(줄열, 최고 도체온도 65.5°C≤절연정격200°C)→CHK
(PAY 요구 REQ-PAY-HAR 대조 포함)→RVW-A(전기)/RVW-B(열·EMC)→RB(조건부
확정)→CM 배포. 제작: PUR→IQC→MFG→CLN. 검사: INS(도통·절연≥238MΩ·
전압강하 0.86~1.72%, PA 입회 No Finding).
- ICD: REQ-HAR-EPS 발행(설계 착수와 동시), 최초 8×20초 폴링 타임아웃 →
  잠정 가정(40A/극, 저항예산 미확정)으로 설계·검도·RVW·RB·CM·PUR·IQC·
  MFG 진행. 이후 EPS 정식 회신 접수(모선50V±5V, 펄스채널45A연속/90A서지,
  저항예산≤41.7mΩ) — INS 단계에서 대조, 실측 저항 19.3~19.5mΩ로 예산
  대비 54% 여유 확인, 재설계 불요.
- REQ-PAY-HAR(PAY 발신, HAR 수신) 접수·회신: 계통당20A·저항≤0.0675Ω
  조건에서 전압강하 0.85%, 단일계통 40A 전량부담 시 1.70% — 만족 회신.

### HAR-U2 신호·데이터 하니스
설계 축약체인: DSN→CHK→RB(RVW 생략, 위험도 낮음 판단)→PUR→IQC→MFG→CLN→
INS(EMC 차폐: 접지본딩6.5mΩ, 실드연속성0.03Ω, 개별실드절연 8쌍 전건
합격).
- ICD: REQ-HAR-OBC 발행(설계 착수와 동시), OBC 정식 회신(MDM-51 51핀,
  SpW5/CAN2/1553B이중화1, 실드접지 41번핀) 신속 접수 — 잠정 가정 불요.

## 리스크·후속조치
1. HAR-U1 EPS 커넥터는 잠정 p/n(PCDU-PWR-J4)으로 발주·제작됨. EPS 정식
   회신의 실커넥터 파트번호와의 물리적 정합은 통합(INT) 단계에서 최종
   확인 필요(전기 성능은 이미 INS에서 재확인 완료, 저항 54% 여유).
2. HAR-U1의 EMC 차폐 정량 실측은 U2-INS-01에서 대표 실시(동일 편조실드·
   SPG 접지 구조). u1-review-b.md 권고에 따라 통합시험(INT) 단계에서
   U1 자체 차폐 실측 권고.

## 산출물 목록
examples/ksat7/deliverables/HAR/{u1-design, u1-thermal-analysis,
u1-drawing-check, u1-review-a, u1-review-b, u1-review-board, u1-iqc,
u1-mfg, u1-cleaning, u1-inspection, pay-req-reply, u2-design,
u2-drawing-check, u2-review-board, u2-iqc, u2-mfg, u2-cleaning,
u2-inspection}.md
