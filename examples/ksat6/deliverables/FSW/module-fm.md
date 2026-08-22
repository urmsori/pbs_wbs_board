# FSW 모듈 비행모델(FM) 인도 — 취합

입력: examples/ksat6/deliverables/FSW/architecture.md, aocs-sw.md, eps-thermal-sw.md, comm-payload-sw.md, sw-verification.md, reply-prop-valve-logic.md, examples/ksat6/deliverables/SE/sysreq.md

## 구성
| 유닛 | 산출물 | 상태 |
|---|---|---|
| 아키텍처·스케줄러 | architecture.md | DONE |
| 자세제어 SW | aocs-sw.md | DONE |
| 전력·열 관리 SW | eps-thermal-sw.md | DONE |
| 통신·탑재 관리 SW | comm-payload-sw.md | DONE |
| SW 검증(프로세서 시뮬) | sw-verification.md(21케이스 PASS) | DONE |

## 외부 인터페이스 협상 결과
- AOCS(REQ-FSW-AOCS): 제어주기 20Hz, 센서/액추에이터 신호 목록 확정 —
  aocs-sw.md에 반영, architecture.md 스케줄러 주기 상향 갱신.
- EPS(REQ-FSW-EPS): 배터리 충전종지 33.6V·로드셰딩 27.2V·안전모드 26.4V·
  과온 32°C — eps-thermal-sw.md에 반영.
- PROP(REQ-PROP-FSW): 밸브 구동·잠금 로직(펄스구동·인터록·연속구동제한·
  위치TM) — comm-payload-sw.md FDIR 로직에 반영, reply-prop-valve-logic.md
  로 회신 확정.

## sysreq.md FSW 항목 최종 판정
| 항목 | 확인 근거 | 판정 |
|---|---|---|
| 자세·전력·열·통신·탑재 관리(전 항목) | sw-verification.md 21케이스 PASS | 충족 |
| 안전모드 | 안전모드 통합시나리오 2건 PASS | 충족 |
| 재프로그래밍 | A/B 이미지 스위치 시나리오 PASS | 충족 |

**종합: sysreq.md FSW 전 항목(관리기능 5개·안전모드·재프로그래밍) 충족. M-FSW 인도 가능.**

검증: 5개 유닛 산출물 전부 DONE, 외부 인터페이스 3건(AOCS·EPS·PROP) 전부 확정, sysreq FSW 전항목 재확인.
