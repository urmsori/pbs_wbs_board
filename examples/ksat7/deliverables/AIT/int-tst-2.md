# 통합시험 2 — 전기 (int-tst-2)

입력: examples/ksat7/deliverables/AIT/rx-2.md, examples/ksat7/deliverables/AIT/rx-3.md,
examples/ksat7/deliverables/GSE/pulse-daq-confirmation.md, examples/ksat7/deliverables/SE/sysreq.md,
examples/ksat7/deliverables/HAR/u2-inspection.md

## EPS 정상모선 총부하 540W EOL 재확인
위성 통합 형상, SAR 촬영모드(COMM 60W 배정 포함, PROP는 SAR와 상호배타이므로 미가산)
기준 실측: OBC/FSW 처리부하 + AOCS 구동부 + COMM 60W + TCS 히터 38.6W + HAR 계통손실 등
정상모선 총부하 **512.6W** — sysreq EOL 소비예산 540W 대비 **마진 27.4W(5.1%)**.
추력모드(PROP 300W, SAR/COMM-Tx 비활성) 대체 케이스도 498.2W≤540W로 충족.
**COMM 이월 2건 중 1건(540W EOL) CLOSED.**

## HAR-U1 EMC 차폐 자체 실측
U2-INS-01 대표측정(접지본딩6.5mΩ·실드연속성0.03Ω)과 별도로 U1 자체 실측 수행:
접지본딩 **6.4mΩ**≤10mΩ, 실드연속성 **0.031Ω**, 개별실드 절연 전건 합격 — U2 대표측정치와
0.1mΩ/0.001Ω 이내로 일치, 대표측정 유효성 확인. **HAR 이월 2건 중 나머지 1건 CLOSED.**

## 1.8kW 펄스 위성통합상태 실증
NEED-GSE-PULSE(16채널 200kHz DAQ, 인라인 프로브)로 실 PAY-U2 송신기가 실 HAR 하니스를
통해 실 EPS-U2 배터리·PCDU에서 전력을 인출하는 상태로 5s×18회/궤도 파형 10궤도 반복:
- 모선전압 46.2~53.9V(50V±5V 이내, 유닛레벨 46.4~53.8V 대비 유사)
- 에지 포착 0.35~0.42ms(<1ms 요구, DAQ 대역폭<0.5ms 이내)
- 슈퍼캡 재충전 19.1s(간격20s 이내), 10궤도 이상 없음

## 판정
sysreq EPS 항목(모선50V±5V·1.8kW버스트) 통합상태 재확인 PASS, 정상모선 총부하 512.6W≤540W
PASS. HAR 이월 2건 전부 CLOSED.

검증: 정상모선 총부하512.6W≤540W(마진5.1%), 1.8kW펄스 통합실측 모선46.2~53.9V 규격내,
HAR-U1 EMC 6.4mΩ/0.031Ω로 U2 대표측정과 일치(CLOSED)
