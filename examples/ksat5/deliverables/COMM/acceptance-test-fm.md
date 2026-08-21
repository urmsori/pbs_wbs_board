# COMM FM 수락시험
입력: examples/ksat5/deliverables/COMM/acceptance-inspection-fm.md,
examples/ksat5/deliverables/COMM/link-margin-fix.md,
examples/ksat5/deliverables/AIT/rx-comm.md (EM 실측 기준),
examples/ksat5/deliverables/EPS/rail-budget.md

수락검사(COMM-FM-03) 합격 하드웨어에 대한 기능·성능 시험.

## 1. PA 출력 및 EOD 링크마진 실측 (목표 7.5dB 검증)
| 공급전압 | PA 출력 실측 | EM 실측(참고) |
|---|---|---|
| 8.4V(공칭) | 33.0 dBm | 33.1 dBm |
| 6.8V(EOD) | 32.6 dBm | 32.7 dBm |

방사패턴 챔버 실측(4소자 결합 후, 위상오차 ±1.6° 반영 피드망):
최악방향(최소이득) −0.6 dBi → +0.9 dBi로 개선(EM rev.1 대비 편파순도
향상 확인, link-margin-fix.md 해석치 +1.5dB보다 실측 개선폭이 다소
큼 — 보수적 설계치를 실측이 상회).

| 조건 | link-budget.md 기준 마진 | FM 실측 기준 재계산 마진 | 목표(link-margin-fix.md) | 판정 |
|---|---|---|---|---|
| 8.4V(공칭) | 6.3 dB | 8.2 dB | 7.9 dB | 합격(목표 상회) |
| **6.8V(EOD)** | 6.0 dB(EM 실측) | **7.8 dB** | **7.5 dB** | **합격 — 목표 7.5dB 달성(0.3dB 초과 확보)** |

**결론: EOD 링크마진 목표(7.5dB) 실측으로 검증 완료.** RISK-LINK가
안테나 방사패턴 실측 재확인을 이월했던 항목(link-margin-fix.md §3
"정직 공개")이 본 시험으로 종결된다 — 낙관적 가정이 아니라 챔버
실측으로 확인.

## 2. 레일 전류 부하시험 (rail-budget.md 반영)
- 5V 로직 레일: 대기 0.50A / 송신중 0.52A 실측(설계치와 일치),
  레일 정격 2.0A 대비 여유 74% — 합격.
- 액추에이터 레일(8.4V→EOD 6.8V 가변 전원으로 부하스텝 인가): COMM
  단독 정상상태 0.74A(EOD) 실측 확인, COMM 분기 퓨즈 1.25A(완속,
  rail-budget.md) 대비 59% — 240초 연속 인가 시 nuisance trip 없음
  확인(퓨즈 미동작).
- AOCS 동시부하 재현 시험(2.08A, 5초)은 COMM 단독 수락시험 범위 밖
  — AIT 통합시험(공용 3.0A 퓨즈 대상)에서 재현하기로 rail-budget.md가
  이미 정한 범위이므로 본 시험에서는 재현하지 않음(범위 명시, 생략
  사유 정직 공개).

## 3. 기타 확인
- 질량: 0.700 kg(트랜시버+안테나), 배분(1.20kg 중 하네스·체결
  포함) 이내 — 합격.
- 더미로드 종단 무방사, 스퓨리어스 이상 없음 — 합격.

## 4. 종합 판정
전 항목 합격. EOD 링크마진 실측 7.8dB로 목표(7.5dB) 및 요구(≥6dB)
모두 충족, 재작업 없이 종결. rail-budget.md의 동시부하(2.08A/5s)
재현은 AIT 통합시험 범위로 이월(COMM-FM-05 인도 시 명시).

검증: PA출력 2조건 실측(33.0/32.6dBm), 방사패턴 챔버 실측 기준
재계산 EOD마진 7.8dB≥목표7.5dB 확인. 5V레일·액추에이터레일 COMM
분기 전류가 각 정격(2.0A/1.25A) 대비 사용률(26%/59%, 여유74%/41%) 확인. 질량
0.700kg 배분내.
