---
id: K10
title: 구조 EM 개발
status: DONE
parent: K00
owner: sonnet-str
deliverable: examples/ksat3/deliverables/str-em.md
after: K01
track: STR
started: 2026-08-21 02:05:38
finished: 2026-08-21 02:12:24
---

2U 구조체의 EM 개발 전체 — 설계·해석·시제·시험은 이 Work의 내부 단계다
(본문 작업 기록으로 남긴다). 다른 트랙의 산출물이 필요해지면 그때 게시글로
올린다.
산출물: examples/ksat3/deliverables/str-em.md

작업 기록:
- 2U 큐브샛 4-레일 표준 골격 구조 개념 확정
- 레일 재질·규격 선정(6061-T6, 코너 레일 4본)
- 내부 스택형 트레이 구성(EPS/COMM/안테나 3단) 배치 확정
- 태양전지 패널 부착 방식(±X/±Y 측면, 박막형 프레임) 결정
- 1차 질량 추산 수행(800 g, 예산 900 g 대비 여유 100 g 확보)
- 외부 입력 필요 항목 식별 → K51(EPS), K52(COMM) 게시글로 분리
- K51(eps-to-str.md)·K52(comm-to-str.md) 입력 반영해 EPS 트레이·안테나
  개구부 형상 확정
- 개구부·트레이 반영해 질량표 재계산(구조 순수 질량 800 g, 예산 900 g
  이내 재확인, EPS 스택 질량은 EPS 배분 항목이라 이중 계상 아님을 확인)
검증: 입력 2건 반영 후 질량 합계가 예산 0.9kg 이내임을 재계산으로 확인
