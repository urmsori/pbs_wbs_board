입력: examples/ksat7/deliverables/PROP/unit1-prop-design.md, examples/ksat7/deliverables/PROP/unit1-performance-analysis.md,
examples/ksat7/deliverables/PROP/unit1-drawing-check.md, examples/ksat7/deliverables/PROP/unit1-review-board.md,
examples/ksat7/deliverables/PROP/unit1-iqc.md, examples/ksat7/deliverables/PROP/unit1-mfg.md,
examples/ksat7/deliverables/PROP/unit1-ins.md, examples/ksat7/deliverables/PROP/ignition-leak-test.md,
examples/ksat7/deliverables/STR/prop-mounting-icd.md, examples/ksat7/deliverables/EPS/hall-thruster-power-confirmation.md,
examples/ksat7/deliverables/PROP/thruster-operating-profile.md, examples/ksat7/deliverables/SE/sysreq.md

# PROP 비행모델(FM) 인도 — module-fm.md

## 구성
PROP-U1(홀추력기 시스템: 300W급 추력기·제논탱크2L·압력조절기·래치밸브×2·
배관) 단일 유닛. 설계 축약체인(DSN→ANL-T→CHK→RB→CM) → 수락·조립 체인
(PUR→IQC→MFG(조립)→INS) → 점화·누설시험(CAL·FAC→TST) 전 단계 완료.

## sysreq PROP 행 충족 판정 (점화·누설시험 실측, ignition-leak-test.md)
| 항목 | 요구(sysreq) | 실측/판정 | 결과 |
|---|---|---|---|
| Δv | 25 m/s | 25.9 m/s(실측Isp1,485s, 충전1.0kg 기준) | 충족(여유3.6%) |
| 추력기급 | 300W급 | 300W(300V/1.0A) 점화 10사이클 정상 | 충족 |
| 배관 누설 | (설계기준) | <5e-9 atm·cc/s | 합격 |

## 인터페이스 확인
- STR: 장착부(-Z면, M6×4, PCD120mm) MS+0.22·1차모드37.2Hz≥35Hz 확인
  (REQ-PROP-STR, DONE).
- EPS: 300W 연속공급 EOL예산 내 확약(REQ-PROP-EPS, DONE), 운전프로파일
  (캠페인당 90분, SAR-추력 상호배타 운용)을 EPS 요청(REQ-EPS-PROP)에 회신,
  동시부하 2.1kW 시나리오 배제.

## 리스크·잔여사항
- 설계 단계 Δv여유는 낮았으나(2.4%) CHK 단계에서 제논 충전량 0.62kg→1.0kg
  상향 권고를 반영해 탱크여유(77%→0.1kg 잔여)로 실측 여유 3.6% 확보.
- 태양활동 고조기 대비 추가 Δv 소요 발생 시 탱크 잔여여유(0.1kg)로 대응 가능.

## 게시글 이력
설계 4건(DSN·ANL-T·CHK·RB, 축약체인) + 조립 3건(IQC·MFG·INS) + 시험 1건(TST)
= PROP track 8건. 서비스 요청 4건(CM·PUR·CAL·FAC 각 1건) 전건 DONE. 협상
REQ 2건(PROP→STR, PROP→EPS) 전건 DONE, 역방향 수신 REQ 1건(EPS→PROP) 회신 DONE.

검증: sysreq PROP 행 Δv25.9m/s≥25m/s(여유3.6%)·300W급 점화정상 실측 충족,
STR·EPS 인터페이스 상호 확인 완료
