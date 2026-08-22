# OBC I/O보드(1553/CAN/SpW) 설계

입력: examples/ksat6/deliverables/SE/sysreq.md

## 인터페이스 구성
| 버스 | 채널 수 | 용도 |
|---|---|---|
| MIL-STD-1553B | 1이중화(A/B) | AOCS·EPS·TCS·PROP 명령/상태(간선 버스) |
| CAN | 2이중화(A/B) | 저속 유닛 상태 폴링(TCS 히터, PROP 밸브 상태 등) |
| SpW | 4채널 | 탑재체(PAY) 영상 다운로드용 2채널, COMM(X-band) 송신 버퍼용 1채널, 예비 1채널 |

판정(sysreq OBC "1553/CAN/SpW 인터페이스"): 세 버스 모두 구현 → **충족**.

## SpW 채널 대역폭 배정 — 잠정 가정
REQ-OBC-PAY(PAY 팀에 탑재체 데이터율·필요 SpW 링크 수 문의)를 발행했으나
회신 대기 중이므로, sysreq.md의 "X-band 150Mbps, 일 60GB" 하향 목표를
역산하여 잠정 배정한다:
- SpW 채널당 물리 대역폭 200 Mbps(표준 SpW 링크), 탑재체 영상용 2채널
  합산 400 Mbps 여유 확보 → X-band 150Mbps 하향에 필요한 버퍼링 처리율을
  충분히 상회한다고 **잠정 가정**.
- PAY 팀 회신이 도착하면 실제 요구 데이터율로 채널 배정을 재검토한다
  (재작업 발생 시 별도 게시글로 기록, 규칙 4절).

검증: 채널 수가 sysreq 3개 버스 종류를 모두 포함함을 확인. SpW 대역폭 배정은 잠정.
