---
id: AOCS-U1-ANL-CTL
title: 지향 제어루프 안정성·과도응답 해석
status: DONE
parent: M-AOCS
source: AOCS-U1-DSN
owner: AOCS-ANL-CTL-01
deliverable: examples/ksat8/deliverables/AOCS/u1-anl-ctl.md
after: AOCS-U1-DSN
track: AOCS
started: 2026-08-27 03:53:30
finished: 2026-08-27 03:53:30
---

설계(DSN)의 제어대역폭 0.02Hz·게인이 폐루프에서 안정한지, 과도응답이 지향오차
예산(제어오차 90arcsec) 이내인지 해석해 CHK(사양서 검도)로 넘겨야 한다.
검증: 위상여유·이득여유, 정착시간 내 제어오차 배분 이내 확인
검증: 위상여유55°/이득여유8dB, 잔류오차78≤90arcsec(마진13%)
