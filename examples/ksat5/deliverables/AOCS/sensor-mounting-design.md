# AOCS 센서 장착 설계 (구조 인터페이스 포함) — EM
입력: examples/ksat5/deliverables/AOCS/pointing-budget.md,
      examples/ksat5/deliverables/AOCS/icd-str-aocs-mass-footprint.md,
      examples/ksat5/deliverables/STR/icd-aocs-str.md

## 1. STR 협의 결과 반영
ICD-AOCS-STR 회신(STR-DSN)에 따라 스타트래커·자이로 장착면 사양을 확정한다.

| 센서 | 정렬 공차(요청 → 회신) | 1차 고유진동수(요청 → 회신) |
|---|---|---|
| 스타트래커 | ≤0.02° → **≤0.015°** | ≥120 Hz → **≥150 Hz** |
| 자이로 | ≤0.02° → 0.02° (동일) | ≥120 Hz → 120 Hz (동일) |

STR 회신치가 AOCS-01의 지향오차 배분 중 "정렬/열변형 여유(0.35°)" 항목의
전제(정렬 공차 ≤0.02°)를 스타트래커 기준 초과 충족하므로, 별도 여유
재계산 없이 pointing-budget.md 배분을 그대로 유지한다.

## 2. 장착 설계 확정
- 스타트래커: –Y 패널, STR 회신 정렬 공차(≤0.015°) 도면 반영, 인접 레일
  15 mm 이내 브래킷(Al 7075-T6, 두께 3.5 mm, M3 4점 체결 — STR 회신 기준)
- 자이로: 스타트래커 인접 배치, 자체 M2.5×4 체결(icd-str-aocs-mass-footprint.md
  홀 패턴 기준), 정렬 0.02°/강성 120 Hz(STR 회신) 그대로 사용
- 질량·외형·체결 홀 패턴·인출면: icd-str-aocs-mass-footprint.md 값을 그대로 채용

## 3. 하위 Work로 넘기는 항목
- 본 장착 설계 확정치는 AOCS-04(통합·기능시험)의 입력이 된다.

검증: STR 회신(정렬≤0.015°/150 Hz)이 AOCS 요청(≤0.02°/120 Hz)을 모두
초과 충족함을 확인, pointing-budget.md 지향오차 배분(0.49°≤0.5°) 재검토
불필요함을 확인.
