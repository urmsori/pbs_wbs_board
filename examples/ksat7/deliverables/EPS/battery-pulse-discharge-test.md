# 배터리팩 1.8kW 펄스 방전 실증시험

입력: examples/ksat7/deliverables/EPS/pcdu-inspection.md, examples/ksat7/deliverables/EPS/battery-inspection.md,
examples/ksat7/deliverables/EPS/pay-pulse-confirmation.md, examples/ksat7/board/CAL-EPS-U2.md, examples/ksat7/board/FAC-EPS-U2.md

## 시험 조건
PAY 실측 파형(5s×18회/궤도, 듀티6%, 첨두1.8kW, 상승/하강<1ms) 20궤도 반복
모의. 교정된 전자부하·DAQ(CAL-EPS-U2), 항온 전기시험실(FAC-EPS-U2), PA
입회(PA-EPS-U2) 하에 시험.

## 결과
- 모선전압: 버스트 중 최저 46.4V, 최고 53.8V — **50V±5V(45~55V) 범위 이내**.
- 배터리 DoD: 궤도당 최대 27.3%(20궤도 반복 평균 24.8%) — **DoD≤30% 충족**.
- 슈퍼캡 재충전: 매 버스트 사이 18.9s 내 완전재충전 확인(설계 예측 15.8s
  대비 근접, 마진 확보).
- 20궤도 반복 중 이상(과열·전압이탈) 없음.

## sysreq 판정
sysreq EPS: "모선 50V±5V, SAR 펄스 1.8kW 버스트 대응, DoD≤30%" →
실측 모선 46.4~53.8V(규격내), DoD 최대27.3%≤30% **충족**.
EPS-U1-RB 조건부 승인의 조건(DoD 실측 재검증)을 본 시험으로 해소.

검증: sysreq EPS(모선50V±5V·1.8kW버스트·DoD≤30%) 실측 충족(모선46.4~53.8V, DoD최대27.3%), RB 조건 해소
