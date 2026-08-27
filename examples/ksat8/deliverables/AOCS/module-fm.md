# M-AOCS 자세제어 비행모델 인도

입력: examples/ksat8/deliverables/AOCS/u1-dsn.md, examples/ksat8/deliverables/AOCS/u1-anl-ctl.md,
examples/ksat8/deliverables/AOCS/u1-anl-dist.md, examples/ksat8/deliverables/AOCS/u1-chk.md,
examples/ksat8/deliverables/AOCS/u1-rvw-a.md, examples/ksat8/deliverables/AOCS/u1-rvw-b.md,
examples/ksat8/deliverables/AOCS/u1-rb.md, examples/ksat8/deliverables/AOCS/u2-iqc.md,
examples/ksat8/deliverables/AOCS/u2-accept-test.md, examples/ksat8/deliverables/AOCS/u1-hil-test.md

## 유닛 구성
- **AOCS-U1 지향 제어계**: 설계(DSN)→해석(ANL-CTL·ANL-DIST)→사양검도(CHK)→
  검토(RVW-A·RVW-B)→검토회(RB, BASELINE AOCS-U1-BL-001)→형상배포(CM)→
  HIL 폐루프 시험(TST)까지 전 직능 사슬 완료.
- **AOCS-U2 센서·휠 수락(축약)**: 구매(PUR)→입고검사(IQC, 축약)→교정(CAL)→
  수락시험(TST) 완료.

## sysreq AOCS 최종 판정
| 항목 | sysreq 요구 | 실측/판정 |
|---|---|---|
| 안테나 지향 | 0.05°(3σ) | **0.0305°(HIL 실측) — PASS(마진39%)** |
| 액추에이터 | 모멘텀휠+이온추력기 언로딩 | 휠4기(3+1)+PROP 이온추력기 언로딩 인터페이스 확정 |

## 정정 이력
- STR 정렬 회신이 설계 착수 시 대기타임아웃(50arcsec 잠정) 후 도착 —
  FIX-AOCS-U1-STR정렬반영으로 정정(실측 반영 21.2arcsec, 마진 31.6%→36.4%
  개선). BASELINE 유지.

검증: sysreq AOCS 항목 전량 PASS — 지향0.0305°≤0.05°(마진39%), 휠+이온추력기
언로딩 인터페이스(PROP) 확정
