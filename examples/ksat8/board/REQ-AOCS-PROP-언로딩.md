---
id: REQ-AOCS-PROP-언로딩
title: "[AOCS→PROP] 이온추력기 모멘텀 언로딩 인터페이스 요청"
status: DONE
parent: M-AOCS
source: M-AOCS
owner: PROP-DSN-02
deliverable: examples/ksat8/deliverables/PROP/aocs-unloading-interface.md
after: -
track: PROP
started: 2026-08-27 03:47:33
finished: 2026-08-27 03:48:36
---

sysreq AOCS는 "모멘텀 휠 + 이온추력기 언로딩"을 규정한다. AOCS-U1 설계(DSN)가
휠 모멘텀 용량과 언로딩 주기를 정하려면 전기추진(이온추력기) 쪽의 추력 수준·
짐벌(또는 고정 캔팅각) 범위·최소 펄스폭·명령 인터페이스(on/off, duty)와,
언로딩 시 발생하는 토크 외란(축별)을 알아야 한다. PROP-U1-DSN 착수 전 회신을
요청한다.
산출물 제안: examples/ksat8/deliverables/PROP/aocs-unloading-interface.md —
추력기 추력(mN)·캔팅각(°)·최소펄스(ms)·명령 인터페이스, 언로딩 토크 외란(N·m).
검증: 회신 토크 외란이 휠 모멘텀 용량 배분과 언로딩 주기 설계에 정합
검증: 이온추력기 배치·캔팅각·최소펄스·명령 인터페이스, 축별 언로딩 토크 회신(잠정)
