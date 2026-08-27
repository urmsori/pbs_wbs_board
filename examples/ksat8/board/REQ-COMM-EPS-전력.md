---
id: REQ-COMM-EPS-전력
title: 송신 전력 할당 요청
status: DONE
parent: M-COMM
source: M-COMM
owner: EPS-U1-DSN-01
deliverable: examples/ksat8/deliverables/EPS/comm-power-allocation.md
after: -
track: EPS
started: 2026-08-27 03:47:05
finished: 2026-08-27 03:47:12
---

TT&C 트랜스폰더(COMM-U1)의 송신기(TWTA/SSPA) 정격을 정하려면 EPS가 COMM에
배정하는 전력 예산이 먼저 필요하다.

무엇을 알려달라: (1) COMM 서브시스템에 배정된 상시 부하 전력(W, EOL·이클립스
포함), (2) 버스 전압(100V±2V) 외 COMM이 받는 조정 전압 레일 유무, (3) 송신기
피크(양방향 레인징·고출력 TM 구간) 허용치.

회신 산출물 경로 제안: examples/ksat8/deliverables/EPS/REQ-COMM-EPS-전력-reply.md
검증: COMM 상시150W·피크220W 배정 확정
