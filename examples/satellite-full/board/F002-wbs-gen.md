---
id: F002
title: WBS 골격 생성
status: DONE
parent: F000
owner: claude
deliverable: examples/satellite-full/tools/gen_wbs.py, examples/satellite-full/board/, examples/satellite-full/runlists/
after: F001
track: SYS
started: 2026-08-21 01:21:40
finished: 2026-08-21 01:21:51
---

규칙 1절의 '미리 올려 두기'를 수행하는 Work. 형상×서브시스템×조립체×잎의
OPEN 게시글 약 2,180건과 조립체 산출물 스텁, 에이전트 실행목록(runlist)을
생성기로 만든다. 산출물: examples/satellite-full/tools/gen_wbs.py와 생성된
board/ 골격.
검증: 생성 후 총 2,190건(잎 2,016·조립체 144·서브시스템 24·형상 3·시스템 3) 확인, 재실행 시 멱등(0건 생성) 확인
