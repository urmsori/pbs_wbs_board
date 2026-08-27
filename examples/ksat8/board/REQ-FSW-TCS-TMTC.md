---
id: REQ-FSW-TCS-TMTC
title: TCS TM/TC·히터 제어 로직 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: TCS-DSN-01
deliverable: examples/ksat8/deliverables/TCS/fsw-tmtc-reply.md
after: -
track: TCS
started: 2026-08-27 03:49:52
finished: 2026-08-27 03:50:29
---

왜: 관리 SW가 TCS 히터를 자동 제어하려면 TM/TC 목록과 히터 제어 로직
(설정점·데드밴드)을 알아야 한다.

무엇을 알려달라: (1) TM 목록(패널/히트파이프 온도센서 채널별, 히터 ON/OFF
상태), (2) TC 목록(히터 채널 ON/OFF, 자동/수동 모드 전환), (3) 히터 제어
로직 — 설정점(°C)과 데드밴드(°C) 채널별 표, 이중화(주/예비 히터) 전환
조건.

회신 산출물 경로 제안: examples/ksat8/deliverables/TCS/fsw-tmtc-reply.md
검증: TM16점·TC12점·6채널 설정점/데드밴드 회신
