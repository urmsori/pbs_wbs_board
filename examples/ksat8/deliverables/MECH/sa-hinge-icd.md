# SA→MECH 회신: 전개 힌지 인터페이스 확정 (REQ-SA-MECH-힌지)

입력: examples/ksat8/deliverables/MECH/mech-u2-dsn.md, examples/ksat8/deliverables/MECH/mech-u2-ins.md

귀 팀이 올린 REQ-SA-MECH-힌지에 대한 회신이다(귀 팀 회신은 별도로
examples/ksat8/deliverables/SA/mech-sa-hinge-reply.md에 이미 완료됨).

## 1) 힌지쌍 회전강성·백래시
실측 **6,080 N·m/rad**(목표6,000 대비+1.3%), 백래시 실측 **0.04°**
≤ 요구 0.05°.

## 2) 패널-힌지 접속부 질량 배분·볼트 패턴
힌지측 자체 기구 질량은 SA 패널 질량(180kg/윙)과 별도 예산(MECH 기구 자체
중량, STR 요크마운트와 어댑터플레이트로 연결). 부착 볼트 패턴: 귀 팀 제안
**6점 M8, PCD150mm** 그대로 채택.

## 3) 전개 충격 허용치·완충 특성·단일고장 허용
회전스프링 구동(저속, 자체발생충격 낮음) + 점성댐퍼(rate limiter)로 래치업
충격 제한. 개시부(릴리즈)는 **이중 액추에이터**로 단일고장 허용(sysreq MECH)
확보 — 기능시험에서 주/예비 각 계열 단독 작동 정상 확인.

검증: 힌지강성6,080N·m/rad·백래시0.04°, 6점M8 PCD150mm 채택, 이중릴리즈로
단일고장허용 확보 — REQ-SA-MECH-힌지 회신 완료
