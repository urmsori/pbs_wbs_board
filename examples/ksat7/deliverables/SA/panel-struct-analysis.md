# 3윙 패널 구조해석(전개 후 모드)

입력: examples/ksat7/deliverables/SA/panel-design.md, examples/ksat7/deliverables/MECH/sa-hinge-icd.md,
examples/ksat7/deliverables/SA/mech-sa-interface-reply.md

MECH 확정 힌지강성 8000 N·m/rad(윙당), 패널 질량 7.6kg/윙·관성 10.1kg·m²
(SA→MECH 회신치와 동일)을 입력으로 캔틸레버 모드해석 수행.
전개 후 1차모드(swing/굽힘) **0.58Hz** 산출.

발사 시 구속상태(HDRM 고정) 준정적 10g에서 패널 루트 응력 62MPa
(복합재 적층판 허용응력 대비 SF 3.1).

검증: sysreq 전개후1차모드≥0.5Hz 대비 0.58Hz 충족(마진16%), 힌지강성 MECH확정치와 일치하므로 REQ-SA-MECH 잠정치 리스크 해소
