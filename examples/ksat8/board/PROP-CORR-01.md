---
id: PROP-CORR-01
title: 전기추진 전력·언로딩 추력 정정(EPS 확약 반영)
status: DONE
parent: M-PROP
source: REQ-PROP-EPS-전력
owner: PROP-DSN-02
deliverable: examples/ksat8/deliverables/PROP/eps-load-profile.md,examples/ksat8/deliverables/PROP/aocs-unloading-interface.md
after: REQ-PROP-EPS-전력
track: PROP
started: 2026-08-27 03:50:48
finished: 2026-08-27 03:51:19
---

왜: REQ-EPS-PROP-부하 회신(eps-load-profile.md)과 REQ-AOCS-PROP-언로딩 회신
(aocs-unloading-interface.md)은 EPS 확약(REQ-PROP-EPS-전력) 전에 채널당
1.5kW·추력 200mN으로 잠정 가정했다. EPS 확약치(채널당 최대 1,000W, 2채널
2,000W 상한, 이클립스 중 미운용)를 반영해 두 회신을 정정한다(규칙 4절
"재작업은 정상 경로").
산출물: examples/ksat8/deliverables/PROP/eps-load-profile.md(갱신),
examples/ksat8/deliverables/PROP/aocs-unloading-interface.md(갱신)
검증: EPS 확약(채널당1,000W·2채널2,000W) 반영해 추력 200→70mN, 전력 3.0→2.0kW로 정정
