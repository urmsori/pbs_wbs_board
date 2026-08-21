# FM 위성 통합시험 결과
입력: examples/ksat5/deliverables/GSE/NEED-FM-DUALLOAD_deliverable.md,
examples/ksat5/deliverables/EPS/rail-budget.md,
examples/ksat5/deliverables/EPS/burn-in-fm.md,
examples/ksat5/deliverables/COMM/acceptance-test-fm.md,
examples/ksat5/deliverables/COMM/link-margin-fix.md,
examples/ksat5/deliverables/AOCS/acceptance-test-fm.md,
examples/ksat5/deliverables/AIT/rx2-str.md, rx2-eps.md, rx2-aocs.md, rx2-comm.md

INT2-TST(AIT-TST-01)의 FM 위성 통합시험 기록. AIT-RX2-* 4건(모듈별
인수 검사)이 모두 합격한 뒤, 위성구조체(STR FM)에 EPS/AOCS/COMM FM을
장착·통합한 상태에서 두 승계 리스크의 최종 재현·확인을 수행한다.

## 1. 동시부하 재현시험 (RISK-RAIL 최종 확인)
NEED-FM-DUALLOAD 이중부하 리그(장비 구성·교정 완료, ±0.5% 정확도)를
사용해 **실제 AOCS FM 모듈 + 실제 COMM FM 모듈**을 공용 급전선(PCU~
분기점, 3.0A 완속 상위 퓨즈)에 동시 연결하고 재현했다(EPS/burn-in-
fm.md의 전자부하 시뮬레이션과 달리 실모듈 동시 구동).

| 시나리오 | 인가 조건 | 결과 |
|---|---|---|
| AOCS 슬루 트리거(need-sw-aocs.md mode_trigger.py 재사용) | 1.34A 첨두 | 정상 발생 |
| COMM 송신 트리거(실제 PA 구동) | 0.74A, 240s 연속 개념 중 5s 구간 중첩 | 정상 발생 |
| 동시 중첩(실모듈) | 2.08A, 5s | 상위 3.0A 완속 퓨즈 **미동작**(트립 없음), 분기 퓨즈(2.0A/1.25A) 모두 건전 |
| 레일 전압 강하 측정 | 리그 전압 텔레메트리(±0.1V 규격) | 5초 중첩 구간 동안 최저 **6.83V**(EOD 하한 6.8V 대비 여유 유지) — 트리거 동기 오차 <100ms로 재현 조건(±5s 이내 중첩) 충족 |
| 퓨즈 선택성 재확인 | AOCS 분기 단락 모사 | AOCS 분기(2.0A)만 트립, COMM 분기·상위 퓨즈 건전 유지 |

**판정: RISK-RAIL 최종 종결.** rail-budget.md가 설계 기준으로 채택한
2.08A/≤5s 조건이 실제 AOCS FM+COMM FM 모듈로 재현됐고, 퓨즈 미동작·
레일 전압 6.83V(6.8V 하한 상회)·선택성 전부 확인됐다. EPS/burn-in-
fm.md(전자부하 시뮬레이션)와 본 시험(실모듈)이 일치된 결과를 냄으로써
이중으로 실증된다.

## 2. 링크마진 통합 확인 (RISK-LINK 최종 확인)
COMM/acceptance-test-fm.md의 챔버 실측(EOD 마진 **7.8dB**, 목표
7.5dB·요구 ≥6dB 모두 충족)을 위성구조체 통합 상태에서 재확인했다 —
안테나 4조 전개 상태·STR 장착 위치에서 PA 출력 32.5dBm(6.8V, 통합
전 32.6dBm 대비 하네스 손실 0.1dB 이내로 무시 가능) 측정, 통합 재계산
마진 **7.8dB** 유지. rx2-comm.md에서 재확인한 방사패턴 결과(module-
fm.md 인용)와 일치 — 안테나 전개 기구가 방사패턴에 미치는 영향 없음.

**판정: RISK-LINK 최종 종결.** link-margin-fix.md의 해석치(7.5dB)를
실측(7.8dB)이 상회함을 통합 상태에서 재확인 — 최근 실측이 이전 해석
예측을 대체하는 정본으로 채택.

## 3. 운용 제약 채택 기록
rail-budget.md §3, EPS/module-fm.md §3, COMM/module-fm.md §"인도
시점 잔여 사항" 2항이 공통으로 이월한 운용 제약을 FM 운용 절차 이관
사항으로 다음과 같이 채택한다(하드웨어 조치가 아니므로 AIT가 종결
처리하지 않고 운영으로 명시 이관):

1. **AOS guard band 10s → 15s 상향** — AOCS 운용 스케줄 절차에 반영.
2. **비필수 슬루(모멘텀덤프 등) COMM 교신 시간대(AOS 전후 ±5분)
   스케줄링 금지** — AOCS 운용 절차에 반영.
3. **AOCS FM의 SW 강제 guard band 로직(여유<5s 시 슬루 자동 취소,
   acceptance-test-fm.md에서 검증)은 위 1·2항과 별도의 SW 안전장치로
   유지** — 운용 절차 상향과 SW 차단이 이중 방어를 구성함을 명시.
4. **FM 초기 궤도 운용(commissioning) 중 액추에이터 레일 전류
   텔레메트리 실측 모니터링** — rail-budget.md 가정(최대 5s/궤도당
   중첩)이 실비행에서도 유지되는지 확인, 이상 시 guard band 재조정.

## 4. 종합 판정
동시부하 재현(레일 전압 6.83V 유지, 퓨즈 미동작·선택성 확인)과
링크마진 통합 확인(7.8dB)으로 두 승계 리스크가 실물 통합 조건에서
최종 확인됐다. 운용 제약 4건은 하드웨어 종결과 분리해 운용 이관
사항으로 명시 채택한다.

검증: 동시부하(2.08A/5s) 실모듈 재현 시 상위 퓨즈 미동작·레일전압
6.83V(≥6.8V 하한)·선택성 확인, 링크마진 통합 재확인 7.8dB(≥7.5dB
목표·≥6dB 요구) 확인, 운용 제약 4건 채택·이관 기록.
