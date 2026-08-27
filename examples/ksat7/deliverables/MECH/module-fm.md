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

## 검증 요약 (rev.1)
sysreq.md "MECH: SAR 2단 전개·SA 3윙 전개, 전개충격 ≤40g, 단일고장 허용" 항목 **모두 충족**
(전개충격 37.1g≤40g 실측, 단일고장 허용 실측 확인). 전 유닛(U1·U2) 설계·제작 체인 완료, U1
전개시험 완료. CM/PUR/FAC 서비스 요청 전건 처리 완료.

## rev.2 갱신 (SA 힌지 1차모드 NCR 해소)
입력: examples/ksat7/deliverables/MECH/mech-u2-anl-s2.md(오픈 리스크 원인), mech-u2-r2-dsn.md,
mech-u2-r2-mfg.md, mech-u2-r2-tst.md

rev.1 마감 이후(M-MECH DONE 처리 후) REQ-MECH-SA 회신치(관성10.1kg·m², 잠정2.5kg·m² 대비
4배) 재검토에서 MECH-U2-ANL-S2가 SA 힌지 전개후 1차모드 약0.31Hz<0.5Hz 미충족(RED)을
확인 — DONE 처리된 rev.1 게시글·산출물은 되돌리지 않고 신규 재작업 체인으로 기록:
MECH-U2-R2-DSN(강성 증대 재설계, source=MECH-U2-ANL-S2) → MECH-U2-R2-MFG(힌지 개조) →
MECH-U2-R2-TST(전개·강성 재검증).

REQ-MECH-SA2로 SA에 관성·질량 재확인을 요청했으나 4×15초 폴링 무응답(SA 팀 세션 종료) —
기존 REQ-MECH-SA 회신치(질량7.6kg/윙, 관성10.1kg·m²)를 정본으로 채택해 설계 진행
(REQ-MECH-SA2는 board에 OPEN으로 잔류, 무응답 처리 기록).

| 항목 | 요구 | rev.1 | rev.2 | 판정 |
|---|---|---|---|---|
| SA 힌지 강성 | - | 8000 N·m/rad | **24,600 N·m/rad**(실측, 목표25,000 대비-1.6%) | - |
| SA 전개 후 1차모드 | ≥0.5Hz | 0.62Hz(해석,잠정관성) → 0.31Hz(재검증,실측관성) | **0.53Hz**(실측, 마진+0.03Hz/6%) | **충족 — NCR CLOSED** |
| 전개충격(MECH-U1, 참고) | ≤40g | 37.1g(실측) | 변경 없음(rev.2 대상 아님) | 충족 |

**최종 검증(rev.2): SA 힌지 전개후 1차모드 0.53Hz≥0.5Hz(실측, NCR CLOSED). MECH-U1 전개충격
37.1g≤40g·단일고장허용은 rev.1대로 유지 — sysreq MECH 전 항목(전개충격·단일고장·SA 참고
1차모드) 충족.**
