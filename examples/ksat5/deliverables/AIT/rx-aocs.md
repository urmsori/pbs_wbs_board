# AOCS EM 모듈 인수 시험 결과
입력: examples/ksat5/deliverables/AOCS/module-em.md,
      examples/ksat5/deliverables/SUPPORT/need-sw-aocs.md,
      examples/ksat5/deliverables/SUPPORT/need-har-aocs.md

AIT-RX-AOCS(AIT-TST)의 AOCS EM 모듈 인수 시험 기록. NEED-SW-AOCS(EGSE
SW)와 NEED-HAR-AOCS(시험 하니스)가 산출한 도구로 module-em.md 인도
내용을 독립 재현·확인한다.

## 1. 시험 구성
- 하니스: need-har-aocs.md의 10채널 하니스로 EM 모듈을 EGSE 브레이크
  아웃 박스에 연결(–Z 트렁크 4채널 합류 + 축별 개별 6채널).
- SW: need-sw-aocs.md의 mode_trigger.py, stim_startracker.py,
  stim_gyro.py, stim_sunsensor.py, tlm_logger.py, pointing_error_calc.py
  5종 스크립트 사용.

## 2. 시험 시나리오 및 결과
| 시나리오 | 판정 기준 | 결과 |
|---|---|---|
| DETUMBLE→NOMINAL 자동 천이(각속도 감쇄 후) | 천이표대로 자동 전이 | 통과 |
| NOMINAL 자세결정·제어(스타트래커 1Hz+자이로 100Hz 융합) | EKF 융합 후 리액션휠 3축 PD 응답 | 통과 |
| 리액션휠 각운동량 포화→MOMENTUM-DUMP 자동 천이 | 마그네토토커 3축 덤핑 지령 발생 | 통과 |
| SAFE 강제 천이(고장 주입, 태양센서 coarse ±5°) | 감쇄+태양지향 확인 | 통과 |
| 종합 지향오차 재현 | ≤0.5° | 0.47° (module-em.md 실측치와 일치) |

## 3. 판정
모드 전이표(SAFE/DETUMBLE/NOMINAL/MOMENTUM-DUMP) 전 경로 정상 동작,
종합 지향오차 0.47°로 SYS-REQ(≤0.5°) 및 module-em.md 인도 수치와
일치. AOCS EM 모듈 인수 **합격**.

검증: 위 5개 시나리오 전건 통과, 지향오차 재현치(0.47°)가 module-em.md
인도치(0.47°)와 일치함을 확인.
