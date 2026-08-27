# REQ-OBC-PAY-TM 회신 — 중계기 TM 점수

입력: examples/ksat8/deliverables/PAY/u1-dsn.md, examples/ksat8/board/REQ-OBC-PAY-TM.md

1) 채널당 TM 점수: **15점**(EIRP추정1, NPR1, TWTA전류1, TWTA온도2, 수신기
   상태1, 스위치행렬상태2, 기타상태7) × 24채널 = 360점 + 공통(예비계열
   상태·공통전원 등) 40점 = **총 400점**.
2) 갱신 주기: 전류·상태(고속) 1Hz, 온도·EIRP추정(저속) 0.1Hz.
3) 이산/아날로그 비율: 아날로그(전류·온도·EIRP) 약 30%, 이산(상태·행렬)
   약 70%.

검증: 총400점(채널당15점×24+공통40) 회신, 갱신주기 1Hz/0.1Hz 구분
