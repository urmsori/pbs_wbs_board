---
id: REQ-FSW-EPS
title: "[FSW→EPS] 배터리 관리 파라미터(충전 종지·저전압 임계) 요청"
status: DONE
parent: FSW-EPS
source: FSW-EPS
owner: EPS-DSN-02
deliverable: examples/ksat6/deliverables/EPS/battery-mgmt-params-for-fsw.md
after: -
track: EPS
started: 2026-08-22 01:23:34
finished: 2026-08-22 01:23:58
---

전력 관리 SW(FSW-EPS)가 sysreq.md의 일식 35분 배터리 심방전 ≤25%를 지키는
충방전 제어를 하려면 배터리 충전 종지 전압/전류, 저전압 로드셰딩 임계,
과온 컷오프 임계값을 EPS 하드웨어 팀에게서 받아야 한다.
산출물: EPS 팀이 충전 종지 전압(V)·전류(A), 저전압 임계(V, 로드셰딩 단계별),
과온 임계(°C)를 회신 문서로 남긴다. FSW는 이를 입력으로 eps-thermal-sw.md의
배터리 관리 로직을 확정한다.
검증: 충전종지33.6V·로드셰딩27.2V·안전모드26.4V·과온32°C 회신, sysreq DoD≤25% 반영
