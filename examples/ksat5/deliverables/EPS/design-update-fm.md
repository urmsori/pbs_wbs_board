# EPS FM 설계 갱신 (EM 승계 리스크 반영)

입력: examples/ksat5/deliverables/EPS/power-conditioning.md,
examples/ksat5/deliverables/EPS/power-generation.md,
examples/ksat5/deliverables/EPS/battery-sizing.md,
examples/ksat5/deliverables/EPS/rail-budget.md

EM 설계(power-generation.md, power-conditioning.md, battery-sizing.md)를
FM 기준선으로 승계하고, RISK-RAIL 확정 결과(rail-budget.md)를 반영해
갱신한다.

## 1. EM에서 그대로 승계하는 항목 (변경 없음)
- 발생계: 몸체 2면+전개 날개 2매, EOL 궤도평균 ≈20.6W (power-generation.md)
- 레귤레이션 방식: S3R+BDR, 1차버스 8.4V(EOD 6.8V) (power-conditioning.md)
- 배터리: 2S1P 18650(3.4Ah), 팩 에너지 ≈25.8Wh (battery-sizing.md)
- 5V/3.3V 레일 구성 및 COMM PA의 액추에이터 레일 이설(rev.2 반영 상태 유지)

## 2. FM 갱신 항목 (rail-budget.md 반영)

| 항목 | EM (미확정) | FM (확정 갱신) |
|---|---|---|
| AOCS 분기 퓨즈 | 미지정 | **2.0 A, 표준 블로우** |
| COMM 분기 퓨즈 | 미지정("정격 미확정"으로 EM 인수 시 이월됨) | **1.25 A, 완속(slow-blow)** |
| PCU~분기점 공용 급전선/커넥터 | 개별 부하 기준 추정치(비확정) | **3.0 A 연속 정격 배선·커넥터 + 3.0A 완속 상위 퓨즈** |
| 회로도 | 액추에이터 레일 분기점에 퓨즈 심볼 없음 | 분기점에 AOCS/COMM 개별 퓨즈 + 상위 공용 퓨즈 3단 반영, 도면 개정 rev.B |

## 3. 운용 절차 반영 필요 항목 (설계 외, 인도문서에 명시)
rail-budget.md §3의 운용 제약(AOS guard band 10s→15s 상향, 비필수
슬루의 교신 시간대 스케줄링 금지, FM 초기 궤도 운용 중 레일 전류
텔레메트리 모니터링)은 EPS 설계 변경 사항이 아니라 AOCS/AIT 운용
절차에 반영되어야 하는 항목이다 — 이 문서에서는 FM 인도 시 AIT에
전달할 인터페이스 노트로 명시해 둔다(EPS 단독으로 종결할 수 없음을
정직하게 밝힘).

## 4. 질량·전력 영향
퓨즈·상위 정격 배선 추가로 인한 질량 증가는 무시할 수준(<5g, 커넥터
핀 추가 없음, 기존 하니스 경로 내 인라인 퓨즈만 추가) — module-fm.md
질량 예산은 EM 확정치(1.27kg)를 그대로 유지한다. 전력 수지 변경 없음.

검증: rail-budget.md의 퓨즈 정격(2.0A/1.25A/3.0A)이 회로도·부품 리스트에 3단 반영되었음을 설계 검토로 확인, EM 대비 발생/버스/배터리 수치 변경 없음(승계) 확인.
