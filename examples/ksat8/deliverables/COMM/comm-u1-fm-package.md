# COMM-U1 TT&C 트랜스폰더 FM 패키지 (취합)

입력: examples/ksat8/deliverables/COMM/comm-u1-design.md, examples/ksat8/deliverables/COMM/comm-u1-linkbudget.md, examples/ksat8/deliverables/COMM/comm-u1-thermal.md, examples/ksat8/deliverables/COMM/comm-u1-checked.md, examples/ksat8/deliverables/COMM/comm-u1-review1.md, examples/ksat8/deliverables/COMM/comm-u1-review2.md, examples/ksat8/deliverables/COMM/comm-u1-baseline.md, examples/ksat8/deliverables/COMM/comm-u1-iqc.md, examples/ksat8/deliverables/COMM/comm-u1-mfg.md, examples/ksat8/deliverables/COMM/comm-u1-asy.md, examples/ksat8/deliverables/COMM/comm-u1-ins.md, examples/ksat8/deliverables/COMM/comm-u1-tst.md

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

## 이월 항목 (module-fm.md에 재기재)
- NCR-COMM-01: 안테나 배치·이득(LGA×2, 3dBi)이 STR 미회신으로 잠정 가정.
- NCR-COMM-02: 부품 입고 실측(PUR 미회신)이 체크리스트 확정 단계에 머묾.
- NCR-COMM-03: RF시험(CAL/FAC 미회신)이 가정 기반 잠정 성적서.

검증: sysreq "COMM: TT&C S-band 상시, 레인징" — S-band(2087.5/2255.5MHz)
상시 링크 확정, PN레인징+240/221 확정. 링크마진(상향≥10dB·하향≥6dB),
RF시험 7항목 PASS로 수치 인용 판정. 단 NCR 3건은 잠정(추후 정정 게시글
필요).
