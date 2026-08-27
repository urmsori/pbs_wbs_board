---
id: REQ-STR-PAY-장착
title: Ka 중계기 패널 질량·장착·방열 인터페이스 요청 (STR→PAY)
status: DONE
parent: M-STR
source: STR-U2-DSN
owner: PAY-DSN-01
deliverable: examples/ksat8/deliverables/PAY/str-pay-mount-reply.md
after: -
track: PAY
started: 2026-08-27 03:55:49
finished: 2026-08-27 03:55:49
---

왜: STR-U2(패널·장착부)에서 TWTA/중계기 장비가 실리는 남/북 패널(샌드위치
구조+매립 히트파이프)을 설계하려면 얹히는 장비의 질량·장착점·발열량을 먼저
알아야 패널 두께·심재·체결점·히트파이프 용량을 정할 수 있다.
요청: (1) Ka 24채널 중계기 장비(TWTA·채널부 등) 총질량과 패널별(남/북) 배분(kg),
(2) 장비 장착 볼트 패턴/피치·체결점 수·국부강성 요구, (3) 방열 인터페이스
요구(패널 계면 최대 열유속 W/m² 또는 장비당 발열 W, 요구 계면 열저항 K/W).
회신 산출물 제안: examples/ksat8/deliverables/PAY/str-pay-mount-reply.md
검증: 회신치를 STR-U2 패널 질량·히트파이프 용량 설계에 반영해 sysreq STR
질량 ≤380kg 배분 내 확인
검증: 총156.6kg(78.3kg/패널), 열유속1.5W/cm²·계면열저항0.15K/W 회신
