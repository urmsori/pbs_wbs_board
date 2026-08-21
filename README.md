# PBS WBS Board

원하는 Product를 여러 에이전트와 사람이 함께 Work로 나눠 만들고, 산출물을 모아
PBS/WBS로 취합하는 게시판 규칙 저장소.

- **규칙 전문**: [RULES.md](RULES.md) — 처음이라면 2절 "바로 따라하기 — 사이클"만 읽어도 된다.
- **게시판**: [board/](board/) — 게시글 1건 = 파일 1개. 프로젝트마다 보드 하나(규칙 v1.4).
- **현황 보기**: `python3 tools/build_board_view.py [보드] [출력]` 실행 후 생성된 html을 연다.
- **검증 결과**: [VALIDATION.md](VALIDATION.md) — 이 규칙은 이 규칙으로 만들어져 검증되었다.
- **적용 예시**:
  - [examples/ksat3/](examples/ksat3/) — **모범 예시(v2.3)**. 확실한 필요만으로
    시작해, 트랙 에이전트들이 일하다 발견한 필요(교차 종속·수정 요청)가
    보드에 올라오고, 통합시험 불합격→수정→재검증의 재작업 루프가 기록된다.
  - [examples/satellite/](examples/satellite/) — 입문 예시(K-SAT 1, 16건).
    최종 형상만 EM/QM/FM, 모듈은 각자 단계.
  - [examples/satellite-full/](examples/satellite-full/) — 실규모(2,190건)·
    레벨-등급·대용량 뷰 실증. 단 Work 단위 기준(v2.3)을 어긴 **반례**로
    보존 — 해당 README의 주석 참조.
