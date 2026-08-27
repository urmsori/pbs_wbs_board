# HAR-U1 100V 전력 하니스 도면 검도

입력: examples/ksat8/deliverables/HAR/u1-design.md,
examples/ksat8/deliverables/HAR/u1-thermal-analysis.md,
examples/ksat8/deliverables/HAR/u1-electrical-analysis.md,
examples/ksat8/deliverables/EPS/distribution-connector-spec.md

HAR-U1-DSN-01 설계, ANL-T-01(줄열)·ANL-E-01(절연·전압강하) 해석 결과를
도면(케이블사양·커넥터핀맵·전압강하계산·열해석)으로 정합 검도한다.
REQ-HAR-EPS-배전 정식 회신(EPS/distribution-connector-spec.md)이 CHK
착수 시점에 접수되어 잠정 가정과 대조한다.

## EPS 정식 회신 대조
| 항목 | 잠정 가정(DSN) | EPS 정식 회신 | 판정 |
|---|---|---|---|
| 주버스 피더 전류 | 150A | 150A(15kW/100V, 마진 미포함) | **일치** — ANL 재계산 불요 |
| 대표 분기채널 전류 | 30A(보수적 최악가정) | PAY 8A/EP 20A/COMM 3A/히터 3A(모두 30A 이하) | 잠정치가 더 보수적 — **여유 초과 확인, 재설계 불요** |
| 도체-도체 이격 | 3mm(잠정) | ≥1.5mm 요구 | 잠정 설계값이 요구 상회 — **충족** |
| 도체-대지 이격 | 4mm(잠정) | ≥2.0mm 요구, 절연저항≥10MΩ@500VDC | 잠정 설계값이 요구 상회 — **충족**(절연저항은 INS 단계 실측 확인) |
| 커넥터 형식 | 잠정 PCU-PWR-J1 | MIL-DTL-38999 III, 채널당 독립 커넥터 | 형식 상이 — PUR 단계에서 실제 파트번호로 대체 필요(리스크) |

## 검도 대상 확인
- 케이블 사양표: AWG2(주버스)·AWG10(분기) 확인
- 커넥터 핀맵: EPS 실제 커넥터(MIL-DTL-38999 III) 반영 필요 — PUR 발주
  시 잠정 p/n 대신 정식 p/n 사용
- 전압강하 계산서: 주버스 0.23%, 분기 0.77%(잠정 30A 기준, 실제 8~20A
  대비 더욱 여유) — 정합
- 절연 이격거리: EPS 요구 상회 — 정합

## 판정
전기적 설계치는 EPS 정식 회신과 정합(대부분 더 보수적). 커넥터
형식만 잠정에서 실제(MIL-DTL-38999 III)로 갱신 필요 — 도면 자체
재설계는 불요, PUR 발주 시 반영. OBC 모니터링 인터페이스·STR 라우팅은
여전히 잠정(회신 미도착) — CM 배포 시 조건부 리스크로 승계.

검증: EPS 정식 회신 대조 완료(주버스 150A 일치, 분기 채널 잠정치가
실제보다 보수적), 커넥터 p/n만 PUR 단계 갱신 필요, 재설계 불요
