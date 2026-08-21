---
id: NEED-RF-COMM
title: COMM 인수 시험용 RF 감쇠기·더미로드
status: OPEN
parent: AIT-RX-COMM
owner: -
deliverable: -
after: -
track: RF
started: -
finished: -
---

AIT-TST의 필요: COMM EM 모듈(module-em.md) 인수 시험(링크버짓·PA 출력
확인)을 시작하려는데, PA가 2W(33dBm)를 SMA 안테나 포트로 직접 출력해
스펙트럼분석기/전력계에 그대로 물리면 계측기 입력 정격을 초과하고
실내에서 방사 송신도 할 수 없다. transceiver-em.md(module-em.md §"모듈
구성" 1항 인용)를 읽고 확인한 구체 요구:

- RF 인터페이스: SMA(f) 안테나 포트 1개, PA 출력 2W(33dBm)
  (transceiver-em.md §인터페이스 커넥터 정의).
- **미해결 리스크**: 액추에이터 레일 EOD 6.8V에서 PA 출력 저하 가능성,
  링크버짓 마진 0.3dB로 협소(transceiver-em.md §리스크, icd-eps-comm-
  power.md §액추에이터 레일 요청) — COMM 팀이 AIT 단계에서 실측
  확인을 요청한 항목.

요청: SMA(m/f) RF 케이블 + 33dBm급 감쇠기(전력계 정격 이내로 감쇠) +
50Ω 더미로드(방사 없이 종단 측정용), PA 출력을 8.4V·6.8V 두 공급전압
조건에서 정확히 측정할 수 있는 구성.
산출물: (지원 역할이 정함)
