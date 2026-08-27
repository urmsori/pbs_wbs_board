# PA 표본감사 4 — AOCS-U1 설계체인 수치·입력경로 대조 (v3.2)

## 감사 대상
AOCS-U1 지향 제어계 설계체인: DSN(1차 사이징·오차예산) → RB(검토회 판정),
그리고 뒤를 이은 서비스 부서 산출물 CM 배포(aocs-u1-baseline.md)·PUR 발주
(aocs-u2-procurement.md).

## 수치 일관성 대조
| 항목 | DSN | RB(판정) | CM 배포 |
|---|---|---|---|
| 지향오차 RSS | 123.1arcsec(0.0342°) | "RSS123.1arcsec(0.0342°)" | 123.1arcsec(0.0342°) ≤0.05°(마진31.6%) |
| 제어대역폭 | 0.02Hz | (승계) | 0.02Hz(SA 1차모드 대비 6.0배 이격) |
| 정렬오차 배분 | 50.0arcsec(잠정, STR 회신대기) | "STR 정렬 정식 회신 도착 시 정렬항 재계산 조건부" | 승계 리스크로 명시(재계산 조건) |
| 별추적기/자이로/휠 배분 | 30/25arcsec, 휠4기 토크≥0.20N·m·모멘텀≥25N·m·s | (승계) | 배포 대상에 명시, PUR 발주치가 전항목 상회(마진 20~28%) |

전 단계 수치 일치, 정렬오차 잠정 조건이 DSN→RB→CM까지 누락 없이
승계됨을 확인.

## "입력:" 경로 적법성 대조
| 파일 | 입력 경로 | 대조 결과 |
|---|---|---|
| u1-dsn.md(AOCS) | sysreq.md, **SA/aocs-mode-interface.md**, **PROP/aocs-unloading-interface.md** | 두 경로 모두 `REQ-AOCS-SA-모드`·`REQ-AOCS-PROP-언로딩`(둘 다 parent: **M-AOCS**) 회신 — AOCS 자기 사슬 회신, **적법** |
| u1-rb.md(AOCS) | u1-rvw-a.md, u1-rvw-b.md | AOCS 자기 track — **적법** |
| aocs-u1-baseline.md(CM, 본 SVC 산출물) | u1-rb.md | source(AOCS-U1-RB)와 일치 — **적법** |
| aocs-u2-procurement.md(PUR, 본 SVC 산출물) | u1-dsn.md | source(AOCS-U1-DSN)와 일치 — **적법** |

### 특기사항 — 산출물 중복 생산자 확인
`PROP/aocs-unloading-interface.md`는 이후 `PROP-CORR-01`(parent: M-PROP,
EPS 확약 반영 정정)이 같은 경로를 갱신했다. 감사 시점에 이 파일이 두
Work(REQ-AOCS-PROP-언로딩과 PROP-CORR-01)의 산출물로 동시에 나타나는지
확인했다 — u1-dsn.md가 인용한 시점(추력 200mN·전력 3.0kW, PROP-CORR-01
정정 전 수치)과 PROP-CORR-01 정정치(70mN·2.0kW)가 다르다. 이는 입력경로
부적법이 아니라 **취합 규칙(3절) "나중 실측·확정이 앞 예측을 이긴다"**에
해당하는 시점차 문제로, AOCS-U1-DSN이 재검토 대상인지는 AOCS 자신의
후속 검증 사안이다(PA 감사 범위는 입력 경로 적법성으로 한정, 본문에
정직 기록만 남긴다).

## 감사 결과
**입력경로 결함 없음.** 다만 위 특기사항(PROP 정정으로 인한 DSN 인용치
시점차)을 발견해 정직 기록으로 남긴다 — 이는 감사1·2의 "타 사슬 무단
인용"과는 다른 종류(적법한 경로이나 갱신 이후 시점차)이므로 별도
수정요청은 발행하지 않고, AOCS 자신의 재검토 필요성 판단에 맡긴다.

검증: 지향오차 RSS·대역폭 수치 전건 일치, "입력:" 경로 4개 산출물 전건
적법 확인, PROP 정정 시점차 1건 정직 기록(수정요청 미발행, 결함 아님) —
감사 완료.
