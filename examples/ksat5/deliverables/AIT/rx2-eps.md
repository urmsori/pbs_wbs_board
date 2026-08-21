# EPS FM 모듈 인수 검사 결과
입력: examples/ksat5/deliverables/EPS/module-fm.md,
examples/ksat5/deliverables/EPS/rail-budget.md,
examples/ksat5/deliverables/EPS/burn-in-fm.md,
examples/ksat5/deliverables/SUPPORT/need-har-eps.md,
examples/ksat5/deliverables/SUPPORT/need-sw-eps.md (EM 장비 재사용)

AIT-RX2-EPS(AIT-QA-01)의 EPS FM 모듈 인수 검사 기록.

## 1. EM 장비 재사용 판단
module-fm.md에 PCU 34핀 백플레인·배터리 2핀/1핀 서미스터 커넥터 변경
언급이 없다(design-update-fm.md도 배선/퓨즈 정격 변경만 다루고
커넥터 형상은 불변). NEED-HAR-EPS(EM 하니스)·NEED-SW-EPS(EM EGSE
SW: rail_tlm_logger.py 등)를 그대로 재사용해 4레일 텔레메트리를
재확인한다.

## 2. RISK-RAIL 종결 근거 재확인 (EPS 소관분)
| 확인 항목 | module-fm.md 근거 | 본 검사 재확인 |
|---|---|---|
| 분기 퓨즈 정격 | 2.0A(AOCS)/1.25A(COMM)/3.0A(상위 완속) | design-update-fm.md 반영 확인, 실물 장착 육안 확인 |
| 실물 시험 실증 | burn-in-fm.md §3 4시나리오 전건 통과 | 동시(2.08A/5s) 시나리오는 EPS 전자부하 시뮬레이션임을 확인(실제 AOCS+COMM 모듈 아님) — **AIT 통합시험(이중부하 리그)에서 실모듈로 별도 재확인 필요, INT2-TST로 이월** |
| 4레일 텔레메트리(EM SW 재사용) | rail_tlm_logger.py로 재현 | 1차버스 6.8~8.4V, 5V/3.3V 리플 ≤50mVpp 전 레일 기준 이내 재확인 |
| 질량 | 1.27kg(EM 확정치 유지) | 육안·저울 재확인 일치 |

## 3. 판정
EPS FM 모듈 인수 **합격**. RISK-RAIL의 EPS 소관 하드웨어 조치(퓨즈
정격)는 module-fm.md·burn-in-fm.md로 종결 확인했으나, "실제 AOCS+
COMM FM 모듈 동시부하" 재현은 EPS 벤치 시험(전자부하 시뮬레이션)으로
대체될 수 없어 INT2-TST(NEED-FM-DUALLOAD 리그)로 이월한다. 운용 제약
(module-fm.md §3)도 AIT/AOCS 인계 사항으로 이월 확인.

검증: EM 하니스·SW 재사용 정합 확인, 4레일 텔레메트리 기준 이내
확인, 분기 퓨즈 정격 실물 대조 일치, 질량 1.27kg 일치 — 단 동시부하
실모듈 재현은 미해결로 INT2-TST 이월 명시.
