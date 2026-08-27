# OBC 보드·저장부 열해석

입력: examples/ksat7/deliverables/OBC/obc-storage-design.md, examples/ksat7/deliverables/SE/sysreq.md

- 최대 발열: 연속 기록(1.2Gbps) 중 NAND 모듈 접합부 62°C, 프로세서 58°C.
- 등급 한계: 상용급 NAND 접합부 정격 -40~+85°C — 마진 23°C.
- TCS 배정 열부하 내 수용(TCS 배터리 5~25°C와 별개 유닛, OBC 자체 방열판
  전도경로로 위성판넬 방열).

검증: 최대접합온도 62°C ≤ 정격 85°C, 마진 23°C(27%) — 충족.
