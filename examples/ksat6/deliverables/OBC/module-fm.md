# OBC 모듈 비행모델(FM) 인도 — 취합

입력: examples/ksat6/deliverables/OBC/proc-board.md, mem-board.md, io-board.md, connector-pinmap.md, obc-integration-test.md, reply-comm-downlink-interface.md, reply-pay-storage-bandwidth.md, examples/ksat6/deliverables/SE/sysreq.md

## 구성
| 유닛 | 산출물 | 상태 |
|---|---|---|
| 프로세서보드 | proc-board.md | DONE |
| 대용량 메모리보드 | mem-board.md | DONE |
| I/O보드(1553/CAN/SpW) | io-board.md(정정판 포함) | DONE |
| 커넥터·핀맵(HAR 인터페이스) | connector-pinmap.md | DONE |
| OBC 통합시험 | obc-integration-test.md | DONE(8케이스 PASS) |

## 외부 인터페이스 협상 결과
- PAY(REQ-OBC-PAY, REQ-PAY-OBC): SpW 2채널(영상1+명령1), 영상버퍼 118GB
  (요청 ≥30GB 대비 여유) — 확정.
- COMM(REQ-COMM-OBC): SpW 1채널, CCSDS AOS 프레이밍, 버퍼 64Mbit — 확정.
- HAR(REQ-HAR-OBC): 커넥터·핀맵 사양 회신 — 확정.

## sysreq.md OBC 항목 최종 판정
| 항목 | 요구 | 확인 | 판정 |
|---|---|---|---|
| 처리여유 | ≥50% | 52%(통합시험 케이스6, AOCS 20Hz 상향 반영 후에도 유지) | 충족 |
| 메모리 | 128GB | 가용 128GB 확보(mem-board.md) | 충족 |
| 인터페이스 | 1553/CAN/SpW | 3버스 전부 구현·시험(통합시험 케이스3,4,5) | 충족 |

**종합: sysreq.md OBC 3개 항목 전부 충족. M-OBC 인도 가능.**

## 잠정 가정이었던 항목의 최종 처리
- SpW 채널 대역폭: REQ-OBC-PAY 회신 지연으로 최초 잠정 배정(io-board.md) →
  PAY 실회신 도착 후 OBC-IO-REV 게시글로 정정, 채널 수 불변(4채널) 확인.

검증: 5개 유닛 산출물 전부 DONE, 외부 인터페이스 3건(PAY·COMM·HAR) 전부 확정, sysreq OBC 3항목 전부 충족 재확인.
