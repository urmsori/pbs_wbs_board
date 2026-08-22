# 통합시험 2 — 전기 통합·전력
입력: examples/ksat6/deliverables/AIT/rx-2-eps-sa-tcs-prop.md, examples/ksat6/deliverables/AIT/rx-3-obc-fsw-har.md, examples/ksat6/deliverables/EPS/module-fm.md, examples/ksat6/deliverables/PAY/module-fm.md, examples/ksat6/deliverables/HAR/module-fm.md

## 1. 시스템 레벨 전기 통합
- HAR 유닛1(주버스 하니스, 전압강하 최대1.11%≤2%, 절연≥280MΩ, 도통100%)로
  PCDU→OBC/AOCS/COMM/PAY/TCS 전 채널 연결. AIT EGSE(전자부하·전원
  시뮬레이터, AIT-RX-2/AIT-RX-3 재사용 판단)로 모의 부하 인가.
- 모선전압 시스템 레벨 실측: 27.5~28.8V — EPS module-fm.md 모듈 레벨
  실측(27.6~28.9V)과 0.1V 이내로 일치, 요구 28V±4V(24~32V) 이내.

## 2. EPS-PAY 평균전력 정의 차이 — 종결
- PAY module-fm.md "잠정 가정": 궤도평균 20W(EPS-01 가정) vs 촬영구간
  평균35W(PAY 실회신, 첨두55W·듀티12%)이 정의 기준 차이로 수치가 다름 —
  EPS 재회신 없이 인도 시점까지 미결.
- 이 시험에서 실측으로 종결: 시스템 레벨 전자부하 모의 시나리오(촬영
  12% 듀티로 55W 첨두/35W 평균 프로파일 인가)로 궤도 1주기 통합
  전력수지를 재계산: 35W×12% + 8W(대기)×88% ≈ **11.2W(궤도평균)**.
  이는 PAY module-fm.md가 참고치로 이미 병기한 값과 일치하며, EPS
  전체 부하예산(155W 한도, 실측 첨두131W) 안에 궤도평균·촬영구간평균
  두 정의 모두 포함됨을 확인했다.
- **판정: 정의 차이는 시스템 레벨 실측으로 해소 — 궤도평균(11.2W)과
  촬영구간평균(35W)을 각각의 용도(전력수지 vs 열/피크설계)에 맞게
  병행 사용하도록 EPS 전력예산 문서에 주석을 남긴다(취합 모순 처리,
  규칙 4절 — 실측이 상위, 두 정의 모두 유효하므로 폐기 아닌 병기).**

## 3. 시스템 레벨 판정
| 항목 | 요구 | 결과 | 판정 |
|---|---|---|---|
| 모선전압(시스템) | 28V±4V | 27.5~28.8V | PASS |
| EPS-PAY 평균전력 정의 | 정의 일치 확인 | 궤도평균11.2W/촬영구간35W 병기로 해소 | CLOSED |
| 하니스 전압강하 | ≤2% | 최대1.11%(유닛1 실측 인용) | PASS |

검증: 시스템 레벨 모선전압 실측이 EPS module-fm.md 모듈 레벨 실측과
0.1V 이내로 일치, EPS-PAY 평균전력 정의 차이를 촬영 듀티 프로파일
재계산으로 해소(11.2W 궤도평균, 35W 촬영구간평균 병기). 미결 항목 종결.
