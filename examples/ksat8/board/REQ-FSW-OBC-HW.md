---
id: REQ-FSW-OBC-HW
title: OBC 하드웨어 스펙(레지스터 맵·드라이버 인터페이스) 요청
status: DONE
parent: M-FSW
source: FSW-U1
owner: OBC-DSN-01
deliverable: examples/ksat8/deliverables/OBC/fsw-hw-reply.md
after: -
track: OBC
started: 2026-08-27 03:49:10
finished: 2026-08-27 03:49:36
---

왜: 관리 SW 코어는 OBC 하드웨어 위에서 동작하므로 레지스터 맵과 드라이버
인터페이스가 있어야 이중화 절체·TM 수집 루틴을 설계할 수 있다. FSW·OBC를
같은 에이전트가 담당하더라도 트랙이 다른 인수인계이므로 게시글로 남긴다
(v3.2 — 남의 파일을 회신 없이 읽는 것은 보이지 않는 종속).

무엇을 알려달라: (1) 레지스터 맵(TM 수집 버퍼, TC 디코더, 이중화 상태
레지스터), (2) 드라이버 인터페이스(버스 드라이버 API, 인터럽트 벡터,
워치독), (3) 이중화 절체 조건·소요시간.

회신 산출물 경로 제안: examples/ksat8/deliverables/OBC/fsw-hw-reply.md
검증: 레지스터맵·드라이버 API·절체조건 회신
