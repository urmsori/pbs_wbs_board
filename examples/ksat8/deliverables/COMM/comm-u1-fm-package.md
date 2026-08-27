# COMM-U1 TT&C 트랜스폰더 FM 패키지 (취합)

입력: examples/ksat8/deliverables/COMM/comm-u1-design.md, examples/ksat8/deliverables/COMM/comm-u1-linkbudget.md, examples/ksat8/deliverables/COMM/comm-u1-thermal.md, examples/ksat8/deliverables/COMM/comm-u1-checked.md, examples/ksat8/deliverables/COMM/comm-u1-review1.md, examples/ksat8/deliverables/COMM/comm-u1-review2.md, examples/ksat8/deliverables/COMM/comm-u1-baseline.md, examples/ksat8/deliverables/COMM/comm-u1-iqc.md, examples/ksat8/deliverables/COMM/comm-u1-mfg.md, examples/ksat8/deliverables/COMM/comm-u1-asy.md, examples/ksat8/deliverables/COMM/comm-u1-ins.md, examples/ksat8/deliverables/COMM/comm-u1-tst.md, examples/ksat8/deliverables/CM/comm-u1-release.md, examples/ksat8/deliverables/PUR/comm-u1-po.md, examples/ksat8/deliverables/CAL/comm-u1-cal.md, examples/ksat8/deliverables/FAC/comm-u1-fac-booking.md, examples/ksat8/deliverables/PA/comm-u1-tst-witness.md, examples/ksat8/deliverables/COMM/comm-corr-01.md, examples/ksat8/deliverables/COMM/comm-corr-02.md

개정(재취합): CM/PUR/CAL/FAC/PA 회신과 정정 2건(comm-corr-01·02)이 최초
취합 이후 도착해 자식으로 추가되었다 — 규칙 4절에 따라 재취합한다.

## 체인 요약
설계(DSN)→RF해석/열해석(ANL×2)→검도(CHK)→검토(RVW×2)→검토회(RB, baseline
승인)→[CM 형상등록 요청]→[부품구매 요청]→입고검사(IQC)→제작(MFG, SN
COMM-FM-001)→조립(ASY)→최종검사(INS, GO)→[교정/시설 요청]→RF시험(TST,
7항목 PASS)→[PA 입회 요청]. 전 단계 DONE.

## FM 인도 사양 (baseline+시험 확정치)
- 주파수: 상향 2087.5MHz / 하향 2255.5MHz.
- 변조: PCM/PSK/PM(명령 2kbps, TM 상시4kbps/버스트8kbps).
- 레인징: PN코드 + 코히런트 턴어라운드비 240/221.
- SSPA 정격 2W(33dBm), 하향 EIRP 4.8~5.0dBW(시험/설계).
- 전력: 상시148W(측정)/설계상한150W, 피크216W(측정)/설계상한220W.
- IF: MIL-STD-1553B 이중버스(콜드스탠바이), TM 32워드/1Hz, TC 16워드/
  10cmd/s.
- SN COMM-FM-001, 중량 1.8kg.

## NCR 이력 (잠정→정정, module-fm.md에 재기재)
- NCR-COMM-01(안테나 배치 잠정가정): STR 실회신 도착 → comm-corr-02.md로
  **CLOSED**(3dBi 가정이 실측 범위 내, EIRP·링크마진 재계산 불필요).
- NCR-COMM-02(부품 입고 미확인): PUR 회신(comm-u1-po.md)으로 발주
  완료·입고예정(2026-09-10~15) 확인 — 결함이 아니라 정상 생산 리드타임으로
  하향, 실물 입고검사는 해당 일정 이후 진행.
- NCR-COMM-03(CAL/FAC 미회신으로 시험 잠정): CAL(comm-u1-cal.md)·
  FAC(comm-u1-fac-booking.md) 소급 확인 + PA 입회(comm-u1-tst-witness.md)
  대조로 **CLOSED**(계측·시설 전제 유효, 시험기록 7항목 수치 일치 확인).
- FSW·OBC 잠정 자답: comm-corr-01.md로 대조 — OBC 가정 일치(정정불요),
  FSW 레인징-TM/TC 공존방식 1건 정정 통지.

검증: sysreq "COMM: TT&C S-band 상시, 레인징" — S-band(2087.5/2255.5MHz)
상시 링크 확정, PN레인징+240/221 확정. 링크마진(상향≥10dB·하향≥6dB),
RF시험 7항목 PASS로 수치 인용 판정. NCR 3건 중 2건 CLOSED, 1건은 정상
생산일정으로 하향 — 전 유닛 및 지원부서 회신 반영 재취합 완료.
