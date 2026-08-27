# GS-U1 관제소 적합성 분석·IOT 30일 계획

입력: examples/ksat8/deliverables/COMM/REQ-GS-COMM-프로토콜-reply.md, examples/ksat8/deliverables/COMM/comm-corr-02.md, examples/ksat8/deliverables/PAY/REQ-GS-PAY-IOT-reply.md, examples/ksat8/deliverables/SE/sysreq.md

## 1. 관제소 적합성 판정 (sysreq "GS: 관제소 적합성")

### 1.1 TT&C(S-band) 관제소
| 요구(COMM 회신) | 관제소 표준 장비 사양 | 판정 |
|---|---|---|
| 상향 2087.5MHz / 하향 2255.5MHz | S-band TT&C 대역(2025–2120/2200–2300MHz) 전대역 대응 | 적합 |
| 변조: PCM/PSK/PM | 표준 복조기 지원 방식 | 적합 |
| 레인징: PN(2²²−1)+턴어라운드240/221 | 표준 레인징 장비 지원 방식 | 적합 |
| 위성 하향 EIRP 4.8dBW(comm-corr-02.md 확정, 재계산 불필요) | 관제소 G/T 5dB/K 가정(COMM 링크버짓 전제와 동일) | 마진 ≥6dB로 링크 성립 — 적합 |

**판정: 기존 표준 S-band TT&C 관제소로 적합(추가 장비 불요).**

### 1.2 Ka-band IOT 시험국 (PAY 회신 기반)
| PAY 요구 | 필요 장비 | 판정 |
|---|---|---|
| 업링크 EIRP ≥85dBW(TWTA 포화구동) | 대형 Ka 업링크 안테나(고출력 HPA) | **전용 Ka 시험국 필요 — S-band TT&C 관제소와 별도 시설**(관제소 적합성 범위에 포함해 확보 요청) |
| 수신 대역폭 ≥40MHz | 광대역 수신기 | 시험국 사양에 포함 |
| G/T ≥30dB/K | 대구경 수신 안테나 | 시험국 사양에 포함 |

**판정: Ka 시험국은 신규/임차 확보 필요 — 적합성 조건부(시험국 확보를
전제로 적합).**

## 2. IOT 30일 계획 (D+1 = 관제소 인수 첫날, 정지궤도 안착 이후 기준)

| 일자 | 활동 | 근거 |
|---|---|---|
| D1–D3 | TT&C 링크 커미셔닝: 양방향 캐리어 획득, 레인징 턴어라운드(240/221) 검증, 안테나 지향 확인 | COMM 회신 §1–3 |
| D4–D5 | S-band 관제소-위성 링크마진 실측(하향 EIRP 4.8dBW 대비 수신 C/N0) | comm-u1-tst.md 시험치, comm-corr-02.md |
| D6–D21 | Ka 24채널 EIRP 전수 측정(1채널/시간, 24시간을 하루 3채널×8일로 분산 — 시험국 가용시간 고려) | PAY 회신 (1) |
| D22 | 대표 4채널 NPR 측정(채널당 30분, 총 2시간) | PAY 회신 (2) |
| D23–D26 | 이상 채널 재시험·예비일(전수 측정 중 편차 초과 채널 대응) | PAY 회신 (1)(±0.5dB 편차 기준) |
| D27–D29 | 종합 마진 분석·불합격 항목 재작업 판정 | sysreq 검증 원칙 |
| D30 | IOT 종료 보고, 운용 이관(정상운용 전환) | sysreq "GS: IOT 30일 계획" |

## 3. 참고사항 (LEOP, IOT 범위 외)
COMM-CORR-02(STR 회신) — 반사판·SA 전개 과도구간(~100초)에는 TT&C 안테나
시야가 일시 차폐될 수 있음. 이는 LEOP(발사 후 궤도 진입) 단계의 1회성
이벤트로 D1(관제소 인수) 이전에 종료되므로 본 IOT 30일 계획에는 반영하지
않음 — LEOP 운용 절차(본 Work 범위 밖)에 참고로만 전달.

검증: sysreq "GS: 관제소 적합성, IOT 30일 계획" — TT&C 관제소 적합
(마진≥6dB, 수치 인용), Ka 시험국 조건부 적합(신규 확보 필요, EIRP≥85dBW·
BW≥40MHz·G/T≥30dB/K 인용), IOT 30일 일정에 PAY 요구 24채널 EIRP(±0.5dB)·
대표4채널 NPR 전부 반영.
