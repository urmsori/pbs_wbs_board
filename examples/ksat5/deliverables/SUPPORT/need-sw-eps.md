# EPS EM 모듈 인수 시험용 EGSE SW(레일 텔레메트리·부하스텝)
입력: examples/ksat5/deliverables/EPS/power-conditioning.md,
      examples/ksat5/deliverables/EPS/test-plan.md,
      examples/ksat5/deliverables/COMM/icd-eps-comm-power.md

NEED-SW-EPS(AIT-TST) 요청에 대한 시험 SW 담당 인도물. power-
conditioning.md §버스구조(4레일)와 test-plan.md §3·§4, icd-eps-comm-
power.md 액추에이터 레일 펄스 요청을 반영한 EGSE 스크립트 세트.

## 스크립트 목록
- `rail_tlm_logger.py` — 1차버스 8.4V(EOD 6.8V)/5V±2%/3.3V±2%/
  액추에이터 레일 8.4V 4레일 동시 전압·리플(≤50mVpp) 텔레메트리 로깅
- `load_step_5v3v3.py` — 5V/3.3V 레일 0→정격80% 부하 스텝 인가, sag/
  overshoot ≤5%·복구시간 ≤1ms 판정(test-plan.md §3)
- `load_step_actuator_comm_pulse.py` — COMM 송신 펄스 프로파일(1.6A→
  2.0A, <5ms 엣지) 재현 부하스텝 파형 생성기, 액추에이터 레일 sag
  측정(icd-eps-comm-power.md 액추에이터 레일 요청 반영)
- `protection_trip_check.py` — 모의 배터리 전압 인가로 UVLO 3.0V/cell,
  OVP 4.2V/cell 트립점 확인, 트립점 ±5% 판정(test-plan.md §4)
- `eod_hold_check.py` — 배터리 방전 말기 6.8V 조건에서 액추에이터
  레일 전압 하한 재현, 4레일 유지 여부 판정(module-em.md §3 EOD 리스크)

## 시험 시나리오
1. 4레일 정상 공급 상태에서 rail_tlm_logger.py로 기준 전압·리플 확보
2. load_step_5v3v3.py로 5V/3.3V 순차 부하 스텝 → sag/overshoot/복구시간
   판정
3. load_step_actuator_comm_pulse.py로 COMM 송신 펄스(1.6A→2.0A, <5ms)
   프로파일 인가 → 액추에이터 레일 sag를 rail_tlm_logger.py와 동시
   기록
4. protection_trip_check.py로 UVLO/OVP 트립점 확인
5. 배터리 시뮬레이터 전압을 6.8V(EOD)까지 낮춰 eod_hold_check.py로
   4레일 유지 및 액추에이터 레일 하한 재확인

검증: NEED-SW-EPS 요청의 4레일 텔레메트리 로거, 부하스텝 파형 생성기
(COMM 펄스 프로파일 포함), 보호회로 트립점 판정기 3항목이 스크립트
목록에 모두 대응됨을 확인. power-conditioning.md 레일 사양·test-plan.md
판정 기준·icd-eps-comm-power.md 펄스 파형과 일치함을 확인.
