---
id: REQ-PAY-HAR
title: 대전류 펄스 배선 요구 전달
status: DONE
parent: M-PAY
source: PAY-U2-DSN
owner: HAR-CHK-01
deliverable: examples/ksat7/deliverables/HAR/pay-req-reply.md
after: -
track: HAR
started: 2026-08-27 01:53:44
finished: 2026-08-27 01:53:57
---

송수신기·펄스발생기 설계(PAY-U2-DSN)가 산출한 대전류 펄스 배선 요구를 HAR 팀에
전달한다: 첨두전류 40.0A(1.8kW/45V, 펄스중 최저 모선전압 기준), 이중화 2계통
분산급전 시 계통당 20.0A, 전압강하 ≤3% @펄스(sysreq HAR 정합) 만족을 위한 계통당
배선저항 상한 0.0675Ω. EMC 차폐(펄스 스위칭 노이즈)도 sysreq HAR 요구에 포함된다.
산출물: HAR 팀이 남기는 문서 — 배선 게이지·경로·차폐 설계가 위 전류·저항·전압강하
조건을 만족함을 확인.
검증: 계통당 20.0A·저항≤0.0675Ω에서 전압강하≤3% 만족 회신
검증: 계통당20A·R<=0.0675옴에서 전압강하0.85%<=3%, 단일계통전량40A도1.70%<=3% 만족
