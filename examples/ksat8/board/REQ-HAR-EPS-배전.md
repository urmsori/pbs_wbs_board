---
id: REQ-HAR-EPS-배전
title: 100V 배전 커넥터·채널 정격 요청 (100V 전력 하니스 설계용)
status: DONE
parent: M-HAR
source: HAR-U1-DSN-01
owner: EPS-U1-DSN-01
deliverable: examples/ksat8/deliverables/EPS/distribution-connector-spec.md
after: -
track: EPS
started: 2026-08-27 03:47:05
finished: 2026-08-27 03:47:12
---

HAR-U1(100V 전력 하니스)을 설계하려면 EPS/PCU 쪽 배전 출력 커넥터
형식과 채널별 전류 정격, 모선 전압(sysreq.md: 100V±2V)을 알아야 한다 —
100V 절연 설계 여유·전압강하 판정을 위해 채널별 최대 전류·허용 케이블
저항 예산이 필요하다.
요청: PCU/배전 유닛 배전 출력 커넥터 파트번호·핀맵·채널별 전류 정격,
100V 절연 이격거리 요구(도체간·대지간).
산출물 제안: examples/ksat8/deliverables/EPS/distribution-connector-spec.md
검증: 채널별 전류정격·100V 절연이격 회신
