---
id: ICD-AOCS-STR
title: AOCS 센서 장착면 정렬·강성 ICD (AOCS↔STR)
status: DONE
parent: AOCS-03
owner: STR-DSN
deliverable: examples/ksat5/deliverables/STR/icd-aocs-str.md
after: -
track: STR
started: 2026-08-21 07:04:53
finished: 2026-08-21 07:05:19
---

AOCS-DSN의 필요: 스타트래커·자이로 등 AOCS 센서 장착면에 대해
(1) 광축 대 위성 기준좌표축 정렬 공차,
(2) 장착부 국부 1차 고유진동수(강성) 요구
를 구조팀(STR)과 협상해 정한다. AOCS가 원하는 목표값(정렬 ≤ 0.02°,
1차 고유진동수 ≥ 120 Hz — 스타트래커 지터 요구 기반 초안)을 제시하니,
STR이 구조 설계 관점에서 실현 가능한 값으로 회신하고 합의된 값을
ICD 파일로 남겨 달라. AOCS-03은 이 결과가 있어야 완료할 수 있다.
산출물: (당사자 협상 결과, STR팀이 채움) 예) examples/ksat5/deliverables/ICD/AOCS-STR.md
검증: 스타트래커 요구(0.02도,120Hz) 대비 회신치(0.015도,150Hz) 초과 충족 확인
