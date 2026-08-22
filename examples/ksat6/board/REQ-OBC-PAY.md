---
id: REQ-OBC-PAY
title: "[OBC→PAY] 탑재체 데이터율·SpW 링크 수 확정 요청"
status: DONE
parent: OBC-IO
source: OBC-IO
owner: PAY-ELEC-01
deliverable: examples/ksat6/deliverables/PAY/obc-datarate-reply.md
after: -
track: PAY
started: 2026-08-22 01:25:41
finished: 2026-08-22 01:26:41
---

OBC I/O보드(OBC-IO)의 SpW 포트 수·채널별 대역폭을 배정하려면 탑재체가
실제로 요구하는 순간 데이터율과 필요한 SpW 링크 개수(영상 다운로드용·명령/
상태용 분리 여부)를 알아야 한다. sysreq.md 기준 X-band 150Mbps/일 60GB를
낼 수 있는 상류 데이터율이 필요하다.
산출물: PAY 팀이 탑재체 데이터율(Mbps, 버스트/평균)과 필요 SpW 링크 수(포트당 대역폭 포함)를
회신 문서로 남긴다. OBC는 이를 입력으로 io-board.md의 채널 배정표를 확정한다.
검증: 데이터율100~115Mbps, SpW 2링크, 버퍼30GB 요청 회신
