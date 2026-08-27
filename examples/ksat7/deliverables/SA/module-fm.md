# 태양전지판(SA) 비행모델 인도 — module-fm

입력: examples/ksat7/deliverables/SE/sysreq.md, SA-U1(3윙 패널) 전체 체인,
REQ-SA-MECH(발신) 및 REQ-MECH-SA(수신) 회신

## 구성
SA-U1: 전개형 3윙 패널 — 설계 축약 체인(DSN→ANL-S→CHK→RB→CM) + 제작 체인
(PUR→IQC→MFG→CLN→INS) + 플래시시험(CAL→TST).

## sysreq 판정 (examples/ksat7/deliverables/SE/sysreq.md 「SA」 행 인용)
"EOL 900W, 전개 후 1차모드 ≥0.5Hz."

| 항목 | 요구 | 실측/해석 | 결과 |
|---|---|---|---|
| EOL 출력 | 900W | 플래시시험 기반 EOL 예측 920W (SA-U1-TST) | 충족(마진2.2%) |
| 전개 후 1차모드 | ≥0.5Hz | 0.58Hz (SA-U1-ANL-S, MECH 확정 힌지강성 8000N·m/rad 반영) | 충족(마진16%) |

## ICD 협상 결과 요약
- REQ-SA-MECH(발신) / REQ-MECH-SA(수신): 힌지쌍 회전강성 8000 N·m/rad,
  백래시≤0.05°, 힌지 볼트패턴(4점 M6, PCD80mm) 상호 확정. 패널측 질량
  7.6kg/윙·관성10.1kg·m² 회신 완료 — 양방향 수치 일치, 잠정 가정 리스크 해소.

## 잠정/인계 사항
- 1차모드 0.58Hz는 해석치(SA-U1-ANL-S)이며, 실측 진동시험은 AIT
  통합시험(INT.md) 단계로 인계한다.

검증: sysreq SA 2항목(EOL900W·1차모드≥0.5Hz) 실측·해석 기반 충족(920W/0.58Hz), ICD 확정, 진동실측은 AIT 인계
