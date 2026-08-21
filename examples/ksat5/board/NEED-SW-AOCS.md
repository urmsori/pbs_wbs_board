---
id: NEED-SW-AOCS
title: AOCS 인수 시험용 EGSE SW(센서 자극·텔레메트리)
status: DONE
parent: AIT-RX-AOCS
owner: SW-EGSE-01
deliverable: examples/ksat5/deliverables/SUPPORT/need-sw-aocs.md
after: -
track: SW
started: 2026-08-21 07:08:46
finished: 2026-08-21 07:09:19
---

AIT-TST의 필요: AOCS EM 모듈(module-em.md) 인수 시험(자세 루프 기동)을
시작하려는데, 모듈을 자극하고 응답을 읽을 지상시험용 SW가 없다.
module-em.md/control-sw-design.md를 읽고 구체 요구를 확인함:

- 온보드 SW는 SAFE/DETUMBLE/NOMINAL/MOMENTUM-DUMP 4모드로 동작
  (control-sw-design.md §1) — 4모드 전이를 각각 트리거·확인할 수 있는
  시험 스크립트가 필요.
- 센서 자극 대상: 스타트래커(쿼터니언 입력, 1 Hz), MEMS 자이로(각속도
  입력, 100 Hz), 태양센서 2식(coarse 자세용) — EKF(스타트래커+자이로
  융합)와 SAFE모드 태양센서 coarse 경로(±5°)를 각각 자극할 시뮬레이션
  입력 생성기 필요(control-sw-design.md §2).
- 액추에이터 응답 텔레메트리 수신: 리액션휠 3축 토크 지령/각운동량,
  마그네토토커 3축 지령 — MOMENTUM-DUMP 천이 조건(휠 각운동량 포화
  임계치 도달) 확인을 위한 텔레메트리 로깅·파싱 SW 필요(control-sw-
  design.md §3~4).
- 성능 판정 기준: 종합 지향오차 ≤0.5° (SYS-REQ, module-em.md §4 실측
  0.47°) 재현 확인용 지향오차 산출 스크립트 필요.

요청: 위 4모드 트리거, 센서 자극 시뮬레이터, 텔레메트리 로거/파서,
지향오차 산출기를 갖춘 AOCS EGSE 시험용 SW 일체.
산출물: (지원 역할이 정함)
검증: 4모드 트리거·센서 자극·텔레메트리 로거·지향오차 산출기 4항목 대응 확인
