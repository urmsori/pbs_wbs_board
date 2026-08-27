# MECH-U2 SA 전개힌지 설계

입력: examples/ksat8/deliverables/SE/sysreq.md (MECH SA2윙 전개·단일고장허용), examples/ksat8/deliverables/SA/mech-sa-hinge-reply.md (질량180kg/윙·관성10,000kg·m²·
강성목표6,000N·m/rad·백래시≤0.05°·6점M8 PCD150mm 제안)

## 기구 설계
- 회전스프링 구동(전개보조) + 점성댐퍼(rate limiter) + 래치(전개완료 잠금).
- **이중 릴리즈 액추에이터**(핀풀러 2계열, 스토우드 구속 해제) — sysreq MECH 단일고장
  허용 반영. 스프링 구동 자체는 수동(단일고장 없음), 개시부만 이중화로 충분.
- 목표 회전강성: SA 회신 목표치 **6,000 N·m/rad** 채택.
- 장착: SA 제안 6점 M8 PCD150mm — STR-U1측 요크마운트(4점M10 PCD200mm)와 별개
  인터페이스(힌지-요크 사이 어댑터 플레이트로 연결), 구조검토 결과 수용 가능.
- 백래시 허용: ≤0.05°(SA 요구 그대로 채택).

## 다음 단계
ANL-S(전개 후 1차모드, SA sysreq ≥0.1Hz 판정)로 확정.
