# INT-TST-2 통합시험2 — 전기 100V·15kW 통합 부하시험

입력: examples/ksat8/deliverables/AIT/rx-2.md,
examples/ksat8/deliverables/GSE/scoe-100v-reply.md,
examples/ksat8/deliverables/EPS/module-fm.md, examples/ksat8/deliverables/PROP/module-fm.md,
examples/ksat8/deliverables/COMM/module-fm.md, examples/ksat8/deliverables/TCS/module-fm.md

## 시험 구성
scoe-100v-reply.md 100V/15kW SCOE로 EPS 비행모델(PCU·배터리)을 통합
본체 형상에서 급전, PAY(11,000W)·PROP-EP(3,000W, 2채널 동시)·
COMM(220W)·TCS 히터(200W)·HK부하 동시 인가(EPS module-fm.md 부하
프로파일 그대로 재현).

## 결과
| 항목 | 요구/확약 | 실측 | 판정 |
|---|---|---|---|
| 버스전압 | 100V±2V | 98.1~101.9V(통합부하 전구간) | PASS |
| 통합부하 인가량 | 14,420W(모듈 실증치) | 14,398W(±0.2%, SCOE 채널모니터 합산) | PASS |
| PAY 인러시 LCL | 트립없음(EPS-U1-TST 9ms 확인치) | 통합형상 재확인 9.4ms, 트립없음 | PASS |
| PROP-EP 2채널 동시 리플 | ≤100mVpp | 실측 88mVpp | PASS |
| 비상차단 인터록 | <10ms(GSE 사양) | 모의차단 8ms | PASS |
| 접지분리 | >100MΩ | 통합형상 재확인 128MΩ | PASS |

모든 서브시스템을 동시에 물린 통합 조건에서도 EPS module-fm.md의
모듈 단위 판정과 수치 정합 — 상호간섭에 의한 열화 없음.

검증: 100V±2V 전구간 유지, 통합부하14,398W≈14,420W 정합, LCL/리플/
인터록/접지분리 전항 PASS
