# FM 위성 통합·인도
입력: examples/ksat5/deliverables/AIT/rx2-str.md,
examples/ksat5/deliverables/AIT/rx2-eps.md,
examples/ksat5/deliverables/AIT/rx2-aocs.md,
examples/ksat5/deliverables/AIT/rx2-comm.md,
examples/ksat5/deliverables/AIT/integration-test-fm.md,
examples/ksat5/deliverables/EPS/rail-budget.md,
examples/ksat5/deliverables/COMM/link-margin-fix.md,
examples/ksat5/deliverables/COMM/acceptance-test-fm.md

INT2(AIT-01)의 FM 통합·인도 기록. STR/EPS/AOCS/COMM 4개 FM 모듈이
모두 인수 검사(AIT-RX2-*)를 합격했고, 통합시험(INT2-TST)으로 두
승계 리스크의 실물 통합 조건 재현·확인을 마쳤으므로 이를 취합해
FM 위성 인도를 판정한다.

## 1. 판정 조건 — EM 승계 리스크 2건 종결 확인

### RISK-RAIL(공유 액추에이터 레일 3자 동시부하) — 종결
- **하드웨어 근거**: EPS 3자 협상(rail-budget.md)으로 분기 퓨즈
  AOCS 2.0A / COMM 1.25A(완속) / 상위 공용 3.0A(완속) 확정, 선택성
  67%/42% ≤80% 기준 충족.
- **실증 근거 1(EPS 벤치)**: burn-in-fm.md §3 — 전자부하로 2.08A/5s
  동시부하 재현, 상위 퓨즈 트립 없음, 버스전압 6.8V 이상 유지.
- **실증 근거 2(AIT 실모듈 최종 확인)**: integration-test-fm.md §1 —
  **실제 AOCS FM + COMM FM 모듈**을 NEED-FM-DUALLOAD 이중부하 리그로
  동시 구동, 2.08A/5s 조건에서 상위 3.0A 퓨즈 미동작, 레일 전압 최저
  **6.83V**(EOD 하한 6.8V 상회) 확인, 분기 퓨즈 선택성 재확인(AOCS
  분기 단락 시 해당 분기만 트립).
- **종결**: EPS 벤치 시뮬레이션과 AIT 실모듈 재현이 일치된 결과를
  내어 이중으로 실증됐다 — **RISK-RAIL 종결**.

### RISK-LINK(EOD 링크마진 0dB) — 종결
- **설계 근거**: link-margin-fix.md — 방안A(안테나 피드망 위상·결합
  재최적화), 해석치 6.0dB(여유0)→7.5dB(여유1.5dB).
- **실증 근거 1(COMM 챔버)**: acceptance-test-fm.md §1 — EOD 조건
  PA 출력 32.6dBm 실측, 방사패턴 챔버 실측 기준 재계산 마진 **7.8dB**
  (목표 7.5dB 상회).
- **실증 근거 2(AIT 통합 확인)**: integration-test-fm.md §2 — 위성
  구조체 장착·안테나 전개 상태에서 PA 출력 32.5dBm(하네스 손실 0.1dB
  이내), 통합 재계산 마진 **7.8dB** 유지 — 구조 통합이 링크성능에
  부정적 영향 없음 확인.
- **종결**: 해석치(7.5dB)를 실측(7.8dB)이 상회하고, 통합 상태에서도
  동일 수치가 유지됨을 확인 — **RISK-LINK 종결**.

## 2. 모듈별 인수 결과 요약
| 모듈 | 판정 | EM 장비 재사용 | 잔여 사항 |
|---|---|---|---|
| STR | 합격 | 지그 10종 전량 재사용 | 없음 |
| EPS | 합격 | 하니스·SW 전량 재사용 | 없음(동시부하 재현은 §1로 종결) |
| AOCS | 합격 | 하니스·SW 전량 재사용 | 없음 |
| COMM | 합격 | 하니스·RF키트 전량 재사용 | 없음(동시부하 재현은 §1로 종결) |

## 3. 운용 제약의 운영 이관
integration-test-fm.md §3에서 채택한 운용 제약 4건(AOS guard band
15s 상향, 비필수 슬루 스케줄링 금지, AOCS SW guard band 이중 방어
유지, 초기궤도운용 레일전류 실측 모니터링)은 하드웨어 조치가 아니므로
**AIT 인도로 종결 처리하지 않고**, AOCS 운용 절차·초기궤도운용
(commissioning) 계획으로 **명시 이관**한다. 이관 완료 여부는 AIT
범위 밖(운영팀 소관)이며, 인도 판정은 이관 사실의 기록으로 조건부
완결된다(4절 "재작업은 정상 경로다" 정신에 따라 하드웨어 종결과
운용 이관을 정직하게 구분).

## 4. 종합 판정
STR/EPS/AOCS/COMM FM 4개 모듈 인수 전건 합격, EM 승계 리스크 2건
(RISK-RAIL, RISK-LINK) 모두 하드웨어·실물 재현 양쪽 근거로 종결
확인, 운용 제약은 운영 이관으로 명시 처리했다. **FM 위성 통합·인도
완료.**

검증: RISK-RAIL 종결(2.08A/5s 실모듈 재현, 레일전압 6.83V≥6.8V,
퓨즈 미동작·선택성 확인 — integration-test-fm.md §1), RISK-LINK
종결(EOD 링크마진 실측 7.8dB≥목표7.5dB, 통합상태 재확인 —
integration-test-fm.md §2), 모듈 4건 인수 전건 합격(rx2-*.md),
운용 제약 4건 운영 이관 명시.
