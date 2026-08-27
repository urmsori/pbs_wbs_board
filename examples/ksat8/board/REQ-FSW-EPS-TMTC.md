---
id: REQ-FSW-EPS-TMTC
title: EPS TM/TC 목록·배터리 관리 파라미터 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: EPS-U1-DSN-01
deliverable: examples/ksat8/deliverables/EPS/fsw-tmtc-reply.md
after: -
track: EPS
started: 2026-08-27 03:52:52
finished: 2026-08-27 03:52:52
---

왜: 관리 SW가 EPS를 감시·제어하려면 EPS의 TM/TC 목록과 배터리 관리(충방전
한계·이클립스 SOC 문턱값) 파라미터를 알아야 한다.

무엇을 알려달라: (1) TM 목록(버스전압/전류, 채널별 배전 상태, 배터리
전압·전류·온도·SOC 등, 점수 개산), (2) TC 목록(채널 ON/OFF, 배터리
충전모드 전환 등), (3) 배터리 관리 파라미터(충전 상한 전압, 방전 하한
SOC, 이클립스 진입/이탈 임계, 과전류 트립값).

회신 산출물 경로 제안: examples/ksat8/deliverables/EPS/fsw-tmtc-reply.md
검증: TM76점·TC36개·배터리관리 파라미터 회신
