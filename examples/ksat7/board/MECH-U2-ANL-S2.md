---
id: MECH-U2-ANL-S2
title: SA 전개힌지 1차모드 재검증(SA 실측 ICD 반영)
status: DONE
parent: M-MECH
source: MECH-U2-RB
owner: MECH-ANL-S-01
deliverable: examples/ksat7/deliverables/MECH/mech-u2-anl-s2.md
after: MECH-U2-RB
track: MECH
started: 2026-08-27 02:07:13
finished: 2026-08-27 02:07:31
---

REQ-MECH-SA 회신(패널 질량7.6kg/윙·관성10.1kg·m²)이 잠정 설계치(2.5kg·m² 가정) 대비 4배
높다. 힌지강성(8000N·m/rad)·볼트패턴은 상호 일치 확인됐으나 1차모드는 관성 변경으로 재계산해야
sysreq(SA 전개후 1차모드≥0.5Hz) 최종 판정을 확정할 수 있다.
검증: 1차모드 약0.31Hz<0.5Hz — 미충족, RED, rev.2 이관
