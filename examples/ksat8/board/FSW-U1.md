---
id: FSW-U1
title: 위성 관리 SW 코어 설계
status: DONE
parent: M-FSW
source: M-FSW
owner: FSW-DSN-01
deliverable: examples/ksat8/deliverables/FSW/fsw-u1-design.md
after: REQ-FSW-EPS-TMTC,REQ-FSW-TCS-TMTC,REQ-FSW-PROP-TMTC,REQ-FSW-AOCS-TMTC,REQ-FSW-COMM-TMTC,REQ-FSW-PAY-TMTC,REQ-FSW-OBC-HW
track: FSW
started: 2026-08-27 04:06:26
finished: 2026-08-27 04:07:12
---

왜: 전 서브시스템(EPS/TCS/PROP/AOCS/COMM/PAY)의 TM/TC 목록·제어 파라미터와
OBC 하드웨어 인터페이스 없이는 관리 SW 코어를 설계할 수 없다 — 설계
착수 전 모든 외부 정보를 요청으로 먼저 받는다(v3.2).
산출물: examples/ksat8/deliverables/FSW/fsw-u1-design.md
검증: 7개 회신 로직/주기/인터락 태스크 반영, AOCS 10Hz 최우선
