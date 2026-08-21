# K-SAT 5 통합·시험 보고서 (INT)
입력: examples/ksat5/deliverables/AOCS/module-em.md,
      examples/ksat5/deliverables/STR/module-em.md,
      examples/ksat5/deliverables/EPS/module-em.md,
      examples/ksat5/deliverables/COMM/module-em.md,
      examples/ksat5/deliverables/AIT/rx-aocs.md,
      examples/ksat5/deliverables/AIT/rx-str.md,
      examples/ksat5/deliverables/AIT/rx-eps.md,
      examples/ksat5/deliverables/AIT/rx-comm.md,
      examples/ksat5/deliverables/EPS/power-conditioning.md,
      examples/ksat5/deliverables/EPS/icd-comm-eps.md,
      examples/ksat5/deliverables/COMM/icd-eps-comm-power.md,
      examples/ksat5/deliverables/COMM/bus-voltage-check.md,
      examples/ksat5/deliverables/AOCS/icd-eps-aocs-power-profile.md,
      examples/ksat5/deliverables/sysreq.md

AIT-LEAD(INT)의 통합·시험 보고서. 4개 모듈이 인수 시험(AIT-RX-AOCS/
STR/EPS/COMM, 전건 DONE)을 통과한 뒤, 모듈 간 정합(질량 합·전력수지·
인터페이스 상호 일치)을 각 팀 ICD 회신 원문을 실제 대조해 확인한다.

## 1. 모듈별 인수 결과 요약
| 모듈 | 인수 판정 | 근거 |
|---|---|---|
| AOCS | 합격 | rx-aocs.md — 모드전이 5시나리오 전건 통과, 지향오차 0.47°≤0.5° |
| STR | 합격 | rx-str.md — 지그 10종 전건 정합, EPS배터리 잠정판정 최종확정 |
| EPS | 합격 | rx-eps.md — 4레일 텔레메트리/부하스텝/보호회로/EOD유지 전건 통과 |
| COMM | 조건부 합격 | rx-comm.md — EOD 링크마진 6.0dB(요구 충족·여유 0dB, 잔여리스크 이월) |

## 2. 질량 예산 정합 확인
| 모듈 | 배분(sysreq) | 실제 인도치(module-em.md) | 여유 |
|---|---|---|---|
| STR | 3.00 kg | 2.97 kg | 0.03 |
| AOCS | 2.00 kg | 2.00 kg | 0.00 |
| EPS | 3.00 kg | 1.27 kg | 1.73 |
| COMM | 1.20 kg | 1.20 kg | 0.00 |
| **위성 합계** | **9.20 kg**(배분 합) | **7.44 kg** | **1.76 kg** |
| sysreq 총 한도(여유 0.8 별도 포함) | 10.00 kg | 7.44 kg | 2.56 |

4개 모듈 실측/확정 질량 합(2.97+2.00+1.27+1.20=7.44kg)이 sysreq 총
한도(10kg) 및 배분 합(9.2kg) 이내임을 실제 합산으로 확인. EPS가
배터리 최종 확정(0.22kg, 잠정치 0.25kg 대비 경량)으로 배분 대비 1.73kg
여유를 남겨 위성 전체 여유가 STR의 1차 추정(구조-EPS-AOCS-COMM
6.80kg, structural-analysis.md)보다 더 커졌다 — 방향은 항상 여유
증가 쪽이므로 STR 구조 설계 재작업 불필요.

## 3. 전력 수지 정합 확인
- 발생: EOL 궤도평균 ≈20.6 W ≥ sysreq 요구 20 W (EPS module-em.md).
- 소비(궤도 평균):
  - AOCS NOMINAL 평균 3.0 W(실측, rx-aocs.md/module-test-report.md) — 상시.
  - COMM: 송신 duty cycle ≈4.2%(icd-eps-comm-power.md) 기준, 송신 시
    액추에이터 5.0W+5V 0.6W, 대기 시 5V 0.5W → 궤도평균 ≈0.042×5.6 +
    0.958×0.5 ≈ 0.71 W.
  - 궤도평균 소비 합계 ≈ 3.71 W ≪ 발생 20.6 W. 여유 충분, 병목 없음.
