# AIT-RX-3 컴퓨터·SW·통신·지상국(OBC/FSW/COMM/GS) 인도 수령·판정

입력: examples/ksat8/deliverables/OBC/module-fm.md,
examples/ksat8/deliverables/FSW/module-fm.md,
examples/ksat8/deliverables/COMM/module-fm.md,
examples/ksat8/deliverables/GS/module-fm.md

## 판정
| 트랙 | sysreq 항목 | 인도 문서 판정 |
|---|---|---|
| OBC | TM8,000점·TC2,000점·이중화절체 | 프레임드롭0건·420ms≤500ms — 충족(COMM 인터페이스 잠정 표기, 아래 참조) |
| FSW | 전 서브시스템 TM/TC 관리 | 7건 요청 전량 회신(1건 잠정: COMM) — 충족 |
| COMM | S-band상시·레인징 | 하향EIRP4.8dBW·턴어라운드비 정합 — 충족 |
| GS | 관제소 적합성·IOT30일계획 | 조건부 적합(Ka 시험국 확보 전제)·D1-D30 일정 확정 — 충족 |

## OBC/FSW의 COMM 잠정 표기 재확인
OBC module-fm.md는 REQ-OBC-COMM-IF 회신을 "COMM-U1 설계 미확정 시점의
잠정"으로, FSW module-fm.md는 REQ-FSW-COMM-TMTC를 "8×20초 폴링 초과로
FSW 리드 대리 작성(잠정)"으로 각각 명시했다. 그런데 COMM module-fm.md는
이미 COMM-U1이 CM/PUR/CAL/FAC/PA 전 서비스 회신을 반영해 재취합 완료
(DONE)됐다고 판정한다 — 즉 COMM 확정치는 인도 문서 안에 이미 있다.
따라서 OBC/FSW의 "잠정" 표기는 COMM module-fm.md 확정 수치(S-band
2087.5/2255.5MHz, 하향EIRP4.8dBW, 1553B 루프백 정상)로 이미 해소된
것으로 인도 문서 범위 내에서 판정하며, 별도 요청 없이 기록만 남긴다
(OBC/FSW 재정정은 각 트랙 자체 게시글 몫이며 module-fm.md 확정 수치와
상충하는 부분이 없어 INT 재작업 불요).

## 이월 항목 — 요청 발행
1. **COMM 부품 납기**: NCR-COMM-02(부품 입고예정 2026-09-10~15)의 실제
   입고·IQC 완료 여부가 module-fm.md에 없어 REQ-AIT-COMM-부품입고
   (track: COMM, source: 본 Work) 발행. 8×20초 폴링(160초) 무응답
   (COMM 팀 에이전트 종료). **OPEN으로 남기고, 인도 문서 범위로 판정**:
   module-fm.md가 이를 "정상 생산일정(결함 아님)"으로 명시했으므로
   INT 통합조립 착수는 진행하되, 해당 부품 입고 완료 확인을 통합조립
   착수 전제조건으로 integration-fm.md에 명시 이관한다.
2. **GS Ka IOT 시험국 조건부 적합**: 신규/임차 확보 확정 여부가
   module-fm.md에 없어 REQ-AIT-GS-Ka시험국(track: GS, source: 본 Work)
   발행. 8×20초 폴링(160초) 무응답(GS 팀 에이전트 종료). **OPEN으로
   남기고, 인도 문서 범위로 판정**: module-fm.md가 "추후 조달 확정 시
   정정 게시글 예정"이라 명시했으므로 INT-TST-3의 TT&C 부분(기존
   S-band 관제소, 조건 없음)은 그대로 수행하고, Ka 24채널 EIRP/NPR
   부분은 Ka 시험국 확보를 전제조건으로 운용 단계 이관한다.

검증: OBC·FSW·COMM·GS sysreq 항목 전량 인도 문서 기준 충족 확인, COMM
잠정표기는 COMM 확정치로 해소 판정, 이월 2건은 요청 게시글 OPEN 상태로
전제조건 명시 후 INT-TST-3/통합조립에 조건부 이관
