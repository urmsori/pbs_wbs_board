입력: examples/ksat8/deliverables/SE/sysreq.md, examples/ksat8/deliverables/EPS/fsw-tmtc-reply.md, examples/ksat8/deliverables/TCS/fsw-tmtc-reply.md, examples/ksat8/deliverables/PROP/fsw-tmtc-reply.md, examples/ksat8/deliverables/AOCS/fsw-tmtc-reply.md, examples/ksat8/deliverables/COMM/fsw-tmtc-reply.md, examples/ksat8/deliverables/PAY/fsw-tmtc-reply.md, examples/ksat8/deliverables/OBC/fsw-hw-reply.md

# 위성 관리 SW(FSW) 코어 설계 (FSW-U1, 축약)

관리 SW는 OBC 하드웨어(레지스터 맵·드라이버, OBC/fsw-hw-reply.md) 위에서
6개 서브시스템(EPS/TCS/PROP/AOCS/COMM/PAY)을 감시·제어하는 태스크 집합
으로 구성한다. 각 태스크의 실행 주기·핵심 로직은 해당 서브시스템의
REQ-FSW-*-TMTC 회신에서 그대로 도출한다.

## 1. 태스크 구성과 실행 주기
| 태스크 | 근거 | 주기 |
|---|---|---|
| EPS 감시(배전·배터리) | EPS 회신 TM≈76점·배터리 파라미터 | 1Hz |
| TCS 히터 자동제어 | TCS 회신 설정점/데드밴드표(H1~H6) | 1Hz(데드밴드 이력제어) |
| PROP 밸브/추력기 구동 잠금 | PROP 회신 interlock 3원칙 | 이벤트 구동(TC 수신 시) |
| AOCS 제어 루프 | AOCS 회신 10Hz, 입력(오차3+각속도3)/출력(휠토크4) | **10Hz** |
| COMM TT&C 프레임 처리 | COMM 회신(잠정) CCSDS 패킷·CRC16·2단계확인 | 프레임 도착시 |
| PAY 채널 스위칭 | PAY 회신 SWM좌표·순차 100ms 간격 | 이벤트 구동 |
| OBC 자체(이중화 감시) | OBC/fsw-hw-reply.md 워치독·절체 레지스터 | 1Hz(워치독 kick) |

스케줄러는 AOCS 10Hz를 최고 우선순위로 고정 배정(sysreq 지향 0.05°
유지가 유일하게 10Hz를 요구), 나머지는 1Hz 베이스 틱에서 라운드로빈.

## 2. 히터 제어(TCS 로직 이식)
TCS 회신의 설정점·데드밴드 표(H1 5±2°C, H2 5±3°C, H3 0±3°C, H4/H5
-5±5°C)를 그대로 이력(hysteresis) 제어 로직으로 구현 — 온도가
(설정점-데드밴드) 이하면 ON, (설정점+데드밴드) 이상이면 OFF. 주 센서
고장 시 TC로 예비 채널 수동 전환(TCS 회신 이중화 방식).

## 3. PROP 안전 잠금(interlock)
PROP 회신의 3원칙(자세안정 플래그·2단계 arm+fire·탱크압력정상, 동일축
대향 추력기 동시점화 금지, 자세이상 시 전 추력기 자동OFF)을 FSW가
TC 디코더 앞단 잠금 계층으로 구현 — 조건 불충족 시 TC 자체를 거부하고
NAK TM을 COMM 태스크로 반환.

## 4. TC 검증(COMM 로직, 잠정)
COMM 회신(잠정)의 CRC-16·2단계 확인·순번검사를 TC 디코더의 표준
검증 파이프라인으로 구현. **COMM-U1 확정 후 정정 필요** — 잠정 항목.

## 5. PAY 채널 전환 시퀀서
PAY 회신의 `SWM[in][out]` 좌표계와 100ms 순차 규칙을 그대로 시퀀서
큐로 구현 — 동시 전환 명령이 오면 큐에 넣고 100ms 간격으로 순차 실행.

## 6. OBC 이중화 연동
fsw-hw-reply.md의 워치독 IRQ0(1s 미갱신 시 리셋) 요구에 맞춰 관리 SW
메인 루프는 매 1Hz 틱마다 워치독 kick을 수행하고, 크리티컬 상태(현재
모드·최근 TC 순번)를 EEPROM 스냅샷에 기록(절체 시 상태 복원용,
fsw-hw-reply.md 절체 소요 목표 ≤500ms 내에 스냅샷 갱신이 끝나도록
주기 1s 권고를 그대로 채택).

검증: 7개 회신의 로직·주기·인터락을 태스크별로 1:1 반영, AOCS 10Hz가
스케줄러 최우선순위임을 확인.
