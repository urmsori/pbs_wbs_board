---
id: K82
title: str-em.md 하단 EPS 트레이 설계를 eps-to-str.md Rev.B 갱신 반영해 재검증
status: OPEN
parent: K40
owner: -
deliverable: -
after: K81
track: STR
started: -
finished: -
---

K81에서 eps-to-str.md가 EPS Rev.B(스택 0.35 kg, 4셀 2S2P, 버스트 국소
발열)로 갱신되면, STR은 이를 입력으로 str-em.md의 하단 EPS 트레이
"확정" 설계(볼트 패턴 근거, 외형 포락선 90×90×20 mm 가정, 방열 접촉면,
내부 트레이 3매 210 g 질량 항목)를 재확인해야 한다. K81의 결과를
입력으로 쓰므로 after: K81을 건다.

## 재검증 항목
- 외형 포락선이 바뀌면 트레이 형상·질량(현재 210 g 추산, 구조 순수질량
  합계 800 g/예산 900 g)도 재계산.
- 방열 접촉면 설계(평탄도 ≤0.1 mm, 접촉률 ≥80%)가 버스트 국소 발열
  증가를 감안해도 유효한지 확인, 필요 시 국부 방열 패드 반영.
- 볼트 패턴이 바뀌면 str-to-eps.md(K61 산출물)도 함께 갱신.

산출물: examples/ksat3/deliverables/str-em.md 갱신(필요 시
examples/ksat3/deliverables/str-to-eps.md도). 입력:
examples/ksat3/deliverables/eps-to-str.md(K81 갱신본).
