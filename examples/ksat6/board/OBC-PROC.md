---
id: OBC-PROC
title: 프로세서보드 설계
status: DONE
parent: M-OBC
source: -
owner: OBC-DSN-01
deliverable: examples/ksat6/deliverables/OBC/proc-board.md
after: -
track: OBC
started: 2026-08-22 01:20:47
finished: 2026-08-22 01:21:29
---

OBC 모듈 인도(M-OBC)를 위해 연산 코어인 프로세서보드부터 확정해야 나머지
보드(메모리·I/O)의 인터페이스와 전력 예산이 정해진다. sysreq.md의
"처리여유 ≥50%"를 만족하는 CPU·클럭·마진을 정한다.
산출물: examples/ksat6/deliverables/OBC/proc-board.md — CPU 선정, 클럭, 처리여유(%), 소비전력.
검증: 부하분석표 합산 결과 처리여유 52%≥50% 충족
