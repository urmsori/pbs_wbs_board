# MECH 비행모델 인도 요약 (module-fm.md)

입력: examples/ksat7/deliverables/MECH/mech-u1-*.md, mech-u2-*.md (전 유닛 산출물),
examples/ksat7/deliverables/SE/sysreq.md

## 구성
- MECH-U1 SAR 2단 전개기구: 설계 풀체인(DSN→ANL-S·ANL-T→CHK→RVW-A/B→RB→CM)+제작
  체인(PUR→IQC→MFG→CLN→INS)+전개시험(FAC→TST)
- MECH-U2 SA 전개힌지: 설계 축약(DSN→ANL-S→CHK→RB)+제작 체인(PUR→IQC→MFG→CLN→INS)

## sysreq MECH 판정 (수치 인용)
| 항목 | 요구 | 결과 | 판정 |
|---|---|---|---|
| 전개충격 | ≤40g | 잠정설계(관성4.2kg·m² 가정) 34.5g → PAY 실측 ICD(관성46.7/44.0kg·m²)
  반영 재해석(댐퍼 재조정 후) 36.4g → **실측(TST) 37.1g** | 충족(마진 2.9g, 7.3%) |
| 단일고장 허용 | 필수 | FMEA 확인(설계) + TST 단일고장 모사(릴리즈 1계열 강제비활성) 정상
  전개 확인 | 충족 |
| SA 전개 후 1차모드 (SA항목 참고) | ≥0.5Hz | MECH-U2 힌지강성 8000N·m/rad 기준 해석 0.62Hz
  (SA 실측 관성 회신 대기, 잠정치 기준) | 충족(잠정, REQ-MECH-SA 회신 반영 필요) |

## 오픈 리스크
1. [YELLOW] MECH-U1 전개충격 마진 7.3%로 STR 대비 타이트 — 댐퍼 점성계수 재조정(+180%/+165%)
   후 실측 확인 완료(37.1g), 추가 마진 확보는 rev.2 검토 권고.
2. REQ-MECH-SA(SA 3윙 패널 실측 질량·관성) 회신 미수신 — MECH-U2 힌지강성(8000N·m/rad, 잠정)은
   SA측 REQ-SA-MECH 무응답시 채택치와 동일하게 유지했으나, 실측 회신 시 힌지 사이징 재검증 필요.
3. STR-U1 1차모드 미충족(NCR, STR module-fm.md 참조)은 MECH-U1 SAR 안테나 전개기구가 장착되는
   모체 구조의 강성 이슈로, MECH 설계 자체에는 영향 없으나 시스템 레벨 인터페이스로 공유 기록.

## 검증 요약
sysreq.md "MECH: SAR 2단 전개·SA 3윙 전개, 전개충격 ≤40g, 단일고장 허용" 항목 **모두 충족**
(전개충격 37.1g≤40g 실측, 단일고장 허용 실측 확인). 전 유닛(U1·U2) 설계·제작 체인 완료, U1
전개시험 완료. CM/PUR/FAC 서비스 요청 전건 처리 완료.
