---
id: REQ-PAY-OBC
title: 대용량 저장·전송 대역 확인
status: DONE
parent: PAY-01
source: PAY-01
owner: OBC-MEM-01
deliverable: examples/ksat6/deliverables/OBC/reply-pay-storage-bandwidth.md
after: -
track: OBC
started: 2026-08-22 01:26:20
finished: 2026-08-22 01:27:04
---

광학계·초점면 1차 산출(PAY-01)에서 TDI 초점면(교차궤도 6000화소, 12bit,
라인율 약 2500라인/s)의 원시 데이터율을 판코로매틱 단일밴드 기준 약
180Mbps로 추산했다(멀티스펙트럼 포함 시 약 230Mbps). 압축(약 2:1) 후
약 100~115Mbps로 X-band 150Mbps 하향 예산 안에 들어오는지, OBC가 이
순간 판독률을 SpaceWire로 받아 대용량메모리(128GB)에 버퍼링할 수 있는지
확인이 필요하다.
산출물: OBC 팀이 정하는 경로에 SpW 인터페이스 지속 처리율(Mbps) 여유,
128GB 중 탑재체 영상버퍼 할당량(GB) 확답을 명시해 달라.
검증: SpW 채널여유(200Mbps>115Mbps), 118GB≈일60GB 대비 2일치 버퍼 여유 계산 확인
