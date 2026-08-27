# M-GS 지상국·운용 비행모델 인도

입력: examples/ksat8/deliverables/GS/gs-u1-iot-plan.md

## 인도 내역
관제소 적합성 판정 + IOT 30일 계획(GS-U1) DONE — 운용 체인(계획수립→
검토→취합)으로 완료, 입력은 전부 COMM·PAY 회신.

## sysreq 대비 판정 (수치 인용)
sysreq "GS: 관제소 적합성, IOT 30일 계획" —
- **관제소 적합성**: 기존 S-band TT&C 관제소로 적합(링크마진 ≥6dB,
  COMM 확정 하향EIRP 4.8dBW 기준). Ka-band IOT 시험국은 신규/임차
  확보 조건(업링크EIRP≥85dBW·대역폭≥40MHz·G/T≥30dB/K)부 적합. **충족**
  (조건부 항목 명시).
- **IOT 30일 계획**: D1–D30 일정 확정 — TT&C 커미셔닝(D1–D5), Ka 24채널
  EIRP 전수측정(D6–D21, 목표 52dBW ±0.5dB), 대표4채널 NPR측정(D22,
  ≥18dB), 예비일(D23–D26), 종합분석(D27–D29), 종료(D30). **충족**.

## 이월 항목
- Ka 시험국 확보(신규/임차)는 IOT 착수 전 별도 조달 필요 — 조건부 적합의
  전제조건으로 module-fm.md에 명시(추후 조달 확정 시 정정 게시글).

검증: sysreq GS 항목(관제소 적합성·IOT 30일 계획) 전항 수치 충족(조건부
1건 명시), GS-U1 DONE.
