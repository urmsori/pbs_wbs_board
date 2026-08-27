---
id: REQ-FSW-PROP-TMTC
title: PROP TM/TC·밸브/추력기 구동·잠금 로직 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: PROP-DSN-01
deliverable: examples/ksat8/deliverables/PROP/fsw-tmtc-reply.md
after: -
track: PROP
started: 2026-08-27 03:49:52
finished: 2026-08-27 03:50:29
---

왜: 관리 SW가 추진계 밸브·추력기를 오발사 없이 구동하려면 TM/TC 목록과
구동·안전 잠금(interlock) 로직을 알아야 한다.

무엇을 알려달라: (1) TM 목록(탱크압력·온도, 밸브 개폐 상태, 추력기
가동시간 누적, 이온추력기 상태), (2) TC 목록(래치밸브 개폐, 추력기
점화/정지, 이원추진 밸브 시퀀스), (3) 구동·잠금 로직 — 추력기 점화 전
필수 선행조건(예: 자세 안정 플래그, 이중 커맨드 확인), 오동작 방지
인터락 표.

회신 산출물 경로 제안: examples/ksat8/deliverables/PROP/fsw-tmtc-reply.md
검증: TM35점·TC16점·점화 인터락 로직 회신(예비)
