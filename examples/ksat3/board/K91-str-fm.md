---
id: K91
title: STR FM — 트레이 높이·방열패드 확정, 진동 경계 반영
status: DONE
parent: K90
owner: sonnet-str
deliverable: examples/ksat3/deliverables/str-fm.md
after: K40,K92
track: STR
started: 2026-08-21 02:28:37
finished: 2026-08-21 02:29:29
---

FM 이관 항목: EPS Rev.B의 배터리 CAD·부스트 위치(K92 산출물)가 나와야
트레이 높이(20→25~28mm 가능성)와 버스트 국부 방열패드를 확정할 수 있다
— after에 K92가 걸린 이유다. 발사체 규격 가정으로 진동 경계조건도 반영.
산출물: examples/ksat3/deliverables/str-fm.md

작업 기록:
- eps-fm.md 확정 치수(90×90×26mm) 반영해 하단 EPS 트레이 높이 26mm로 확정(K82 미결 해소)
- 부스트 스테이지 위치(좌측 하단 모서리) 반영해 15×15mm 국부 방열패드 존 트레이 방열면에 추가
- 발사체 규격 미확정으로 GEVS급 가정치(랜덤진동 14.1 Grms 등)로 진동 경계조건 정성 판단 수행(정량 해석은 리스크로 남김)
- 질량표 재계산(국부 방열패드 마운트 5g 반영, 여유 재배분) — 구조 순수 질량 800g, 예산 900g 이내 재확인
검증: K92 확정 치수로 트레이·방열 확정, 질량 예산 이내 재확인
