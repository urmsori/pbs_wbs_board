# PAY→OBC 회신: SAR 원시데이터율·SpW 링크 요구
입력: examples/ksat7/deliverables/PAY/u1-antenna-design.md, examples/ksat7/deliverables/PAY/u2-transceiver-design.md

## 원시데이터율(모드별)
| 모드 | 대역폭(chirp) | 샘플링 | 양자화 | 순간 첨두 데이터율 | 평균(활성 관측구간) |
|---|---|---|---|---|---|
| 스트립맵(3m) | 100 MHz | 200 MHz | 4bit BAQ, I/Q | 1.2 Gbps | 450 Mbps |
| 스팟(1m) | 300 MHz | 600 MHz | 4bit BAQ, I/Q | 3.2 Gbps | 1.1 Gbps |

버스트 구조: 최대 90s/궤도(sysreq 정합, PAY-U2-DSN 파형과 동일 전제).

## 필요 SpW 링크
- 스팟 모드 순간 첨두(3.2Gbps) 대응: SpW 4채널(채널당 실효 ~800Mbps).
- 스트립맵 모드(1.2Gbps): SpW 2채널로 충분.
- 버퍼 여유: 순간 첨두-평균 차(스팟 기준 3.2→1.1Gbps) 흡수를 위해 OBC측
  기록 버퍼 ≥1초 분량(스팟 400MB) 권고.

검증: 위 데이터율·채널수를 입력으로 OBC 저장부 쓰기대역폭·버퍼 확정 가능
(sysreq 원시 2TB 저장 용량은 다중 관측 누적을 위한 고정 스토리지 용량이며
1회 관측 데이터량은 위 표의 평균률×관측시간으로 산출).
