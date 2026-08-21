---
id: ICD-COMM-EPS
title: 송신 시 버스 전압 유지 확인 요청
status: DONE
parent: COMM-04
owner: EPS-DSN
deliverable: examples/ksat5/deliverables/EPS/icd-comm-eps.md
after: -
track: EPS
started: 2026-08-21 07:05:57
finished: 2026-08-21 07:06:52
---

COMM의 필요: 트랜시버 EM(COMM-02 산출물, 송신 전류 프로파일)을
전력 팀에 전달하고, 해당 송신 전류 펄스 하에서 버스 전압이 규정
범위(± 허용치) 안에서 유지되는지 EPS 팀의 확인(해석 또는 실측)을
받아야 한다. COMM과 EPS 당사자 간 협상으로 ICD를 완성한다(SE는
중재만).
산출물: 전력 팀이 남기는 확인 결과 문서(버스 전압 유지 여부, 필요 시
디커플링/여유 설계 권고) — 경로는 협상 결과에 따라 EPS 팀이 정한다.
검증: COMM 실측 전류프로파일×EPS-02 레일정격 합산 결과 엣지 조건 정격 20% 초과 확인, 설계변경 권고 회신
