---
id: FSW-COMM
title: 통신·탑재 관리 SW
status: DONE
parent: M-FSW
source: -
owner: FSW-COMM-01
deliverable: examples/ksat6/deliverables/FSW/comm-payload-sw.md
after: FSW-ARCH
track: FSW
started: 2026-08-22 01:21:51
finished: 2026-08-22 01:22:58
---

sysreq.md의 COMM(S/X-band TT&C·다운링크)·PAY(탑재체 관리) 요구를
소화하려면 명령처리·텔레메트리 포맷팅·탑재체 시퀀서·FDIR(밸브류 등 액추에이터
안전 로직 포함) SW가 필요하다. 다른 유닛(PROP 등)에서 밸브 시퀀스·안전
인터록 요청이 도착하면 이 Work가 받는다(track: FSW REQ 수신처).
산출물: examples/ksat6/deliverables/FSW/comm-payload-sw.md — 명령/TM 처리, 탑재체 시퀀서, FDIR 로직, 검증 케이스.
검증: 6개 검증 케이스 정의, TM 우선순위·인터록 로직 명세 확인
