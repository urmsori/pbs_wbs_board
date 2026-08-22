# EPS → TCS 회신: 히터 채널 배전 확인
입력: examples/ksat6/deliverables/EPS/pcdu-design.md

TCS 히터 배분(배터리10W·추진탱크8W·광학부4W·마진3W, 합계 25W ≤ sysreq TCS
히터예산 25W)을 PCDU 3+1채널로 배전 가능함을 확인한다: 배터리 0.75A,
추진탱크 0.6A, 광학부 0.3A, 마진 0.3A(퓨즈 정격, 24V 기준). 회로 여유 있음
— PCDU 부하 표(EPS-01/EPS-02)에 이미 25W 히터 예산이 반영되어 있어 추가
증설 없이 수용 가능.

검증: PCDU 채널표로 TCS 4채널 배전 가능 확인, sysreq 히터예산 ≤25W 이내 확정.
