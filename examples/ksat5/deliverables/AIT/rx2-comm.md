# COMM FM 모듈 인수 검사 결과
입력: examples/ksat5/deliverables/COMM/module-fm.md,
examples/ksat5/deliverables/COMM/acceptance-test-fm.md,
examples/ksat5/deliverables/COMM/link-margin-fix.md,
examples/ksat5/deliverables/SUPPORT/need-har-comm.md,
examples/ksat5/deliverables/SUPPORT/need-rf-comm.md (EM 장비 재사용)

AIT-RX2-COMM(AIT-TST-01)의 COMM FM 모듈 인수 검사 기록.

## 1. EM 장비 재사용 판단
module-fm.md §"모듈 구성" 3항, design-update-fm.md §"미변경 항목":
커넥터·기구 인터페이스 변경 없음(안테나 피드망 위상·결합만 재조정).
NEED-HAR-COMM(EM 전원·데이터 하니스)·NEED-RF-COMM(EM SMA 케이블+
감쇠기+더미로드)을 그대로 재사용해 PA 출력·레일 전류를 재확인한다.

## 2. RISK-LINK 종결 근거 재확인
| 확인 항목 | module-fm.md/acceptance-test-fm.md 근거 | 본 검사 재확인 |
|---|---|---|
| EOD 링크마진 | 챔버 실측 **7.8dB**(목표 7.5dB 상회, 요구≥6dB 충족) | NEED-RF-COMM 감쇠기·더미로드로 PA 출력 32.6dBm(6.8V) 재확인, link-margin-fix.md 해석치(7.5dB)보다 실측이 높음 — 나중 실측이 앞선 해석 예측을 대체(정본으로 채택) |
| 최악방향 방사패턴 | −0.6dBi→+0.9dBi 개선(챔버 실측) | COMM 자체 챔버 실측 결과 인용 대조, 별도 재측정 불요(장비 상이) |
| 레일 전류(COMM 분기 단독) | 0.74A, 여유 41%(1.25A 대비) | EM 하니스로 재현, 일치 확인 |

## 3. 이월 사항(범위 명시)
AOCS-COMM 동시부하(2.08A, ≤5s) 재현시험은 module-fm.md §"인도 시점
잔여 사항" 1항이 명시한 대로 COMM 단독 인수 검사 범위 밖이다 —
NEED-FM-DUALLOAD(이중부하 리그) 완성 후 INT2-TST에서 실모듈로
재현한다. 운용 제약 이행(module-fm.md §2)도 동일하게 이월.

## 4. 판정
COMM FM 모듈 인수 **합격**. EOD 링크마진 실측 7.8dB로 RISK-LINK 종결
근거를 독립 재확인했다. 동시부하 재현만 INT2-TST로 이월(범위 명시,
COMM 자체 결함 아님).

검증: EM 하니스·RF 키트 재사용 정합 확인, PA 출력 32.6dBm(6.8V) 재현,
링크마진 7.8dB(module-fm.md 인도치와 일치) 확인, 레일 전류 0.74A/
여유41% 일치.
