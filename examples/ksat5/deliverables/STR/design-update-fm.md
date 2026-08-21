# STR-FM-01: 설계 갱신 (EM 승계 리스크 반영)
입력: examples/ksat5/deliverables/STR/module-em.md,
examples/ksat5/deliverables/STR/mounting-interfaces.md,
examples/ksat5/deliverables/AIT/rx-str.md,
examples/ksat5/deliverables/EPS/module-em.md

## EM 이월 항목 확인: EPS 배터리 브래킷
- EM 인도 시점(module-em.md)에는 "잠정 합격"으로 이월된 유일 항목.
- AIT 인수 시험(rx-str.md §2)에서 최종 발자국 95×90×20mm 기준 JIG-03
  정합 확인 — **브래킷 형상·홀 패턴(M3×4) 변경 없음**.
- EPS 최종 질량(EPS module-em.md §2): 0.22 kg (잠정치 0.25 kg 대비
  -0.03 kg, 마진 방향). EPS 문서 자체가 "STR 설계 변경 불필요"를
  명시.
- 판단: 브래킷 도면·체결 위치는 EM 그대로 FM에 승계한다. 새 EPS FM
  회신 요청은 발행하지 않는다 — 이미 두 건(AIT 재확인 + EPS 확정치)
  으로 필요가 해소됐기 때문이다. AOCS/COMM은 이 시점 FM 변경 요청이
  board에 없어 EM 인터페이스(icd-aocs-str.md, icd-comm-str.md,
  mounting-interfaces.md)를 그대로 승계한다.

## FM 설계 갱신 내역
- 구조 형상·데크 배치·전 부재 도면: EM(mounting-interfaces.md)과 동일.
- 질량표 갱신(EPS 배터리 확정치 반영):

| 항목 | EM(kg) | FM(kg) |
|---|---|---|
| STR 구조체(레일·패널·데크·브래킷) | 2.95 | 2.95 (변경 없음) |
| (참고) EPS 배터리 예약 발자국 질량 | 0.25(잠정) | 0.22(확정) — STR 구조 질량 자체에는 미포함 항목 |

STR 자체 구조 질량은 EPS 배터리 질량 변경과 무관(브래킷은 빈 예약
슬롯 구조물일 뿐, 탑재 질량은 EPS 소관) — **STR 구조 질량 2.95kg로
불변, 배분 3.00kg 대비 여유 0.05kg 유지**.
- 재료·공정: 비행 인증(FM) 등급 Al 6061-T6/7075-T6, 로트 추적 관리
  적용(EM 대비 신규 요구, STR-FM-03에서 반영).

## 검증
AIT 인수 시험(rx-str.md) 및 EPS 최종 질량(module-em.md)을 대조해
EPS 배터리 브래킷 형상 변경 없음·질량 마진 방향 확인. STR 구조
질량 2.95kg 불변으로 배분 3.00kg 이내 유지 확인.
