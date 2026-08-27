---
id: FIX-TCS-COMM-YPANEL
title: COMM -Y측판 국부 열점 통합 열해석 반영 요청 (AIT→TCS)
status: OPEN
parent: M-TCS
source: INT-TST-4
track: TCS
owner: -
deliverable: -
after: -
started: -
finished: -
---

INT-TST-4 통합 열해석에서 COMM-U1 SSPA 베이스플레이트 국부 온도가 위성 공유 라디에이터
경로 기준 +51.6°C로, sysreq TCS 대역(-15~+45°C, SAR송수신기 기준) 대비 +6.6°C 초과가
재확인됐다(comm-u1-anl-t.md에서 COMM 자체 판정 범위 밖으로 승계한 항목). COMM 부품 자체
정격(85°C) 마진은 33°C로 충분하나, TCS 라디에이터 국부 설계(MLI 개구부·히트파이프4식
배치)에 이 열점을 반영한 재검토를 요청한다. 산출물 제안:
examples/ksat7/deliverables/TCS/comm-ypanel-thermal-review.md
검증: TCS 통합열해석 반영 후 국부 초과분 해소 또는 수용 가능 판정 회신
