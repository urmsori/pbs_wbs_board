# MECH-U2 SA 전개힌지 1차모드 재검증 (SA 실측 ICD 반영)

입력: examples/ksat7/deliverables/MECH/mech-u2-anl-s.md, examples/ksat7/board/REQ-MECH-SA.md,
examples/ksat7/deliverables/SA/mech-sa-interface-reply.md

## 변경 입력
윙당 패널 관성: 잠정 2.5kg·m² → 실측 **10.1kg·m²**(약 4배). 힌지강성(8000N·m/rad)·볼트패턴은
SA측과 상호 일치 확인되어 변경 없음.

## 재해석 결과
1차모드 f∝1/√I 근사 스케일링: 0.62Hz × √(2.5/10.1) ≈ **0.31 Hz**. sysreq(SA 항목 참고
"전개 후 1차모드≥0.5Hz") **미충족** — 부족분 0.19Hz.

## 판정 및 조치
**리스크 등급: 높음(RED), SA-MECH 공유 리스크.** 힌지강성 8000N·m/rad를 상향(예 약×3
~24000N·m/rad)해야 0.5Hz 요구 회복 가능(개략 계산). 힌지강성 상향은 힌지 본체 재설계(더 큰
토션스프링/구조 단면) 필요 — MECH-U2 rev.2 설계반복 대상으로 이관. SA 팀과 공동 검토 필요
(모드 요구는 sysreq SA 항목이므로 SA module-fm에도 동일 리스크 공유 권고).
**본 Work는 재검증(수치 확정)까지가 범위이며, 힌지 재설계는 M-MECH 후속 설계반복(rev.2)으로
이관 — module-fm.md에 오픈 리스크로 기록.**
