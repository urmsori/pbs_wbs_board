---
id: REQ-COMM-OBC
title: X-band 800Mbps 전송 버퍼·인터페이스 요청
status: DONE
parent: M-COMM
source: COMM-U1-DSN
owner: OBC-DSN-01
deliverable: examples/ksat7/deliverables/OBC/comm-interface-spec.md
after: -
track: OBC
started: 2026-08-27 01:53:04
finished: 2026-08-27 01:53:19
---

COMM-U1(X-band 800Mbps DVB-S2 송신계)을 설계하려면 OBC 저장부에서
변조기로 넘어오는 인터페이스 종류·속도와 버스트 재생 시 버퍼 심도를
알아야 한다 — 800Mbps 연속 하향에 맞춰 레코더 재생 대역폭이 병목이
없는지, 변조기 입력단 지터/버퍼언더런 여유를 링크버짓·타이밍설계에
반영해야 한다.
요청:
1) OBC→COMM 고속 인터페이스 종류(SpW/기타)와 보장 처리량(Mbps)
2) 800Mbps 연속 하향 중 재생 버퍼 심도(Mbit) 및 언더런 여유
3) 원시 2TB 중 1회 접촉당 하향 가능한 예상 재생률 범위
산출물 제안: examples/ksat7/deliverables/OBC/comm-interface-spec.md
검증: SpW 850Mbps·버퍼256Mbit·언더런마진15% 회신, PAY데이터율 잠정(무응답)
