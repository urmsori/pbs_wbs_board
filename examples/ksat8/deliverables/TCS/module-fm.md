# 열제어(TCS) 비행모델 인도 — module-fm
입력: examples/ksat8/deliverables/TCS/panel-design.md, examples/ksat8/deliverables/TCS/thermal-analysis.md,
examples/ksat8/deliverables/TCS/structural-analysis.md, examples/ksat8/deliverables/TCS/drawing-check.md,
examples/ksat8/deliverables/TCS/review-01.md, examples/ksat8/deliverables/TCS/review-02.md,
examples/ksat8/deliverables/TCS/rb-disposition.md, examples/ksat8/deliverables/TCS/panel-mfg.md,
examples/ksat8/deliverables/TCS/tvac-test.md, examples/ksat8/deliverables/SE/sysreq.md

## TCS-U1: TWTA 히트파이프 매립 패널 (설계 풀체인 + 제작 + 열진공시험)
DSN→ANL-T/ANL-S(2인)→CHK→RVW(2인)→RB→CM 배포→MFG→TVAC 전 단계 완료.

- 채널당 발열 210W×24 = 5.04kW(PAY 확정) ≤ 확약 방열용량 6.3kW(마진 1.26kW,
  20%).
- 패널 1.6m×1.2m(STR 확정), CFRP 면판, 히트파이프 8본/매(16본 합계), M6
  40개소 체결, 1차모드 64.2Hz(STR 실측, 요구 60Hz 이상), 구조질량
  52kg/매(104kg/2매).
- TVAC 실측: 고온 +52°C(해석과 일치), 저온 -9°C(히터 보정 후) — sysreq
  작동범위 **-10~+60°C** 충족, 방열 **6kW** 요구 충족(마진 포함).
- 이클립스 히터 200W(6채널), 배터리/추진배관/밸브 우선순위(EPS 확약과
  일치). TM 16점·TC 12점 FSW 회신 완료.

## sysreq 대조(판정)
| 요구 | 값 | 달성 |
|---|---|---|
| 방열 | 6kW | 5.04kW 부하, 6.3kW 용량(마진 1.26kW) — 충족 |
| 작동범위 | -10~+60°C | TVAC 실측 -9~+52°C — 충족 |

## 잠정→정정 이력
1. TCS-DSN-01: PAY/STR 회신 대기(8×20초×2회) 초과로 250W/채널·4점체결
   가정 후 착수 → TCS-CORR-01(PAY 확정 210W 반영) → TCS-CORR-02(STR 확정
   1.6×1.2m·CFRP·M6 40개소·64.2Hz 반영)로 순차 정정 완료.
2. TCS-MFG-01: REQ-TCS-CM-형상관리 회신 대기 초과로 RB-01 산출물을 입력
   삼아 착수 — 이후 CM(owner CM-01)이 정식 배포 완료(내용 상충 없음).

검증: sysreq TCS 항목(방열 6kW·작동 -10~+60°C) 수치 인용 충족, 전 유닛
설계 풀체인(DSN-ANL×2-CHK-RVW×2-RB-CM)+제작+TVAC 완료
