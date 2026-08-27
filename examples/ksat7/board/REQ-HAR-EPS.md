---
id: REQ-HAR-EPS
title: 배전 커넥터·채널 전류정격 요청 (대전류 펄스 배선 설계용)
status: DONE
parent: M-HAR
source: HAR-U1-DSN-01
owner: EPS-U1-DSN-01
deliverable: examples/ksat7/deliverables/EPS/distribution-connector-spec.md
after: -
track: EPS
started: 2026-08-27 01:56:45
finished: 2026-08-27 01:57:26
---

HAR-U1(대전류 펄스 배선, SAR 1.8kW)을 설계하려면 EPS/PCDU 쪽 배전 출력
커넥터 형식과 채널별 전류 정격, 모선 전압(sysreq.md: 50V±5V)을 알아야
한다 — 전압강하 ≤3% @펄스 판정을 위해 채널별 최대 전류·허용 케이블
저항 예산이 필요하다.
요청: PCDU 배전 출력 커넥터 파트번호·핀맵·채널별 전류 정격(특히 SAR
펄스 버스트 채널), 슈퍼커패시터/배터리 하이브리드 출력단 커넥터 사양.
산출물 제안: examples/ksat7/deliverables/EPS/distribution-connector-spec.md
검증: PCDU 펄스채널 45A/90A, 전압강하예산 41.7mΩ 회신
