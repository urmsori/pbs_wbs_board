---
id: RISK-LINK
title: EOD 링크마진 0dB 확보 설계 종결
status: DONE
parent: INT2
owner: COMM-DSN
deliverable: examples/ksat5/deliverables/COMM/link-margin-fix.md,examples/ksat5/deliverables/COMM/antenna-design.md
after: -
track: COMM
started: 2026-08-21 07:35:35
finished: 2026-08-21 07:36:40
---

(담당 역할: COMM-DSN)

AIT의 필요: EM 인수시험(rx-comm.md)에서 EOD 6.8V 조건 PA 출력을
실측한 결과 32.7dBm으로, 링크마진이 정확히 6.0dB(요구 ≥6dB 충족,
여유 0dB)로 나왔다. 추가 열화 여지가 없어 FM에서는 그대로 넘길 수
없는 잔여 리스크다.

요청: FM에서 마진을 확보할 설계 방안(안테나 이득 상향, 코딩/부호화
이득, EOD 전압에서의 PA 출력 유지 중 팀이 판단해 선택)을 확정하고
재검증까지 마쳐 종결하라.
산출물: examples/ksat5/deliverables/COMM/link-margin-fix.md
검증: 방안A(피드망 위상 재최적화, 무게/전력 영향없음) 채택, EOD 마진 6.0dB(여유0)→7.5dB(여유1.5dB) 재계산 확인; 방사패턴 실측은 FM AIT로 이월
