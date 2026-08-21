---
id: 011
title: 도구 상태 문구를 새 "끝" 정의와 사이클에 맞추기
status: DONE
parent: 008
owner: claude
deliverable: tools/build_board_view.py
after: 010
started: 2026-08-21 00:43
finished: 2026-08-21 00:44
---

008의 수행·검증 중 발견한 필요(사이클 4단계). OPEN이 0건이고 TAKEN만 남은
상태에서도 board.html 요약이 "OPEN 게시글을 집어 계속한다"라고 말하고, 완료
문구도 옛 정의("OPEN 없음")를 쓴다. v1.3의 끝 정의는 "OPEN·TAKEN 없음 + 루트
DONE"이다.
산출물: 상태 문구를 고친 tools/build_board_view.py.
검증: OPEN 0·TAKEN 3 상태에서 도구를 실행해 "TAKEN 게시글 3건이 끝나기를
기다린다"가 출력됨을 확인. 이 게시글은 PBS에 이미 있는 파일(도구)의 일부만
갱신한 사례다 — Product 구성 목록은 바뀌지 않고 갱신 Work만 추가된다.
