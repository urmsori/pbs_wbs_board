---
id: NEED-HAR-COMM
title: COMM 인수 시험용 전원·데이터 시험 하니스
status: DONE
parent: AIT-RX-COMM
owner: HAR-TECH-01
deliverable: examples/ksat5/deliverables/SUPPORT/need-har-comm.md
after: -
track: HAR
started: 2026-08-21 07:13:40
finished: 2026-08-21 07:15:01
---

AIT-TST의 필요: COMM EM 모듈을 EGSE에 연결해 시험하려는데, 전원 2계통과
데이터 커넥터가 하나의 인출면에 나란히 있어 이를 EGSE로 모을 시험
하니스가 없다. transceiver-em.md(module-em.md §"모듈 구성" 인용)를
읽고 확인한 구체 요구:

- 커넥터 인출 위치: 보드 90mm 변 한쪽에 RF(SMA)·전원 2핀×2·데이터
  (UART) 일렬 배치, 인출 방향 −X 데크 모서리 쪽
  (icd-str-comm-footprint.md §커넥터 인출 위치).
- 전원: 2핀(액추에이터 레일 8.4V, PA 전용, EOD 6.8V까지 가변 필요) +
  2핀(5V 로직 레일) — 두 레일을 EGSE 가변전원에서 독립 공급해야
  EOD 조건 재현 가능(module-em.md §미해결 리스크).
- 데이터: UART 3.3V TTL, OBC 인터페이스 — EGSE에서 OBC를 대신해
  링크 상태·텔레메트리를 주고받을 채널 필요.

요청: 전원 2핀×2(액추에이터 레일 가변 6.8~8.4V, 5V 로직 레일) + UART
3.3V TTL 1채널을 갖춘 COMM EM 모듈 전원·데이터 시험 하니스.
산출물: (지원 역할이 정함)
검증: 전원2핀x2(6.8~8.4V가변,5V)+UART 3.3V TTL 1채널이 요청과 일치, 인출 위치·방향 확인
