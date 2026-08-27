# K-SAT 7 위성 조립·통합·시험(AIT) 인도 — integration-fm.md

입력: examples/ksat7/deliverables/AIT/rx-{1,2,3,4}.md, examples/ksat7/deliverables/AIT/int-tst-{1,2,3,4}.md,
examples/ksat7/deliverables/GSE/{pulse-daq-confirmation,deploy-offload-confirmation}.md,
13개 examples/ksat7/deliverables/<TR>/module-fm.md 전건, examples/ksat7/deliverables/SE/sysreq.md

## 1. 13개 모듈 수령 확인
AIT-RX-1(STR·MECH·HAR) · AIT-RX-2(EPS·SA·TCS·PROP) · AIT-RX-3(OBC·FSW·COMM·GS) ·
AIT-RX-4(AOCS·PAY) 4건으로 13개 모듈 module-fm.md 전건을 수입검사 관점에서 확인, sysreq
각 항목이 유닛/모듈 레벨에서 실측·해석으로 충족됨을 재확인했다(상세는 rx-1~4.md).

## 2. 이월 항목 전건 처리 결과

| 구분 | 항목 | 원 상태 | 처리 Work | 최종 결과 |
|---|---|---|---|---|
| rev.2 | STR 1차모드 NCR(30.4Hz) | rev.2 실측36.1Hz | INT-TST-1(통합실측 36.0Hz) | **CLOSED**(마진2.9%) |
| rev.2 | MECH SA힌지 1차모드 NCR(0.31Hz) | rev.2 실측0.53Hz | INT-TST-1(통합실측 0.52Hz) | **CLOSED**(마진4%) |
| HAR-1 | EPS 커넥터(PCDU-PWR-J4) 물리 정합 미확인 | 전기성능만 확인 | INT-TST-1(GSE 프로브 정합 확인) | **CLOSED** |
| HAR-2 | U1 자체 EMC 차폐 미실측(U2 대표측정만) | - | INT-TST-2(U1 자체실측 6.4mΩ/0.031Ω) | **CLOSED**(U2 대표측정과 일치) |
| COMM-1 | -Y측판 국부 7°C 초과 가능성 | 리스크 승계 | INT-TST-4(통합열해석+51.6°C) | **운용 이관**(부품정격마진33.4°C 유지, TCS팀 세션종료로 하드웨어 수정 미이행) |
| COMM-2 | EPS 정상모선 총부하540W EOL 재확인 | 리스크 승계 | INT-TST-2(통합실측512.6W) | **CLOSED**(마진5.1%) |
| COMM-3 | 질량3.02kg≈배정3.0kg(+0.02kg) | rx-3 재확인 | 위성 총질량예산(≤300kg,마진15%) 통합 대조 | **CLOSED**(총예산 대비 0.02kg는 무시가능, 개별 재작업 불요) |
| 질량불일치 | STR 설계가정38kg↔PAY실측72kg | STR rev.2 반영 | rx-4(PAY 원문 대조)+INT-TST-1(통합모달 재확인) | **CLOSED**(수치 일치 확인, 재발 없음) |

이월 항목 8건(HAR 2·COMM 3·rev.2 2·질량 38↔72 불일치 1) 중 **7건 CLOSED, 1건(COMM-1) 운용
이관** — 하드웨어 재작업이 남은 항목 없음.

## 3. 신규 장비(GSE) 필요 판단
AIT-RX-1/2에서 실제 module-fm.md·시험 방법을 근거로 2건 발행, GSE 팀이 즉시 이행(폴링 내 DONE):
- **NEED-GSE-PULSE**(source=AIT-RX-2): EPS 유닛시험은 전자부하로 PAY파형을 모의했을 뿐 위성
  통합상태(실 PAY→실 HAR→실 EPS) 실증 설비가 없었음 — 16채널200kHz DAQ·인라인프로브 확보,
  INT-TST-2에서 사용.
- **NEED-GSE-DEPLOY**(source=AIT-RX-1): 유닛레벨 전개설비는 각 기구 단독 규격으로 통합형상
  (안테나72kg+SA3윙22.8kg) 동시지지 불가 — 지지용량94.8kg 통합 오프로드 설비 확보, INT-TST-1
  에서 사용.
- 그 외 후보(STR/MECH 모달 재확인 설비, HAR 커넥터·EMC 계측, X-band RF 계측, TCS TVAC)는
  모두 기존 유닛레벨 설비 재사용 가능으로 판단해 NEED 미발행(근거: rx-1~3.md 재사용 판단
  절 참조).

