---
id: EPS-04
title: EPS 통합시험(모의 부하)
status: DONE
parent: M-EPS
source: -
owner: EPS-AIT-01
deliverable: examples/ksat6/deliverables/EPS/integration-test.md
after: EPS-02, EPS-03
track: EPS
started: 2026-08-22 01:28:24
finished: 2026-08-22 01:28:42
---

PCDU(EPS-02)·배터리팩(EPS-03)이 준비되고 AOCS/COMM/PAY의 실제 부하 회신
(REQ-EPS-AOCS/COMM/PAY)이 도착했으므로, 전자부하로 실제 부하 프로파일을
모의해 모선전압·전류·DoD를 최종 검증해야 M-EPS를 인도할 수 있다.
산출물: examples/ksat6/deliverables/EPS/integration-test.md — 실측 프로파일
기반 최종 전력예산 재검증과 모의부하 시험 결과.
검증: sysreq EPS 3항목(28V±4V·155W·DoD≤25%) 실측 기반 재검증 통과(평균91.4W/첨두131W/모선27.6~28.9V/DoD16.6~20.8%), 예산 초과 없음
