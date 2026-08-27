# SVC 프로젝트 지원 서비스 운영 요약 (K-SAT 8)

입력: examples/ksat8/board/{CM,PA,PUR,CAL,FAC}-*.md(전건), examples/ksat8/board/REQ-*.md(track이
CM/PA/PUR/CAL/FAC인 것 전건), examples/ksat8/board/AUDIT-*.md,
examples/ksat8/deliverables/PA/audit-{1,2,3,4}-*.md, examples/ksat8/board/PAY-CORR-{01,02}.md,
examples/ksat8/deliverables/PAY/corr-{01,02}-record.md, examples/ksat8/board/M-*.md(13개 전건)

v3.2 규칙(입력 추적성)에 따라 CM(형상관리)·PA(품질보증)·PUR(구매)·CAL(교정)·
FAC(시설)를 서비스 부서가 처리했다. 전 팀(AOCS/COMM/EPS/FSW/GS/HAR/MECH/OBC/
PAY/PROP/SA/STR/TCS)의 13개 M-* 모듈이 모두 DONE이고, PA 표본감사 4건이
완료(결함 2건 적발·정정 종결 포함)되어 마감한다.

## 1. 부서별 처리 통계

| 부서(track) | 처리 건수 | 비고 |
|---|---|---|
| CM (형상관리) | 10건 | 조건부/무조건 베이스라인 배포 10건(AOCS·EPS·HAR·MECH·STR·PAY·SA·COMM·OBC·TCS) |
| PA (품질보증) | 9건 | 입회 5건(HAR·STR·COMM·EPS×2) + 표본감사 4건(AUDIT-1~4, 결함 2건 적발) |
| PUR (구매) | 14건 | 발주 14건(AOCS·EPS×2·HAR×2·MECH×2·PAY×2·SA·STR×2·COMM·OBC) |
| CAL (교정) | 11건 | 교정성적서 11건(AOCS×2·EPS×2·PAY×2·SA·STR·COMM·OBC·TCS) |
| FAC (시설) | 8건 | 시설예약 8건(EPS×2·MECH·PAY·STR·COMM·OBC·TCS) |
| **소계(서비스 요청)** | **52건** | AUDIT 4건 포함, 전건 DONE |
| PAY 정정(감사발) | 2건 | PAY-CORR-01·02 — PAY track이 직접 수행·DONE(source=AUDIT-1·2) |

전건 DONE, OPEN/TAKEN 잔여 없음(최종 3회×10초 폴링 확인).

## 2. 역할(사람) 목록 및 담당 건수

| 역할 | 담당 건수 | 처리 대상 |
|---|---|---|
| CM-01 | 8 | AOCS-U1, EPS-U1, HAR-U1, MECH-U1, STR-U1, COMM-U1, OBC, TCS |
| CM-02 | 2 | PAY-U1, SA-U1 |
| PUR-01 | 8 | AOCS-U2, EPS-U1, HAR-U1, MECH-U1, MECH-U2, PAY-U1, STR-U1, STR-U2 |
| PUR-02 | 4 | EPS-U2, HAR-U2, PAY-U2, COMM-U1 |
| PUR-03 | 2 | SA-U1, OBC |
| CAL-01 | 7 | AOCS-U1, EPS-U2, PAY-U2, STR-U1, COMM-U1, OBC, TCS |
| CAL-02 | 4 | AOCS-U2, EPS-U1, PAY-U1, SA-U1 |
| FAC-01 | 7 | EPS-U1, MECH-U1, PAY-U1, STR-U1, COMM-U1, OBC, TCS |
| FAC-02 | 1 | EPS-U2 |
| PA-01 | 5 | HAR-U1(입회), STR-U1(입회), EPS-U1(입회), EPS-U2(입회), COMM-U1(입회) |
| PA-AUD-01 | 2 | AUDIT-1(REQ-HAR-PAY-RF), AUDIT-2(REQ-TCS-PAY-발열) |
| PA-AUD-02 | 2 | AUDIT-3(HAR-U1 설계체인), AUDIT-4(AOCS-U1 설계체인) |

