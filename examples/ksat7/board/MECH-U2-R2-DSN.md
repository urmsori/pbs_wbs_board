---
id: MECH-U2-R2-DSN
title: SA 전개힌지 rev.2 강성 증대 재설계
status: DONE
parent: M-MECH
source: MECH-U2-ANL-S2
owner: MECH-DSN-01
deliverable: examples/ksat7/deliverables/MECH/mech-u2-r2-dsn.md
after: -
track: MECH
started: 2026-08-27 02:11:19
finished: 2026-08-27 02:12:55
---

MECH-U2-ANL-S2에서 전개 후 1차모드 약0.31Hz<0.5Hz 미충족(RED)이 확인됐다. 힌지 회전강성을
증대(약 8000→25000 N·m/rad 목표)해야 sysreq(SA 전개 후 1차모드≥0.5Hz)를 회복할 수 있다.
검증: 힌지강성25000N·m/rad(관성10.1kg·m² 정본 채택), 예측0.545Hz≥0.5Hz
