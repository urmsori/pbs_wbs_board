---
id: 020
title: 규칙 개정 v2.2 — id 접두어 충돌 정정 (post.py 정확 일치)
status: DONE
parent: 000
owner: claude
deliverable: tools/post.py, RULES.md
after: 019
track: -
started: 2026-08-21 01:40:30
finished: 2026-08-21 01:41:58
---

sonnet-agg-a의 불편 보고(QM 취합 중). post.py의 find_by_id가
`<id>-*.md` 글롭으로 파일을 찾는데, 계층 id(`QM-STR-BR`)와 그 잎
(`QM-STR-BR-01`)이 접두어 관계라 잎 파일까지 매칭된다. 선행 검사에서
엉뚱한 파일의 status를 읽어 거짓 승인/거부가 날 수 있는 실제 결함이다.

산출물: tools/post.py(글롭 후보 중 frontmatter id가 정확히 일치하는 파일만
채택), RULES.md v2.2(3절: 계층 접두어 id를 쓸 때의 주의와 도구의 정확 일치
보장 명시).
검증: QM-STR-BR과 QM-STR-BR-01이 각자 정확한 파일로 해석됨을 실보드에서 확인
