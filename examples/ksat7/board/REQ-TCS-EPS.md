---
id: REQ-TCS-EPS
title: 히터 40W 배분 확정 요청
status: DONE
parent: M-TCS
source: TCS-DSN-01
owner: EPS-U1-DSN-01
deliverable: examples/ksat7/deliverables/EPS/heater-channel-confirmation.md
after: -
track: EPS
started: 2026-08-27 01:56:45
finished: 2026-08-27 01:57:26
---

sysreq 히터 예산 ≤40W를 채널별로 배분(배터리 히터·추진 배관 히터·구조부 히터 등)한
초안을 TCS가 만들었으나, EPS PCDU가 이 채널 구성을 실제로 배전(스위칭·전류제한)할
수 있는지 확인·확정이 필요하다. TCS 단독으로는 배전 회로 여유를 알 수 없다.
산출물 제안: examples/ksat7/deliverables/EPS/heater-channel-confirmation.md — 채널별
배전 가능 여부(회로·차단기 정격 여유) 확인.
검증: 히터 총 40W 이내 채널 배분이 EPS 배전 회로로 수용 가능함을 확인
검증: 40W 3채널 배분 배전회로 여유로 수용 가능