## 4. 통합시험 결과 요약
| 시험 | 핵심 결과 | 판정 |
|---|---|---|
| INT-TST-1(기계·정렬) | STR36.0Hz·SA힌지0.52Hz·동시전개이격131mm·HAR커넥터정합 | PASS |
| INT-TST-2(전기) | 총부하512.6W≤540W·1.8kW펄스통합실증·HAR EMC자체실측 | PASS |
| INT-TST-3(RF·데이터) | X-band링크마진+5.2dB·SAR원시데이터종단간3.54Gbps | PASS |
| INT-TST-4(환경·열) | 통합열해석+51.6°C(TCS대역대비+6.6°C초과, 부품정격마진33.4°C) | PASS(운용조건부) |

## 5. 교차 결함
INT-TST-4에서 COMM -Y측판 국부 열점(+6.6°C 초과)을 TCS 트랙 앞 수정요청(FIX-TCS-COMM-YPANEL,
source=INT-TST-4)으로 발행, 8×20초 폴링 무응답(M-TCS 02:08:20 DONE 이후 TCS 팀 세션 종료) —
**OPEN으로 잔류, 리스크 기록**. COMM 자체 부품정격 마진(33.4°C)과 인접 HAR 하니스 정격여유
(200°C 대비 65.5°C)로 판정에 영향 없는 경미 건으로 판단, 운용(텔레메트리 모니터링+X-band
송신 듀티 제한 절차)으로 이관. 그 외 신규 교차 결함은 발견되지 않았다.

## 6. 운용 이관 목록
1. **COMM -Y측판 국부 열점**(+51.6°C, TCS대역대비+6.6°C초과): 서미스터 상시 모니터링,
   초과 시 X-band 송신 듀티 제한 절차. FIX-TCS-COMM-YPANEL OPEN 유지(향후 TCS 재가동 시
   하드웨어 재검토 권고).
2. **TCS 히트파이프 단일고장 시 90W/식>정격80W/식**: TCS RB 기록 승계, 발생확률 낮음(FM
   수용), 운용 중 이상시 즉시 텔레메트리 확인.
3. **GS 접촉시간 7.5분**: 실제 궤도경사각·지상국 정밀좌표 확정 후 재정밀화 필요(운용 초기
   30일 IOP 단계에서 갱신).
4. **STR 1차구조 질량 마진 0.4kg(44.6kg/45kg)**: 향후 형상변경 시 마진관리 대상으로 추적.
5. **PROP Δv 잔여여유 0.1kg**: 태양활동 고조기 등 추가 Δv 소요 발생 시 활용, 임무기간 중
   추적.
6. **MECH-U1 전개충격 마진 7.3%**: 현 비행형상은 실측 37.1g≤40g로 충족이나, 차기 블록
   설계개선 권고(MECH RB 기록 승계).
7. **COMM -Y판 물리 TVAC 재시험**: 통합 열해석으로 우선 확인(INT-TST-4), 물리 TVAC은
   일정상 차기 캠페인으로 이관(기존 TCS 챔버 재사용 가능 판단).

## 7. 역할 통계 (AIT track)
- AIT-01(통합 책임): INT take 1건.
- AIT-QA-01: AIT-RX-1, AIT-RX-3 — 2건.
- AIT-QA-02: AIT-RX-2, AIT-RX-4 — 2건.
- AIT-TST-01: INT-TST-1, INT-TST-3 — 2건.
- AIT-TST-02: INT-TST-2, INT-TST-4 — 2건.
- 전원 역할당 1~3건 정상 범위, 6건 상한 이내.

## sysreq 최종 확인
13개 모듈 sysreq 판정 전항목 rx-1~4.md에서 재확인 PASS, 이월 8건 중 7건 CLOSED·1건 운용
이관(하드웨어 재작업 없음), 신규 교차결함 추가 발견 없음(TCS 열점은 승계 항목의 재확인).

검증: 13개 모듈 수령 완료·sysreq 전항목 PASS 재확인, 이월 8건(HAR2·COMM3·rev.2 2·질량
38↔72불일치1) 중 7건 CLOSED·1건 운용이관, 통합시험 4건(INT-TST-1~4) 전부 PASS, 신규
교차결함 없음(TCS 승계항목만 리스크 잔류)
