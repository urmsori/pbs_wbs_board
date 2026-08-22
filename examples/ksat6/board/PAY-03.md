---
id: PAY-03
title: 탑재 전자부
status: DONE
parent: M-PAY
source: -
owner: PAY-ELEC-01
deliverable: examples/ksat6/deliverables/PAY/payload-electronics.md
after: PAY-02
track: PAY
started: 2026-08-22 01:25:24
finished: 2026-08-22 01:27:06
---

초점면 조립체(PAY-02)의 라인율·TDI 단수·비트심도가 먼저 확정되어야
(after=PAY-02) 이를 구동·판독·기내보정(비균일보정·압축)하는 탑재 전자부의
처리율·전력이 정해진다. sysreq의 "기내 보정" 요구를 이 유닛이 충족한다.
산출물: examples/ksat6/deliverables/PAY/payload-electronics.md — 판독/보정
처리율, 촬영시퀀스 전력(평균/첨두), 출력 데이터율(압축 전/후).
검증: 압축후100~115Mbps ≤150Mbps, 처리지연400µs이내 PASS
