---
id: REQ-PAY-EPS-전력
title: "[PAY→EPS] 11kW 공급·100V 전력품질 확약 요청"
status: DONE
parent: M-PAY
source: M-PAY
owner: EPS-U1-DSN-01
deliverable: examples/ksat8/deliverables/EPS/pay-power-capability.md
after: -
track: EPS
started: 2026-08-27 03:47:05
finished: 2026-08-27 03:47:12
---

sysreq 전력은 탑재체 11kW(버스 100V±2V)를 규정한다. PAY-U1 설계(DSN)가
24채널 중계기(수신기·TWTA 24기·스위치 매트릭스)의 채널별 전력 배분을
정하려면 EPS가 탑재체 채널 정격(11kW 배분 가능 여부)과 100V 버스 품질
(전압 리플·과도응답·순시 최대전류 대응)을 확약해야 한다.
산출물 제안: examples/ksat8/deliverables/EPS/pay-power-capability.md —
탑재체 채널 배분 가능 용량(kW), 100V 버스 리플(mVpp)·과도응답(정착시간),
TWTA 기동 시 순시전류 대응 여부.
검증: 확약 용량 ≥11kW, 리플·과도응답이 TWTA 전원 규격 이내인지 확인
검증: 확약용량11kW, 리플/과도응답 규격내
