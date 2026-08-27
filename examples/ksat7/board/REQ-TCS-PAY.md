---
id: REQ-TCS-PAY
title: SAR 송수신기 첨두 발열 프로파일 요청
status: DONE
parent: M-TCS
source: TCS-DSN-01
owner: PAY-U2-DSN-01
deliverable: examples/ksat7/deliverables/PAY/tcs-thermal-profile.md
after: -
track: PAY
started: 2026-08-27 01:52:47
finished: 2026-08-27 01:53:26
---

TCS 히트파이프·라디에이터 용량을 정하려면 SAR 송수신기의 첨두 발열 프로파일이
필요하다: sysreq 첨두 펄스 부하 1.8kW·최대 90s/궤도를 전제로, TCS는 (1) 송수신기
발열량(W, 열로 변환되는 비율), (2) 펄스 지속시간·주기당 반복 횟수, (3) 발열원
표면적·인터페이스 위치를 요청한다. TCS 단독으로는 PAY 전력-발열 변환효율을 알 수
없어 PAY 확인이 필요하다.
산출물 제안: examples/ksat7/deliverables/PAY/tcs-thermal-profile.md — 첨두 발열
프로파일(W, 지속시간, 위치) 확정.
검증: TCS 히트파이프 설계 입력으로 사용 가능한 수치 형태(W·s) 제공 확인
검증: 첨두발열270W×5s×18회/궤도, 인터페이스0.30㎡, -15~+45°C 요구 회신
