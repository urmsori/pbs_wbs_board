# 3윙 패널 플래시시험

입력: examples/ksat7/deliverables/SA/panel-inspection.md, examples/ksat7/board/CAL-SA-U1.md

## 시험 조건
AM0 1367W/㎡ 교정 시뮬레이터(CAL-SA-U1)로 3윙 전체 I-V 스윕 측정.

## 결과
- BOL 최대출력(Pmp): **1082W**(설계 예측 대비 셀효율 실측치29.8% 반영).
- EOL 예측(4년, 방사선 감쇠계수 0.85 적용): **920W**.
- 전개 상태(3윙 전개 지그) 최대출력 균일도: 윙간 편차 ≤2.1%.

## sysreq 판정
sysreq SA: "EOL 900W" → 실측 기반 EOL 예측 920W ≥900W **충족**(마진 2.2%).
1차모드는 SA-U1-ANL-S-01 해석치 0.58Hz(≥0.5Hz 충족, 실측 진동시험은
AIT 통합시험에서 재확인 예정으로 인계).

검증: sysreq SA EOL900W 대비 실측기반 EOL예측920W 충족(마진2.2%), 1차모드는 해석치0.58Hz로 AIT 인계
