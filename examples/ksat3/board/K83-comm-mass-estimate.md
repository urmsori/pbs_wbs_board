---
id: K83
title: comm-em.md에 질량 추산 추가
status: TAKEN
parent: K40
owner: sonnet-comm
deliverable: -
after: -
track: COMM
started: 2026-08-21 02:20:45
finished: -
---

K40 통합시험(불합격 항목 3) 결과: sysreq.md는 COMM 트랙에 질량 배분
0.5 kg을 할당했으나, comm-em.md에는 질량 추산이 전혀 없다(트랜시버
PCB, PA, 안테나 전개 기구, RF 케이블 등). 이 때문에 시스템 전체 질량
합계(2.6 kg) 검증이 COMM 항목만 미확정 상태로 남는다.

## 필요 사항
- comm-em.md에 질량 절을 추가한다: 트랜시버 보드(PA·LNA·필터 포함),
  안테나 전개 기구(다이폴 소자+방출 트리거), RF 커넥터/케이블 등 항목별
  추산과 합계.
- sysreq 배분 0.5 kg 대비 여유/초과 여부를 명시.

산출물: examples/ksat3/deliverables/comm-em.md 갱신(질량 절 추가).
