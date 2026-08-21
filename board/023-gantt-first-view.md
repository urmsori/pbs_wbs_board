---
id: 023
title: 규칙 개정 v2.5 — Gantt 중심 뷰: 모듈별·사람별 레인
status: TAKEN
parent: 000
owner: claude
deliverable: -
after: 022
track: -
started: 2026-08-21 03:49:00
finished: -
---

사용자 지적: 뷰에서 중요한 것은 Gantt다. Gantt가 모듈별·사람별로 보여야
하고, 나머지(요약표·WBS·PBS·시간순 목록)는 접을 수 있어야 하며 기본으로는
안 보여도 된다. v2.4로 owner가 사람(역할) 단위가 되면서 사람별 레인이
비로소 의미를 갖는다(수백 명 규모).

산출물: RULES.md v2.5(5절), tools/build_board_view.py —
① Gantt가 페이지 최상단(요약 줄·경고 바로 아래)이고 세 모드 버튼으로
   전환: **모듈별**(track 레인, 기본), **사람별**(owner 레인), **계층**.
② 레인 모드 = 그룹 롤업 막대(그 그룹 Work 전체 구간·진행률) 하나씩 +
   그룹별 상세 Gantt(접힘).
③ 요약표·WBS·PBS 구성·PBS 트리·시간순 목록은 전부 접힘(details)이 기본.
검증: 기존 보드 4개(규칙·K-SAT 1·2·3)와 신규 ksat4에서 렌더 확인.
