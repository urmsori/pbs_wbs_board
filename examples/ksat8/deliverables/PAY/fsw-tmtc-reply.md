# REQ-FSW-PAY-TMTC 회신 — 중계기 TM/TC·채널 스위칭 명령셋

입력: examples/ksat8/deliverables/PAY/u1-dsn.md, examples/ksat8/board/REQ-FSW-PAY-TMTC.md

## TM 목록(발췌, 채널당)
- EIRP(dBW, 추정치), NPR(dB, 시험모드시), TWTA 전류(A)·온도(°C) x2점,
  스위치 행렬 상태(입출력 경로) — 채널당 약 6점 x24=144점(상세는 OBC 회신 참조).

## TC 목록(발췌)
- 입력/출력 스위치 행렬 전환(좌표 지정), TWTA ON/OFF, TWTA 이득설정(OBO 조정).

## 채널 스위칭 명령셋
- 좌표 표기: `SWM[in:1-4][out:1-28]` — 입력 4계열 × 출력 28포트(24운용+4예비).
- 순차 실행 규칙: **동시 전환 금지, 1채널씩 순차**(전환 간격 ≥100ms) — 인러시
  중첩 방지(EPS 소프트스타트 상승시간 10ms 대비 10배 여유).

검증: TM144점(발췌)·TC·좌표표기·순차규칙(100ms 간격) 회신
