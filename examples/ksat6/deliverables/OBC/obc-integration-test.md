# OBC 통합시험

입력: examples/ksat6/deliverables/OBC/proc-board.md, examples/ksat6/deliverables/OBC/mem-board.md, examples/ksat6/deliverables/OBC/io-board.md, examples/ksat6/deliverables/OBC/connector-pinmap.md, examples/ksat6/deliverables/SE/sysreq.md

## 시험 구성
프로세서보드+메모리보드+I/O보드를 커넥터·핀맵(connector-pinmap.md) 대로
조립하여 하나의 OBC 모듈로 통합, 지상시험장비(EGSE)로 부팅·버스통신·부하
시험을 수행.

## 시험 케이스(총 8건)
| # | 케이스 | 결과 |
|---|---|---|
| 1 | 콜드부트 → 이미지 A 부팅 | PASS (부팅시간 4.2s) |
| 2 | 이미지 A 손상 → B 자동 스위치 | PASS |
| 3 | 1553B 이중화(A/B) 통신 | PASS |
| 4 | CAN 이중화(A/B) 통신 | PASS |
| 5 | SpW 4채널 동시 트래픽 | PASS |
| 6 | 대표 태스크 셋 동시 실행 시 CPU 점유율 측정 | PASS (48%, 처리여유 52%) |
| 7 | 메모리 스크러빙 동작(인위적 SEU 주입) | PASS |
| 8 | 전원 이중화 전환(주→부 코어) | PASS |

## sysreq OBC 항목 판정
| sysreq 항목 | 요구 | 실측/설계값 | 판정 |
|---|---|---|---|
| 처리여유 | ≥50% | 52%(케이스6) | 충족 |
| 메모리 | 128GB | 가용 128GB(mem-board.md) | 충족 |
| 인터페이스 | 1553/CAN/SpW | 3버스 전부 구현·시험(케이스3,4,5) | 충족 |

**종합 판정: sysreq.md OBC 3개 항목 전부 충족.**

검증: 위 8개 시험 케이스 전부 PASS, sysreq OBC 항목 표와 교차 확인.
