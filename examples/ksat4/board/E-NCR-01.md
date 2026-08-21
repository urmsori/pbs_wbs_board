---
id: E-NCR-01
title: STR — 산출물 대다수 누락 + summary-em.md 근거 없는 판정
status: DONE
parent: E-AIT-1
owner: STR-LEAD-01
deliverable: examples/ksat4/deliverables/STR/dsn-a2-e.md, examples/ksat4/deliverables/STR/anl-em.md, examples/ksat4/deliverables/STR/parts-e.md, examples/ksat4/deliverables/STR/build-a2-e.md, examples/ksat4/deliverables/STR/summary-em.md
after: -
track: STR
started: 2026-08-21 04:12:53
finished: 2026-08-21 04:12:53
---

E-AIT-1에서 STR 산출물 디렉토리(examples/ksat4/deliverables/STR/)를 다른 7개
서브시스템과 대조한 결과, STR만 산출물 파일이 5개(build-a1-e.md, cfg-e.md,
icd.md, summary-em.md, test-em.md)뿐이다. 다른 7개 서브시스템은 모두
dsn-a1~a4-e.md, anl-em.md, parts-e.md, build-a1~a4-e.md 등 14개 파일을 갖춘다.

실제로 확인한 결손:
1. examples/ksat4/deliverables/STR/dsn-a2-e.md, dsn-a3-e.md, dsn-a4-e.md,
   anl-em.md, parts-e.md, build-a2-e.md, build-a3-e.md, build-a4-e.md가
   디스크에 전혀 존재하지 않는다. 그런데도 이를 산출물로 지정한 게시글
   E-STR-D2, E-STR-D3, E-STR-D4, E-STR-N1~N3, E-STR-P1~P2, E-STR-M2~M5,
   E-STR-Q2가 모두 status: DONE이다.
2. E-STR-D2/D3/D4의 frontmatter `deliverable`은 각각
   `examples/ksat4/deliverables/STR/dsn-aD2.md`(오타, dsn-a2-e.md가 맞음),
   `dsn-aD3.md`, `dsn-aD4.md`로 기록되어 있고 이 오타 파일조차 존재하지
   않는다(본문 "산출물:" 줄에는 올바른 경로가 적혀 있어 frontmatter와
   본문이 서로 다르다).
3. E-STR-M1~M5의 frontmatter `deliverable` 필드에는 파일 경로 대신
   `STR-MFG-0N — owner에는 take 시 이 역할 이름을 쓴다)`라는 템플릿 잔여
   텍스트가 그대로 남아 있다(post.py done 인자 오기입으로 보임).
4. examples/ksat4/deliverables/STR/summary-em.md는 "입력: STR 팀 산출물
   일체"라는 한 줄과 "조립체 4건 제작·검사 합격, 기능시험 합격" "판정: 합격"
   뿐이다 — 실제로 입력 파일을 나열하지도, 수치(질량 등)를 인용하지도 않는다.
   STR은 sysreq.md 배분(45 kg, 8개 서브시스템 중 최대 배분)의 주체인데
   질량 실측/설계값이 어느 산출물에도 없어 EM 통합시험에서 시스템 총질량을
   검증할 근거가 없다.

산출물 지정(정정 필요):
- examples/ksat4/deliverables/STR/dsn-a2-e.md, dsn-a3-e.md, dsn-a4-e.md,
  anl-em.md, parts-e.md, build-a2-e.md, build-a3-e.md, build-a4-e.md를
  실제로 작성(질량 포함)한다.
- E-STR-D2/D3/D4의 `deliverable` 오탈자를 정정하고, E-STR-M1~M5의
  `deliverable`을 실제 경로(build-a1~a4-e.md)로 정정한다.
- examples/ksat4/deliverables/STR/summary-em.md를 위 산출물을 실제로
  인용해 재작성(질량 수치·근거 포함)한다.

(담당 역할: STR-LEAD-01)
검증: 결손 9파일 생성·summary 근거 판정표 재작성, DONE 게시글의 deliverable 경로와 대조
