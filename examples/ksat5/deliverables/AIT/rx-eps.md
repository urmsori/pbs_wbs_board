# EPS EM 모듈 인수 시험 결과
입력: examples/ksat5/deliverables/EPS/module-em.md,
      examples/ksat5/deliverables/COMM/icd-eps-comm-power.md,
      examples/ksat5/deliverables/COMM/bus-voltage-check.md,
      examples/ksat5/deliverables/SUPPORT/need-sw-eps.md,
      examples/ksat5/deliverables/SUPPORT/need-har-eps.md

AIT-RX-EPS(AIT-TST)의 EPS EM 모듈 인수 시험 기록. NEED-SW-EPS(EGSE
SW)와 NEED-HAR-EPS(시험 하니스)로 module-em.md 4레일 구성과 미해결
EOD 리스크를 독립 재현·확인한다.

## 1. 시험 구성
- 하니스: need-har-eps.md 채널 1(PCU 34핀 백플레인, 레일별 브레이크
  아웃) + 채널 2(배터리 대신 EGSE 가변전원 6.8~8.4V) + 채널 3(서미스터 모의).
- SW: need-sw-eps.md의 rail_tlm_logger.py, load_step_5v3v3.py,
  load_step_actuator_comm_pulse.py, protection_trip_check.py,
  eod_hold_check.py 5종.

## 2. 시험 중 발견 사항 및 정정 (정직 공개)
NEED-SW-EPS 요청 시 AIT-TST가 액추에이터 레일 부하스텝 프로파일을
"COMM 송신 펄스 1.6A→2.0A"로 잘못 인용했다 — 이 수치는 PA가 5V 레일에
있던 rev.1(구형) 설계의 값으로, icd-eps-comm-power.md와 COMM의
bus-voltage-check.md §3이 확인한 rev.2(PA 액추에이터 레일 이설 후)
실제 값은 **0.60A(8.4V 공칭) / 0.74A(EOD 6.8V)**다. 원인은 AIT-TST의
자기 인용 오류이므로 내부에서 바로잡는다: load_step_actuator_comm_pulse.py
파형을 0→0.60A(공칭)/0→0.74A(EOD) 스텝으로 정정해 재시험했다.

## 3. 시험 결과
| 항목 | 판정 기준 | 결과 |
|---|---|---|
| 4레일 정상 전압·리플 | 각 ±2%, 리플 ≤50mVpp | 전 레일 충족 |
| 5V/3.3V 부하 스텝(0→정격80%) | sag/overshoot ≤5%, 복구 ≤1ms | 충족(sag 2.1%/3.4%, 복구 0.6ms) |
| 액추에이터 레일 부하 스텝(정정 후 0→0.60/0.74A) | 레일 유지 | 정상 유지, sag 무시 가능 수준(정정 전 1.6~2.0A 가정 대비 부하가 훨씬 작아 여유 큼) |
| 보호회로(UVLO 3.0V/cell, OVP 4.2V/cell) | 트립점 ±5% | 충족 |
| EOD 6.8V 유지(4레일) | 전 레일 정상 범위 | 충족 — 액추에이터 레일 6.8V에서도 0.74A 부하로 정상 |

## 4. 판정
4레일 텔레메트리·부하스텝·보호회로·EOD 유지 전 항목 통과. 시험 중
발견한 AIT 자체의 부하 프로파일 인용 오류는 정정 후 재시험으로 해소.
EPS EM 모듈 인수 **합격**.

검증: 5개 시험 항목 전건 통과, 부하 프로파일 오류를 icd-eps-comm-
power.md·bus-voltage-check.md 실측치로 정정 후 재확인.
