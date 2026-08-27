---
id: REQ-FSW-AOCS-TMTC
title: AOCS TM/TC·제어 알고리즘 인터페이스 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: AOCS-DSN-01
deliverable: examples/ksat8/deliverables/AOCS/fsw-tmtc-reply.md
after: -
track: AOCS
started: 2026-08-27 03:53:08
finished: 2026-08-27 03:53:08
---

왜: 관리 SW가 자세제어 루프(모멘텀 휠 + 이온추력기 언로딩)를 주기 실행하려면
TM/TC 목록과 제어 알고리즘 호출 인터페이스(주기·입출력)를 알아야 한다.

무엇을 알려달라: (1) TM 목록(자세 오차·각속도, 휠 속도·토크, 센서
상태), (2) TC 목록(모드 전환, 휠 바이어스 명령, 언로딩 개시), (3) 제어
알고리즘 인터페이스 — 실행 주기(Hz), 입력 벡터(센서 TM)·출력 벡터(구동기
TC) 정의, 지향 0.05°(3σ) 유지에 필요한 최소 샘플링 주기.

회신 산출물 경로 제안: examples/ksat8/deliverables/AOCS/fsw-tmtc-reply.md
검증: 실행주기10Hz 회신, TM/TC 목록·제어인터페이스 확정
