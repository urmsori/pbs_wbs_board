# 히터 채널 배전 확정 (REQ-TCS-EPS)

입력: examples/ksat7/board/REQ-TCS-EPS.md, examples/ksat7/deliverables/EPS/pcdu-pulse-design.md

TCS 히터 총 예산 ≤40W(sysreq)를 PCDU 배전 3채널(배터리/추진배관/구조부)로
수용 가능함을 확인.
- 채널 스위치 정격: 각 2A@50V(=100W 여유), 40W 총합 대비 충분한 마진.
- 채널별 차단기: 3A 퓨즈(배터리 히터 15W 기준 정상전류 0.3A 대비 마진 10배 이상).

판정: **가능**. 히터 채널 배전 회로 여유 확인, 추가 설계 변경 불필요.

검증: 40W 이내 3채널 배분이 배전회로(채널정격100W/차단기3A) 여유로 수용 가능함을 확인
