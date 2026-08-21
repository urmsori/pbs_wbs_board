---
id: K30
title: 통신 EM 개발
status: DONE
parent: K00
owner: sonnet-comm
deliverable: examples/ksat3/deliverables/comm-em.md
after: K01
track: COMM
started: 2026-08-21 02:06:00
finished: 2026-08-21 02:12:25
---

UHF 트랜시버+안테나의 EM 개발 전체 — 내부 단계는 본문 작업 기록.
외부 필요는 발견되는 대로 게시글로.
산출물: examples/ksat3/deliverables/comm-em.md

## 작업 기록
- 트랜시버 아키텍처 확정: UHF 반이중, 9.6 kbps GMSK, 단일 PA 송신단 + LNA 수신단 구성.
- 링크버짓 1차 산출: 9.6 kbps 기준 링크마진 ≥6 dB 확보(자유공간 손실·안테나 이득·수신단 NF 가정치로 계산, sysreq 다운링크 요구 충족).
- 송신 출력 배분: PA 출력 및 효율 가정으로 버스트 피크 소비전력 12 W(10초)로 설정 — sysreq 교차 요구(버스 전압 ≥7.0 V) 대응은 EPS 확인 필요로 분리.
- 안테나 형식 선정: 모노폴 대비 전개형 다이폴(턴스타일) 채택 — 이득·편파 다양성 확보, 전개 기구는 STR 확인 필요로 분리.
- RF 하니스·커넥터 형식 잠정 선정(SMA, 동축 RG178급) — 질량 예산(COMM 0.5 kg) 내 가배분.
- 내부 검토 결과 EPS(버스 전압)·STR(전개 공간·방향) 확인 없이는 EM 통합 진행 불가로 판단, 필요 2건을 게시글로 분리.
- K71(eps-to-comm.md) 반영: 현 EPS 1S/DET 기준선으로는 12 W 버스트 시 ≥7.0 V 불가 확인(구조적 미달) — EPS Rev.B 재설계 전제로 12 W 기준안 유지, 8 W 축소안(마진 약 4.2 dB, 요구 미달) 대안도 함께 산정.
- K72(str-to-comm.md) 반영: 안테나 전개 기구 수용 공간·전개 방향(반경 방향 직교 2조) 모두 확보 가능으로 확인 — 안테나 항목 해소.
- comm-em.md 개정(2차) 완료 — 12 W 조건의 최종 성립 여부는 K40 통합시험 검증 항목으로 이관하고 K30을 마감한다.
검증: 입력 2건 반영, 12W 조건의 성립 여부를 K40 검증 항목으로 이관
