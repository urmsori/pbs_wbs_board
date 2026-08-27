---
id: REQ-EPS-PAY
title: SAR 첨두 펄스 부하 프로파일 요청 (1.8kW 버스트 파형·듀티)
status: DONE
parent: M-EPS
source: EPS-U1-DSN
owner: PAY-U2-DSN-01
deliverable: examples/ksat7/deliverables/PAY/eps-pulse-profile-reply.md
after: -
track: PAY
started: 2026-08-27 01:54:40
finished: 2026-08-27 01:55:02
---

PCDU 슈퍼캡 하이브리드 방전 회로(EPS-U1-DSN)를 설계하려면 SAR 능동위상배열
송신 펄스의 실제 전력 파형이 필요하다. sysreq 가정치: 첨두 1.8kW, 최대 90s/궤도
버스트. 확인 요청:
1) 펄스 상승/하강 시간(rise/fall, ms 단위)과 버스트 내 리플 허용폭
2) 버스트 듀티(스트립맵 vs 스팟 모드별 on/off 주기, 궤도당 총 버스트 횟수)
3) 버스트 중 최대 전류(A) 및 모선 50V±5V 기준 순간 전압강하 허용치
산출물: PAY 팀이 정하는 경로(예: examples/ksat7/deliverables/PAY/)에 위 3항목을
수치로 명시해 달라. 무응답 시 sysreq 가정치(1.8kW/90s, 구형파 근사)로 잠정 설계한다.
검증: 상승/하강<1ms, 5s×18회/궤도 듀티6%, 첨두전류40.0A·전압강하≤3% 회신
