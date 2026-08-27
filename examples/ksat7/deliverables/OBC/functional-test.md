# OBC 유닛 기능시험(처리여유·2TB 기록/판독)

입력: examples/ksat7/deliverables/OBC/ins.md, examples/ksat7/deliverables/CAL/obc-u1-cal.md, examples/ksat7/deliverables/OBC/obc-storage-design.md

## 시험 케이스 (8건)
| # | 항목 | 결과 |
|---|---|---|
| 1 | CPU 처리여유(대표 부하 프로파일) | 51.6% 실측 |
| 2 | 2TB 저장 가용용량 실측 | 2.01TB |
| 3 | 기록대역폭(스팟모드 3.2Gbps 주입) | 3.55Gbps 실측(설계3.6Gbps 대비 -1.4%) |
| 4 | 판독대역폭(800Mbps 하향 재생) | 935Mbps 실측 |
| 5 | 1553B 버스 통신(이중화 A/B 전환) | PASS |
| 6 | CAN 버스 통신(2채널) | PASS |
| 7 | SpW 5채널 동시통신 | PASS |
| 8 | 기록버퍼 언더런(스팟 첨두-평균 전이) | 언더런 0건 |

## sysreq OBC 최종 판정
| 항목 | 요구 | 실측 | 판정 |
|---|---|---|---|
| 처리여유 | ≥50% | 51.6% | 충족 |
| 저장용량 | 원시 2TB | 2.01TB | 충족 |
| 인터페이스 | SpW/CAN(1553 포함) | 케이스5,6,7 전부 PASS | 충족 |

검증: 처리여유 51.6%≥50%(충족, 설계치52%와 -0.4%p 오차 내 정합),
저장용량 2.01TB≥2TB(충족), 기록3.55Gbps≥첨두3.2Gbps(마진10.9%),
8/8케이스 PASS — sysreq OBC 3항목 전부 최종 충족.
