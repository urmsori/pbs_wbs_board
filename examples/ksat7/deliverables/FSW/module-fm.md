# FSW 모듈 비행모델(FM) 인도 — 취합

입력: examples/ksat7/deliverables/FSW/core-design.md, sequencer-design.md,
code-review-core.md, code-review-sequencer.md, review-a-U1.md, review-b-U1.md,
review-a-U2.md, review-b-U2.md, rb-decision-U1.md, rb-decision-U2.md,
unit-test-core.md, unit-test-sequencer.md, sim-test-core.md, sim-test-sequencer.md,
examples/ksat7/deliverables/SE/sysreq.md

## FSW-U1(비행SW 코어) 직능 체인(축약)
| 단계 | Work | 산출물 | 상태 |
|---|---|---|---|
| 설계 | FSW-U1-DSN(+REV) | core-design.md | DONE |
| 코드리뷰 | FSW-U1-CHK | code-review-core.md | DONE |
| 검토(기능안전) | FSW-U1-RVW-A | review-a-U1.md | DONE |
| 검토(인터페이스) | FSW-U1-RVW-B | review-b-U1.md | DONE |
| 검토회 | FSW-U1-RB | rb-decision-U1.md | DONE |
| 단위시험 | FSW-U1-VV1 | unit-test-core.md | DONE |
| PA입회(서비스) | PA-FSW-U1 | PA/fsw-u1-witness.md | DONE |
| 프로세서시뮬레이션 | FSW-U1-VV2 | sim-test-core.md | DONE |

## FSW-U2(SAR 촬영 시퀀서) 직능 체인(축약)
| 단계 | Work | 산출물 | 상태 |
|---|---|---|---|
| 설계 | FSW-U2-DSN(+REV) | sequencer-design.md | DONE |
| 코드리뷰 | FSW-U2-CHK | code-review-sequencer.md | DONE |
| 검토(기능안전) | FSW-U2-RVW-A | review-a-U2.md | DONE |
| 검토(인터페이스) | FSW-U2-RVW-B | review-b-U2.md | DONE |
| 검토회 | FSW-U2-RB | rb-decision-U2.md | DONE |
| 단위시험 | FSW-U2-VV1 | unit-test-sequencer.md | DONE |
| PA입회(서비스) | PA-FSW-U2 | PA/fsw-u2-witness.md | DONE |
| 프로세서시뮬레이션 | FSW-U2-VV2 | sim-test-sequencer.md | DONE |

## 외부 인터페이스 협상 결과
- AOCS(REQ-FSW-AOCS, 발신): 제어주기 20Hz로 잠정 설계 → 실회신(10Hz,
  신호5종) 도착 후 FSW-U1-DSN-REV로 정정. 확정.
- PAY(REQ-FSW-PAY, 발신): 90s 누적 인터록으로 잠정 설계 → 실회신(버스트
  5s·18회·간격300s) 도착 후 FSW-U2-DSN-REV로 4중 인터록 정정. 확정.

## sysreq.md FSW 항목 최종 판정
| 항목 | 요구 | 확인 | 판정 |
|---|---|---|---|
| 비행 관리 전 기능 | 필수 | 스케줄러12태스크·TM/TC·요스티어링10Hz루프(sim-test-core) | 충족 |
| 안전모드 | 필수 | 3조건 자동트리거, VV1/VV2 3/3 PASS | 충족 |
| SAR 촬영 시퀀서 | 필수 | 명령셋5종·4중인터록, 18/18버스트 PASS(sim-test-sequencer) | 충족 |

**종합: sysreq.md FSW 3개 항목(관리 전 기능·안전모드·시퀀서) 전부 충족. M-FSW 인도 가능.**

## 잠정 사항의 최종 처리
- AOCS 제어인터페이스(REQ-FSW-AOCS): 8회×20초 폴링 중 회신 도착 → 정정
  게시글(FSW-U1-DSN-REV)로 20→10Hz·신호5종 반영, VV2에서 지터0.3% 재확인.
- PAY 촬영파라미터(REQ-FSW-PAY): 8회×20초 폴링 중 회신 도착 → 정정
  게시글(FSW-U2-DSN-REV)로 4중 인터록 반영, VV2에서 18/18버스트 재확인.

검증: 16개 유닛 Work 전부 DONE, 외부 인터페이스 2건(AOCS·PAY) 전부 확정,
sysreq FSW 3항목(관리 전 기능·안전모드·시퀀서) 전부 충족 재확인.
