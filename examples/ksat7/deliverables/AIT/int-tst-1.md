# 통합시험 1 — 기계·정렬 (int-tst-1)

입력: examples/ksat7/deliverables/AIT/rx-1.md, examples/ksat7/deliverables/STR/str-u1-r2-tst.md,
examples/ksat7/deliverables/MECH/mech-u2-r2-tst.md, examples/ksat7/deliverables/GSE/deploy-offload-confirmation.md,
examples/ksat7/deliverables/GSE/pulse-daq-confirmation.md

## 시험 구성
위성 플라이트 형상(STR-U1 rev.2 + STR-U2 rev.2 브래킷 + MECH-U1/U2 rev.2 + PAY-U1 SAR
안테나 실장착) 상태로 NEED-GSE-DEPLOY 중력보상 설비(지지용량94.8kg, 오프로드 7식,
모션캡처<1mm)에 거치 후 가진·전개 시험 수행.

## 결과
| 항목 | rev.2(유닛레벨) | 통합 실측 | 요구 | 판정 |
|---|---|---|---|---|
| STR 1차모드(안테나 장착) | 36.1Hz | **36.0Hz**(경계조건 차 -0.1Hz, 오차범위내) | ≥35Hz | 충족(마진1.0Hz/2.9%) |
| SA힌지 전개후 1차모드 | 0.53Hz | **0.52Hz** | ≥0.5Hz | 충족(마진0.02Hz/4%) |
| SAR2단+SA3윙 동시전개 간섭 | - | 최소이격거리 **131mm**(설비교정치127mm 대비 정상) | >100mm | 충족 |
| 전개 중 수직편차 | - | 7.1mm | <15mm | 충족 |

## HAR-U1 EPS 커넥터 물리 정합
NEED-GSE-PULSE 설치 과정에서 인라인 프로브 분기패드 장착 시 HAR-U1↔EPS-PCDU 커넥터
(잠정p/n PCDU-PWR-J4)의 실물 정합을 직접 확인: 핀아웃·체결(락킹링 완전결합)·극성 전부
일치, EPS 정식 커넥터와 물리적으로 정합됨(GSE pulse-daq-confirmation.md "핀아웃 확인
완료" 기준과 교차 확인). **HAR 이월 1건 CLOSED — 재설계 불요.**

## 오픈 사항
없음. 통합 형상에서도 rev.2 실측치가 유효함을 재확인, 동시전개 간섭 여유 확보.

검증: STR 36.0Hz≥35Hz·SA힌지 0.52Hz≥0.5Hz 통합 실측 재확인, 동시전개 이격131mm>100mm,
HAR-U1 EPS 커넥터 물리 정합 확인(CLOSED)
