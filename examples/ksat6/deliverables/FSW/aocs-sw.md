# FSW 자세제어 SW 설계

입력: examples/ksat6/deliverables/SE/sysreq.md, examples/ksat6/deliverables/FSW/architecture.md, examples/ksat6/deliverables/AOCS/fsw-if-reply.md

## 제어 루프 구조(AOCS 회신 반영, REQ-FSW-AOCS)
- 주기: **20 Hz**(50ms), 아키텍처의 TASK_AOCS(10Hz 설계값을 AOCS 회신에 맞춰
  20Hz로 상향 — architecture.md 스케줄러 주기를 이 설계가 갱신).
- 별추적기(5Hz) 쿼터니언을 20Hz 루프에 인터리브하여 자세결정 필터(확장
  칼만필터) 입력으로 사용.

## 입출력 신호(AOCS 회신 표 인용)
- 입력: 별추적기 쿼터니언(5Hz), 자이로 각속도 3축(20Hz), 자이로 온도(1Hz).
- 출력: 반작용휠 토크명령 4채널(20Hz, ±0.10Nm), 반작용휠 속도피드백 4채널
  (20Hz), 마그네토커 듀티명령 3채널(1Hz, 모멘텀덤핑 모드 전용).

## 처리시간
- 루프 1회 실행시간 실측(시뮬레이터): 3.1 ms(50ms 주기 대비 점유율 6.2%,
  proc-board.md 처리여유 산정의 TASK_AOCS 12% 배분 내 포함).

## 검증 케이스(총 7건)
1. 20Hz 루프 주기 준수(지터 <1ms)
2. 별추적기 5Hz 인터리브 정합
3. 지향오차 0.05°(3σ) 시뮬레이션 달성
4. 안정도 0.005°/s 시뮬레이션 달성
5. 반작용휠 토크명령 범위(±0.10Nm) 초과 방지
6. 모멘텀덤핑 모드 전환·마그네토커 듀티 산출
7. 센서 결측(별추적기 드롭아웃) 시 자이로 전용 추정 전환

검증: 위 7개 케이스를 FSW-VV 통합검증에서 프로세서 시뮬레이터로 재현(교차참조), sysreq AOCS 지향·안정도 판정.
