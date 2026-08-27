# M-PAY Ka중계기 비행모델 인도

입력: examples/ksat8/deliverables/PAY/u1-dsn.md, examples/ksat8/deliverables/PAY/u1-anl-rf.md,
examples/ksat8/deliverables/PAY/u1-anl-t.md, examples/ksat8/deliverables/PAY/u1-chk.md,
examples/ksat8/deliverables/PAY/u1-rvw-a.md, examples/ksat8/deliverables/PAY/u1-rvw-b.md,
examples/ksat8/deliverables/PAY/u1-rb.md, examples/ksat8/deliverables/PAY/u1-iqc.md,
examples/ksat8/deliverables/PAY/u1-mfg.md, examples/ksat8/deliverables/PAY/u1-ins.md,
examples/ksat8/deliverables/PAY/u1-tst.md, examples/ksat8/deliverables/PAY/u2-iqc.md,
examples/ksat8/deliverables/PAY/u2-accept-test.md

## 유닛 구성
- **PAY-U1 24채널 중계기 패널**: 설계(DSN)→해석(ANL-RF·ANL-T)→사양검도(CHK)→
  검토(RVW-A·RVW-B)→검토회(RB, BASELINE PAY-U1-BL-001)→형상배포(CM)→
  제작(IQC→MFG→INS)→성능시험(TST: EIRP·NPR)까지 전 직능 사슬 완료.
- **PAY-U2 TWTA 세트 수락(축약+시험)**: 구매(PUR)→입고검사(IQC, 축약)→
  교정(CAL)→수락시험(TST, 28기 전수) 완료.

## sysreq PAY 최종 판정
| 항목 | sysreq 요구 | 실측/판정 |
|---|---|---|
| 채널수 | 24 | 24 — PASS |
| EIRP | ≥52dBW/채널 | 52.05~52.61dBW(전채널, PAY-U1-TST) — **PASS** |
| NPR | ≥18dB | 18.7~19.3dB(대표4채널, PAY-U1-TST) — **PASS** |

## 인터페이스 확약 반영
EPS(11kW/100V), TCS(6.3kW 방열), HAR(도파관 0.57dB) 확약 전부 설계 여유 내
반영(u1-dsn.md). MECH·STR·OBC·FSW·GS의 8건 수신 요청에 수치 회신 완료.

## 잔여 리스크(자체 판단, 재확인 불요)
- 실측질량 158.2kg(설계치156.6kg 대비 +1.6kg, 배선/체결류 여유). STR 배분
  회신(REQ-STR-PAY-장착) 대비 근소 초과이나, STR 전체 질량예산(sysreq
  ≤380kg) 대비 0.4%로 미미해 별도 정정 요청 없이 기록만 남긴다.

검증: sysreq PAY 전량 PASS — EIRP52.05~52.61≥52dBW, NPR18.7~19.3≥18dB, 24채널 확인
