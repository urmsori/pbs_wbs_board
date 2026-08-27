---
id: EPS-U1-TST
title: PCU·배전유닛 기능·부하시험
status: DONE
parent: M-EPS
source: -
owner: EPS-U1-TST-01
deliverable: examples/ksat8/deliverables/EPS/pcu-functional-test.md
after: CAL-EPS-U1, FAC-EPS-U1
track: EPS
started: 2026-08-27 04:10:27
finished: 2026-08-27 04:10:53
---

PCU를 전자부하 뱅크로 0~15kW 전 채널 부하를 인가해 100V±2V 조절 성능과
PAY 채널 인러시(12.8A/10ms) 대응성을 실증한다. 교정된 전자부하·DAQ
(CAL-EPS-U1), 시험실(FAC-EPS-U1), PA 입회(PA-EPS-U1 완료) 하에 검사자
(INS)와 다른 사람(시험)이 수행한다. RB 조건부 승인의 조건(인러시 실측)을
해소한다.
검증: sysreq EPS 100V±2V·15kW 실측 충족, 인러시 LCL 트립여유 확인
검증: 100V±2V·15kW 실측충족, RB조건 해소
