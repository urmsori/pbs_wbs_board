# AIT 수령검사 — EPS·SA·TCS·PROP (rx-2)

입력: examples/ksat7/deliverables/EPS/module-fm.md, examples/ksat7/deliverables/EPS/battery-pulse-discharge-test.md,
examples/ksat7/deliverables/SA/module-fm.md, examples/ksat7/deliverables/TCS/module-fm.md,
examples/ksat7/deliverables/PROP/module-fm.md

## EPS 수령
- sysreq EPS 3항목(모선50V±5V·1.8kW버스트·DoD≤30%) 전부 실측 충족 확인(모선46.4~53.8V,
  DoD최대27.3%). ICD 5건(PAY·PROP·COMM·HAR·TCS) 전부 실측/회신 확정, 잠정 없음.
- **시험 방법 확인**: EPS-U2 펄스 실증(battery-pulse-discharge-test.md)은 "교정된 전자부하·
  DAQ"로 PAY 실측 파형을 **모의**한 것이며, 실제 PAY 송신기가 실 하니스를 통해 위성 통합
  상태(다른 서브시스템 정상부하 동시 인가)에서 인출하는 조건은 아직 검증되지 않음. INT
  단계에서 위성 통합 상태 1.8kW 펄스 실증(→ INT-TST-2)이 필요.
- EPS 정상모선 총부하 540W EOL 이내 여부: COMM module-fm.md가 승계 리스크로 지정(COMM 단독
  43.7W는 배정60W 이내이나 전체 통합부하 미확인) — INT-TST-2에서 재확인 필요.

## SA 수령
- EOL출력 920W≥900W(마진2.2%), 전개후 1차모드 0.58Hz(해석치, MECH 확정 힌지강성8000N·m/rad
  기준) — 이후 MECH rev.2에서 힌지강성 24,600N·m/rad로 재설계, 실측 1차모드는 MECH-U2-R2-TST
  0.53Hz로 최종 확정(SA-U1-ANL-S 해석치와 함께 교차 확인 완료, 불일치 아님 — 해석 vs 통합
  실측 차이로 정상 범위).
- ICD(REQ-SA-MECH/REQ-MECH-SA): 질량7.6kg/윙·관성10.1kg·m² 양방향 일치, 잠정 리스크 해소.
- 1차모드 실측 진동시험은 SA 자체 module-fm.md가 명시적으로 "AIT 통합시험 단계로 인계"라고
  기록 — MECH rev.2 재시험(0.53Hz)으로 이미 인계 이행 완료로 판단(추가 SA 단독 진동시험 불요).

## TCS 수령
- TVAC 4사이클 실측: 고온+43.5°C≤45°C(여유1.5°C), 저온-13.8°C≥-15°C(여유1.2°C), 배터리
  +7.5~9.2°C(규격내), 히터38.6W≤40W(여유1.4W) — sysreq TCS 4항목 전부 충족.
- 히트파이프 단일고장시 90W/식>정격80W/식은 FM 수용(발생확률 낮음)으로 RB 기록 — INT 신규
  조치 불요, 운용 중 모니터링 대상으로 인계.
- COMM -Y측판 국부 7°C 초과 가능성(COMM module-fm.md 승계)은 TCS 자체 module-fm.md에는
  기록 없음(TCS 단독 유닛 TVAC은 COMM 장착 전 상태) — 통합 열해석/TVAC 확인 필요(→ INT-TST-4).

## PROP 수령
- Δv 25.9m/s≥25m/s(여유3.6%), 300W급 점화 10사이클 정상, 배관누설<5e-9 atm·cc/s — sysreq
  PROP 전항목 충족. STR·EPS ICD 상호 확인 완료(SAR-추력 상호배타 운용 확정, 동시부하 2.1kW
  시나리오 배제 — EPS 총부하 재확인 시 PROP은 SAR과 상호배타이므로 동시가산 대상 아님, 산정에서
  제외).

## 재사용 판단
- SA 진동시험: 별도 신규 설비 불요, MECH rev.2 재시험 결과로 대체 확인(중복 시험 지양).
- TCS TVAC: 유닛레벨 챔버는 이미 사용됨. 통합열해석은 해석 작업(설비 아님) — TVAC 챔버 신규
  필요는 근거 부족(COMM 부착 상태 국부 열점은 우선 해석으로 판단 가능, 챔버 재사용 가능 규모로
  추정) — 신규 GSE 불요, FAC 재예약으로 충분.
- EPS 1.8kW 펄스 위성통합 실증: 유닛레벨은 "전자부하·DAQ 모의" 방식으로, 통합상태에서는 실제
  PAY 송신기 부하 + 540W 배경부하를 동시에 고속(<1ms 에지) 계측할 수 있는 설비가 필요 —
  **신규 GSE 필요 판단**(NEED-GSE-PULSE 발행, source=본 RX).

## 판정
EPS·TCS·PROP sysreq 전항목 충족 재확인. SA 1차모드는 MECH rev.2 실측으로 인계 완료 확인.
EPS 1.8kW 통합실증·EPS 총부하 540W 재확인·COMM 열해석은 INT-TST-2/4로 이관, 통합 펄스
계측설비는 신규 GSE 필요로 판단.
