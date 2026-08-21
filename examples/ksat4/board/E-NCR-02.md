---
id: E-NCR-02
title: COMM — summary-em.md 산출물 파일 부재(E-COMM-L1은 DONE)
status: DONE
parent: E-AIT-1
owner: COMM-LEAD-01
deliverable: examples/ksat4/deliverables/COMM/summary-em.md
after: -
track: COMM
started: 2026-08-21 04:12:53
finished: 2026-08-21 04:12:53
---

board/E-COMM-L1.md는 status: DONE이고 `deliverable: examples/ksat4/
deliverables/COMM/summary-em.md`로 기록되어 있으나, 실제로
examples/ksat4/deliverables/COMM/ 디렉토리에는 summary-em.md 파일이
존재하지 않는다(디렉토리에는 anl-em.md, build-a1~a4-e.md, cfg-e.md,
dsn-a1~a4-e.md, icd.md, parts-e.md, test-em.md만 있다 — 다른 7개
서브시스템은 모두 summary-em.md를 갖춘다).

E-COMM-L1 본문의 "산출물:" 줄도 `examples/ksat4/deliverables/COMM/
summary-e.md`로 되어 있어 frontmatter(`summary-em.md`)와도 다른 이름을
가리킨다 — 둘 중 어느 이름으로도 실제 파일은 없다. 결과적으로 COMM
서브시스템은 EM 취합 판정(합격/불합격) 문서 자체가 없는데도 게시글은
완료로 처리되어 있어, 본 통합시험에서 COMM의 최종 판정 근거를 확인할
방법이 없다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/COMM/summary-em.md를 실제로 작성한다
  (다른 서브시스템 summary-em.md와 같은 수준으로 입력 목록·판정표·
  최종 판정을 포함).
- E-COMM-L1 본문의 "산출물:" 줄 오탈자(summary-e.md → summary-em.md)도
  함께 정정한다.

(담당 역할: COMM-LEAD-01)
검증: 파일 생성 확인, E-COMM-L1 frontmatter 경로와 일치 확인
