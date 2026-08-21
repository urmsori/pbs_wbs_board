---
id: NEED-SW-EPS
title: EPS 인수 시험용 EGSE SW(레일 텔레메트리·부하스텝)
status: OPEN
parent: AIT-RX-EPS
owner: -
deliverable: -
after: -
track: SW
started: -
finished: -
---

AIT-TST의 필요: EPS EM 모듈(module-em.md) 인수 시험(버스 레귤레이션·
부하응답 확인)을 시작하려는데, 4개 레일을 동시에 감시하고 부하 조건을
인가할 지상시험 SW가 없다. module-em.md/power-conditioning.md/test-plan.md/
icd-eps-comm-power.md를 읽고 확인한 구체 요구:

- 4레일 구조: 1차버스 8.4V(비규제, EOD 6.8V), 5V±2%, 3.3V±2%, 액추에이터
  레일 8.4V(버스직결, 개별 과전류 차단) — 4레일 동시 전압·리플(≤50mVpp)
  텔레메트리 로거 필요(power-conditioning.md §버스구조).
- 부하 스텝 시험: 5V/3.3V 레일 0→정격 80% 스텝, sag/overshoot ≤5%·
  복구시간 ≤1ms 판정 스크립트 필요(test-plan.md §3).
- **액추에이터 레일 미해결 리스크**: icd-eps-comm-power.md에 따르면
  COMM 송신 펄스(1.6A→2.0A, <5ms 엣지)가 이 레일에 실린다 — EPS-04
  시험계획도 "COMM 송신 펄스 파형을 실측 조건으로 추가 필요"라고
  명시. 이 펄스 파형을 재현해 액추에이터 레일 sag를 측정하는 부하
  스텝 스크립트 필요.
- 보호회로 시험: UVLO 3.0V/cell, OVP 4.2V/cell 트립점 확인(모의 배터리
  전압 인가, 트립점 ±5% 판정)(test-plan.md §4).
- 배터리 방전 말기(6.8V) 조건에서 액추에이터 레일 전압 하한 재현 및
  4레일 유지 확인 필요(module-em.md §3 EOD 리스크).

요청: 4레일 텔레메트리 로거, 부하스텝 파형 생성기(COMM 펄스 프로파일
포함), 보호회로 트립점 판정기를 갖춘 EPS EGSE 시험용 SW 일체.
산출물: (지원 역할이 정함)
