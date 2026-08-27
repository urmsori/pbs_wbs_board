# AIT 수령검사 — OBC·FSW·COMM·GS (rx-3)

입력: examples/ksat7/deliverables/OBC/module-fm.md, examples/ksat7/deliverables/FSW/module-fm.md,
examples/ksat7/deliverables/COMM/module-fm.md, examples/ksat7/deliverables/COMM/comm-u1-anl-t.md,
examples/ksat7/deliverables/COMM/comm-u1-ins.md, examples/ksat7/deliverables/GS/module-fm.md

## OBC 수령
- 처리여유51.6%≥50%, 저장용량2.01TB≥2TB, 인터페이스(1553×1·CAN×2·SpW×5) 全PASS — sysreq
  OBC 3항목 전부 충족. PAY 회신 지연으로 잠정치(1.2Gbps·2채널) 설계 후 실회신(3.6Gbps·5채널)
  반영 정정, 기능시험 3.55Gbps 재확인 — 잠정 사항 전건 해소.

## FSW 수령
- sysreq FSW 3항목(관리 전 기능·안전모드·SAR 시퀀서) 전부 충족. AOCS·PAY 잠정 설계 후 실회신
  정정(20→10Hz, 90s누적→4중 인터록) 전건 해소.
- SAR 원시데이터 경로: FSW-U2 시퀀서(4중 인터록, 18/18버스트 PASS)가 OBC 저장부(3.6Gbps·
  5채널)로 넘기는 종단간 경로는 시뮬레이션(sim-test-sequencer) 기준 — 통합 실측(실제 OBC·
  PAY 하드웨어 연동)은 미실시, INT 단계 필요(→ INT-TST-3).

## COMM 수령 — 이월 3건
1. **TCS -Y측판 국부 7°C 초과 가능성**: comm-u1-anl-t.md 확인 — SSPA 베이스플레이트 52°C(자체
   부품정격85°C 대비 마진33°C)이나, sysreq TCS 대역(-15~+45°C, SAR송수신기 기준) 대비 +7°C
   초과. COMM 자체 판정 범위 밖으로 명시, TCS 통합 열해석 필요 — INT-TST-4로 확인.
2. **EPS 총부하540W EOL 재확인**: COMM 단독43.7W는 배정60W 이내이나 위성 전체 통합부하는
   미확인 — INT-TST-2로 확인(rx-2 EPS 항목과 동일 시험으로 통합 처리).
3. **질량 3.02kg≈배정3.0kg**: comm-u1-ins.md 확인 결과 실측 3.02kg, 배정 3.0kg 대비 +0.02kg
   (+0.7%) 근소 초과. module-fm.md 본문에는 "≈"로 표기했으나 수치상 엄밀히는 배정 초과 —
   위성 전체 질량예산 통합 시 재확인 필요 항목으로 판단, 신규 GSE 대상 아님(저울 재사용,
   통합 시 전체 질량예산 대조로 처리).
- X-band 실측마진 +5.4dB(예측+8.9dB 대비 -3.5dB 열화, 원인 4건 정직기록), S-band
  64.0kbps/2.00Mbps 실측 — sysreq COMM 항목 PASS. 단, 열화원인 중 GS G/T -1.4dB은 GS 자체
  G-TST(3개소 실측)에서 이미 재확인되어 추가 열화 없음 확인됨(GS 리스크승계 항목 해소 기록).

## GS 수령
- 수신3개소 G/T 실측 26.9~28.5dB/K, 링크마진 +4.5~+5.1dB — 3항목(수신3개소·초기운용30일·SAR
  보정계획) 전부 PASS. 서비스요청·ICD 없음(기존 운용시설 활용).
- G-OPS 접촉시간 7.5분은 실측 기반이나 실제 궤도경사각·정밀좌표 재정밀화를 INT/운용단계에
  권고 — 판정에 영향 없는 경미 사항으로 운용 이관 대상.

## 재사용 판단
- SAR 원시데이터 종단간(OBC-FSW-PAY) 실측: 기존 OBC/FSW 기능시험 장비(DAQ·SpW 인터페이스
  테스터) 재사용 가능, 신규 장비 불요 — 통합 배선·형상만 신규.
- X-band 링크마진 재확인: COMM-U1-TST에 사용된 RF 계측장비(스펙트럼분석기·BER테스터,
  CAL-COMM 교정필) 재사용 가능 — 신규 장비 불요.
- COMM 열해석/TVAC: TCS 유닛레벨 TVAC 챔버(FAC-TCS 예약분) 재사용 가능 규모로 판단(COMM은
  이미 TCS 라디에이터 공유 경로로 설계됨) — 신규 GSE 불요, FAC 재예약 대상.

## 판정
OBC·FSW·GS sysreq 전항목 충족. COMM 이월 3건 중 질량초과(+0.02kg)는 위성 질량예산 통합
확인으로 처리(신규장비 불요), 나머지 2건(열해석·540W)은 INT-TST-2/4로 이관. SAR 원시데이터
종단간 실측은 INT-TST-3 신규 항목으로 편입.
