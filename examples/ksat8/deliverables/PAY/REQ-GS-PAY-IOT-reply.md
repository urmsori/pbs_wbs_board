# REQ-GS-PAY-IOT 회신 — 중계기 IOT 시험 요구

입력: examples/ksat8/deliverables/PAY/u1-dsn.md, examples/ksat8/board/REQ-GS-PAY-IOT.md

1) 채널 확인 범위: **24채널 전수** EIRP 측정(시간당 1채널, 총 24회). 목표
   52dBW 대비 허용편차 **±0.5dB**(52.43dBW 설계치 기준 마진 0.43dB 고려 시
   최소 51.5dBW 이상이면 PASS).
2) NPR: 전수 측정은 비효율적 — **대표 4채널**(패널 좌표상 모서리·중앙 배치
   채널)에서 노이즈로딩 시험. 채널당 소요시간 약 30분(로딩 안정화+측정),
   총 2시간.
3) 지상 시험국 요구: Ka 업링크 EIRP ≥85dBW(TWTA 포화구동 확인용), 수신
   대역폭 ≥40MHz, 우선편파 정합(급전 설계 기준), G/T ≥30dB/K.

검증: 24채널 EIRP(±0.5dB), 대표4채널 NPR(≥18dB) 측정 계획 회신
