# PCU·배전유닛 열해석

입력: examples/ksat8/deliverables/EPS/pcu-distribution-design.md

15kW 배전 정상상태(주버스 150A) 및 S3R 션트 최대 소산 조건에서 PCU
내부 소자 온도를 해석.

## 결과
- S3R 션트 소자(최대 션트 조건, EOL 초과잉여 전력 소산 시) 국부 온도
  피크: +72°C(허용 +85°C 이내, 여유 13°C).
- LCL 카드(정상 부하) 정상상태 온도: +48°C(허용 +70°C 이내).
- TCS 방열 인터페이스: PCU 판넬 전도 방열, TCS 히터 예산(200W, 6채널)과
  별개 — PCU 자체 발열은 구조 패널 전도로 방열(TCS 협의 완료,
  eps-heater-budget.md 참조).

검증: S3R소자 +72°C(여유13°C), LCL카드 +48°C(허용내), TCS 방열 인터페이스 정합
