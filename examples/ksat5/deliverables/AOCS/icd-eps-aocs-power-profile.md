# AOCS 구동기 소비 전력 프로파일 (ICD-EPS-AOCS 회신)
입력: examples/ksat5/deliverables/AOCS/pointing-budget.md,
      examples/ksat5/deliverables/AOCS/control-sw-design.md

EPS-03(배터리 방전심도·첨두부하 산정)의 요청에 대한 AOCS 팀 회신.
sysreq의 지향정확도 ≤0.5° 요구를 만족하는 구동기 구성(리액션휠 3축 +
마그네토토커 3축, pointing-budget.md 선정)을 기준으로 작성한다.

## 모드별 소비 전력

| 모드 | 구성품 | 평균 소비전력 | 지속시간 |
|---|---|---|---|
| NOMINAL(정상 지향 유지) | 리액션휠 3축 (미소 토크 유지) | 1.5 W (3×0.5 W) | 상시 |
| NOMINAL | 스타트래커+자이로(EKF 상시 구동) | 1.6 W (1.2+0.4) | 상시 |
| NOMINAL | 태양센서(대기) | 0.1 W | 상시 |
| **NOMINAL 평균 합계** | | **≈ 3.2 W** | 상시 |
| SLUE/기동(첨두) | 리액션휠 3축 (최대 토크) | 7.5 W (3×2.5 W) | 최대 60 s/회 |
| DETUMBLE/MOMENTUM-DUMP(첨두) | 마그네토토커 3축 | 3.0 W (3×1.0 W) | 최대 300 s/회(궤도당 1~2회) |
| **첨두(슬루+휠 동시 최대)** | | **≈ 9.1 W** | 슬루 지속시간 내 |

## 구동기 버스 레일 동작 전압 범위
- 공칭: 8.4 V (버스 직결 액추에이터 레일)
- 방전 말기(EOD) 하한: 6.8 V
- 리액션휠·마그네토토커 드라이버는 6.8~8.4 V 전 구간에서 정격 토크 출력 유지(설계 여유 포함)로 확인됨 —
  EOD 조건에서도 NOMINAL 모드 지향 유지(제어오차 배분 0.30°, control-sw-design.md)에 지장 없음.

검증: NOMINAL 평균(3.2 W)·첨두(9.1 W) 산정치가 pointing-budget.md 질량/구성 선정과
정합함을 확인, 6.8~8.4 V 전 구간 동작 가능 확인.
