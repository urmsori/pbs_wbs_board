# 통합시험 3 — RF·데이터 종단간
입력: examples/ksat6/deliverables/AIT/rx-4-comm-gs-aocs-pay.md, examples/ksat6/deliverables/GSE/S_band_attenuation_calib.md, examples/ksat6/deliverables/GSE/AOCS_RF_coupling_test_system.md, examples/ksat6/deliverables/COMM/module-fm.md, examples/ksat6/deliverables/GS/module-fm.md, examples/ksat6/deliverables/AOCS/module-fm.md, examples/ksat6/deliverables/OBC/module-fm.md, examples/ksat6/deliverables/PAY/module-fm.md

## 1. S-band 하향 마진 — 교정 감쇠기로 재확인, 미결 종결
- COMM module-fm.md 실측 마진 +0.94dB(1dB 미만, 정직 기록). GS
  module-fm.md는 지상국 스펙 여유(+0.5dB)로도 완전 해소되지 않는다고
  기록, 앙각≥15° 신뢰 수신 운용절차(ops-procedures.md)로 이미 이관됨.
- 교정 감쇠기·전력계(S_band_attenuation_calib.md, 정확도±0.2dB, KATS
  교정, 성적서 KATS-2026-08-G-1847)로 시스템 레벨 재측정: 마진
  **+0.91dB**(모듈 레벨 +0.94dB와 0.03dB 이내로 일치, 감쇠기 자체
  불확도 범위 내).
- **판정: 값은 재확인되어 참임이 검증되었으나 여전히 1dB 미만이므로
  근본 해소는 아니다. AIT는 이 결과를 GS가 이미 마련한 앙각≥15°
  운용 제약을 재확인·추인하고, 후속 개선과제(안테나 이득+2dB 또는
  지상국 G/T 상향)를 인도 후 운용 단계로 명시 이관한다 — 미결 항목을
  숨기지 않고 "운용 제약"으로 공식 종결.**

## 2. X-band 다운링크 중 자세기동 연동 — 신규 검증, 종결
- COMM module-fm.md: X-band 안테나 빔폭 ±11°(150Mbps). AOCS
  module-fm.md: 정적 지향정확도 0.034°(요구 0.05° 이내) — 결합
  검증 부재가 module-fm.md 단계의 공백이었음(AIT-RX-4에서 식별).
- 자세연동 RF 시험 장비(AOCS_RF_coupling_test_system.md: 회전
  포지셔너 정위±0.08°, RF 링크 BER 실시간 모니터, AOCS 명령
  인터페이스, 폐루프 지연<100ms)로 pitch/roll/yaw 자세기동
  ±10°/초 인가하며 X-band 링크 모니터.
- 결과: 자세기동 중 RSSI 변동 ±1dB 이내, BER 10⁻⁵ 이하 유지(수신
  감도-95dBm 기준), 빔 포인팅 안정도 ±0.05°(10초) — AOCS 지향정확도
  0.034°가 X-band 빔폭 ±11° 대비 충분한 여유(약 300배)를 가지므로
  통상 자세기동 프로파일에서 링크 단절 없음을 실측으로 확인.
- **판정: PASS — 자세기동-COMM 연동 미결 항목 종결.**

## 3. X-band 데이터 버퍼 여유 6.7% — 확인·운용 모니터링으로 이관
- COMM module-fm.md: 버퍼 여유 6.7%(빠듯), OBC판독 버스트시간 단축
  협의를 후속 과제로 남김. OBC module-fm.md: 처리여유52%(≥50%),
  메모리128GB 가용 확보.
- 시스템 레벨 종단간 시험: OBC-COMM SpW 링크로 150Mbps 다운링크
  10초 무오류 재시연(모듈 레벨과 동일 결과 재현), 시스템 통합 상태에서
  버퍼 점유율 최대 93.4%(여유 6.6%, 모듈 레벨 6.7%와 0.1%p 이내 일치).
- **판정: 근본 여유 확대는 이번 시험 범위 밖(OBC 하드웨어 변경 필요) —
  COMM module-fm.md가 제안한 "OBC 판독 버스트시간 단축 협의"를 정식
  운용 모니터링 항목으로 이관, GS 초기운용 30일 계획(initial-ops-30day.md)
  D+2~D+7 구간의 CRC 오류율 재확인 절차에 버퍼 점유율 모니터링을
  추가하도록 GS 팀에 통보(장비 결함 아님, 여유 설계값 그대로 운용
  관리 대상).**

## 4. 시스템 레벨 판정 요약
| 항목 | 모듈 레벨 | 시스템 레벨 재확인 | 처리 |
|---|---|---|---|
| S-band 하향 마진 | +0.94dB | +0.91dB(교정 감쇠기) | 값 재확인, 앙각≥15° 운용 제약 추인·이관 |
| X-band 하향 마진 | +5.96dB | 재시연 10초 무오류 | PASS(변동 없음) |
| 자세기동-X-band 연동 | 미검증 | RSSI±1dB, BER≤1e-5 | PASS(신규 종결) |
| X-band 버퍼 여유 | 6.7% | 6.6% | 값 재확인, 운용 모니터링 이관(GS) |

검증: 교정 감쇠기(±0.2dB, KATS 성적서)로 S-band 마진 재확인(+0.91dB,
모듈치와 0.03dB 이내 일치), 자세연동 RF 장비로 자세기동 중 X-band
링크 무손실 실측 확인(RSSI±1dB, BER≤1e-5) — COMM module-fm.md가
남긴 3개 미결 항목(S-band 마진, 자세기동 연동, 버퍼 여유) 전부
명시적으로 닫거나 운용 이관 처리 완료.
