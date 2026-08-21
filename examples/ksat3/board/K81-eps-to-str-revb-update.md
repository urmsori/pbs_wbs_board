---
id: K81
title: eps-to-str.md를 EPS Rev.B 기준으로 갱신
status: DONE
parent: K40
owner: sonnet-eps
deliverable: examples/ksat3/deliverables/eps-to-str.md
after: -
track: EPS
started: 2026-08-21 02:20:35
finished: 2026-08-21 02:21:10
---

K40 통합시험(불합격 항목 7) 결과: eps-em.md는 Rev.B(2S2P 4셀 + 버스트
전용 부스트 스테이지, 스택 질량 0.35 kg)로 개정되었으나, K51 산출물
eps-to-str.md는 여전히 Rev.A 수치(스택 0.23 kg, 배터리 2셀, 외형
90×90×20 mm, 평시 발열 약 0.4 W)에 머물러 있다. eps-em.md 스스로도
"미결/리스크" 절에서 이 수치가 낡았다고 명시하며 K40에서 정합이
확인될 것으로 남겨두었다 — 이제 그 확인 결과가 불합격이다.

str-em.md의 하단 EPS 트레이 "확정" 설계(볼트 패턴, 방열 접촉면, 트레이
두께)가 이 낡은 입력에 근거하고 있어 정합 재확인이 필요하다.

## 갱신 필요 사항
1. 스택 질량을 0.35 kg(Rev.B)로 갱신.
2. 배터리 4셀(2S2P) 배치에 따른 외형 치수 재확인 — 기존 90×90×20 mm
   포락선이 4셀 구성에서도 유지되는지, 유지되지 않으면 신규 치수 제시.
3. 배전보드 볼트 패턴 변경 여부 확인(부스트 스테이지 추가 부품 실장
   공간 포함 여부).
4. 발열 갱신 — 평시 발열(약 0.4 W)이 Rev.B에서도 유지되는지, 버스트
   10초 동안 부스트 손실로 인한 국소 발열(약 1.2 W)이 방열 접촉면 요구
   (평탄도 ≤0.1 mm, 접촉률 ≥80%)에 영향을 주는지 명시.

산출물: examples/ksat3/deliverables/eps-to-str.md 갱신(입력:
examples/ksat3/deliverables/eps-em.md Rev.B).
검증: eps-em Rev.B 수치와 대조 확인
