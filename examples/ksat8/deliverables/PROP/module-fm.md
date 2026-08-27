# 추진(PROP) 비행모델 인도 — module-fm
입력: examples/ksat8/deliverables/PROP/biprop-design.md, examples/ksat8/deliverables/PROP/biprop-review.md,
examples/ksat8/deliverables/PROP/biprop-acceptance-leak-test.md, examples/ksat8/deliverables/PROP/ep-design.md,
examples/ksat8/deliverables/PROP/ep-review.md, examples/ksat8/deliverables/PROP/ep-ignition-test.md,
examples/ksat8/deliverables/SE/sysreq.md

## PROP-U1: 이원추진제 계통(축약 설계체인 + 수락·누설시험)
DSN→RVW→TST(수락+누설) 완료.
- Δv 1,500m/s(정지궤도 진입), 추진제 1,363kg(산화제846/연료517, Isp320s·
  MR1.65), LAE 400N + RCS 10N×12기.
- STR 확정 인터페이스(탱크링 Ø600/520mm, 트러니언4점×2, 국부모드실측
  61.4Hz≥60Hz, 설계하중 축8.5g/횡4.5g)와 완전 정합(추가 정정 불필요 —
  최초 제안치가 그대로 채택됨).
- 누설시험 1×10⁻⁶scc/s(규격 1×10⁻⁵ 이내), 프루프압 이상無, 밸브응답
  ≤15ms — 합격.

## PROP-U2: 전기추진(축약 설계체인 + 점화시험)
DSN→RVW→TST(점화) 완료.
- Δv 750m/s(GEO 유지+언로딩), 제논 100kg(Isp1,600s), 이온추력기
  4기(2for2), 채널당 1,000W/70mN.
- EPS 확약(2,000W 상한, 이클립스 미운용)과 AOCS 확정 요구(정렬≤1.0°,
  세션253초≪예산)를 정량 충족.
- 점화시험: 채널당 980~1,015W·68~72mN, 2채널 동시 리플≤100mVpp — 합격.

## Δv 총합 대조(sysreq)
1,500(진입) + 750(유지) = **2,250m/s** = sysreq 요구치와 정확히 일치.

## 잠정→정정 이력
1. PROP-DSN-01: REQ-PROP-STR-장착 회신 대기(8×20초×2회) 초과로 자기 제안
   수치(트러니언4점·축8.5g/횡4.5g)로 착수 → STR 정식 회신이 동일 수치를
   그대로 채택 확인(정정 불필요, ICD 협상 성공 사례).
2. PROP-CORR-01: REQ-PROP-EPS-전력 확정 회신(채널당 1,000W 상한, 최초
   가정 1.5kW 대비 하향) 반영해 eps-load-profile.md·
   aocs-unloading-interface.md의 추력을 200mN→70mN으로 정정.

검증: sysreq PROP 항목(Δv 합계 2,250m/s) 수치 정확히 일치, 양 유닛 축약
체인(DSN-RVW-TST)+시험 완료
