---
id: REQ-HAR-OBC-핀맵
title: OBC 커넥터·핀맵 요청 (전력계통 모니터링 신호 하니스 설계용)
status: DONE
parent: M-HAR
source: HAR-U1-DSN-01
owner: OBC-DSN-01
deliverable: examples/ksat8/deliverables/OBC/io-connector-pinmap.md
after: -
track: OBC
started: 2026-08-27 03:49:10
finished: 2026-08-27 03:49:36
---

HAR-U1(100V 전력 하니스)에 동봉되는 전압·전류 모니터링/제어 신호선이
OBC로 종단되므로, OBC 쪽 인터페이스 커넥터 형식과 핀맵을 알아야 한다.
sysreq.md: OBC TM 8,000점·TC 2,000점 처리, 이중화.
요청: OBC I/O 커넥터 파트번호·핀맵(전력 모니터링 아날로그/디스크리트
채널수·이중화 계통 구성), EMC 접지 요구(실드 접지핀 위치).
산출물 제안: examples/ksat8/deliverables/OBC/io-connector-pinmap.md
검증: 커넥터·핀맵·접지 회신, obc-design.md와 정합
