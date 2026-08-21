---
id: K84
title: str-em.md 안테나 개구부 치수(90mm) vs str-to-comm.md(30mm) 모순 정정
status: OPEN
parent: K40
owner: -
deliverable: -
after: -
track: STR
started: -
finished: -
---

K40 통합시험(불합격 항목 10) 결과: str-em.md 본문은 "상단 패널(+Z면)
중앙에 지름 약 90 mm급 개구부"로 전개형 다이폴 수납 포락선을 수용한다고
기술한다. 그런데 STR이 K72(COMM 요청) 회신으로 직접 작성한
str-to-comm.md는 실제 패널 개구부를 "지름 30 mm급"(전개 기구 자체는
별도로 상단 트레이 40×40×15 mm급 공간에 수용)으로 명시하고 있다 —
같은 STR 트랙의 두 산출물이 서로 다른 개구부 치수를 말하고 있다.

comm-to-str.md의 "지름 약 90 mm 이내 수납 포락선"은 안테나 소자가 접힌
상태의 keep-clear 반경 요구로 읽히며, 패널을 관통하는 실제 개구부
치수와는 다른 개념으로 보인다. str-em.md가 이를 "개구부"로 혼동
기술해 str-to-comm.md의 더 상세한 30 mm 수치와 모순된 것으로 판단된다.

## 필요 사항
- str-em.md의 "상단 안테나 전개부 개구부" 절을 정정: 실제 패널 관통
  개구부(30 mm급, str-to-comm.md 기준)와 안테나 접힘 포락선(90 mm급
  keep-clear 존, 개구부 아님)을 구분해 명시.
- comm-em.md·comm-to-str.md와 용어(개구부 vs 포락선)가 일관되는지
  확인.

산출물: examples/ksat3/deliverables/str-em.md 갱신(안테나 개구부 절
정정). 입력: examples/ksat3/deliverables/str-to-comm.md,
examples/ksat3/deliverables/comm-to-str.md.
