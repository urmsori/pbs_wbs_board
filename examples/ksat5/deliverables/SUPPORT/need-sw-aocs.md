# AOCS EM 모듈 인수 시험용 EGSE SW
입력: examples/ksat5/deliverables/AOCS/module-em.md,
      examples/ksat5/deliverables/AOCS/control-sw-design.md

NEED-SW-AOCS(AIT-TST) 요청에 대한 시험 SW 담당 인도물. control-sw-design.md
§1~4 온보드 SW 설계를 반영한 EGSE 스크립트 세트.

## 스크립트 목록
- `mode_trigger.py` — SAFE/DETUMBLE/NOMINAL/MOMENTUM-DUMP 4모드 전이표
  (§4)를 순회 트리거하고 각 상태에서 SAFE 복귀 경로를 검증
- `stim_startracker.py` — 쿼터니언 입력 시뮬레이터, 1 Hz (§2 EKF 보정 입력)
- `stim_gyro.py` — 각속도 입력 시뮬레이터, 100 Hz (§2 EKF 예측 입력)
- `stim_sunsensor.py` — 태양센서 2식 coarse 자세 자극(±5° 정확도 경로),
  SAFE 모드 전용 (§2)
- `tlm_logger.py` — 리액션휠 3축 토크 지령/각운동량, 마그네토토커 3축
  지령 텔레메트리 수신·파싱, MOMENTUM-DUMP 천이 조건(휠 각운동량 포화
  임계치) 도달 시점 로깅 (§3~4)
- `pointing_error_calc.py` — 종합 지향오차 산출, module-em.md §4 실측치
  0.47°(SYS-REQ ≤0.5°) 재현 확인용

## 자극 시나리오
1. DETUMBLE 진입 → 자이로 자극으로 각속도 감쇄 확인 → B-dot 감쇄 완료 시
   NOMINAL 자동 천이 트리거
2. NOMINAL 진입 → 스타트래커(1 Hz) + 자이로(100 Hz) 동시 자극 → EKF 융합
   자세결정 → 리액션휠 3축 PD 제어 응답을 tlm_logger.py로 수신
3. 리액션휠 각운동량 포화 시뮬레이션 → MOMENTUM-DUMP 자동 천이 확인 →
   마그네토토커 3축 덤핑 지령 로깅
4. SAFE 강제 천이(고장 주입) → 태양센서 coarse 경로(±5°) 자극으로 감쇄+
   태양지향 확인
5. 전 시나리오에서 pointing_error_calc.py로 종합 지향오차 산출 → 0.5°
   이내 재현 확인

검증: NEED-SW-AOCS가 요구한 4모드 트리거/센서 자극 시뮬레이터(스타트래커
1 Hz·자이로 100 Hz·태양센서 coarse)/텔레메트리 로거·파서/지향오차
산출기 4항목이 스크립트 목록에 모두 대응됨을 확인. control-sw-design.md
§1~4와 자극 대상·주기가 일치함을 확인.
