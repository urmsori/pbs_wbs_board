# 비행SW 코어 프로세서 시뮬레이션 검증

입력: examples/ksat7/deliverables/FSW/unit-test-core.md, examples/ksat7/deliverables/OBC/obc-storage-design.md, examples/ksat7/deliverables/PA/fsw-u1-witness.md

OBC 프로세서 시뮬레이터(200MIPS 모델) 상에서 코어 SW 24시간 연속 구동.
- CPU 부하: 평균 46MIPS, 최대 96MIPS(AOCS 10Hz 제어 루프 포함) — 처리여유
  (200-96)/200=52%, OBC-U1-DSN-REV 설계치와 일치 확인.
- 안전모드 3조건 트리거 재현: 3/3 PASS(시뮬레이션 환경).
- 요 스티어링 10Hz 루프 지터: 최대 0.3ms(주기 100ms 대비 0.3%) — 안정.
- PA 입회: PA-01, 이상 없음(examples/ksat7/deliverables/PA/fsw-u1-witness.md).

검증: 처리여유 52%≥50%(OBC sysreq 충족 재확인), 안전모드 3/3 PASS, 10Hz
루프 지터 0.3% — PASS.
