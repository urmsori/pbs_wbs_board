---
id: AIT-RX-2
title: 전력·전개·열·추진(EPS/SA/TCS/PROP) 인도 수령·판정
status: DONE
parent: INT
source: INT
owner: AIT-QA-01
deliverable: examples/ksat8/deliverables/AIT/rx-2.md
after: M-EPS, M-SA, M-TCS, M-PROP
track: AIT
started: 2026-08-27 04:22:22
finished: 2026-08-27 04:26:30
---

왜: 전력(EPS)·태양전지판(SA)·열제어(TCS)·추진(PROP) 4개 트랙의 비행모델
인도 문서를 수령해 sysreq 판정을 확인해야 INT-TST-2(전기 통합부하)·
INT-TST-4(환경·열)의 입력이 확정된다.

수령 대상: EPS/SA/TCS/PROP module-fm.md 4건.
확인 사항:
1) EPS 100V±2V·15kW배전(14,420W 실증)·이클립스2.4kWh(usable2.44kWh) — 충족.
2) SA EOL16kW(16,120W, 마진0.75%)·1차모드≥0.1Hz(0.118Hz) — 충족(EOL 마진
   낮음, 운용 단계 관찰 권고 — INT 재작업 대상 아님).
3) TCS 방열6kW(부하5.04kW/용량6.3kW)·작동범위-10~+60°C(TVAC실측-9~+52°C)
   — 충족. TWTA 6kW 방열 성능은 INT-TST-4에서 통합 열시험으로 재확인.
4) PROP Δv합계2,250m/s(1,500+750) 정확 일치 — 충족.
잠정/이월 항목 없음(4개 트랙 module-fm.md 전량 "잠정 없음" 또는 해소
완료로 명시) — 세부 기록 요청 불요.
검증: EPS·SA·TCS·PROP sysreq 전량 충족, 이월 리스크 없음
