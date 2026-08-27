입력: examples/ksat8/deliverables/EPS/fsw-tmtc-reply.md, examples/ksat8/deliverables/TCS/fsw-tmtc-reply.md, examples/ksat8/deliverables/PROP/fsw-tmtc-reply.md, examples/ksat8/deliverables/AOCS/fsw-tmtc-reply.md, examples/ksat8/deliverables/COMM/fsw-tmtc-reply.md, examples/ksat8/deliverables/PAY/fsw-tmtc-reply.md, examples/ksat8/deliverables/OBC/fsw-hw-reply.md

# 위성 전체 TM/TC 데이터베이스 (FSW-U2)

7건의 REQ-FSW-*-TMTC/HW 회신을 그대로 취합한 것이 이 Work의 전부다 —
새로운 설계 판단 없이 목록을 표준 형식으로 정리한다.

| 서브시스템 | TM 개수(회신 기준) | TC 개수(회신 기준) | 상태 |
|---|---|---|---|
| EPS | ≈76(개산) | 36 | 확정(EPS-U2 시 배터리 파라미터 정정 가능) |
| TCS | 16 | 12 | 확정 |
| PROP | 35(예비치) | 16(예비치) | PROP-DSN-01/02 확정 후 갱신 예정 |
| AOCS | 발췌(정확 개수 미회신) | 발췌 | 상세 개수 후속 요청 필요 |
| COMM | 발췌(**잠정** — COMM-U1 미확정) | 발췌(잠정) | 정정 예정 |
| PAY | 144(발췌, 채널당 6×24) | 발췌 | 세부는 OBC 회신(400점) 참조 |
| OBC(레지스터 맵) | 이중화 상태 레지스터 포함 | TC 디코더 큐 | 확정 |

## 후속 필요(발견됨)
AOCS·PAY의 TM 목록이 "발췌"로만 회신되어 정확한 점수 집계가 안 된다 —
FSW-U1 스케줄링에는 영향 없으나(로직·주기는 회신됨), 지상국 DB 완전성을
위해 상세 목록 후속 요청이 필요하다(추후 REQ-FSW-AOCS-TMTC-상세 등으로
발행 예정, 이번 인도 범위 밖).

검증: 7건 회신 전량 표로 취합, 미결(AOCS/PAY 상세, COMM 확정) 항목 명시.
