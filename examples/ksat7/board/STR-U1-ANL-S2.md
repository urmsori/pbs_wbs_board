---
id: STR-U1-ANL-S2
title: 1차구조체 1차모드 재검증(안테나 실측 ICD 반영)
status: DONE
parent: M-STR
source: STR-U1-RB
owner: STR-ANL-S-01
deliverable: examples/ksat7/deliverables/STR/str-u1-anl-s2.md
after: STR-U1-RB
track: STR
started: 2026-08-27 01:57:58
finished: 2026-08-27 01:58:26
---

STR-U1-RB 판정의 조건(REQ-STR-PAY 회신 수신 시 재검증)을 이행한다. PAY 회신(안테나 72.0kg,
3점 킨매틱 PCD400mm 8-M8, 로컬강성≥50N/µm)을 반영해 1차모드를 재계산해야 sysreq STR
1차모드≥35Hz 충족 여부를 확정할 수 있다.
검증: 1차모드 약29.5Hz<35Hz — 미충족, RED리스크로 rev.2 이관
