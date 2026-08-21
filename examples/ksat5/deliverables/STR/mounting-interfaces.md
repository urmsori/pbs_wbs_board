# STR-02: 서브시스템 장착 인터페이스 설계
입력: examples/ksat5/deliverables/STR/primary-structure-design.md,
examples/ksat5/deliverables/EPS/icd-str-eps.md,
examples/ksat5/deliverables/AOCS/icd-str-aocs-mass-footprint.md,
examples/ksat5/deliverables/COMM/icd-str-comm-footprint.md,
examples/ksat5/deliverables/STR/icd-aocs-str.md,
examples/ksat5/deliverables/STR/icd-comm-str.md

## 데크별 장착 브래킷·컷아웃 확정

### 데크 1단(+Z, EPS)
- 태양전지판 몸체 패널 2면: 6U 측면 규격 발자국(≈100×340mm)에 맞춰 +Y/-Y
  측면 패널에 M2.5×4 인서트 4개소(코너 5mm 인셋)를 표준 레일 피치로 배치.
- 전개 힌지 브래킷: M3×2/힌지, 데크 러그 2개소 신설(패널 모서리 보강).
- PCU 보드: 데크 1단 상면에 M3 코너 4점, 90.17×96.13mm PC/104 피치로
  스탠드오프 4개 신설.
- 배터리 팩: 데크 1단 인접 슬롯에 잠정 발자국(95×90×20mm)으로 M3 브래킷
  4점 예약 — EPS-03 확정 후 재확인 필요(질량 여유 1.70kg으로 큰 변경
  가능성 낮음, EPS 회신 5항 참조).

### 데크 2단(중단, AOCS)
- 리액션휠 3개: 본체 직교 3축에 개별 브래킷(Ø50 원통용 M3×3, PCD40)
  신설 — 축 방향이 데크 각 모서리를 향하도록 배치.
- 마그네토토커 3개: 패널 내측면 클램프(양단 2점) 3조, 리액션휠과 별도
  직교 3축.
- 스타트래커: -Y 패널에 M3×4(PCD 50×50) 장착면 신설. 정렬 공차
  ≤0.015°, 국부 1차 고유진동수 ≥150Hz로 STR이 회신·확정(icd-aocs-str.md).
- 관성센서(자이로): M2.5×4(PCD30×30), 정렬 ≤0.02°/≥120Hz(icd-aocs-str.md
  회신치, AOCS-01 배분과 동일). 태양센서 2개: M2×2(PCD14×14), 패널 관통
  후면 장착.

### 데크 3단(-Z, COMM)
- 트랜시버 보드: 데크 상면 평탄 장착, M3 코너 4점(82×88mm 대각 피치),
  −X 데크 모서리 방향으로 RF/전원/데이터 커넥터 인출 여유 공간 확보,
  코너 홀 중 −X측 1개소를 GND 스트랩 겸용으로 지정.
- 안테나: -Z 패널 중앙(X=0,Y=0), 4조 대칭(±X/±Y 45°) 배치, 수납 시
  -Z 패널면 기준 돌출 ≤8mm(6U 포락선 내), 전개 후 ±35° 원뿔 스윕,
  국부 보강 더블러(2.5mm, 40×40mm)+M3×4(icd-comm-str.md 회신치 반영).

## 갱신된 STR 질량 배분 확인
| 항목 | 질량(kg) |
|---|---|
| 1차 구조(STR-01) | 2.40 |
| 장착 브래킷·컷아웃·보강 신설분 실측 반영 | 0.55 |
| **STR 구조 합계** | **2.95** |
| STR 배분(sysreq) | 3.00 |
| 여유 | 0.05 |

배터리(EPS 잠정치) 변경 시에도 STR 자체 구조 질량에는 영향 없음(브래킷
발자국은 이미 잠정치 기준으로 예약 완료).

## 검증
EPS/AOCS/COMM 3팀 회신 발자국·체결 패턴을 모두 도면 치수로 반영,
AOCS 정렬·강성 요구(icd-aocs-str.md) 및 COMM 안테나 포락선(icd-comm-str.md)
요구 충족 확인. STR 구조 질량 합계 2.95kg ≤ 배분 3.00kg 확인.
