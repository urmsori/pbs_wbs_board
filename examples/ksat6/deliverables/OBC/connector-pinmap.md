# OBC 커넥터·핀맵 사양 (HAR-D1 회신)

입력: examples/ksat6/deliverables/OBC/proc-board.md, examples/ksat6/deliverables/SE/sysreq.md

HAR 팀의 REQ-HAR-OBC(주버스 하니스 설계용) 회신.

## 커넥터 구성
| 커넥터 | 파트번호(예시) | 핀수 | 용도 |
|---|---|---|---|
| J1 (전원) | MDM-9P | 9 | 모선 28V±4V 입력 |
| J2 (1553B) | MDM-15P | 15 | 1553B 이중화 버스 A/B |
| J3 (CAN) | MDM-9P | 9 | CAN 버스 A/B(이중화) |
| J4 (SpW) | MDM-9P ×4 | 9×4 | SpW 링크 4채널(REQ-OBC-PAY 회신 반영) |

## 핀맵
### J1 전원(9핀)
| 핀 | 신호 | 정격 |
|---|---|---|
| 1 | +28V_MAIN_A | 3A |
| 2 | +28V_MAIN_B(이중화) | 3A |
| 3-7 | RTN(귀환) ×5 | - |
| 8 | CHASSIS_GND | - |
| 9 | INHIBIT/ENABLE | 신호 |

### J2 1553B(15핀, MIL-STD-1553B 표준 핀배치)
| 핀 | 신호 |
|---|---|
| 1,2 | BUS A HI/LO |
| 3,4 | BUS B HI/LO |
| 5-15 | 실드/예비(표준 배치 준용) |

### J3 CAN(9핀, DB9 표준)
| 핀 | 신호 |
|---|---|
| 2 | CAN_A_L |
| 7 | CAN_A_H |
| 1,3 | CAN_B_L/H(이중화, 비표준 확장) |
| 6 | GND |
| 나머지 | 예비 |

### J4 SpW ×4 (각 9핀, ECSS-E-ST-50-12 준용)
| 핀 | 신호 |
|---|---|
| 1-2 | Data In +/- |
| 3-4 | Strobe In +/- |
| 5-6 | Data Out +/- |
| 7-8 | Strobe Out +/- |
| 9 | Shield |

## 정격 요약
- 전원 입력: 28V±4V, 최대 3A(이중화 채널당).
- 신호선(1553/CAN/SpW): 5V 로직/차동, 각 채널 절연.

검증: 사양이 MIL-STD-1553B, ECSS-E-ST-50-12 표준 핀배치를 준용함을 확인, io-board.md의 채널 수(1553×1이중화, CAN×2, SpW×4)와 일치.
