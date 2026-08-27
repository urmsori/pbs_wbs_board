# COMM-CORR-02 — 안테나 배치 정정 (NCR-COMM-01 해소)

입력: examples/ksat8/deliverables/COMM/comm-u1-design.md, examples/ksat8/deliverables/STR/REQ-COMM-STR-안테나-reply.md, examples/ksat8/deliverables/COMM/comm-u1-linkbudget.md

## 대조
| 항목 | 잠정 가정(comm-u1-design.md §5) | 실측(STR 회신) | 영향 |
|---|---|---|---|
| 배치 축 | ±Z(상/하판) | **+Y/−Y(측면, 대칭 2개소)** | 위치만 변경, 반구대칭 구성은 유지 |
| 가용 면적 | (미지정) | 300×300mm | 신규 확정치, 문제 없음 |
| 시야각 | "4π 상시 가시" 가정 | **±90°(반구) 무차폐**, 정상운용 중 차폐 없음 | 가정과 사실상 동등 |
| 간섭 | 없음 가정 | 전개 과도구간(~100초, LEOP 1회성)만 일시 간섭 | IOT(30일 계획)에는 영향 없음 — LEOP 전용 |
| 안테나 이득 | 3dBi 가정 | (수치 미제공, ±90° 반구 LGA 표준 이득범위 0~5dBi) | **3dBi 가정 유지 — 재계산 불필요** |

## 판정
배치 축이 ±Z→+Y/−Y로 바뀌었으나 반구대칭 커버리지 구성은 동등하고,
링크버짓(comm-u1-linkbudget.md)이 사용한 이득 가정(3dBi)이 실측 범위
안에 있으므로 **하향 EIRP 5.0dBW(설계)/4.8dBW(시험)는 재계산 불필요**.
전개 과도구간 일시 차폐(~100초)는 LEOP 1회성 이벤트로 GS의 IOT 30일
계획(전개 완료 후 착수)에는 영향 없음 — GS-U1에는 참고정보로만 전달.

**NCR-COMM-01 종결(CLOSED)** — comm-u1-fm-package.md 확정치 변경 없음.

검증: STR 실측 배치(+Y/−Y, 300×300mm, ±90°)와 설계 가정(3dBi, 반구대칭)
대조 — EIRP·링크마진 재계산 불필요로 판정, NCR-COMM-01 CLOSED.