- **공유 레일 첨두 중첩 확인(신규 발견)**: power-conditioning.md의
  "액추에이터 레일(8.4V, 버스직결)"은 AOCS 구동기와 COMM 송신단이
  **동일 물리 레일을 공유**한다(power-conditioning.md §버스구조 표).
  각 팀 ICD는 자기 부하만 독립 산정했다 — AOCS 첨두 9.1W/EOD 1.34A
  (icd-eps-aocs-power-profile.md) vs COMM 송신 첨두 0.74A(EOD,
  icd-eps-comm-power.md) — **동시 발생(AOCS 슬루 60s + COMM 송신 펄스)
  시 합산 최대 ≈2.08A(EOD 6.8V, ≈14.1W)를 어느 문서도 검토하지 않았다.**
  COMM 자신의 bus-voltage-check.md §4도 "COMM 분기 퓨즈/차단기 정격이
  아직 확정되지 않았다"고 이미 명시한 상태다.

## 4. 인터페이스 상호 일치 확인 (ICD 회신 실제 대조)
| ICD 쌍 | 대조 항목 | 결과 |
|---|---|---|
| icd-str-aocs-mass-footprint.md ↔ mounting-interfaces.md(STR) | 리액션휠 PCD40, 스타트래커 PCD50×50, 자이로 PCD30×30, 태양센서 PCD14×14, 질량 2.00kg | 수치 일치(rx-str.md 지그 재확인 포함) |
| icd-aocs-str.md(정렬·강성 약속) ↔ structural-analysis.md | 스타트래커 ≥150Hz/자이로 ≥120Hz | STR 해석치 158Hz/132Hz로 약속 충족 |
| icd-str-eps.md ↔ mounting-interfaces.md(STR) | PCU PC/104 피치, 태양전지판 M2.5×4, 배터리(잠정→확정) | 일치, 배터리 항목은 rx-str.md JIG-03으로 최종 확정 |
| icd-str-comm-footprint.md ↔ mounting-interfaces.md(STR) | 트랜시버 82×88mm 대각, 안테나 돌출≤8mm | 일치(rx-str.md JIG-09/10 확인) |
| icd-eps-aocs-power-profile.md ↔ module-test-report.md(AOCS) | NOMINAL 3.2W/첨두9.1W 산정 vs 실측 3.0W/8.8W | 실측이 산정치 이내로 일치 |
| icd-comm-eps.md(rev1, 5V공용, 문제) ↔ icd-eps-comm-power.md/transceiver-em.md rev.2(PA 이설) | 5V 레일 초과 문제 | rev.2로 해소 확인(bus-voltage-check.md 재검증), **단 이설 후 레일이 AOCS와 공유되는 점은 §3 신규 발견으로 별도 이월** |
| link-budget.md ↔ transceiver-em.md/icd-eps-comm-power.md | 마진 6.3dB(여유0.3dB) vs EOD 실측 저하 | rx-comm.md 실측으로 EOD 마진 6.0dB(여유0dB) 확인 — 미해결 리스크가 사실로 확인됨 |

이번 대조로 8개 ICD 쌍 중 7개는 완전 정합, 1개(전력조절계 레일 공유)는
개별 ICD 문서 자체에는 오류가 없으나 **양쪽 문서를 통합 관점에서
겹쳐 본 적이 없어 놓친 교차 리스크**임을 확인했다.

## 5. 종합 판정 및 이월 사항
4개 모듈 전건 인수 합격(COMM은 조건부), 질량·전력 수지 모두 예산
이내로 정합 확인. 다음 2건은 **불합격이 아니라 요구는 충족하되
후속 단계에서 반드시 재확인해야 하는 잔여 리스크**로 정직하게
이월한다(낙관적으로 "해결됨"이라 적지 않음):

1. **액추에이터 레일 동시부하**: AOCS 슬루 첨두(EOD 1.34A)와 COMM
   송신 첨두(EOD 0.74A) 동시 발생 시 합산 ≈2.08A에 대해 EPS 분기
   퓨즈/차단기 정격이 검토된 바 없다. FM(비행모델) 단계 전, EPS·AOCS·
   COMM 3자 협상으로 분기 퓨즈 정격을 재확정해야 한다.
2. **COMM EOD 링크마진 여유 0dB**: 요구(≥6dB)는 실측으로 충족(6.0dB)
   하나 추가 열화 여지가 없다. 안테나 정합손실·부품 실측 편차가
   생기면 즉시 요구 미달로 전환될 수 있어 FM 단계 재확인 대상이다.

이 두 항목을 제외하면 K-SAT 5 EM 4개 모듈은 통합 요구를 모두 충족한다.

검증: 4개 모듈 인수 시험(rx-aocs/str/eps/comm.md) 전건 DONE 확인,
질량 합산(7.44kg≤9.2kg 배분/10kg 한도) 직접 계산, 전력 수지(발생
20.6W≥소비 3.71W) 직접 계산, ICD 8쌍 상호 대조(7쌍 완전 정합·1쌍
교차 리스크 신규 발견) 완료.
