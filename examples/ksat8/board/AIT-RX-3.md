---
id: AIT-RX-3
title: 컴퓨터·SW·통신·지상국(OBC/FSW/COMM/GS) 인도 수령·판정
status: DONE
parent: INT
source: INT
owner: AIT-QA-02
deliverable: examples/ksat8/deliverables/AIT/rx-3.md
after: M-OBC, M-FSW, M-COMM, M-GS
track: AIT
started: 2026-08-27 04:22:22
finished: 2026-08-27 04:26:30
---

왜: OBC·FSW·COMM·GS 4개 트랙의 비행모델 인도 문서를 수령해 sysreq 판정을
확인해야 INT-TST-3(RF 종단간: TT&C+Ka)의 입력이 확정되고, 이월 항목
(COMM 부품 납기, GS Ka IOT 시험국 조건부 적합)의 처리 방향을 정할 수 있다.

수령 대상: OBC/FSW/COMM/GS module-fm.md 4건.
확인 사항:
1) OBC TM8,000점·TC2,000점·이중화절체420ms — 충족(단 REQ-OBC-COMM-IF가
   COMM 미확정 시점 잠정 회신으로 남아 있음 — COMM-U1이 이후 확정됐으므로
   INT 단계 정합 재확인 필요 여부 판단).
2) FSW 7건 TM/TC 요청 회신(1건 COMM 잠정, AOCS/PAY 상세 미확보) — INT
   단계에서 COMM 확정치와의 정합, AOCS/PAY TM 상세는 별도 요청 필요 여부
   판단.
3) COMM S-band상시·레인징 충족, NCR 3건 중 2건 CLOSED·1건(부품 입고,
   NCR-COMM-02)은 발주 완료·입고예정 2026-09-10~15로 하향 — **인도 문서
   수준에서는 "예정일" 확인까지만 가능, 실제 입고·IQC 완료 여부는
   module-fm.md에 없음 → 요청 필요**.
4) GS 관제소 적합성(조건부: Ka IOT 시험국 신규/임차 확보 전제)·IOT
   30일계획 — **Ka 시험국 확보 확정 여부는 module-fm.md에 "추후 조달
   확정 시 정정 게시글" 예정으로만 적혀 있어 현재 상태 불명 → 요청
   필요**.

세부 기록 요청 예정: REQ-AIT-COMM-부품입고, REQ-AIT-GS-Ka시험국(본 Work가
source).
검증: OBC·FSW·COMM·GS sysreq 전량 충족, COMM부품·GS Ka시험국 REQ OPEN으로 조건부 이관
