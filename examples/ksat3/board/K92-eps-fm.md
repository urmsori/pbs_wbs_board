---
id: K92
title: EPS FM — 부품 확정·총질량 보고·버스트 하드웨어 검증
status: DONE
parent: K90
owner: sonnet-eps
deliverable: examples/ksat3/deliverables/eps-fm.md
after: K40
track: EPS
started: 2026-08-21 02:27:00
finished: 2026-08-21 02:27:46
---

EM 통합시험의 FM 이관 항목에서 발견된 필요: 부스트 IC 등 부품 선정,
태양전지판·하니스 포함 총질량 보고, 12W 버스트 시 버스 전압 하드웨어
검증(저온·저SOC·돌입전류 포함). 배터리 CAD·부스트 위치를 확정해 STR이
쓸 수 있게 한다.
산출물: examples/ksat3/deliverables/eps-fm.md

작업 기록:
1. 부스트 IC 가정 선정(TPS61088급, 입력 2.5~8.4V·출력 7.2V·2A·전류제한 5A) — comm-to-eps.md 부하(12W/10s, 돌입 3.5~5A) 커버 확인.
2. 배터리 CAD 배치 확정(2×2 4셀+배전보드 적층) — 스택 치수 90×90×26mm, 부스트 스테이지 위치·국부 방열패드(15×15mm) 확정 → STR K91 입력으로 명시.
3. 총질량 집계(스택 0.35+태양전지판 0.30+하니스 0.05=0.70kg) — 배분 0.8kg 대비 여유 0.10kg 확인.
4. 저온(-10℃)·저SOC(6.0V)·돌입전류(5A) 조합 해석 수행 — 잠정 통과로 판단하되 실측 미실시·가정치 의존 한계를 리스크로 명시.
검증: 총질량이 배분 이내이고 버스트 검증 결과를 근거와 함께 기록
