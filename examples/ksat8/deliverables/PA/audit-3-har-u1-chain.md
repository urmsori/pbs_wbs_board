# PA 표본감사 3 — HAR-U1 설계체인 수치·입력경로 대조 (v3.2)

## 감사 대상
HAR-U1 100V 전력 하니스 설계체인: DSN-01 → ANL-T-01(열)·ANL-E-01(절연·
전압강하) → CHK-01(도면검도) → RVW-A-01(전기)·RVW-B-01(열/절연) → RB-01
(검토회 판정), 그리고 그 뒤를 이은 서비스 부서 산출물 CM 배포
(har-u1-release.md)·PUR 발주(har-u1-po.md, har-u2-po.md).

## 수치 일관성 대조
| 항목 | DSN(설계) | CHK(검도, EPS정식대조) | RVW-A | RB(판정) | CM 배포 |
|---|---|---|---|---|---|
| 전압강하(분기, 최악) | 0.766V/0.77%(잠정30A) | 0.77%(잠정, 실제8~20A대비 더 여유) | 0.77% | 0.23%/0.77% | 0.23%/0.77% |
| 도체간 이격 | 3mm | 3mm(EPS요구1.5mm 상회) | 3mm | (승계) | (승계) |
| 대지간 이격 | 4mm | 4mm(EPS요구2.0mm 상회) | 4mm | (승계) | (승계) |
| 커넥터 p/n | 잠정 PCU-PWR-J1 | 정식 MIL-DTL-38999 III 필요 확인 | 조건부(갱신조건) | 조건부 승계 | **PUR 발주 시 정식 p/n 반영**(har-u1-po.md 확인) |

전 단계 수치 일치, 조건(커넥터 p/n) 추적이 CHK→RVW→RB→CM→PUR까지
끊기지 않고 승계·이행됨을 확인(PUR 발주서에 "정식 MIL-DTL-38999 III
p/n으로 발주 — RB-01 조건 이행 완료" 명시).

## "입력:" 경로 적법성 대조 (표본)
| 파일 | 입력 경로 | 대조 결과 |
|---|---|---|
| u1-drawing-check.md(CHK) | u1-design.md, u1-thermal-analysis.md, u1-electrical-analysis.md, **EPS/distribution-connector-spec.md** | EPS 경로는 `REQ-HAR-EPS-배전`(parent: **M-HAR**) 회신 — HAR 자기 사슬 회신, **적법** |
| har-u1-release.md(CM, 본 SVC 산출물) | u1-design/thermal/electrical/drawing-check/review-a/review-b/review-board.md 7건 | 전건 parent=M-HAR(HAR 자기 사슬) — **전건 적법** |
| har-u1-po.md(PUR, 본 SVC 산출물) | u1-review-board.md | source(HAR-U1-RB-01)와 일치 — **적법** |
| har-u2-po.md(PUR, 본 SVC 산출물) | u2-review-board.md | source(HAR-U2-RB-01)와 일치, 축약체인(CM 생략) 조건 그대로 반영 — **적법** |

## 감사 결과
**결함 없음.** 수치 전건 일치, 조건(커넥터 p/n) 승계·이행 확인, "입력:"
경로 전건 적법(자기 사슬 또는 source 일치) — 감사1·2에서 발견한 "타 사슬
무단 인용" 패턴이 HAR 체인 및 본 SVC 산출물에는 없음.

검증: 전압강하·이격거리 수치 전건 일치, 커넥터 p/n 조건 CHK→PUR까지 승계
이행 확인, "입력:" 경로 4개 산출물 전건 적법 — 감사 완료(결함 없음).
