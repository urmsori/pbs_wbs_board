# MECH-U2 rev.2 힌지 강성 증대 재설계

입력: examples/ksat7/deliverables/MECH/mech-u2-anl-s2.md, examples/ksat7/board/REQ-MECH-SA2.md

## REQ-MECH-SA2 처리
SA 팀에 관성 재확인을 요청했으나 4×15초 폴링 무응답(SA 세션 종료) — **기존 REQ-MECH-SA
회신치(질량7.6kg/윙, 관성10.1kg·m²)를 정본으로 채택**하고 이를 기준으로 설계를 확정한다.
REQ-MECH-SA2는 OPEN 상태로 board에 잔류(추후 SA 팀 복귀 시 확인용, 무응답 처리 기록).

## 재설계
힌지 토션스프링 단면·자유장 증대로 회전강성을 **8000 → 25,000 N·m/rad**로 상향(약 3.1배).
힌지 본체 축 직경 +2mm, 브래킷 보강. 볼트 패턴(4점 M6 PCD80mm)·백래시 요구(≤0.05°)는 rev.1과
동일 유지(SA측과 이미 상호 확인된 항목이므로 변경 없음).

## 예측
f≈0.01096·√(k/I) 근사(관성10.1kg·m² 고정): k=25,000 → **f≈0.545 Hz** — sysreq(SA 전개후
1차모드≥0.5Hz) 대비 마진 +0.045Hz(9%). **판정: 충족(예측), 마진 타이트 — MFG·TST에서 확정.**
