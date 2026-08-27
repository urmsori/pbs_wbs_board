# AIT 수령검사 — STR·MECH·HAR (rx-1)

입력: examples/ksat7/deliverables/STR/module-fm.md, examples/ksat7/deliverables/MECH/module-fm.md,
examples/ksat7/deliverables/HAR/module-fm.md

## STR 수령
- rev.2가 최종 인도본: 1차구조 질량 44.6kg≤45kg(마진 0.4kg, 타이트), 1차모드(SAR 안테나 장착)
  36.1Hz≥35Hz(실측, NCR CLOSED, 마진+1.1Hz/3.1%), 준정적10g 손상없음 — sysreq STR 3항목 전부
  충족 확인.
- U2 브래킷도 3점 킨매틱 PCD400mm/8-M8로 재제작(실측5.4kg), 로컬강성62N/µm≥50N/µm 확인 —
  rev.1의 인터페이스 형상 불일치(4점 PCD500)는 해소.
- **질량 38↔72kg 불일치**: 초기 설계가정(안테나38kg)과 PAY 실측(72.0kg)의 괴리가 1차모드 미충족
  (rev.1, 30.4Hz)의 원인이었음을 확인. rev.2 재해석·재제작(72.0kg 반영)으로 36.1Hz 달성 —
  질량 불일치 자체는 rev.2에서 실측 반영으로 해소됨. INT 단계에서 통합 상태 실측 재확인 필요
  (→ INT-TST-1).

## MECH 수령
- U1 SAR 2단 전개기구: 전개충격 37.1g≤40g(마진7.3%), 단일고장 허용 실측 확인 — 변경 없음.
- U2 SA 힌지 rev.2: 강성 24,600N·m/rad(목표25,000 대비-1.6%), 전개후 1차모드 0.53Hz≥0.5Hz
  (실측, NCR CLOSED, 마진+0.03Hz/6%) — 최종 인도본.
- **REQ-MECH-SA2 재확인**: MECH module-fm.md는 "4×15초 폴링 무응답(SA팀 세션종료)"으로
  기록했으나, board 실제 상태는 REQ-MECH-SA2 **DONE**(SA-DSN-02 회신, 질량7.6kg/윙·관성10.1kg·m²
  변경없음 재확인) — MECH의 기록이 회신 도착 이전 시점의 스냅샷이었던 것으로 판단, 현재는
  리스크 해소됨. AIT 기록에 정정 반영.
- SA 3윙 + SAR 2단 동시(또는 순차 근접) 전개는 유닛 레벨 FAC 예약이 각 기구 단독 시험용으로만
  이뤄졌음(MECH-U1-TST, MECH-U2-R2-TST 모두 단일 기구 기준) — 통합형상 전체(72kg 안테나 2단
  붐 전장 + 3윙 SA) 동시 지지가 가능한 중력보상 설비 존재 여부 불명 → GSE 필요 판단 대상.

## HAR 수령 — 이월 2건
1. **EPS 커넥터 물리 정합**: HAR-U1은 잠정 p/n(PCDU-PWR-J4)으로 발주·제작. 전기 성능(저항
   19.3~19.5mΩ, 예산41.7mΩ 대비 54%여유)은 INS에서 이미 재확인됐으나, EPS 정식 회신의 실커넥터
   파트번호와의 **물리적 정합**은 미확인 — INT 단계 확인 필요(→ INT-TST-1).
2. **U1 자체 EMC 차폐 실측**: u1-review-b.md 권고에 따라, U2-INS-01(동일 편조실드·SPG 접지
   구조)로 대표 실시한 EMC 차폐 실측(접지본딩6.5mΩ·실드연속성0.03Ω)을 U1 자체로도 실측
   확인 필요 — INT 단계 확인 필요(→ INT-TST-2).

## 재사용 판단
- STR/MECH rev.2 모달 재확인: 기존 진동시험 설비(STR-U1-R2-TST, MECH-U2-R2-TST에 사용된 FAC
  가진기·고정지그) 재사용 가능 — 통합 형상 장착 지그만 신규 제작(설비 자체는 NEED 대상 아님).
- HAR 커넥터 물리정합·EMC 실측: 기존 기계 게이지·EMC 실측 장비(U2-INS-01급) 재사용 가능 —
  신규 장비 불요.
- SAR 2단+SA 3윙 통합형상 동시 중력보상: 유닛 레벨 설비는 개별 기구 전용 규격으로, 통합형상
  전체 지지용량·리치 부족 가능성 — **신규 GSE 필요 판단**(NEED-GSE-DEPLOY 발행, source=본 RX).

## 판정
STR·MECH rev.2 최종 인도본 확인, sysreq 전항목 충족. HAR 이월 2건은 INT-TST-1/2로 확인 예정.
MECH REQ-MECH-SA2는 board상 DONE으로 최신화 확인(리스크 해소). 대형 동시전개 중력보상 설비는
신규 GSE 필요로 판단.
