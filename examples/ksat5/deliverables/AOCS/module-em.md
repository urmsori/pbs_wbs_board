# 자세제어(AOCS) EM 모듈 인도 문서
입력: examples/ksat5/deliverables/AOCS/pointing-budget.md,
      examples/ksat5/deliverables/AOCS/control-sw-design.md,
      examples/ksat5/deliverables/AOCS/sensor-mounting-design.md,
      examples/ksat5/deliverables/AOCS/module-test-report.md,
      examples/ksat5/deliverables/AOCS/icd-str-aocs-mass-footprint.md,
      examples/ksat5/deliverables/AOCS/icd-eps-aocs-power-profile.md

SE-01(M-AOCS)의 "자세제어 EM 모듈 인도" 요청에 대한 AOCS 팀의 인도물.

## 1. 구성
- 센서: 스타트래커 1식, MEMS 자이로 1식, 태양센서 2식
- 액추에이터: 리액션휠 3축, 마그네토토커 3축
- 온보드 SW: SAFE/DETUMBLE/NOMINAL/MOMENTUM-DUMP 4모드, EKF 자세결정 + PD 제어

## 2. 확정 인터페이스
- 구조(STR): 질량·발자국·체결 홀 패턴 확정(icd-str-aocs-mass-footprint.md),
  스타트래커·자이로 장착면 정렬·강성 STR 회신치로 확정(sensor-mounting-design.md,
  스타트래커 ≤0.015°/≥150 Hz, 자이로 ≤0.02°/≥120 Hz)
- 전력(EPS): 소비전력 프로파일 회신 및 시험 실측 완료(icd-eps-aocs-power-profile.md,
  module-test-report.md) — NOMINAL 평균 3.0 W, 첨두 8.8 W, 6.8~8.4 V 전 구간 동작 확인

## 3. 총질량
2.00 kg (SYS-REQ AOCS 배분 2.0 kg과 일치, pointing-budget.md)

## 4. 성능 확인
module-test-report.md 기능시험 결과: 종합 지향오차 0.47° (SYS-REQ 요구
≤0.5° 충족)

## 5. 인도 판정
질량·전력·지향정확도 요구를 모두 충족하고 구조·전력 인터페이스가
STR·EPS와 협상 완료되었으므로 EM 모듈 인도 가능.

검증: 하위 Work(AOCS-01~04) 전건 DONE, module-test-report.md의 종합
지향오차(0.47°)가 SYS-REQ(≤0.5°) 이내임을 확인.
