---
id: OBC-U1-CHK
title: 도면·설계 검도
status: DONE
parent: M-OBC
source: OBC-U1-DSN
owner: OBC-CHK-01
deliverable: examples/ksat8/deliverables/OBC/drawing-check.md
after: OBC-U1-ANLE,OBC-U1-ANLT,REQ-OBC-COMM-IF,REQ-OBC-PAY-TM
track: OBC
started: 2026-08-27 03:59:49
finished: 2026-08-27 04:00:06
---

왜: 해석(전자/신뢰성·열) 결과와 외부 인터페이스 회신(COMM·PAY)이 모두
모이면, 독립 검도자가 설계를 확정하기 전 정합성(치수·예산·인터페이스)을
검도한다. 특히 obc-design.md의 PAY TM 배정은 REQ-OBC-PAY-TM 회신 전
잠정치였으므로 이번 검도에서 정정한다.
산출물: examples/ksat8/deliverables/OBC/drawing-check.md
검증: PAY TM 400점 정정, 마진 3,200 확보, COMM 인터페이스는 잠정 유지
