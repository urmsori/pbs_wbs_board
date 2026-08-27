입력: examples/ksat7/deliverables/TCS/unit1-thermal-design.md, examples/ksat7/deliverables/TCS/unit1-thermal-analysis.md,
examples/ksat7/deliverables/TCS/unit1-structural-analysis.md, examples/ksat7/deliverables/TCS/unit1-drawing-check.md,
examples/ksat7/deliverables/TCS/unit1-review-a.md, examples/ksat7/deliverables/TCS/unit1-review-b.md,
examples/ksat7/deliverables/TCS/unit1-review-board.md, examples/ksat7/deliverables/TCS/unit1-iqc.md,
examples/ksat7/deliverables/TCS/unit1-mfg.md, examples/ksat7/deliverables/TCS/unit1-cln.md,
examples/ksat7/deliverables/TCS/unit1-ins.md, examples/ksat7/deliverables/TCS/tvac-test.md,
examples/ksat7/deliverables/PAY/tcs-thermal-profile.md, examples/ksat7/deliverables/EPS/heater-channel-confirmation.md,
examples/ksat7/deliverables/SE/sysreq.md

# TCS 비행모델(FM) 인도 — module-fm.md

## 구성
TCS-U1(SAR 열관리: 히트파이프4식·라디에이터0.35㎡·MLI·히터/서미스터3채널)
단일 유닛. 설계 풀체인(DSN→ANL-T·ANL-S→CHK→RVW-A/B→RB→CM) → 제작 체인
(PUR→IQC→MFG→CLN→INS) → 열진공 검증(CAL·FAC·PA→TST) 전 단계 완료.

## sysreq TCS 행 충족 판정 (TVAC 4사이클 실측, tvac-test.md)
| 항목 | 요구(sysreq) | 실측 | 판정 |
|---|---|---|---|
| 전 유닛 온도(고온) | ≤+45°C | +43.5°C(EOL열화 포함) | 충족(여유1.5°C) |
| 전 유닛 온도(저온) | ≥-15°C | -13.8°C | 충족(여유1.2°C) |
| 배터리 온도 | 5~+25°C | +7.5~+9.2°C | 충족 |
| 히터 소비 | ≤40W | 38.6W | 충족(여유1.4W) |

## 인터페이스 확인
- PAY: 첨두발열 270W×5s×18회/궤도, 0.30㎡ 확정(REQ-TCS-PAY, DONE) — 설계 반영.
- EPS: 히터 40W 3채널 배전 가능 확인(REQ-TCS-EPS, DONE) — 실측 38.6W로 충족.
- PAY로부터 역방향 요청(REQ-PAY-TCS)도 동일 수치로 상호 확인, DONE 회신.

## 리스크·잔여사항
- 히트파이프 단일고장 시 90W/식>정격80W/식 — FM은 수용(발생확률 낮음),
  차기 블록에서 정격 상향 검토 권고(RB 기록).
- EOL 코팅 열화는 TVAC에서 α_EOL=0.12 가정 실측 재확인 완료 — RB 조건 해소.

## 게시글 이력
설계 7건(DSN·ANL-T·ANL-S·CHK·RVW-A·RVW-B·RB) + 제작 4건(IQC·MFG·CLN·INS) +
시험 1건(TST) = TCS track 12건. 서비스 요청 5건(CM·PUR·CAL·FAC·PA) 전건 DONE.
협상 REQ 2건(TCS→PAY, TCS→EPS) 전건 DONE, 역방향 수신 REQ 1건(PAY→TCS) 회신 DONE.

검증: sysreq TCS 행 4항목 전부 TVAC 4사이클 실측 충족(고온+43.5°C·저온-13.8°C·
배터리+7.5~9.2°C·히터38.6W≤40W), PAY·EPS 인터페이스 상호 확인 완료
