# 슬루 첨두 시간 프로파일 확인 (REQ-RAIL-AOCS 회신)
입력: examples/ksat5/deliverables/AOCS/icd-eps-aocs-power-profile.md,
      examples/ksat5/deliverables/AOCS/module-test-report.md

RISK-RAIL(EPS-DSN 주관, 액추에이터 레일 3자 동시부하 예산)의 요청에 대한
AOCS 팀 회신. 궤도주기 90분(5400 s, LEO 6U 기준) 가정.

## 1. 슬루 첨두(1.34A, EOD) 발생 빈도·지속시간
| 항목 | 값 |
|---|---|
| 궤도당 슬루 이벤트 수 | 평시 4회, 최대(운용 밀집일) 6회 |
| 1회당 첨두 지속시간 | 통상 20 s, 최대 60 s(module-test-report.md 슬루 시험 기준) |
| 궤도당 첨두 누적시간(최악) | 6 × 60 s = 360 s |
| 듀티비(최악) | 360 s / 5400 s ≈ 6.7% |
| 듀티비(통상) | 4 × 20 s / 5400 s ≈ 1.5% |

## 2. 지상국 교신 시간대와의 겹침 여부
- **NOMINAL 교신 중**: 안테나(고정 패치)를 지상국 지향으로 유지하는
  것은 고정 자세 유지이며, 이때 리액션휠은 NOMINAL 유지 부하
  (icd-eps-aocs-power-profile.md 평균 0.5W/축)만 필요 — **슬루 첨두
  1.34A는 교신 중 발생하지 않는다(설계상 배제).**
- **교신 직전 확보(acquisition) 슬루**: 교신 자세로 전환하는 슬루가
  AOS(신호 획득) 직전 1회 필요. AOCS는 이 슬루를 AOS 예정시각보다
  **≥10 s 여유(guard band)** 를 두고 완료·정착하도록 스케줄링한다 —
  정상 운용에서는 슬루 첨두와 COMM 송신 첨두가 겹치지 않는다.
- **최악 조건(스케줄 지터)**: 온보드 스케줄링 지터로 guard band가
  잠식되는 경우, 슬루 종료~정착 구간과 AOS 직후 COMM 송신 시작이
  **최대 5 s** 겹칠 수 있다 — 이 구간에서만 AOCS 1.34A + COMM 0.74A
  동시부하(≈2.08A, EOD)가 발생 가능(RISK-RAIL이 지목한 최악 조건과 일치).

## 3. RISK-RAIL 입력 요약
- 동시 최악 부하 ≈2.08A는 궤도당 최대 5 s로 제한되는 드문 조건(스케줄
  지터 겹침)이며, 상시·정상 조건은 아니다.
- 분기 퓨즈/차단기 정격은 이 5 s 최악 조건을 기준으로 EPS가 정할 것.

검증: 궤도당 첨두 누적시간(최악 360 s, 통상 80 s)이 module-test-report.md
슬루 시험 지속시간(≤60 s/회) 및 icd-eps-aocs-power-profile.md 첨두치와
정합함을 확인.
