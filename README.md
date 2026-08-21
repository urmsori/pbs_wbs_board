# PBS WBS Board

원하는 Product를 여러 에이전트와 사람이 함께 Work로 나눠 만들고, 산출물을 모아
PBS/WBS로 취합하는 게시판 규칙 저장소.

- **규칙 전문**: [RULES.md](RULES.md) — 처음이라면 2절 "바로 따라하기 — 사이클"만 읽어도 된다.
- **게시판**: [board/](board/) — 게시글 1건 = 파일 1개. 프로젝트마다 보드 하나(규칙 v1.4).
- **현황 보기**: `python3 tools/build_board_view.py [보드] [출력]` 실행 후 생성된 html을 연다.
- **검증 결과**: [VALIDATION.md](VALIDATION.md) — 이 규칙은 이 규칙으로 만들어져 검증되었다.
- **적용 예시**: [examples/satellite/](examples/satellite/) — 인공위성(K-SAT 1) 개발을
  병렬 에이전트들이 이 규칙의 사이클로 진행한 예시. 최종 형상만 EM/QM/FM이고
  모듈은 각자 단계를 나눈다.
