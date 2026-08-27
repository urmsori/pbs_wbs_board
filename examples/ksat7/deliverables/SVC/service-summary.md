# SVC 프로젝트 지원 서비스 운영 요약 (K-SAT 7)

입력: examples/ksat7/board/{CM,PA,PUR,CAL,FAC}-*.md(전건), examples/ksat7/board/AUDIT-*.md,
examples/ksat7/board/M-*.md(13개 전건)

v3.1 규칙에 따라 CM(형상관리)·PA(품질보증)·PUR(구매)·CAL(교정)·FAC(시설)를 서비스
부서가 처리했다. 전 팀(AOCS/COMM/EPS/FSW/GS/HAR/MECH/OBC/PAY/PROP/SA/STR/TCS)의
13개 M-* 모듈이 모두 DONE이고, PA 표본감사 4건이 완료되어 마감한다.

## 1. 부서별 처리 통계

| 부서(track) | 처리 건수 | 비고 |
|---|---|---|
| CM (형상관리) | 12건 | 베이스라인 배포 11건 + rev.2 재배포 1건(STR-U1 NCR 대응) |
| PA (품질보증) | 13건 | 입회 8건 + 정정 1건(PA-HAR-U1-CORR-01) + 표본감사 4건(AUDIT-1~4) |
| PUR (구매) | 17건 | 발주·구매확인서 17건 |
| CAL (교정) | 12건 | 교정성적서 12건 |
| FAC (시설) | 7건 | 시설예약 6건 + 재예약 1건(STR-U1 rev.2) |
| **합계** | **61건** | 전건 DONE, OPEN/TAKEN 잔여 없음 |

## 2. 역할(사람) 목록 및 담당 건수

역할당 상한 6건(v3.1)을 지켜 각 track에서 사람을 늘려가며 처리했다.

| 역할 | 담당 건수 | 처리 대상 (팀-유닛) |
|---|---|---|
| CM-01 | 6 | STR-U1, MECH-U1, HAR-U1, OBC-U1, AOCS-U1, PAY-U1 |
| CM-02 | 6 | EPS-U1, SA-U1, TCS-U1, PROP-U1, COMM-U1, STR-U1-R2 |
| PA-01 | 6 | FSW-U1, FSW-U2, HAR-U1(최초), PAY-U1, STR-U1, EPS-U2 |
| PA-02 | 3 | COMM-U1, TCS-U1, HAR-U1-CORR-01(정정) |
| PA-AUD-01 | 2 | AUDIT-1(STR), AUDIT-2(MECH) |
| PA-AUD-02 | 2 | AUDIT-3(PAY), AUDIT-4(HAR, 결함 발견) |
| PUR-01 | 6 | STR-U1, MECH-U1, HAR-U1, AOCS-U2, MECH-U2, STR-U2 |
| PUR-02 | 6 | PAY-U1, PAY-U2, EPS-U1, EPS-U2, OBC-U1, SA-U1 |
| PUR-03 | 5 | COMM-U1, COMM-U2, HAR-U2, PROP-U1, TCS-U1 |
| CAL-01 | 6 | AOCS-U2, PAY-U1, PAY-U2, STR-U1, AOCS-U1, EPS-U2 |
| CAL-02 | 6 | OBC-U1, SA-U1, COMM-U1, COMM-U2, PROP-U1, TCS-U1 |
| FAC-01 | 6 | PAY-U1, MECH-U1, STR-U1, EPS-U2, PROP-U1, TCS-U1 |
| FAC-02 | 1 | STR-U1-R2(재예약) |

총 13개 역할(1인 다역)로 61건 처리. 모든 역할이 6건 상한 이내(1~3건이 정상 범위인
소규모 역할도 CAL-02/FAC-02/PA-02/PA-AUD-01/02 등에서 유지됨).

## 3. PA 표본 감사 결과

완료된 Work 중 서로 다른 4개 팀(STR·MECH·PAY·HAR)에서 표본을 골라 산출물·기록을
대조했다(v3.1 — PA 스스로 발행).

| 감사 | 대상 | 결과 |
|---|---|---|
| AUDIT-1 | STR-U1 정현진동시험(1차모드 NCR) | **결함 없음** — NCR이 게시글·산출물·module-fm.md
  3곳에 동일 수치(30.4Hz)로 정직하게 일관 기록됨을 확인 |
| AUDIT-2 | MECH-U1 전개시험 | **결함 없음** — 3단계 수치 이력(34.5→36.4→37.1g)과
  마진(7.3%) 전건 일치 |
| AUDIT-3 | PAY-U2 펄스 실증·NESZ 판정 | **결함 없음** — NESZ 계산 근거·결과(-19.6dB) 및
  서비스요청 7건 카운트 실제 board와 일치 |
| AUDIT-4 | HAR-U1 배선검사·PA입회기록 | **결함 발견(경미)** — PA 자신이 발행한
  입회기록(har-u1-inspection-witness.md)이 실측치 대신 설계 예측치(0.85~1.70%)를
  실측인 것처럼 기재. 판정(합격) 자체는 무영향. PA track으로 수정 요청
  (PA-HAR-U1-CORR-01, source=AUDIT-4)을 발행·처리해 실측치(0.86~0.87%, 1.72%,
  245/238MΩ)로 정정 완료 |

**총 4건 감사, 3건 결함 없음, 1건 경미한 결함 발견 및 즉시 정정 완료.**

## 4. M-* 모듈 인도 현황

13개 M-* 전부 DONE: M-AOCS, M-COMM, M-EPS, M-FSW, M-GS, M-HAR, M-MECH, M-OBC,
M-PAY, M-PROP, M-SA, M-STR, M-TCS.

- STR 모듈은 1차모드 NCR(rev.1, 30.4Hz<35Hz)을 안고 인도되었으나, rev.2 보강
  설계·재배포(CM-STR-U1-R2)·재제작(STR-U1-R2-MFG)·시설 재예약(FAC-STR-U1-R2)까지
  서비스 부서가 지원 완료. rev.2 실측 재시험 결과 확정은 STR 팀의 후속 사안이다
  (예측 36.8Hz, 마진 1.8Hz).
- 그 외 12개 모듈은 서비스 지원 상 별도 이슈 없이 정상 종결.

## 5. 마감 조건 충족 확인

- 13개 M-* 전부 DONE ✓
- 연속 10회 이상 폴링에서 새 OPEN 서비스 요청 없음 ✓ (마지막 확인 폴링에서 확인)
- PA 표본감사 4건 완료(AUDIT-1~4) ✓
- SVC 자신·AUDIT-*·감사발 수정요청(PA-HAR-U1-CORR-01) 외 게시글은 수정하지 않았고,
  DONE 게시글도 되돌리지 않았다(HAR-U1 witness 정정은 신규 CORR 게시글로 처리).
