# AOCS 비행모델 인도 — module-fm
입력: examples/ksat7/deliverables/AOCS/u1-yaw-steering-design.md, u1-stability-analysis.md,
u1-design-check.md, u1-review-a.md, u1-review-b.md, u1-review-board.md, u1-hil-test.md,
u2-iqc.md, u2-ins.md, u2-accept-test.md, examples/ksat7/deliverables/STR/aocs-alignment-spec.md

## 구성 유닛
- **AOCS-U1 요 스티어링 제어계**: 설계(DSN)→안정성해석(ANL-S)→검도(CHK)→검토
  A/B(RVW-A/B)→검토회(RB, 승인)→CM 배포 요청, HIL 검증(CAL 요청→TST).
- **AOCS-U2 센서·반작용휠**: 구매요청(PUR)→입고검사(IQC)→최종검사(INS)→
  수락시험(CAL 요청→TST).

## ICD 협상
- REQ-AOCS-STR(→STR): 정렬기준면 수직도·열드리프트 7.3arcsec≤배분12.6arcsec,
  안테나1차모드37.2Hz≫요구4.0Hz — 회신 수신, 조건 해소.
- REQ-FSW-AOCS(←FSW 수신): 제어주기10Hz·신호5종 회신.

## sysreq AOCS 최종 판정 (u1-hil-test.md 인용)
| 항목 | 요구 | 실측 | 판정 |
|---|---|---|---|
| 지향정확도(3σ) | 0.02° | 0.0183° | PASS(마진8.5%) |
| 요 스티어링 | ±4° | ±4.0° | PASS |
| 안정도(노출시간 중) | 0.003°/s | 0.00251°/s | PASS(마진16.3%) |

## 서비스 요청 처리
CM-AOCS-U1(배포), PUR-AOCS-U2(구매), CAL-AOCS-U2(수락시험 교정),
CAL-AOCS-U1(HIL시험 교정) — 4건 전량 DONE.

## 결론
sysreq AOCS 3개 항목 전량 충족. AOCS 비행모델 인도 완료.
