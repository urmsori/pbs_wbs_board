---
id: REQ-SA-MECH
title: 3윙 힌지 인터페이스 확정 요청
status: DONE
parent: M-SA
source: SA-U1-DSN
owner: MECH-IF-01
deliverable: examples/ksat7/deliverables/MECH/sa-hinge-icd.md
after: -
track: MECH
started: 2026-08-27 01:55:33
finished: 2026-08-27 01:55:44
---

3윙 태양전지판(SA-U1-DSN) 설계에서 전개 후 1차모드 ≥0.5Hz(sysreq) 판정을
하려면 힌지 강성·질량 인터페이스가 필요하다. 확인 요청:
1) 힌지쌍 회전강성(N·m/rad)과 전개 잠금 후 백래시 허용치
2) 패널-힌지 접속부 질량 배분 한도(kg, 윙당) 및 부착 볼트 패턴/좌표
3) 전개 충격 ≤40g(sysreq) 기준 힌지측 완충 특성
산출물: MECH 팀이 정하는 경로(예: examples/ksat7/deliverables/MECH/)에 위 3항목을
수치로 명시해 달라. 무응답 시 힌지 강성 8000 N·m/rad(1윙 기준 가정)로 잠정 설계 후
모드해석에서 민감도만 표기한다.
검증: 힌지강성8000N·m/rad, 백래시≤0.05˚, 질량한도≤3.0kg/윙 회신
