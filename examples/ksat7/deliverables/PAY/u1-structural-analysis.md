# PAY-U1 안테나 패널 구조해석(전개·발사하중)
입력: examples/ksat7/deliverables/PAY/u1-antenna-design.md, examples/ksat7/deliverables/PAY/mech-deployment-reply.md

## 정적해석(준정적 10g)
루트/팁 패널 최대 응력 발생 위치: 힌지 브래킷 체결부. 안전계수(MS) 1.6(알루미늄
7075 패널 구조 기준). sysreq STR 준정적 10g 요구 충족.

## 모드해석(전개 상태)
| 경계조건 | 1차모드 |
|---|---|
| 패널 자체(자유단) | 6.8 Hz |
| 버스 장착 상태(STR 인터페이스 강성 50N/µm 가정) | 37.2 Hz(STR ANL-S 해석치, aocs-alignment-spec.md 인용) |

AOCS-U1-DSN이 요구한 제어대역 이격(안테나 1차모드≥4.0Hz) 대비 37.2Hz로
9.3배 이격 — 충족.

## 판정
준정적10g MS=1.6, 1차모드37.2Hz≥4.0Hz(AOCS 요구) 충족. 검도·검토회 상정 가능.
