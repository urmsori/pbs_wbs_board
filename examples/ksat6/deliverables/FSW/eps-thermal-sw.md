# FSW 전력·열 관리 SW 설계

입력: examples/ksat6/deliverables/SE/sysreq.md, examples/ksat6/deliverables/FSW/architecture.md, examples/ksat6/deliverables/EPS/battery-mgmt-params-for-fsw.md

## 배터리 관리 로직(EPS 회신 반영, REQ-FSW-EPS)
| 파라미터 | 값 | 동작 |
|---|---|---|
| 충전 종지 | 33.6V, 테이퍼 컷오프 0.05C | 정전압 충전 종료 |
| 저전압 로드셰딩 1단계 | 27.2V | 비필수 부하(탑재체 등) 차단 |
| 저전압 안전모드 임계 | 26.4V | TASK_SAFEMODE_MON이 안전모드 트리거 |
| 과온 충전금지 | 32°C(재개 28°C) | 배터리 온도 센서로 충전 인터록 |
| 저온 충전금지 | 0°C 미만 | 히터 선행 가동 후 충전 재개 |

## 히터 제어 로직
- sysreq TCS 히터 예산 ≤25W 준수: PID 기반 온스탠바이 제어, 우선순위
  배터리>추진계>구조부. 배터리 0~30°C 유지.

## 검증 케이스(총 5건)
1. 33.6V 도달 시 충전 종지(테이퍼 확인)
2. 27.2V 하강 시 로드셰딩 1단계 실행
3. 26.4V 하강 시 안전모드 트리거
4. 32°C 초과 시 충전 금지, 28°C 재개
5. 히터 총 소비전력 ≤25W 유지(다중 히터 동시 구동 시나리오)

검증: EPS 회신 임계값표를 배터리 관리 로직에 1:1 반영 확인, sysreq DoD≤25%·히터≤25W 판정.
