# 예시: K-SAT 1 인공위성 개발

PBS WBS Board 규칙(../../RULES.md)을 규칙 프로젝트가 아닌 실제 개발 모양의
프로젝트에 적용해 본 예시다. 여러 에이전트가 각자 사이클을 병렬로 돌며
진행했다.

- **보드**: [board/](board/) — 게시글 16건.
- **현황**: `python3 tools/build_board_view.py examples/satellite/board` 실행 후
  [board.html](board.html).
- **산출물**: [deliverables/](deliverables/)

## 이 예시가 보여주는 것

- **최종 위성 형상만 EM → QM → FM** 세 단계다(S002 → S003 → S004, `after`로
  직렬). 우리가 규칙을 한 번에 못 만들고 v1.0부터 고쳐 온 것처럼, 위성도 한
  번에 만들지 않는다.
- **모듈은 각자 알아서 단계를 나눈다** — 정해진 단계 집합을 강제하지 않는다:
  - 구조(STR): STM → FM (EM·QM 없음)
  - 전력(EPS): BB → EM → FM
  - 자세제어(AOCS): 시뮬레이션 → EM → FM
  - 통신(COMM): EM → QM → FM (신규 개발이라 모듈 단독 인증 단계가 있음)
- **병렬 진행**: 모듈 트랙들은 서로 `after`가 없어 동시에 진행되고, 형상
  Work는 필요한 모듈 단계만 `after`로 기다린다. QM 형상이 진행되는 동안 FM
  모듈들이 병렬로 제작된다 — Gantt에서 겹친 막대와 화살표로 보인다.
- 각 게시글의 `track` 필드가 모듈/분야를 표시한다(규칙 v1.5).

## 결과 (루트 S000 취합)

- 게시글 16건 전부 DONE, FRR 판정 "K-SAT 1 FM 인도 가능"
  ([sat-fm-readiness.md](deliverables/sat-fm-readiness.md)). FM 질량 46.3/50 kg.
- 에이전트 6명이 사이클을 돌았다: claude(S000·S001), agent-str, agent-eps,
  agent-aocs, agent-comm(각 모듈 트랙), agent-ait(형상 EM→QM→FM).
- 두 웨이브의 병렬 기록: 웨이브 1에서 모듈 4트랙이 동시 진행, 웨이브 2에서
  EM 형상 통합(S002)이 FM 모듈 제작(S011/S022/S032/S042)과 겹쳐 진행 —
  Gantt에서 확인된다.
- 이 예시를 진행하며 규칙이 v1.4→v1.8로 5번 개정되었다(다중 보드, track·병렬
  운용, 에이전트 불편 반영, --ready 조회, 취합 모순 처리). 에이전트들이
  보고한 불편이 그대로 개정 게시글(규칙 보드 012~016)이 되었다.
