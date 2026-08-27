---
id: AIT-RX-1
title: 구조·기구·하니스(STR/MECH/HAR) 인도 수령·판정
status: DONE
parent: INT
source: INT
owner: AIT-QA-01
deliverable: examples/ksat8/deliverables/AIT/rx-1.md
after: M-STR, M-MECH, M-HAR
track: AIT
started: 2026-08-27 04:22:22
finished: 2026-08-27 04:26:30
---

왜: 통합(INT)에 앞서 구조(STR)·기구(MECH)·하니스(HAR) 3개 트랙의 비행모델
인도 문서를 수령해 sysreq 판정·이월 리스크를 확인해야 뒤이은 통합시험
(INT-TST-1 기계·정렬)의 입력이 확정된다.

수령 대상: STR/MECH/HAR module-fm.md 3건.
확인 사항:
1) STR 349.7kg≤380kg·1차모드31.8Hz≥30Hz — 충족 확인.
2) MECH 반사판2기·SA힌지2윙 전개, 단일고장허용 — 충족 확인.
3) HAR 100V절연·도파관손실0.58dB≤0.8dB — 충족 확인, 단 이월 리스크
   4건(HAR module-fm.md「리스크·후속조치」) 중 INT 이관 대상 식별:
   - HAR-PAY 도파관 플랜지 WR-28상당(제작)↔WR-42(PAY 정식규격) 물리
     정합 미확인 → INT-TST-1에서 실물 체결 확인 필요(전기 성능은 이미
     검증 완료, 물리 정합만 남음).
   - PA 입회 미확인(PA-HAR-U1), STR 라우팅 정식회신 미접수는 HAR 자체
     기록으로 남아 있고 STR module-fm.md에 대응 리스크 언급 없음(STR
     경로 확정 완료로 판단) — INT 재작업 불요, 기록만 유지.
검증: STR·MECH·HAR sysreq 전량 충족, HAR 플랜지 이월건 REQ OPEN으로 INT-TST-1 이관
