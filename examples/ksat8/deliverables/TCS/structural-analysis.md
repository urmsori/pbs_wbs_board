# 패널 매립 구조·질량 해석
입력: examples/ksat8/deliverables/TCS/panel-design.md, examples/ksat8/deliverables/STR/panel-interface.md

[정정 이력: TCS-CORR-02에서 STR 확정 인터페이스(1.6×1.2m, CFRP, M6 40개소
그리드 체결) 반영. 1차모드는 STR-U2-ANL-S 실해석 결과(64.2Hz)를 채택하고,
질량은 STR 확정 구조질량(52kg/매)에 TCS측 히트파이프 8본/매를 반영해
갱신 — 최초본(45Hz 자체추정·15.0kg/매)보다 정확하다.]

## 결과
- 히트파이프 매립홈(깊이 6mm, 홈-면판 잔여두께 1.5mm)이 CFRP 면판(0.3mm)과
  분리되어 면판 좌굴강도 저하 없음(홈은 심재에만 형성, STR 확정 인터페이스
  기준 재확인).
- 패널 1차모드(M6 40개소 그리드 체결, STR-U2-ANL-S 실해석): **64.2Hz** —
  요구 60Hz 대비 여유 확보(STR panel-interface.md에서 채택).
- 질량 예산(STR 확정): 구조체(면판+코어+체결, 히트파이프 제외) **52kg/매**
  (STR-U2 목표 104kg/2매 내). 히트파이프 8본/매(1본당 약 0.6kg 가정)
  ≈4.8kg/매은 STR-U2 총질량에 "TCS/STR 공동 몫 22kg(2매)"로 이미 포함됨
  (개별 배분은 상세설계 단계에서 확정).

검증: 1차모드 64.2Hz≥요구 60Hz(STR 실측 채택), 구조질량 52kg/매(STR 확정
회신과 일치, 히트파이프분은 STR 총질량에 포함)
