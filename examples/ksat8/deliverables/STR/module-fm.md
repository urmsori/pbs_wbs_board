# STR 비행모델 인도 요약 (module-fm.md)

입력: examples/ksat8/deliverables/STR/str-u1-*.md, str-u2-*.md (전 유닛 산출물),
examples/ksat8/deliverables/SE/sysreq.md

## 구성
- STR-U1 중앙 실린더: 설계 풀체인(DSN→ANL-S·ANL-T→CHK→RVW-A/B→RB→CM)+제작
  체인(PUR→IQC→MFG→CLN→INS)+시험 체인(CAL·FAC·PA→TST 정현)
- STR-U2 중계기 패널·장착부: 설계 축약(DSN→ANL-S→CHK→RB)+제작 체인(PUR→IQC→MFG→CLN→INS)

## 외부 인터페이스 (정보 요청 회신 반영)
발신 3건(REQ-STR-PAY-장착·REQ-STR-PROP-탱크·REQ-STR-SA-하중) 전건 실회신 수신
(PROP 탱크습식1,363kg·트러니언4점·PAY 중계기156.6kg·M6그리드·SA 180kg/윙·전개반력
2,500N/3,000N·m) — 설계에 모두 반영, 잠정 가정으로 남은 입력 없음. 수신 5건
(AOCS·COMM·HAR·PROP·TCS→STR) 전건 회신 완료.

## sysreq STR 판정 (수치 인용)
| 항목 | 요구 | 결과 | 판정 |
|---|---|---|---|
| 구조 질량 | ≤380kg | U1 실측246.5kg + U2 실측103.2kg = **349.7kg**(마진30.3kg/8%) | 충족 |
| 1차모드(횡) | ≥30Hz | 해석33.6Hz → **실측(TST-SINE) 31.8Hz**(마진1.8Hz/6%) | 충족 |
| 트러니언(탱크) 국부모드 | ≥60Hz(PROP요구) | 실측61.4Hz(마진2.3%) | 충족 |
| 패널(TWTA) 국부모드 | ≥60Hz(PAY요구) | 해석64.2Hz(마진7%) | 충족 |

## 오픈 리스크
1. [YELLOW] 트러니언 국부모드 마진(2.3%)이 상대적으로 타이트 — RVW-A 조건대로
   TST-SINE에서 실측 재확인 완료했으나, 향후 마진관리 대상으로 계속 추적 권고.
2. REQ-COMM-STR-안테나 회신에서 반사판·SA 전개 과도구간(~100초) TT&C 시야 일시
   간섭 가능성을 언급 — GS/COMM과 운용계획 협의 필요(STR 설계 자체는 영향 없음).

## 검증 요약
sysreq.md "STR: 중앙 실린더 1차모드≥30Hz(횡), 질량≤380kg" 2개 항목 **모두 충족**
(1차모드 실측31.8Hz≥30Hz, 질량 실측349.7kg≤380kg, 마진8%). 전 유닛(U1·U2) 설계·제작
체인 완료, U1 시험 체인(정현) 완료. CM/PUR/CAL/FAC/PA 서비스 요청 전건 처리 완료.
발신 정보요청 3건 전건 실회신 수신, 수신 요청 5건 전건 회신 완료 — 잠정 가정으로
남은 입력 없음(전부 실회신으로 확정).

**최종 검증: 1차모드31.8Hz≥30Hz(실측, 마진6%), 질량349.7kg≤380kg(실측, 마진8%)
— sysreq STR 2개 항목 전부 충족.**
