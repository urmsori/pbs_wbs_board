---
id: STR-ARCH-REV
title: 구조 아키텍처 PAY 인터페이스 개정(실회신 반영)
status: DONE
parent: STR-ARCH
source: REQ-STR-PAY
owner: STR-DSN-02
deliverable: examples/ksat6/deliverables/STR/architecture.md
after: REQ-STR-PAY
track: STR
started: 2026-08-22 01:34:11
finished: 2026-08-22 01:34:50
---

STR-ARCH를 마칠 때 PAY 팀 회신(REQ-STR-PAY)이 폴링 시간 내 도착하지 않아
잠정 가정(질량15kg·8-M6 볼트원)으로 진행했다. 이후 PAY 팀이 실제 값(질량
35kg·3점 킨매틱 마운트·각변위≤0.01°·병진≤10µm)으로 회신했으므로, 이 차이를
architecture.md에 반영하고 구조 예산에 영향이 없는지 재확인해야 한다(규칙
4절 재작업 경로 — 원인이 입력 산출물이므로 정정 게시글로 처리).
산출물: examples/ksat6/deliverables/STR/architecture.md(PAY 절 갱신).
검증: PAY 실회신(질량35kg·3점킨매틱·각변위≤0.01°·병진≤10µm) 반영, 최초 형상(킨매틱3점) 유지로 1차구조 재설계 불필요, sysreq STR 질량≤22kg(21.9kg) 판정 유지
