---
id: COMM-CORR-01
title: FSW·OBC 잠정회신 정정 — TT&C 프로토콜/인터페이스 확정치
status: DONE
parent: COMM-U1
source: COMM-U1
owner: COMM-LEAD-01
deliverable: examples/ksat8/deliverables/COMM/comm-corr-01.md
after: -
track: COMM
started: 2026-08-27 04:03:01
finished: 2026-08-27 04:04:28
---

REQ-FSW-COMM-TMTC·REQ-OBC-COMM-IF는 COMM-U1 완료 전 FSW·OBC가 sysreq
근거로 잠정 자답(DONE, "COMM-U1 확정 후 정정 예정" 명기)한 상태였다.
COMM-U1이 완료되어 확정치를 공지, 정정을 요청한다.

정정 내용(comm-u1-fm-package.md 확정치 기준):
- 프레임 동기·프로토콜: 스페이스패킷/ASM 여부는 baseline에 미포함 —
  FSW 가정은 COMM 범위 밖(OBC-FSW 자체 협의 필요) 항목으로 COMM은 확인
  불가. TC CRC/2단계 확인/순번검사 가정은 COMM 트랜스폰더 레벨과 무관
  (OBC/FSW 프로토콜 계층) — 정정 불필요.
- 레인징-TM/TC 공존: FSW 가정(주파수분할·별도 서브캐리어)은 **부정확** —
  실제로는 comm-u1-design.md §1대로 **동일 캐리어 결합변조**(레인징 부반송파
  억압 방식)다. FSW 정정 필요.
- OBC 버스: 1553B 이중버스는 가정과 일치(정정 불필요). TM 프레임은
  1Hz 기준 32워드/프레임(가정보다 구체화), TC는 16워드/프레임·최대
  10cmd/s·콜드스탠바이(가정과 일치).

회신 산출물 경로 제안: FSW/OBC가 자기 산출물에 반영 후 확인 게시글
(examples/ksat8/deliverables/FSW/, examples/ksat8/deliverables/OBC/)
검증: OBC 가정 일치, FSW 레인징 공존방식 1건 정정 통지
