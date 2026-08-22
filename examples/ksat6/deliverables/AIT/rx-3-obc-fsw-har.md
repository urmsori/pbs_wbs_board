# 수령검사 — 항전·SW(OBC/FSW/HAR)
입력: examples/ksat6/deliverables/OBC/module-fm.md, examples/ksat6/deliverables/FSW/module-fm.md, examples/ksat6/deliverables/HAR/module-fm.md

## 수령 확인
| 모듈 | 핵심 수치(인도 문서 인용) | 수령 판정 |
|---|---|---|
| OBC | 처리여유52%(≥50%), 메모리128GB, 1553/CAN/SpW 3버스 전부 시험 | 이상 없음 |
| FSW | sw-verification.md 21케이스 PASS, 안전모드·재프로그래밍 PASS | 이상 없음 |
| HAR | 전압강하 최대1.11%(≤2%), EMC 접지연속성 0.03~0.05Ω, 절연≥280MΩ, 도통100% | 이상 없음 |

## 통합시험 필요 장비 판단
- OBC·FSW는 프로세서 시뮬레이터·통합시험 벤치에서 이미 전 항목(버스
  3종, 21케이스) 시험을 마쳤고, module-fm.md에 시스템 레벨에서만 새로
  드러나는 인터페이스 이슈가 없다 — 신규 NEED 근거 없음.
- HAR module-fm.md "잔여 리스크" 항목은 유닛2(전개부) 굽힘 관련 MECH
  측 문의가 늦게 들어올 가능성을 언급하나, "이 인도 시점까지 수신된
  문의 없음"으로 닫혀 있어 현재 장비 필요로 이어지지 않는다.
- 시스템 레벨 항전 통합(OBC-AOCS-COMM-PAY 버스 연결)은 각 모듈이 이미
  확정한 인터페이스(1553/CAN/SpW, connector-pinmap.md)를 그대로 쓰는
  배선 작업이며, HAR 유닛1(주버스 하니스)이 이미 그 커넥터·핀맵으로
  제작·검사 완료되어 별도 치구 없이 연결 가능하다.
- 억지로 NEED를 만들지 않는다 — 근거 있는 장비 필요가 이 수령검사에서는
  발견되지 않았다.

## 재사용 판단
- OBC 통합시험 벤치(1553/CAN/SpW 인터페이스 어댑터)는 AIT EGSE의
  표준 항전 인터페이스 어댑터와 호환 — INT-TST-2/INT-TST-3에서 그대로
  재사용한다.
- 도통·절연·EMC 차폐 측정기(HAR-I1/I2 사용 장비)는 AIT 표준 계측 장비와
  동일 — 시스템 레벨 하니스 재검사가 필요해지면(사용 안함, 현재 불필요)
  재사용 가능.

검증: OBC·FSW·HAR module-fm.md의 sysreq/시험 판정을 각 1개씩 인용해
수령 수치 일치 확인. 신규 장비 필요 근거 없어 NEED 미발행 — 재사용
판단 2건 명시.
