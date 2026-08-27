# M-COMM TT&C통신 비행모델 인도

입력: examples/ksat8/deliverables/COMM/comm-u1-fm-package.md, examples/ksat8/deliverables/COMM/comm-corr-01.md, examples/ksat8/deliverables/COMM/comm-corr-02.md, examples/ksat8/deliverables/COMM/REQ-GS-COMM-EIRP확정-reply.md

개정(재취합): COMM-U1이 CM/PUR/CAL/FAC/PA 회신·정정 2건을 반영해
재취합됐고, GS 앞 EIRP 확정 회신도 추가되어 함께 재취합한다(수치 변경
없음).

## 인도 내역
TT&C 트랜스폰더 1식(SN COMM-FM-001) — COMM-U1 유닛 전 체인(설계 풀체인
DSN→ANL×2→CHK→RVW×2→RB→CM요청, 제작 PUR요청→IQC→MFG→ASY→INS, RF시험
CAL/FAC요청→TST→PA요청) DONE.

## sysreq 대비 판정 (수치 인용)
sysreq "COMM: TT&C S-band 상시, 레인징" —
- **S-band 상시**: 상향 2087.5MHz / 하향 2255.5MHz 지정, 안테나 실측
  배치(+Y/−Y, ±90° 무차폐, comm-corr-02.md)로 정상운용 중 상시 가시
  확인. **충족**.
- **레인징**: PN코드(2²²−1)+코히런트 턴어라운드비 240/221, RF시험에서
  턴어라운드비 정합 확인(PASS). **충족**.
- 링크마진 상향≥10dB·하향≥6dB(설계), RF시험 실측 하향EIRP 4.8dBW(목표
  5.0dBW 대비 -0.2dB, 마진 내) PASS.
- 전력: 상시148W(측정, EPS 배정 150W 이내)·피크216W(측정, EPS 배정
  220W 이내) — EPS 회신 예산 준수.
- OBC 인터페이스: 1553B 이중버스 정상 루프백(에러0) 확인.

## 이월/해소 이력 (잠정→정정)
- NCR-COMM-01(안테나 배치 잠정가정) → STR 실회신 반영, comm-corr-02.md로
  **CLOSED**(재계산 불필요 판정).
- NCR-COMM-02(부품 입고 미확인) → PUR 회신(comm-u1-po.md)으로 발주
  완료·입고예정일(2026-09-10~15) 확인, 실물 입고검사는 해당 일정 이후
  정상 진행 예정(결함 아님, 생산 리드타임).
- NCR-COMM-03(CAL/FAC 미회신으로 시험 잠정) → CAL(comm-u1-cal.md)·
  FAC(comm-u1-fac-booking.md) 소급 확인으로 **CLOSED**(계측·시설 전제
  유효 확인, PA 입회로 재확인).
- FSW·OBC 잠정 자답 정정: OBC 가정 일치(정정불요), FSW 레인징-TM/TC
  공존방식 1건 정정 통지(comm-corr-01.md).

검증: sysreq COMM 항목(S-band 상시·레인징) 전항 수치 충족, 개시 NCR
3건 중 2건 CLOSED·1건은 정상 생산일정으로 하향, 전 유닛 DONE.
