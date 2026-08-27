---
id: REQ-FSW-COMM-TMTC
title: TT&C 프로토콜·TC 검증 규칙 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: COMM-TMTC-01
deliverable: examples/ksat8/deliverables/COMM/fsw-tmtc-reply.md
after: -
track: COMM
started: 2026-08-27 03:58:37
finished: 2026-08-27 03:58:56
---

왜: 관리 SW가 지상국과 TT&C 링크로 TM/TC를 주고받으려면 S-band TT&C
프로토콜과 TC 수락 전 검증 규칙(오류정정·인가)을 알아야 한다.

무엇을 알려달라: (1) TM/TC 프레임 프로토콜(예: CCSDS TC/TM 스페이스
패킷 여부, 동기어), (2) TC 검증 규칙 — CRC/체크섬, 명령 인가(2단계
확인 필요 명령 목록), 순번(sequence) 검사, 거부 시 응답 TM, (3) 레인징
신호와 TM/TC 공존 방식.

회신 산출물 경로 제안: examples/ksat8/deliverables/COMM/fsw-tmtc-reply.md
검증: 잠정: sysreq TT&C 요약+표준 CCSDS 관행 근거, COMM-U1 확정 후 정정 예정
