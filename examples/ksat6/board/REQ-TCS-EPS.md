---
id: REQ-TCS-EPS
title: 히터 전력 할당 확정 요청
status: DONE
parent: M-TCS
source: TCS-01
owner: EPS-DSN-02
deliverable: examples/ksat6/deliverables/EPS/heater-channel-confirmation.md
after: -
track: EPS
started: 2026-08-22 01:23:34
finished: 2026-08-22 01:23:58
---

TCS 열해석(TCS-01)에서 히터 예산 25W(sysreq ≤25W)를 채널별로 배분했다
(배터리 10W·추진탱크 8W·광학부 4W·마진 3W). EPS PCDU가 이 채널 구성을
배전(스위칭·전류제한)할 수 있는지 확인·확정이 필요하다 — TCS 단독으로는 배전
회로 여유를 알 수 없다.
산출물: EPS 팀이 채널별 배전 가능 여부(회로·차단기 스펙)를 확인한 문서
(examples/ksat6/deliverables/EPS/ 아래, EPS 팀이 경로를 정한다).
검증: TCS 25W 히터예산 4채널 배전 가능 확인(퓨즈 정격 여유)

정정(PM-01, v3.0): 취합 부모를 TCS-01(낳은 설계)에서 M-TCS(취합될 모듈)로 정정 — 원인은 source가 담는다(3절).
