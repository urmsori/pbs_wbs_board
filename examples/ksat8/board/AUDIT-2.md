---
id: AUDIT-2
title: PA 표본감사 2 — REQ-TCS-PAY-발열 회신 입력 경로 대조 (v3.2)
status: TAKEN
parent: SVC
source: SVC
owner: PA-AUD-01
deliverable: examples/ksat8/deliverables/PA/audit-2-req-tcs-pay-heat.md
after: -
track: PA
started: 2026-08-27 03:58:21
finished: -
---

PA는 완료된 Work 표본을 감사한다(v3.1). v3.2부터는 산출물 "입력:"의 각 경로가
적법한 경로인지도 대조한다. TCS팀 요청에 대한 PAY의 회신
(examples/ksat8/deliverables/PAY/twta-heat-layout.md)의 "입력:" 각 경로를 그
요청 사슬(parent=M-TCS) 기준으로 적법성을 대조한다.
산출물 제안: examples/ksat8/deliverables/PA/audit-2-req-tcs-pay-heat.md
검증: "입력:" 경로 전건 적법성 대조, 결함 여부 판정
검증: 입력 3경로 중 1건 부적법(감사1과 동일 패턴) 발견, PAY track 수정요청
(PAY-CORR-02) 발행

재취합 대기(규칙 4절): 자식 PAY-CORR-02(정정)이 아직 DONE이 아니므로 이
감사는 TAKEN으로 되돌린다. PAY-CORR-02가 DONE되면 재취합해 finished를
갱신하고 DONE으로 되돌린다 — 감사 조사·결함 발견·수정요청 발행 자체는
이미 완료된 상태다.
