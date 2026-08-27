# PAY-CORR-02 수정 기록 — twta-heat-layout.md 입력 경로 정정

입력: examples/ksat8/deliverables/PA/audit-2-req-tcs-pay-heat.md, examples/ksat8/board/PAY-CORR-02.md

## 결함
AUDIT-2가 지적한 대로, REQ-TCS-PAY-발열 회신(examples/ksat8/deliverables/PAY/
twta-heat-layout.md, parent: M-TCS)의 "입력:"이 별도 사슬(REQ-PAY-TCS-방열,
parent: M-PAY)의 회신 examples/ksat8/deliverables/TCS/pay-thermal-capability.md를
정식 요청 없이 인용해 AUDIT-1과 동일 유형의 "보이지 않는 종속"이었다.

## 조치 — 이미 수정됨(선행 조치)
본 감사 요청이 올라오기 전, 동일 원인자(당시 PAY-DSN-01, 現 PAY-IF-01)가
REQ-HAR-PAY-RF 건과 함께 자체 점검으로 발견·수정을 완료했다. twta-heat-layout.md
"입력:" 줄에서 examples/ksat8/deliverables/TCS/pay-thermal-capability.md 경로를
제거하고, 채널당/24채널 발열 수치의 판정 기준을 "sysreq TCS 방열배분(6kW/24채널
=250W/채널)"로 재작성해 TCS 확약 문서에 대한 직접 인용 없이도 자기 사슬(sysreq,
after=REQ) 안에서 판정이 성립하도록 재작성했다.

현재 twta-heat-layout.md 입력 줄(수정 후, 확인):
```
입력: examples/ksat8/deliverables/PAY/u1-dsn.md,
examples/ksat8/board/REQ-TCS-PAY-발열.md
```
두 경로 모두 적법(자기 트랙 산출물 · 보드 게시글).

## 재발 방지(AUDIT-2 지적 반영)
양방향 ICD(서로 다른 팀이 서로에게 요청을 올리는 경우) 응답 시, 자신이 별도로
발행한 상대 요청의 회신 문서를 "입력:"에 직접 인용하지 않는다 — 그 회신의
parent가 내 사슬(M-PAY)일 뿐, 지금 답하는 요청(parent가 상대팀 M-*)의 사슬
위에는 있지 않기 때문이다. 필요하면 sysreq(after로 받은 산출물)나 자기 트랙
산출물(u1-dsn.md)로 대체 근거를 삼는다.

검증: twta-heat-layout.md "입력:" 경로 2건 전부 적법(자기 트랙·보드 게시글) 재확인, AUDIT-1과 동일 원인 재발방지 서술 반영
