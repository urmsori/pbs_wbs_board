# 2윙 패널 플래시시험(EOL 16kW 판정)

입력: examples/ksat8/deliverables/SA/panel-inspection.md, examples/ksat8/deliverables/CAL/sa-u1-cal.md

교정된 태양광 시뮬레이터(AM0 1367W/㎡, CAL-SA-U1)로 2윙 패널 I-V 특성을
측정.

## 결과
| 항목 | 요구 | 실측/예측 | 결과 |
|---|---|---|---|
| BOL 출력 | - | 16,890 W | - |
| EOL 출력(15년 열화 예측) | ≥16,000 W | 16,120 W(마진 0.75%) | 충족 |
| 전개 후 1차모드 | ≥0.1 Hz | 0.118 Hz(SA-U1-ANL-S 해석치, MECH 실측 힌지강성 반영) | 충족(AIT 인계) |

EOL 마진이 0.75%로 낮아 리스크 기록 — AIT 통합 후 실제 궤도상 성능
추이를 GS 관제 데이터로 추적 권고.

검증: EOL예측16,120W≥16,000W(마진0.75%, 리스크기록), 1차모드0.118Hz(해석)로 AIT 인계