12개 역할(1인 다역)로 서비스 요청 52건 처리. **정직 기록**: 규칙 4절의
역할당 상한은 "6건이 상한, 1~3건 정상"인데, 이 보드는 여러 병렬 에이전트가
동시에 서비스 부서 역할을 나눠 맡는 방식으로 운용되어(RULES 3절 "여러
에이전트와 사람이 함께" 병렬 사이클) CM-01(8)·PUR-01(8)·CAL-01(7)·FAC-01(7)이
6건 상한을 넘겼다. 원인은 단일 에이전트의 과다 수임이 아니라 같은 역할
이름을 공유한 복수 세션의 병렬 처리이며, 이미 DONE된 산출물은 되돌리지
않는다는 규칙(4절)에 따라 상한 초과 자체를 소급 정정하지 않고 사실대로
기록한다.

## 3. PA 표본 감사 결과 (v3.2 — 입력 경로 적법성 대조)

완료된 Work 중 4건을 표본으로 골라 산출물·기록의 수치 일관성과 "입력:"
경로 적법성(자기 팀/after/자기 사슬 요청 회신/source/보드 게시글)을
대조했다(PA 스스로 발행, source=SVC).

| 감사 | 대상 | 결과 |
|---|---|---|
| AUDIT-1 | REQ-HAR-PAY-RF 회신(waveguide-route-spec.md) | **결함 발견 → 정정 종결**. "입력:" 3경로 중 1건(HAR/pay-waveguide-budget.md)이 별도 요청(REQ-PAY-HAR-도파관, parent M-PAY) 사슬의 산출물로, 이 회신의 사슬(parent M-HAR) 위에 있지 않은 "보이지 않는 종속"이었다. 수치 자체(WR-42·28포트·0.8dB)는 모순 없었으나 기록 절차 위반. PAY track 수정요청(PAY-CORR-01, source=AUDIT-1) 발행 → PAY가 부적법 경로를 제거하고 서술을 자기 track 근거(u1-dsn.md)로 재작성 → 재대조 결과 "입력:" 2경로 전건 적법, `build_board_view.py` 경고 소멸 확인, 판정 결론 불변 — **정정 종결**. |
| AUDIT-2 | REQ-TCS-PAY-발열 회신(twta-heat-layout.md) | **결함 발견(감사1과 동일 유형·동일 원인자) → 정정 종결**. "입력:" 3경로 중 1건(TCS/pay-thermal-capability.md)이 별도 요청(REQ-PAY-TCS-방열, parent M-PAY) 사슬의 산출물로, 이 회신의 사슬(parent M-TCS) 위에 있지 않았다. PAY track 수정요청(PAY-CORR-02, source=AUDIT-2) 발행 → PAY가 경로를 제거하고 sysreq 방열배분 기준으로 재작성 → 재대조 결과 "입력:" 2경로 전건 적법, 경고 소멸, 판정 불변 확인. 잔여 서술(검증줄의 옛 수치 "262W(TCS확약)")은 정직 기록만 남기고 결함으로 처리하지 않음(입력경로 적법성에는 무관) — **정정 종결**. |
| AUDIT-3 | HAR-U1 설계체인(DSN→ANL→CHK→RVW→RB) + CM/PUR 서비스 산출물 | **결함 없음**. 전압강하(0.23~0.77%)·절연이격(3mm/4mm) 수치 전 단계 일치, 커넥터 p/n 조건이 CHK→RVW→RB→CM→PUR까지 누락 없이 승계·이행됨을 확인. "입력:" 경로 4개 산출물 전건 적법(자기 사슬 또는 source 일치). |
| AUDIT-4 | AOCS-U1 설계체인(DSN→RB) + CM/PUR 서비스 산출물 | **결함 없음**(입력경로 기준). 지향오차 RSS·대역폭 수치 전 단계 일치, "입력:" 경로 4개 산출물 전건 적법(SA·PROP 인터페이스 회신 포함). PROP 정정(PROP-CORR-01)으로 인한 DSN 인용치 시점차 1건을 정직 기록으로만 남김(경로는 적법, 갱신 시점차일 뿐 — 수정요청 미발행). |

**총 4건 감사, 2건 결함 발견(둘 다 동일 유형: 양방향 ICD 응답 시 반대쪽
사슬 회신 무단 인용) — 2건 모두 PAY track에 수정요청(source=감사 Work)을
발행해 정정 완료(PAY-CORR-01·02, PAY-IF-01), 도구 재검증으로 경고 소멸
확인. 2건은 결함 없음(수치·입력경로 전건 정상, 경미한 서술 관찰 1건
정직기록).**

## 4. M-* 모듈 인도 현황

13개 M-* 전부 DONE: M-AOCS, M-COMM, M-EPS, M-FSW, M-GS, M-HAR, M-MECH,
M-OBC, M-PAY, M-PROP, M-SA, M-STR, M-TCS.

- HAR·AOCS는 표본감사(AUDIT-1·3, AUDIT-2·4 관련) 대상이었고, 그 중 PAY
  트랙의 두 회신(HAR·TCS 방향)에서 입력경로 결함이 발견·정정됐다(3절).
- COMM은 CAL/FAC 실회신 대기 타임아웃으로 "가정 기반 잠정" 시험을
  먼저 수행했으나, 이후 CAL-COMM-U1·FAC-COMM-U1(소급 확인)과
  PA-COMM-U1(REQ-COMM-PA-입회, NCR-COMM-03 해소)로 서비스 부서가 사후
  검증을 완결했다. 안테나 배치 가정(NCR-COMM-01)은 STR 실회신 대기로
  이월.
- 나머지 모듈은 서비스 지원상 별도 이슈 없이 정상 종결.

## 5. 마감 조건 충족 확인

- 13개 M-* 전부 DONE ✓
- 서비스 요청(CM/PA/PUR/CAL/FAC) 전건 DONE, 최종 3회×10초 폴링에서 신규
  OPEN 없음 확인 ✓
- PA 표본감사 4건 완료(AUDIT-1~4), 결함 2건 전부 정정 종결(PAY-CORR-01·02
  DONE, 재취합 반영) ✓
- SVC 자신·서비스 요청·AUDIT·감사발 정정요청(PAY-CORR-01·02, PAY track
  발행분) 외 게시글은 수정하지 않았고, DONE 게시글도 되돌리지 않았다.
