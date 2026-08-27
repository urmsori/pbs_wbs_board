---
id: AIT-RX-4
title: 자세제어·탑재체(AOCS/PAY) 인도 수령·판정
status: DONE
parent: INT
source: INT
owner: AIT-QA-02
deliverable: examples/ksat8/deliverables/AIT/rx-4.md
after: M-AOCS, M-PAY
track: AIT
started: 2026-08-27 04:22:22
finished: 2026-08-27 04:26:30
---

왜: 자세제어(AOCS)·탑재체(PAY) 2개 트랙의 비행모델 인도 문서를 수령해
sysreq 판정을 확인해야 INT-TST-1(정렬)·INT-TST-3(RF 종단간 Ka)의 입력이
확정된다.

수령 대상: AOCS/PAY module-fm.md 2건.
확인 사항:
1) AOCS 지향0.0305°≤0.05°(마진39%), 휠+이온추력기 언로딩 인터페이스
   확정 — 충족.
2) PAY 24채널·EIRP52.05~52.61≥52dBW·NPR18.7~19.3≥18dB — 충족(전채널
   PASS). 실측질량 158.2kg(+1.6kg vs 설계)는 PAY 자체 판단으로 재확인
   불요 기록.
잠정/이월 항목 없음(AOCS module-fm.md 정정 이력은 설계 단계에서 이미
BASELINE 유지로 종결, PAY 잔여 리스크는 자체 판단으로 재확인 불요 명시)
— 세부 기록 요청 불요.
검증: AOCS·PAY sysreq 전량 충족, 이월 리스크 없음
