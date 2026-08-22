# 히터·서미스터 세트 사양
입력: examples/ksat6/deliverables/TCS/thermal-analysis.md

## 히터 채널 (예산 ≤25W, sysreq TCS 행)
| 채널 | 용도 | 정격전력 | 서모스탯 설정 | 상태 |
|---|---|---|---|---|
| H1 | 배터리 팩 | 10 W | ON -2°C / OFF +2°C | EPS 배전 확인 완료(REQ-TCS-EPS, 0.75A) |
| H2 | 추진 탱크·배관 트레이스 | 8 W | ON +5°C / OFF +10°C | EPS 배전 확인 완료(REQ-TCS-EPS, 0.6A) |
| H3 | 광학부 구조·배플 | 4 W | ON -15°C / OFF -10°C | EPS 배전 확인 완료(REQ-TCS-EPS, 0.3A) |
| 마진 | 예비 | 3 W | - | 미배선 예비 채널 |
| **합계** | | **25 W** | | **sysreq ≤25W 이내** |

## 서미스터 배치
- 유닛당 최소 2점(제어용 1 + 텔레메트리 감시용 1): 배터리팩 2점, 추진탱크 2점,
  광학부 3점(구배 감시 위해 벤치 양단+중앙), 구조패널 대표점 4점 = 총 11점.

## EPS 확인 반영
입력: examples/ksat6/deliverables/EPS/heater-channel-confirmation.md
EPS가 REQ-TCS-EPS 회신으로 채널별 배분(H1 10W/H2 8W/H3 4W/마진 3W, 합계 25W)을
PCDU 3+1채널(각 0.75A/0.6A/0.3A/0.3A, 24V)로 증설 없이 수용 가능함을 확인했다
— 변경 없이 확정치로 채택.

검증: 채널별 정격전력 실측(H1/H2/H3 각 ±5% 이내), 서모스탯 설정온도 실측 확인.
