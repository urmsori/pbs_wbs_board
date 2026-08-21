---
id: EPS-03
title: 배터리 용량 설계
status: DONE
parent: M-EPS
owner: EPS-BAT
deliverable: examples/ksat5/deliverables/EPS/battery-sizing.md
after: EPS-01
track: EPS
started: 2026-08-21 07:01:48
finished: 2026-08-21 07:08:44
---

EPS-LEAD의 필요: 배터리 용량은 발생 전력(EPS-01)만으로 정할 수 없고
식(蝕) 구간과 첨두 구간의 실제 부하 소비 전력이 있어야 한다. 이 Work를
집는 사람이 부족한 부하 프로파일을 상대 팀에 직접 요청(ICD)해서 모은
뒤 용량을 확정한다.
산출물: examples/ksat5/deliverables/EPS/battery-sizing.md
검증: 식 구간 에너지수요(마진포함 5.71Wh) 대비 선정팩 25.8Wh로 DoD 22% 산출, LEO Li-ion 통상 한도(25~30%) 이내 확인, 첨두전류 2.46A 셀 정격 이내
