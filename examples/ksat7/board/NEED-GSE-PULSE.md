---
id: NEED-GSE-PULSE
title: SAR 1.8kW 펄스 위성통합상태 흡수·계측 설비
status: OPEN
parent: INT
source: AIT-RX-2
track: GSE
owner: -
deliverable: -
after: -
started: -
finished: -
---

EPS-U2 펄스 실증(battery-pulse-discharge-test.md)은 "교정된 전자부하·DAQ"로 PAY 파형을
모의한 유닛레벨 시험이었다(위성 조립 전, 실 PAY 송신기 아님). PAY-U2 펄스시험(u2-pulse-test.md)
역시 실험실 전원 기준 자체 시험이다. INT-TST-2(위성상태 1.8kW 펄스 실증)를 위해서는 ①
실제 PAY 송신기가 HAR 실 배선을 통해 EPS 배터리·PCDU로부터 전력을 인출하는 상태에서, ②
위성 전체 정상부하(EPS module-fm.md 기준 540W EOL 목표대역) 위에 5s×18회/궤도·상승/하강<1ms
펄스가 중첩되는 것을 동시에 고속 계측할 수 있는 설비가 필요하다.

요구 사양(안):
- 버스 전압·전류 고속 DAQ(<1ms 에지 포착, 다채널 동시계측 — 펄스채널+정상부하 배경채널 분리)
- 1.8kW 첨두 부하를 실제로 인가·회수하는 전자부하가 아니라, 실 하니스·실 PAY 하드웨어를
  그대로 두고 "계측만" 수행하는 인라인 전류/전압 프로브 세트(HAR 커넥터 핀아웃과 정합)
- 슈퍼커패시터 재충전 구간(18.9s) 포함 20궤도 이상 연속 로깅 가능한 저장용량

재사용 불가 판단 근거: 기존 EPS-U2 시험설비(CAL-EPS-U2 교정 전자부하)는 부하를 "발생"시키는
용도로, 위성 통합 상태에서는 부하가 이미 실 PAY 하드웨어이므로 전자부하가 아니라 인라인
계측기가 필요 — 용도가 다르다.

산출물 제안: examples/ksat7/deliverables/GSE/pulse-daq-confirmation.md
검증: 요청 사양 대비 확보 설비(형식·채널수·대역폭) 회신
