---
id: COMM-04
title: 송신 시 버스 전압 유지 확인
status: DONE
parent: M-COMM
owner: COMM-RF
deliverable: examples/ksat5/deliverables/COMM/bus-voltage-check.md
after: COMM-02
track: COMM
started: 2026-08-21 07:02:12
finished: 2026-08-21 07:08:13
---

COMM-LEAD의 필요: 트랜시버 EM(COMM-02)의 송신 전류 펄스가 위성 버스
전압을 규정 범위 밖으로 흔들지 않는지 확인해야 한다. 실제 버스
임피던스·전압 유지 여부는 전력 팀만 알 수 있으므로, 이 Work를 맡은
사람이 EPS 팀에 직접 ICD 요청(ICD-COMM-EPS)을 올린다.
산출물: examples/ksat5/deliverables/COMM/bus-voltage-check.md (송신
전류 프로파일 대비 EPS 확인 결과 반영)
검증: EPS 회신 반영, 5V레일 rev.1 초과문제(-0.4A)를 rev.2 레일분리로 해소(+1.48A 여유) 확인; 액추에이터레일 퓨즈정격·EOD출력저하는 EPS-04 실측범위로 명시
