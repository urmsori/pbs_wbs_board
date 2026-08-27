# M-INT 위성 조립·통합·시험·인도 — integration-fm

입력: examples/ksat8/deliverables/AIT/rx-1.md, examples/ksat8/deliverables/AIT/rx-2.md,
examples/ksat8/deliverables/AIT/rx-3.md, examples/ksat8/deliverables/AIT/rx-4.md,
examples/ksat8/deliverables/AIT/int-tst-1.md, examples/ksat8/deliverables/AIT/int-tst-2.md,
examples/ksat8/deliverables/AIT/int-tst-3.md, examples/ksat8/deliverables/AIT/int-tst-4.md,
examples/ksat8/deliverables/STR/module-fm.md, examples/ksat8/deliverables/MECH/module-fm.md,
examples/ksat8/deliverables/TCS/module-fm.md, examples/ksat8/deliverables/PROP/module-fm.md,
examples/ksat8/deliverables/EPS/module-fm.md, examples/ksat8/deliverables/SA/module-fm.md,
examples/ksat8/deliverables/AOCS/module-fm.md, examples/ksat8/deliverables/OBC/module-fm.md,
examples/ksat8/deliverables/COMM/module-fm.md, examples/ksat8/deliverables/PAY/module-fm.md,
examples/ksat8/deliverables/HAR/module-fm.md, examples/ksat8/deliverables/FSW/module-fm.md,
examples/ksat8/deliverables/GS/module-fm.md

## 인도 구성
13개 트랙(STR/MECH/TCS/PROP/EPS/SA/AOCS/OBC/COMM/PAY/HAR/FSW/GS)
비행모델 인도 문서를 4개 수령 Work(AIT-RX-1~4)로 취합해 sysreq 판정을
재확인하고, 4개 통합시험(INT-TST-1~4)으로 개별 트랙 시험으로는 확인할
수 없는 통합 형상 성능(정렬·동시전개·통합부하·RF종단간·통합열)을
검증했다.

## sysreq 전체 판정 (13개 트랙, module-fm.md 인용)
| 트랙 | 요구 | 결과 |
|---|---|---|
| STR | 질량≤380kg·1차모드≥30Hz | 349.7kg·31.8Hz — 충족 |
| MECH | 반사판2기·SA2윙 전개·단일고장허용 | 개별+통합(INT-TST-1) 전개 확인 — 충족 |
| TCS | 방열6kW·-10~+60°C | 개별5.04kW/6.3kW + 통합(INT-TST-4)5.34kW/6.3kW — 충족 |
| PROP | Δv 2,250m/s | 1,500+750 — 충족 |
| EPS | 100V±2V·15kW배전·이클립스2.4kWh | 개별14,420W+통합(INT-TST-2)14,398W — 충족 |
| SA | EOL16kW·1차모드≥0.1Hz | 16,120W(마진0.75%)·0.118Hz — 충족 |
| AOCS | 지향0.05°·언로딩 | 0.0305° — 충족 |
| OBC | TM8,000·TC2,000·이중화 | 프레임드롭0·420ms — 충족 |
| COMM | S-band상시·레인징 | 개별4.8dBW+통합(INT-TST-3)4.78dBW — 충족 |
| PAY | 24채널·EIRP≥52·NPR≥18 | 개별52.05~52.61/18.7~19.3 + 통합(INT-TST-3)52.01~52.57/18.6~19.2 — 충족(전채널) |
| HAR | 100V절연·도파관≤0.8dB | 개별0.58dB + 통합 어댑터조치후(INT-TST-1)0.62dB — 충족 |
| FSW | 전 서브시스템 TM/TC | 7건 회신(1건 잠정, COMM확정치로 해소 — rx-3.md) |
| GS | 관제소적합성·IOT30일계획 | 조건부적합(Ka시험국)·일정확정 — 충족(조건부 1건 이관) |

## 이월 3건 처리 표
| 항목 | 출처 | 처리 |
|---|---|---|
| HAR-PAY 도파관 플랜지 WR-42/28 물리정합 | HAR module-fm.md 리스크1항 | **CLOSED** — INT-TST-1에서 실물 불일치 확인→어댑터 4개소 조치→재체결·손실재측정(0.62dB≤0.8dB) 완료 |
| COMM 부품 납기(NCR-COMM-02) | COMM module-fm.md | **후속 이관(운용 준비)** — REQ-AIT-COMM-부품입고 발행, 8×20초 폴링(160초) 무응답(COMM 팀 종료)으로 OPEN 유지. 인도 문서 범위로 판정: module-fm.md가 "정상 생산일정(결함 아님)"으로 명시했고 인도된 COMM-FM-001은 이미 RF시험·PA 완료 상태이므로 INT 통합조립 자체에는 영향 없음. 입고예정일(2026-09-10~15) 경과 후 실물 입고·IQC 완료 확인을 발사 전 운용 준비 점검 항목으로 이관 |
| GS Ka IOT 시험국 조건부 적합 | GS module-fm.md | **후속 이관(IOT 운용 단계)** — REQ-AIT-GS-Ka시험국 발행, 8×20초 폴링(160초) 무응답(GS 팀 종료)으로 OPEN 유지. 인도 문서 범위로 판정: INT-TST-3(지상 AIT)은 GSE 자체 장비로 완결되어 Ka 시험국 확보 여부와 무관함을 확인(int-tst-3.md). GS의 "Ka IOT 시험국"은 발사 후 IOT 운용 단계의 별도 지상국이므로 그 확보 확정은 IOT 착수 전 조달 점검 항목으로 이관 |

## 요청 게시글 처리 요약
- REQ-AIT-HAR-플랜지실측: OPEN(무응답) — 그러나 INT-TST-1 실물 확인으로
  같은 질문이 시험으로 직접 해소되어 재작업 불요.
- REQ-AIT-COMM-부품입고, REQ-AIT-GS-Ka시험국: OPEN(무응답) — 위 표와
  같이 조건부 이관, 통합시험/조립 자체에는 영향 없음을 인도 문서
  범위 내에서 확인.
- NEED-GSE-100V통합전원·NEED-GSE-전개중력보상·NEED-GSE-Ka24채널시험장비:
  GSE 팀이 3건 모두 이행(DONE) — INT-TST-2/1/3에 각각 사용.

## GSE 장비 재사용/신규 판단 요약
| 장비 | 판단 |
|---|---|
| 100V/15kW 통합전원 SCOE | 신규(기존 EPS 모듈 전자부하뱅크는 소스 아닌 부하 시뮬레이터라 용도 다름). DAQ는 재사용 |
| 반사판+SA 동시전개 대형 중력보상 지그 | 신규(기존 MECH 지그는 반사판 단독용 소형). 기존 소형지그는 사전점검용 재사용 |
| Ka 24채널 동시 시험장비 | 신규(기존 PAY 챔버는 단품 baseline용 근접전계 스캐너). 노이즈로딩 NPR장비·챔버 자체는 재사용 |

검증: sysreq 13개 트랙 전량 개별+통합 이중 확인으로 충족, 이월 3건 중
1건 CLOSED(HAR-PAY 플랜지)·2건 조건부 후속 이관(COMM 부품·GS Ka시험국,
통합조립·시험에는 영향 없음 확인), GSE 신규장비 3건 전량 이행 완료
