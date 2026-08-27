---
id: REQ-OBC-PAY
title: "[OBC→PAY] SAR 원시데이터율·2TB 기록 경로 인터페이스 확정 요청"
status: DONE
parent: M-OBC
source: OBC-U1-DSN
owner: PAY-DSP-01
deliverable: examples/ksat7/deliverables/PAY/obc-datarate-reply.md
after: -
track: PAY
started: 2026-08-27 01:52:47
finished: 2026-08-27 01:53:26
---

OBC 2TB 저장부(OBC-U1-DSN)의 기록 경로(채널 수·포트당 대역폭·버퍼 여유)를
확정하려면 SAR 능동위상배열이 실제로 쏟아내는 원시데이터율(순간 첨두/평균,
Mbps 또는 Gbps)과 링크 형식(SpW 채널 수, 스트립맵/스팟 모드별 차이)을 알아야
한다. sysreq.md 기준 원시 2TB/궤도 저장, X-band 800Mbps 하향을 전제로 한다.
산출물: PAY 팀이 원시데이터율(첨두/평균, 모드별)과 필요 SpW 링크 수·포트당
대역폭을 회신 문서로 남긴다. OBC는 이를 입력으로 저장부 쓰기대역폭·버퍼를 확정한다.
검증: 데이터율 회신 기준 2TB 저장 용량 내 1궤도 관측 데이터 수용 가능 여부 확인
검증: 스팟첨두3.2Gbps/평균1.1Gbps, 스트립맵첨두1.2Gbps/평균450Mbps, SpW4채널 회신
