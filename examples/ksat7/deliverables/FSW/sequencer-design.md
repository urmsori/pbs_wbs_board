# SAR 촬영 시퀀서 SW 설계

입력: examples/ksat7/deliverables/SE/sysreq.md, examples/ksat7/deliverables/FSW/core-design.md

## 명령셋(확정 — PAY 실회신 반영)
| 명령 | 기능 | 파라미터(확정치) |
|---|---|---|
| SAR_MODE_SET | 스트립맵/스팟 모드 전환 | 모드ID, 전환시간 2.5s |
| SAR_PULSE_ARM | 펄스 시퀀스 준비 | PRF 3,000Hz, 펄스폭 스트립맵20µs/스팟6.7µs |
| SAR_ANT_POINT | 안테나 지향 큐 등록 | 방위각/앙각, 큐잉시각 |
| SAR_ACQ_START/STOP | 촬영 시작/종료 | 버스트 최대 5s |
| SAR_DATA_TAG | 원시데이터 태깅 | 궤도번호, 모드, 타임스탬프 |

## 첨두부하 인터록 로직(정정 — PAY 실회신 반영)
잠정판은 "90s 누적시 자동정지"라는 단순 카운터였으나, PAY 실회신
(examples/ksat7/deliverables/PAY/fsw-sequencer-reply.md)의 세 겹 제약을
모두 반영하도록 정정한다:
1. 버스트 길이 상한: SAR_ACQ_START 후 5s 경과 시 자동 SAR_ACQ_STOP.
2. 궤도당 버스트 횟수 상한: 18회 도달 시 이후 SAR_ACQ_START 명령 거부
   (지상 오버라이드 없이는 재개 불가).
3. 버스트 간 최소 간격: 직전 SAR_ACQ_STOP 후 300s 미경과 시 SAR_ACQ_START
   거부(열 완화 대기, TCS 열관리 근거).
4. 누적 90s 상한: 위 1~3을 만족해도 궤도 누적 촬영시간이 90s(=18회×5s)를
   넘지 않도록 이중 확인.

## sysreq FSW 항목 판정(시퀀서 관할분)
| 항목 | 요구 | 확인 | 판정 |
|---|---|---|---|
| SAR 촬영 시퀀서 | 필수 | 명령셋 5종·4중 인터록 구현 | 충족 |

## 정정 이력(FSW-U2-DSN-REV, REQ-FSW-PAY 실회신 반영)
- 명령 파라미터: placeholder → 위 표의 확정 수치.
- 인터록: 단순 90s 누적 카운터 → 버스트상한(5s)·횟수상한(18회)·최소간격
  (300s)·누적상한(90s) 4중 로직.
- 근거: examples/ksat7/deliverables/PAY/fsw-sequencer-reply.md

검증: 명령셋 5종 확정치 반영, 4중 인터록 로직이 PAY 회신의 버스트5s×18회
(누적90s)·최소간격300s 제약을 전부 커버 — sysreq PAY 펄스 1.8kW/90s 제약
정합 확인(잠정 사항 해소).
