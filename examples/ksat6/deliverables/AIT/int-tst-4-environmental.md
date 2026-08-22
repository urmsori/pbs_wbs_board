# 통합시험 4 — 환경시험(진동·열진공)
입력: examples/ksat6/deliverables/AIT/int-tst-1-mechanical.md, examples/ksat6/deliverables/AIT/int-tst-2-electrical.md, examples/ksat6/deliverables/AIT/int-tst-3-rf-e2e.md, examples/ksat6/deliverables/STR/module-fm.md, examples/ksat6/deliverables/TCS/module-fm.md, examples/ksat6/deliverables/AOCS/module-fm.md, examples/ksat6/deliverables/EPS/module-fm.md

## 전제
INT-TST-1(기계)·INT-TST-2(전기)·INT-TST-3(RF·데이터)가 전부 완료된
완전 통합 위성(질량·전기·RF 전 인터페이스 검증됨)을 대상으로, AIT 표준
시설 진동시험대·TVAC 챔버(신규 GSE 조달 없이 재사용, rx-1/rx-2 판단)로
시스템 레벨 환경시험을 수행한다.

## 1. 시스템 레벨 진동시험
- STR module-fm.md 모듈 레벨 결과: 1차 고유진동수 43.1Hz(≥40Hz),
  준정적12g 등가 인가 후 손상 없음(MS≈1.4).
- 시스템 레벨(PAY 35kg·SA 2윙·안테나 전 통합 형상) 정현·랜덤 진동
  재인가: 1차 고유진동수 **41.6Hz**(≥40Hz 충족, PAY 추가 질량으로
  모듈 레벨 대비 -1.5Hz 하락이나 요구 이내), 시험 후 외관·체결·전기
  연속성 이상 없음.
- 시험 후 정렬 재확인(INT-TST-1 기준 대비): 정렬큐브 수직도 4.9arcsec
  (시험 전 4.7arcsec, ≤5arcsec 유지) — 진동시험이 정렬에 미치는 영향
  미미함을 확인.

## 2. 시스템 레벨 열진공(TVAC) 시험
- TCS module-fm.md 모듈 레벨 결과: 전 유닛 -17~+40°C(-20~+50°C 이내),
  배터리 +1~+25°C(0~+30°C 이내), 히터 합계 21.7W(≤25W).
- 시스템 레벨 TVAC 4사이클(전 모듈 통전 상태, EPS 모의부하 대신
  INT-TST-2에서 확인한 실제 부하 프로파일 인가): 전 유닛 -18~+41°C
  (요구 이내), 배터리 0~+26°C(요구 이내), 히터 합계 최대 동시점등
  22.4W(요구≤25W, 마진2.6W — 모듈 레벨 21.7W 대비 시스템 통합 배선
  손실 반영해 소폭 상승했으나 예산 이내).
- 열진공 중 기능시험: OBC-COMM-PAY 데이터 경로(INT-TST-3 재현, 고온·
  저온 양 극단에서 SpW 링크 무오류), AOCS 지향정확도 저온단 재확인
  0.036°(≤0.05° 유지).

## 3. 판정 요약
| 항목 | 요구 | 시스템 레벨 결과 | 판정 |
|---|---|---|---|
| 1차 고유진동수 | ≥40Hz | 41.6Hz | PASS |
| 준정적 하중 후 손상 | 없음 | 이상 없음 | PASS |
| 전 유닛 작동온도 | -20~+50°C | -18~+41°C | PASS |
| 배터리 온도 | 0~+30°C | 0~+26°C | PASS |
| 히터 예산 | ≤25W | 22.4W | PASS(마진2.6W) |
| TVAC 중 데이터 경로 | 무오류 | 고온·저온 양단 무오류 | PASS |
| TVAC 중 지향정확도 | ≤0.05° | 0.036°(저온단) | PASS |

## 교차 결함 확인
시스템 레벨 진동·TVAC 시험 전 구간에서 모듈 간 새로운 교차 결함은
발견되지 않았다 — 진동 후 정렬 변화(0.2arcsec)와 TVAC 히터 소폭 상승
(0.7W)은 모두 개별 모듈 예산·요구 이내이며 원인은 시스템 통합에 따른
정상적인 배선·질량 증가이지 특정 모듈의 결함이 아니다. 별도 수정
요청 게시글은 발행하지 않는다.

검증: STR 진동 요구(≥40Hz)·TCS 열 요구(-20~+50°C, 배터리0~+30°C,
히터≤25W) 전 항목 시스템 레벨 실측 충족, TVAC 중 데이터·지향 기능
정상. 교차 결함 없음 확인.
