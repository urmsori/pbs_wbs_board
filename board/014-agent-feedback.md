---
id: 014
title: 규칙 개정 v1.6 — 웨이브 1 에이전트 불편 반영
status: DONE
parent: 000
owner: claude
deliverable: RULES.md, tools/build_board_view.py
after: 013
track: -
started: 2026-08-21 00:57
finished: 2026-08-21 00:59
---

웨이브 1에 투입된 에이전트 4명(agent-str/eps/aocs/comm)이 보고한 실제 불편.
규칙 7절 "불편했던 점을 게시글로 올린다"의 적용이며, 보고한 쪽이 아니라
다음에 올 에이전트들이 불편할 것이므로 웨이브 2 전에 고친다.

1. (전원) 분 단위 시각이라 짧은 Work는 started=finished가 되어 Gantt 막대
   폭이 0이 된다 → 시각에 초 단위 허용(`YYYY-MM-DD HH:MM[:SS]`).
2. (eps) "지금 집을 수 있는 OPEN 게시글" 조회 수단이 없어 에이전트마다 선행
   DONE 확인을 각자 구현한다 → 뷰와 도구 출력에 "집기 가능" 표시.
3. (str, comm) 산출물 경로·검증 문구가 본문과 frontmatter/산출물 파일에 중복
   기재된다 → 정본 명시: 경로는 frontmatter `deliverable`, 검증 기록은 게시글
   본문이 정본이고 나머지는 설명/선택.
4. (aocs) 커밋을 취합자가 대신 할 때 TAKEN 잠금 시점이 애매하다 → 공유 작업
   공간에서는 게시글 파일 수정이 곧 공표(잠금)이고, push 선점 규칙은 저장소가
   분리된 에이전트 사이에만 적용됨을 명시.

산출물: RULES.md v1.6, 집기 가능 표시가 추가된 tools/build_board_view.py.
검증: parse_dt가 초 단위 시각을 파싱함을 확인. 위성 보드에 도구를 돌려 "집기
가능: S002, S011, S022, S032, S042"가 출력됨을 확인 — 선행이 안 끝난 S003,
S004는 목록에 없다. 정본·잠금 규칙은 문안 검토로 확인.
