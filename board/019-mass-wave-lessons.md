---
id: 019
title: 규칙 개정 v2.1 — 대규모 웨이브 운용에서 배운 것
status: DONE
parent: 000
owner: claude
deliverable: RULES.md, tools/post.py
after: 018
track: -
started: 2026-08-21 01:33
finished: 2026-08-21 01:31:04
---

K-SAT 2 EM 페이즈(잎 672건, haiku 8 + sonnet 2)를 돌리며 겪은 불편.

1. 한 에이전트(haiku-aocs)가 잎을 한 건씩 손으로 처리하다 정체되어 전체
   웨이브를 지연시켰고, 다른 두 에이전트는 완료 후 자기 루프를 두 번 돌아
   "이미 DONE"이라며 혼동 보고를 했다(그중 하나는 DONE을 OPEN으로 리셋하려
   시도 — 기록 덮어쓰기 금지 위반 직전) → 정형화된 잎 Work 다수는 실행목록
   (runlist) 기반 **배치 처리 관례**를 규칙에 명문화하고, DONE 리셋 금지를
   재확인한다. take의 "OPEN 아님" 거부는 재실행 방지 장치로 정상 동작했다.
2. TAKEN인 채 오래 움직이지 않는 게시글(정체·이탈)의 처리 규정이 없다 →
   취합자가 정체를 판단하면 owner를 교체할 수 있게 한다(교체 사실을 본문에
   기록 — 기록은 덮어쓰지 않고 쌓는다).
3. post.py ready 출력이 head 등과 파이프될 때 BrokenPipe 트레이스백을 냈다
   → 정정.

산출물: RULES.md v2.1, tools/post.py(파이프 정정).
검증: 배치 관례·DONE 불가역·정체 인계 조항이 4절에 있음을 재독으로 확인, ready 파이프 정정은 head 파이프 재실행으로 확인
