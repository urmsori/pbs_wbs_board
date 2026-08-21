---
id: 017
title: 규칙 개정 v1.9 — 레벨과 에이전트 등급, 상태 전환 소도구
status: DONE
parent: 000
owner: claude
deliverable: RULES.md, tools/post.py
after: 016
track: -
started: 2026-08-21 01:14
finished: 2026-08-21 01:16
---

불편 두 가지. (1) 실제 위성 개발 규모(Work 2,000건 이상, 5레벨 분해)를
올리려는데, 모든 Work를 같은 값비싼 에이전트가 집는 것은 낭비다 — 깊은
레벨의 Work는 작고 정형화되어 있어 가벼운 에이전트로 충분하다. 레벨과
에이전트 등급의 관계가 규칙에 없다. (2) 웨이브 1·2 에이전트 전원이 보고한
남은 과제: 상태 전환마다 date 실행과 frontmatter 손 편집을 반복해야 하고
오기입 여지가 있다.

산출물: RULES.md v1.9(레벨-등급 규칙), tools/post.py(take/done/ready —
초 단위 자동 시각, after 미완·상태 오류 거부).
검증: post.py를 임시 보드에서 시험 — 선행 미완 take 거부, 산출물 없는 done
거부, 정상 take/done 시 초 단위 시각 자동 기록, ready가 집기 가능 게시글만
출력함을 확인. 레벨-등급 규칙은 satellite-full 예시(하이쿠 잎/소넷 취합/
클로드 형상)로 실증 예정.
