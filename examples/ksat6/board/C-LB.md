---
id: C-LB
title: S/X-band 링크 버짓 산출
status: DONE
parent: M-COMM
source: -
owner: COMM-DSN-01
deliverable: examples/ksat6/deliverables/COMM/link-budget.md
after: -
track: COMM
started: 2026-08-22 01:22:06
finished: 2026-08-22 01:22:53
---

sysreq.md의 S-band TT&C(상향 64kbps/하향 2Mbps)·X-band 150Mbps 요구를
만족하는 송신기·안테나를 뒤이어 설계하려면 먼저 EIRP·G/T·마진을 링크
버짓으로 정해야 한다. 궤도 700km SSO, 최소 앙각 10°를 가정한 최악 슬랜트
레인지로 계산한다. 이 설계에서 X-band 데이터 인터페이스(OBC)·안테나
장착/FOV(STR)·X-band 송신 첨두전력 허용치(EPS)가 함께 필요함을 알게 되어
REQ-COMM-OBC, REQ-COMM-STR, REQ-COMM-EPS를 발행한다(source=이 게시글).
산출물: examples/ksat6/deliverables/COMM/link-budget.md — S-band 상/하향, X-band
하향 EIRP·G/T·C/N0·Eb/N0·마진 표.
검증: FSPL/C/N0/Eb-N0 계산 재검산, S-band 하향 마진 +1.44dB(빠듯), X-band 하향 +6.26dB, S-band 상향 +29.5dB로 정직 기록
