---
id: REQ-AOCS-SA-모드
title: "[AOCS→SA] 태양전지판 전개 구조모드 요청"
status: DONE
parent: M-AOCS
source: M-AOCS
owner: SA-U1-DSN-01
deliverable: examples/ksat8/deliverables/SA/aocs-mode-interface.md
after: -
track: SA
started: 2026-08-27 03:47:05
finished: 2026-08-27 03:47:12
---

sysreq는 SA 전개 후 1차모드 ≥0.1Hz만 규정한다. AOCS-U1 제어계 설계(DSN)가
제어대역폭을 정하려면 태양전지판(2윙) 전개 후 1차모드의 실제(잠정) 값과 감쇠비,
그리고 태양추적(1축 구동) 중 발생하는 외란 토크 프로파일을 알아야 제어-구조
연성(둘 사이 대역 분리, 통상 5배 이상)을 확인하고 노치필터 설계 여부를 정할 수
있다. SA-U1-DSN 착수 전 회신을 요청한다.
산출물 제안: examples/ksat8/deliverables/SA/aocs-mode-interface.md — 전개 후
1차모드(Hz)·감쇠비, 태양추적 구동 외란 토크(N·m, 주파수).
검증: 1차모드가 AOCS 제어대역폭 목표의 5배 이상인지 확인, 외란 토크를 휠 용량 배분에 반영
검증: 1차모드0.12Hz목표·SADA외란 회신, 이격마진조건 제시
