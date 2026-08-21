# AOCS 제어 알고리즘 및 온보드 SW 설계 (EM)
입력: examples/ksat5/deliverables/AOCS/pointing-budget.md

## 1. 모드 구성
- SAFE(태양센서 기반 감쇄+태양지향, coarse)
- DETUMBLE(마그네토토커 B-dot 감쇄)
- NOMINAL(스타트래커+자이로 융합 자세결정, 리액션휠 3축 지향 제어)
- MOMENTUM-DUMP(마그네토토커로 리액션휠 각운동량 주기적 덤핑)

## 2. 자세결정 알고리즘
- 확장 칼만필터(EKF): 스타트래커 쿼터니언 + 자이로 각속도 융합, 100 Hz 자이로 예측/1 Hz 스타트래커 보정
- 안전모드용 태양센서 coarse 자세결정(±5° 정확도) 별도 경로

## 3. 자세제어 알고리즘
- NOMINAL: 쿼터니언 오차 기반 PD 제어 → 리액션휠 3축 토크 지령
- 입력 pointing-budget.md의 제어오차 배분(0.30°)을 설계 목표로 사용
- 휠 각운동량 포화 감시 → 임계치 도달 시 MOMENTUM-DUMP 모드 자동 천이

## 4. 온보드 SW 구조
- 태스크: SENSOR_ACQ(자이로 100 Hz, 스타트래커 1 Hz) → EKF → MODE_MGR → CTRL_LAW → ACTUATOR_CMD
- 모드 전이표: SAFE↔DETUMBLE↔NOMINAL↔MOMENTUM-DUMP, 고장 감지 시 즉시 SAFE 복귀

## 5. 하위 Work로 넘기는 항목
- 본 SW 설계는 AOCS-04(통합·기능시험)의 입력이 된다.

검증: 모드 전이표 완결성(모든 상태에서 SAFE로의 경로 존재) 확인,
제어 목표(0.30°)가 pointing-budget.md 배분과 일치함을 확인.
