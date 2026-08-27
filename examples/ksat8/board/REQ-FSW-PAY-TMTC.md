---
id: REQ-FSW-PAY-TMTC
title: 중계기 TM/TC·채널 스위칭 명령셋 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: PAY-DSN-01
deliverable: examples/ksat8/deliverables/PAY/fsw-tmtc-reply.md
after: -
track: PAY
started: 2026-08-27 03:55:49
finished: 2026-08-27 03:55:49
---

왜: 관리 SW가 24채널 중계기 구성을 지상 운용 계획에 맞춰 전환하려면
TM/TC 목록과 채널 스위칭 명령셋을 알아야 한다.

무엇을 알려달라: (1) TM 목록(채널별 EIRP·NPR·TWTA 전류/온도, 스위치
행렬 상태), (2) TC 목록(입력/출력 스위치 행렬 전환, TWTA ON/OFF·이득
설정), (3) 채널 스위칭 명령셋 — 채널×스위치 매트릭스 좌표 표기법,
동시 전환 시 서지 방지를 위한 순차 실행 규칙.

회신 산출물 경로 제안: examples/ksat8/deliverables/PAY/fsw-tmtc-reply.md
검증: TM/TC·좌표표기·순차전환규칙(100ms간격) 회신
