# GS-U1 수신 3개소 적합성 계획

입력: examples/ksat7/deliverables/SE/sysreq.md, examples/ksat7/deliverables/COMM/comm-u1-dsn.md,
examples/ksat7/deliverables/COMM/comm-u1-tst.md

## 1. 판정 대상 (sysreq.md 인용)
- GS: **수신 3개소**, **초기운용 30일**, SAR 보정 계획.
- COMM-U1 확정: X-band 8.1GHz, 32APSK 5/6, 180.6Msps(800Mbps), 요구 C/N0 98.4dBHz,
  설계 G/T 기준 28.5dB/K(comm-u1-dsn.md), 실측 시험국 G/T 27.1dB/K(comm-u1-tst.md,
  앙각 12° 저고도 조건).

## 2. 수신 3개소 배치안
| 국명(가정) | 위도대 | 안테나 구경 | 목표 G/T | 역할 |
|---|---|---|---|---|
| GS-1 (국내 주국) | 중위도 | 11m | 28.8 dB/K | 주 임무자료 수신·SAR 보정 기준국 |
| GS-2 (극지 보조국) | 고위도(극궤도 통과빈도 高) | 9m | 27.5 dB/K | 접촉기회 최대화, 초기운용 30일 집중지원 |
| GS-3 (해외 분산국) | 저위도/해외 | 9m | 27.5 dB/K | 접촉 공백 최소화, 글로벌 임무데이터 회수 |

- 각 국 목표 G/T는 COMM-U1-TST 실측치(27.1dB/K, 저앙각 조건)에 **+0.4~1.7dB 설계
  여유**를 둬 링크마진 저하 리스크(comm-u1-tst.md "-3.5dB 열화" 기록)를 흡수한다.
- 앙각 마스크: 10°(3개소 공통), 최악 슬랜트레인지 1816km 기준 링크 성립 확인
  (comm-u1-dsn.md FSPL 175.8dB 재사용).

## 3. 수신체인 적합성 요구
- 복조기: DVB-S2 32APSK 5/6 대응, 180.6Msps
- 시스템온도: ≤180K(11m국), ≤210K(9m국) — G/T 목표 역산
- 데이터 기록: 접촉당 최대 800Mbps×600s = 480Gb 순간 기록 대역 확보

## 4. 초기운용 30일 개념
- Day 1-3: LEOP(초기궤도운용) — GS-1/2/3 전체 가용, S-band TT&C(COMM-U2) 상시 교신
- Day 4-14: 서브시스템 커미셔닝, X-band 다운링크 초기 링크 검증(본 계획 기준 접촉 스케줄)
- Day 15-30: SAR 보정 계획 — 코너리플렉터·트랜스폰더 기준점 관측 반복 수행,
  NESZ·기하보정 계수 산출(sysreq PAY NESZ≤-19dB 대비 GS 수신 SNR 여유 확인용)

## 5. GS-U1-TST(적합성 시험)로 인계할 판정 기준
- 3개소 각 실측 G/T가 목표치(표 2) 대비 -1.0dB 이내
- COMM-U1-TST 실측 링크마진(+5.4dB) 대비 지상국 수신단에서 추가 열화 없음 확인

검증: sysreq GS 3개소 계획 수립(11m/9m/9m, G/T 27.5~28.8dB/K), 초기운용 30일
일정·SAR 보정 계획 포함 — 수치로 GS-U1-TST 판정기준까지 명시.
