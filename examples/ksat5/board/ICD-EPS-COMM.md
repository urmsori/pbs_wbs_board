---
id: ICD-EPS-COMM
title: COMM 송신기 소비 전력 프로파일 요청
status: DONE
parent: EPS-03
owner: COMM-RF
deliverable: examples/ksat5/deliverables/COMM/icd-eps-comm-power.md,examples/ksat5/deliverables/COMM/transceiver-em.md
after: -
track: COMM
started: 2026-08-21 07:05:57
finished: 2026-08-21 07:06:54
---

EPS-BAT의 필요: 배터리 용량(방전 심도, 첨두 부하)을 산정하려면 UHF
송신기의 실제 소비 전력 프로파일이 필요하다 — 송신 시(피크)와 대기 시
(평균) 소비 전력(W), 1궤도당 송신 duty cycle(교신 횟수·지속시간), 버스
직결 액추에이터 레일(8.4V 공칭, 방전 말기 하한 약 6.8V) 동작 가능
전압 범위를 COMM 팀이 직접 확인해 알려주기 바란다. sysreq의 UHF
9.6kbps 마진 ≥6dB 조건에서 요구되는 송신 출력 기준으로 작성해 달라.
산출물: COMM 팀이 남기는 송신 전력 프로파일 문서(경로는 COMM 팀이 정함).
검증: 전력 프로파일·duty cycle 회신, PA효율 역산치와 transceiver-em.md rev.2 정합 확인
