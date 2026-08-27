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

## 검증 요약
sysreq.md "STR: 1차구조 ≤45kg, 1차모드 ≥35Hz(SAR 안테나 장착 상태), 준정적 10g" 3개 항목 중
질량·준정적10g **2개 충족**, 1차모드 **1개 미충족(오픈 NCR)**. 전 유닛(U1·U2) 설계·제작 체인
완료, U1 시험 체인 완료(정현·랜덤). CM/PUR/CAL/FAC/PA 서비스 요청 전건 처리 완료.
