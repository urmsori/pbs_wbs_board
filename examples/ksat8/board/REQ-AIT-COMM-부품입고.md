---
id: REQ-AIT-COMM-부품입고
title: COMM NCR-COMM-02 부품 입고·IQC 완료 여부 요청
status: OPEN
parent: INT
source: AIT-RX-3
owner: -
deliverable: -
after: -
track: COMM
started: -
finished: -
---

왜: COMM module-fm.md의 NCR-COMM-02(부품 입고 미확인)가 PUR 발주 완료·
입고예정일(2026-09-10~15)로 하향됐으나 "정상 생산일정"으로만 기록돼
있고 실제 입고·IQC 완료 여부는 module-fm.md에 없다. INT 통합조립 착수
전 COMM-FM-001 하위 부품의 실물 입고 상태를 확인해야 통합시험 일정에
영향이 없는지 판단할 수 있다.

요청: NCR-COMM-02 대상 부품의 실제 입고일·IQC 완료 여부(완료/미완료),
미완료 시 INT 착수에 미치는 영향.
회신 산출물 제안: examples/ksat8/deliverables/COMM/req-ait-parts-reply.md
