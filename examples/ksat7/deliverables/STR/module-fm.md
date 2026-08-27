# STR 비행모델 인도 요약 (module-fm.md)

입력: examples/ksat7/deliverables/STR/str-u1-*.md, str-u2-*.md (전 유닛 산출물),
examples/ksat7/deliverables/SE/sysreq.md

## 구성
- STR-U1 1차구조체: 설계 풀체인(DSN→ANL-S·ANL-T→CHK→RVW-A/B→RB→CM)+제작 체인(PUR→IQC→MFG→CLN→INS)
  +시험 체인(CAL·FAC·PA→TST 정현·랜덤)
- STR-U2 SAR 장착 브래킷: 설계 축약(DSN→ANL-S→CHK→RB)+제작 체인(PUR→IQC→MFG→CLN→INS)

## sysreq STR 판정 (수치 인용)
| 항목 | 요구 | 결과 | 판정 |
|---|---|---|---|
| 1차구조 질량 | ≤45kg | 41.3kg(U1 실측)+4.9kg(U2 실측)=46.2kg 총합이나, sysreq 항목은
  "1차구조 ≤45kg"로 U1(1차구조체) 단독 기준 적용 시 **41.3kg 충족**(U2 브래킷은 2차구조 항목,
  STR-U1-DSN 질량예산 내 브래킷·체결류 6.5kg에 포함되어 이중계상 아님) | 충족 |
| 1차모드(SAR 안테나 장착 상태) | ≥35Hz | 잠정설계(38kg 가정) 해석 37.2Hz → PAY 실측 ICD(안테나
  72.0kg, 3점 킨매틱) 반영 재해석 29.5Hz → **실측(TST-SINE) 30.4Hz** | **미충족(NCR/RED)** |
| 준정적 10g | 손상 없음 | ANL-S MS>0 다수, TST 정현시험 손상·영구변형 없음(랜덤시험 후에도
  모드 변화 -0.2Hz로 미미, 워크맨십 결함 없음) | 충족 |

## 오픈 리스크 / 비적합
1. **[RED, NCR] 1차모드 미충족**: 안테나 실측질량(72.0kg)이 초기 설계 가정(38kg)보다 커
   1차모드가 30.4Hz로 실측, sysreq 35Hz 미달(부족 4.6Hz). STR-U1-ANL-S2에서 권고한 상판·튜브
   보강 및 3점 킨매틱 인터페이스(PCD400mm, 로컬강성≥50N/µm) 반영 재설계가 rev.2로 이관됨.
   현재 비행형상(rev.1)은 이 항목 미충족 상태로 인도됨 — SE/PAY와 후속 협의 필요.
2. STR-U2 브래킷 실측 4.9kg는 REQ-STR-PAY 회신(3점 킨매틱 PCD400mm 8-M8)과 형상이 다른
   잠정설계(4점 PCD500 M10) 기준 제작됨 — rev.2에서 인터페이스 재설계 시 브래킷도 재설계 필요.

## 검증 요약 (rev.1)
sysreq.md "STR: 1차구조 ≤45kg, 1차모드 ≥35Hz(SAR 안테나 장착 상태), 준정적 10g" 3개 항목 중
질량·준정적10g **2개 충족**, 1차모드 **1개 미충족(오픈 NCR)**. 전 유닛(U1·U2) 설계·제작 체인
완료, U1 시험 체인 완료(정현·랜덤). CM/PUR/CAL/FAC/PA 서비스 요청 전건 처리 완료.

## rev.2 갱신 (NCR 해소)
입력: examples/ksat7/deliverables/STR/str-u1-r2-dsn.md, str-u1-r2-anl.md, str-u1-r2-mfg.md,
str-u1-r2-tst.md, str-u2-r2-mfg.md, str-u2-r2-ins.md

재작업 체인(정상 경로, DONE 원본 미변경): STR-U1-R2-DSN(보강 재설계, source=STR-U1-TST-SINE)
→ STR-U1-R2-ANL(재해석 예측36.8Hz) → CM-STR-U1-R2(도면 재배포) → STR-U1-R2-MFG(보강 개조)
→ FAC-STR-U1-R2(시설 재예약) → STR-U1-R2-TST(정현 재시험). 병행: STR-U2-R2-MFG(3점
PCD400/8-M8 재제작, source=REQ-STR-PAY) → STR-U2-R2-INS(검사).

| 항목 | 요구 | rev.1 | rev.2 | 판정 |
|---|---|---|---|---|
| 1차구조 질량 | ≤45kg | 41.3kg | **44.6kg**(실측, 마진 0.4kg) | 충족(타이트) |
| 1차모드(SAR 안테나 장착) | ≥35Hz | 30.4Hz(NCR) | **36.1Hz**(실측, 마진+1.1Hz/3.1%) | **충족 — NCR CLOSED** |
| 준정적 10g | 손상 없음 | 충족 | 충족(재확인, 손상·영구변형 없음) | 충족 |

STR-U2 브래킷도 3점 킨매틱 PCD400mm/8-M8로 재제작 완료(실측5.4kg), STR-U1 rev.2 인터페이스와
정합 확인(로컬강성 62N/µm≥50N/µm 요구). rev.1에서 남겼던 오픈 비적합 2건 중 1차모드는
CLOSED, 인터페이스 형상 불일치는 재제작으로 해소. 질량마진(0.4kg)은 향후 마진관리 대상으로
계속 추적.

**최종 검증(rev.2): 1차모드 36.1Hz≥35Hz(실측, NCR CLOSED), 질량44.6kg≤45kg, 준정적10g 충족
— sysreq STR 3개 항목 전부 충족.**
