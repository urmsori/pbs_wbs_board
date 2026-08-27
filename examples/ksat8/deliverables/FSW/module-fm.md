입력: examples/ksat8/deliverables/FSW/fsw-u1-design.md, examples/ksat8/deliverables/FSW/fsw-u1-ver1.md, examples/ksat8/deliverables/FSW/fsw-u1-ver2.md, examples/ksat8/deliverables/FSW/fsw-tmtc-db.md

# FSW 비행모델 인도 (module-fm)

## 요약
관리 SW 코어(FSW-U1)를 6개 서브시스템(EPS/TCS/PROP/AOCS/COMM/PAY)의
TM/TC·제어 파라미터 회신 7건(OBC 하드웨어 포함)을 입력으로 설계하고,
2단계 검증(단위→통합/HIL)을 마쳤다. TM/TC 데이터베이스(FSW-U2)는 같은
7건 회신을 그대로 취합한 별도 산출물이다.

## sysreq 대조
- "FSW: 전 서브시스템 관리 — 각 팀의 TM/TC 목록·제어 파라미터를
  요청으로 받아라" — REQ-FSW-{EPS,TCS,PROP,AOCS,COMM,PAY}-TMTC 6건 +
  REQ-FSW-OBC-HW 1건, 총 7건 발행·회신 완료. 회신 없이 읽은 외부
  서브시스템 파일 없음(도구 입력 추적 경고 0, 아래 확인).

## 잠정 → 확정 상태
| 항목 | 상태 |
|---|---|
| EPS/TCS/PROP/AOCS/PAY 회신 | **실회신**(해당 트랙 담당자가 직접 회신) |
| COMM 회신(REQ-FSW-COMM-TMTC) | **잠정**(8×20초 폴링 초과, sysreq+CCSDS 표준 관행 근거로 FSW 리드가 대리 작성) — COMM-U1 확정 시 정정 게시글 예정, FSW-U1-VER2가 재시험 필요 항목으로 기록 |
| AOCS/PAY TM 상세 개수 | 발췌 회신만 확보 — 후속 상세 요청 필요(FSW-U2에 기록) |

## 검증 결과
- VER1(단위): 태스크-설계 1:1 대응, 경계값 시험 통과.
- VER2(통합/HIL): 7태스크 동시 스케줄링·PROP 인터락·워치독 리셋 정상.

검증: 7건 요청 전량 회신 확보(1건 잠정), 2단계 검증 통과, 미결 항목(COMM
확정·AOCS/PAY 상세)은 정정/후속 요청 대상으로 명시.
