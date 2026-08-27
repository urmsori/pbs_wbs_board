# 비행SW 코어 설계(스케줄러·안전모드·TM/TC·요 스티어링 인터페이스)

입력: examples/ksat7/deliverables/SE/sysreq.md

## 구성
- 태스크 스케줄러: 고정우선순위 RTOS 태스크 12개, 주기 10/50/100/1000ms 4계층.
- 안전모드: 자세이탈(>1°)·전력저전압(<47V)·통신두절(72h) 3조건 자동 트리거,
  태양지향 세이프홀드로 천이, 지상명령으로만 정상모드 복귀.
- TM/TC: CCSDS 패킷, 1553B 상 1Hz HK 텔레메트리, 명령 검증(2단계 확인) 처리.
- 요 스티어링 제어 인터페이스(확정, AOCS 실회신 반영): 제어주기 10Hz.
  신호 5종 — YAW_STEER_CMD(FSW→AOCS, float32, 10Hz, deg),
  ATT_FB(AOCS→FSW, 쿼터니언 float32×4, 10Hz), RATE_FB(AOCS→FSW,
  float32×3, 10Hz, deg/s), RWA_TORQUE_CMD(AOCS→FSW 모니터, float32×4,
  10Hz, N·m), MODE_STATUS(AOCS→FSW, enum, 1Hz) — sysreq 요 스티어링
  ±4°, 안정도 0.003°/s 관리 루프의 상위 SW 로직.

## sysreq FSW 항목 판정(코어 관할분)
| 항목 | 요구 | 확인 | 판정 |
|---|---|---|---|
| 비행 관리 전 기능 | 스케줄러·TM/TC | 12태스크·CCSDS 패킷 구현 | 충족 |
| 안전모드 | 필수 | 3조건 자동 트리거 세이프홀드 구현 | 충족 |

## 정정 이력(FSW-U1-DSN-REV, REQ-FSW-AOCS 실회신 반영)
- 제어주기: 20Hz(잠정) → 10Hz(확정, AOCS 실회신 — 폐루프 대역폭 0.79Hz의
  12.7배 여유로 sysreq 안정도 0.003°/s 배분과 정합 확인됨).
- 신호 목록: 미정 → 5종 확정(위 표).
- 근거: examples/ksat7/deliverables/AOCS/fsw-interface-reply.md

검증: 스케줄러·안전모드·TM/TC 구현 확인(sysreq FSW 비행관리+안전모드 요구
충족), AOCS 제어주기 10Hz·신호 5종 확정 반영 완료(잠정 사항 해소).
