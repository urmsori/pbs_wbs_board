# SAR 촬영 시퀀서 프로세서 시뮬레이션 검증

입력: examples/ksat7/deliverables/FSW/unit-test-sequencer.md, examples/ksat7/deliverables/PAY/fsw-sequencer-reply.md, examples/ksat7/deliverables/PA/fsw-u2-witness.md

1궤도(약 95분) 시뮬레이션 시나리오: 18회 버스트 시도(각 5s, 간격 300s
이상)로 스케줄링. 결과: 18/18 버스트 정상 실행, 19번째 시도 시 횟수상한
거부 확인, 간격 300s 미만 조기 재시도 시 거부 확인, 누적 촬영시간
90.0s(=18×5s) 정확히 상한과 일치. PA 입회: PA-01, 이상 없음.

검증: 18/18 버스트 PASS, 횟수·간격·누적 3중 인터록 전부 정상 거부 동작
확인 — sysreq PAY 90s/궤도 제약 위반 없음.
