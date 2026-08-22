# 수령검사 — 전력·열·추진(EPS/SA/TCS/PROP)
입력: examples/ksat6/deliverables/EPS/module-fm.md, examples/ksat6/deliverables/SA/module-fm.md, examples/ksat6/deliverables/TCS/module-fm.md, examples/ksat6/deliverables/PROP/module-fm.md

## 수령 확인
| 모듈 | 핵심 수치(인도 문서 인용) | 수령 판정 |
|---|---|---|
| EPS | 모선27.6~28.9V, 부하평균91.4W(마진41%), DoD16.6~20.8%(≤25%) | 이상 없음 |
| SA | EOL 356.4W(≥340W), 전개후 1차모드0.837Hz(≥0.8Hz) | 이상 없음 |
| TCS | 전유닛 -17~+40°C(-20~+50°C), 히터합계21.7W(≤25W) | 이상 없음 |
| PROP | Δv마진100%, 누설9.2e-7 scc/s(≤1e-6) | 수락검사서 확인, 이상 없음 |

## 통합시험 필요 장비 판단
- 각 모듈이 sysreq 항목을 자체 실측(모의부하·플래시시험·TVAC·누설시험)으로
  이미 충족 확인했고, module-fm.md 어디에도 시스템 레벨 통합에서 새로
  발생하는 장비 필요(전용 치구·특수 계측기)가 근거로 나타나지 않는다.
  EPS-PAY 평균전력 정의 차이(궤도평균 vs 촬영구간평균, PAY module-fm.md
  "잠정 가정" 항목)는 **장비 필요가 아니라 시험·판정 방법의 문제**이므로
  NEED가 아니라 INT-TST-2(전기 통합·전력)에서 직접 재정의·재측정으로
  닫는다(4단계 참조).
- 이 수령검사에서는 억지로 NEED를 만들지 않는다 — 근거 없는 장비 요청은
  발행하지 않는다(규칙 4절: 계획표가 아니라 필요의 기록).

## 재사용 판단
- 전자부하 모의시험 장비(EPS-04에서 사용)는 AIT EGSE 표준 전자부하와
  동일 규격 — 시스템 레벨 전력통합시험(INT-TST-2)에서 재사용한다.
- TVAC 챔버(TCS-04 tvac-test.md 사용)와 진동시험대는 AIT-RX-1에서
  이미 판단한 대로 환경시험(INT-TST-4)에서 AIT 표준 시설로 재사용한다
  (중복 판단 방지를 위해 여기서는 결론만 인용).
- PROP 누설시험용 헬륨 검지기는 PROP 자체 수락검사 장비이며 시스템
  레벨에서 배관을 재개봉하지 않으므로 통합시험 단계에서 재사용 필요
  없음(이미 완결된 검증).

검증: EPS·SA·TCS·PROP module-fm.md의 sysreq 판정표를 각 1개씩 인용해
수령 수치 일치 확인. 신규 장비 필요는 근거 없어 발행하지 않음 — 재사용
판단 3건과 EPS-PAY 정의차 이관(INT-TST-2행) 1건을 명시.
