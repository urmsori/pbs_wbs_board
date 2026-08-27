# COMM-U2 S-band TT&C 기능시험

입력: examples/ksat7/deliverables/COMM/comm-u2-ins.md, examples/ksat7/deliverables/CAL/comm-u2-cal.md

## 시험 조건
- 교정필 S-band 신호발생기·스펙트럼분석기·전력계(CAL-COMM-U2) 사용
- 업링크 코맨드 시뮬레이터 → 트랜스폰더 → 다운링크 텔레메트리 루프

## 실측 결과
| 항목 | 요구(sysreq.md) | 실측 |
|---|---|---|
| 업링크 데이터율 | 64 kbps | 64.0 kbps, BER < 1e-6, 락 유지 |
| 다운링크 데이터율 | 2 Mbps | 2.00 Mbps, BER < 1e-7 |
| 다운링크 RF 출력 | (헤리티지 규격 2W) | 1.95 W (39.9 dBm) |
| 수신감도(업링크) | 헤리티지 규격 -108dBm | -110dBm 락 유지(마진 2dB) |

판정: sysreq.md S-band 64k/2M 요건 실측 충족(업링크 64.0kbps, 다운링크 2.00Mbps
정확히 일치, 마진 정상 범위).

검증: sysreq S-band 64k/2M → 실측 64.0kbps/2.00Mbps 충족, BER 규격 이내.
