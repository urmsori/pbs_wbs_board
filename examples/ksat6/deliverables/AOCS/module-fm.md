# AOCS 비행모델(FM) 인도 — 취합
입력: examples/ksat6/deliverables/AOCS/pointing-budget.md, star-tracker-accept.md, gyro-accept.md, rwa-accept.md, magnetorquer.md, hil-test.md, fsw-if-reply.md, eps-load-reply.md, examples/ksat6/deliverables/STR/interface-aocs.md, examples/ksat6/deliverables/EPS/aocs-wheel-current-allowance.md

## 구성
별추적기 1기, 자이로(IMU) 1기, 반작용휠 4기(3축+여유1기), 마그네토커 3기
(직교3축), 정렬 큐브(STR 인도), 지향 예산·모드 설계 문서.

## sysreq 판정 (자기 항목)
| sysreq 항목 | 요구 | 실측/확정(HIL) | 판정 |
|---|---|---|---|
| 지향정확도 | 0.05°(3σ) | 0.034° | PASS |
| 지향안정도 | 0.005°/s | 0.0028°/s | PASS |
| 모멘텀 덤핑 | 자기토커 | 3축 마그네토커, 축당 20Am² | PASS |

hil-test.md 실측치가 pointing-budget.md 예측치보다 최신 확정 사실이므로
실측치를 최종 채택(규칙 4절 취합 모순 처리 — 예측보다 실측 우선).

## 완료된 인터페이스 협상 (ICD)
- REQ-AOCS-STR ↔ STR: 정렬큐브 수직도 5arcsec, 열드리프트 3.2arcsec — 요청치
  이내로 인도(examples/ksat6/deliverables/STR/interface-aocs.md).
- REQ-AOCS-EPS ↔ EPS: PCDU AOCS채널 4A 연속/6A·20ms 서지 — 요청 첨두전류
  이내로 인도(examples/ksat6/deliverables/EPS/aocs-wheel-current-allowance.md).
- REQ-EPS-AOCS(수신) ↔ EPS: 부하 프로파일 회신(첨두38W/평균25.7W) — 완료.
- REQ-FSW-AOCS(수신) ↔ FSW: 제어주기20Hz·신호목록 회신 — 완료.

## 잠정 가정
없음 — 모든 송·수신 인터페이스 요청이 폴링 내 회신 완료됨.

검증: hil-test.md 실측 0.034°/0.0028°/s ≤ sysreq 0.05°/0.005°/s(마진32%/44%),
전 유닛(6건) DONE, 송신 REQ 2건·수신 REQ 2건 모두 회신 완료.
