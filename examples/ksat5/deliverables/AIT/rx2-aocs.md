# AOCS FM 모듈 인수 검사 결과
입력: examples/ksat5/deliverables/AOCS/module-fm.md,
examples/ksat5/deliverables/AOCS/acceptance-test-fm.md,
examples/ksat5/deliverables/AOCS/calibration-report-fm.md,
examples/ksat5/deliverables/SUPPORT/need-har-aocs.md,
examples/ksat5/deliverables/SUPPORT/need-sw-aocs.md (EM 장비 재사용)

AIT-RX2-AOCS(AIT-TST-01)의 AOCS FM 모듈 인수 검사 기록.

## 1. EM 장비 재사용 판단
module-fm.md §1~2에 EKF/PD 게인 미세조정, guard band SW 강제 로직
갱신만 있고 10채널 커넥터 인출면 변경 언급이 없다. NEED-HAR-AOCS(EM
10채널 하니스)·NEED-SW-AOCS(EM EGSE SW: mode_trigger.py 등)를 그대로
재사용해 모드 전이·지향오차를 재현한다.

## 2. 검사 결과
| 항목 | module-fm.md/acceptance-test-fm.md 근거 | 본 검사 재현(EM 하니스·SW 재사용) |
|---|---|---|
| 모드 전이(4모드) | 정상, EM과 동일 | mode_trigger.py로 재현, 전건 통과 |
| 종합 지향오차 | 0.45°(SYS-REQ 0.5° 이내) | pointing_error_calc.py로 재현, 0.45° 일치 |
| guard band 강제 로직 | 여유<5s 시 슬루 자동 취소 | stim 시나리오(여유 3s) 주입 → 취소 동작 재확인 |
| 질량 | 1.998kg(배분 2.000kg 이내) | 저울 재확인 일치 |

## 3. RISK-RAIL 관련 확인
AOCS의 SW 대응(guard band<5s 시 슬루 취소)은 "AOCS가 스스로 여유
부족을 감지해 슬루를 취소"하는 국소(local) 방어이며, rail-budget.md
§3-1이 권고한 "AOS guard band 10s→15s 상향"(스케줄 버퍼 확대,
운용 절차)과는 층위가 다르다 — 후자는 발생 빈도를 낮추는 운용
조치, 전자는 발생 시 즉시 차단하는 SW 안전장치로 상호 보완 관계임을
확인. 두 조치 모두 INT2-TST 운용 제약 채택 기록에 함께 남긴다.

## 4. 판정
AOCS FM 모듈 인수 **합격**. 인터페이스 변경 없어 EM 장비 전량 재사용,
신규 대기 항목 없음.

검증: EM 하니스·SW 재사용 정합 확인, 모드 전이 전건 통과, 지향오차
0.45° 일치, guard band 로직(여유<5s 취소) 재현 확인, 질량 1.998kg
일치.
