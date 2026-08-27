# OBC 프로세서보드·2TB 저장부 상세설계

입력: examples/ksat7/deliverables/SE/sysreq.md, examples/ksat7/deliverables/OBC/comm-interface-spec.md

## 프로세서보드
- CPU: 방사선강화 듀얼코어 32bit RISC급, 200MIPS 정격.
- 예상 부하: 비행SW(FSW-U1/U2) + SAR 시퀀서 실행 시 96MIPS 사용.
- 처리여유: (200-96)/200 = 52% ≥ sysreq OBC 처리여유 50% — 충족(마진 2%p).
- 버스: MIL-STD-1553B 1채널(플랫폼 제어), CAN 2채널(서브시스템), SpW 5채널
  (탑재체 원시데이터 입력용 4 + COMM 다운링크 출력용 1 — REQ-OBC-PAY·
  REQ-COMM-OBC 실회신 반영, 정정판).

## 2TB 저장부
- 구성: NAND 플래시 모듈 4×512GB, RAID0 유사 병렬 스트라이핑, 컨트롤러 이중화.
- 총 용량: 2.05TB(가용 2.0TB, ECC/여유 예약 2.5%).
- 기록(write) 대역폭: ≥3.6Gbps (REQ-OBC-PAY 실회신 스팟모드 순간 첨두
  3.2Gbps 대비 마진 12.5%, SpW 4채널×채널당 실효 900Mbps 병렬 기록으로 달성).
- 기록 버퍼: 512MB(회신 권고 스팟 400MB 대비 마진 28%), 순간 첨두-평균
  차(3.2→1.1Gbps) 흡수.
- 판독(read/재생) 대역폭: ≥920Mbps, REQ-COMM-OBC 회신(언더런 마진 15%,
  버퍼 256Mbit)과 정합(변경 없음).

## sysreq OBC 항목 판정
| 항목 | 요구 | 확인 | 판정 |
|---|---|---|---|
| 처리여유 | ≥50% | 52% | 충족 |
| 저장용량 | 원시 2TB | 가용 2.0TB | 충족 |
| 인터페이스 | SpW/CAN | 1553×1, CAN×2, SpW×5 구현 | 충족 |

## 정정 이력(OBC-U1-DSN-REV, REQ-OBC-PAY 실회신 반영)
- 기록대역폭: 1.2Gbps(잠정) → 3.6Gbps(확정, 실회신 스팟첨두 3.2Gbps 대비
  마진 12.5%).
- SpW 채널: 2채널(잠정) → 5채널(확정, PAY입력 4 + COMM출력 1).
- 근거: examples/ksat7/deliverables/PAY/obc-datarate-reply.md
  (스팟 첨두3.2Gbps/평균1.1Gbps, 스트립맵 첨두1.2Gbps/평균450Mbps, SpW 4채널 요구).

검증: 처리여유 52%≥50%(충족), 저장용량 2.0TB≥2TB(충족), 기록대역폭
3.6Gbps≥실회신 첨두3.2Gbps(마진12.5%, 충족), SpW 5채널로 PAY·COMM 양쪽
실회신 요구 수용 — sysreq OBC 3항목 전부 충족(정정 완료, 잠정 사항 해소).
