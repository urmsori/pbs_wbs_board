# PA 표본감사 2 — REQ-TCS-PAY-발열 회신 "입력:" 경로 적법성 대조 (v3.2)

## 감사 대상
examples/ksat8/deliverables/PAY/twta-heat-layout.md — TCS팀이 자기 사슬
(parent=M-TCS)에서 발행한 요청 `REQ-TCS-PAY-발열`(TCS→PAY, TWTA 채널별
발열·배치 요청)의 회신. 작성자: PAY-DSN-01(감사1과 동일 역할).

## "입력:" 경로 대조
| 경로 | 만든 Work | 그 Work의 parent | 적법성 판정 |
|---|---|---|---|
| examples/ksat8/deliverables/PAY/u1-dsn.md | PAY 자체 산출물 | M-PAY | 응답자(PAY) 자기 팀 산출물 — **적법**(자기 track) |
| examples/ksat8/board/REQ-TCS-PAY-발열.md | REQ-TCS-PAY-발열 자신 | — | 보드 게시글(공용 기록) — **적법**(예외) |
| examples/ksat8/deliverables/TCS/pay-thermal-capability.md | `REQ-PAY-TCS-방열`(PAY→TCS, parent: **M-PAY**, track: TCS) | M-PAY | **부적법** — 감사1과 동일 유형 |

### 부적법 판정 상세
`pay-thermal-capability.md`는 REQ-TCS-PAY-발열(parent=**M-TCS**)의 취합
사슬 위에 있지 않다. 이 파일을 만든 Work `REQ-PAY-TCS-방열`은 parent가
**M-PAY**로, PAY가 별도로 TCS에 낸 요청("TWTA 패널 방열 능력 확약
요청")의 회신이다. 적법 경로 5가지 중 어느 것도 성립하지 않는다(자기
track 아님·after 아님·자기 사슬(M-TCS) 회신 아님·source인 TCS-DSN-01의
산출물도 아님). 감사1(REQ-HAR-PAY-RF)과 **완전히 같은 패턴** —
PAY-DSN-01이 두 방향의 요청(TCS→PAY, PAY→TCS)을 동시에 처리하며 반대쪽
회신 수치(방열 용량 6.3kW 확약)를 정식 절차 없이 재사용했다.
(`tools/build_board_view.py` 경고: "REQ-TCS-PAY-발열가 요청 없이 남의
산출물을 읽었다: …pay-thermal-capability.md")

수치 자체는 정확하고 모순 없음: 채널당 210W≤262W(TCS확약), 24채널
5.04kW≤6.3kW(마진 1.26kW) — PAY 자체 계산(u1-dsn.md)과도 일치.

## 감사 결과
**결함 발견(감사1과 동일 유형, 동일 원인자).** PAY track으로 수정 요청
(source=본 감사 AUDIT-2)을 발행한다: 이 사슬 위반이 PAY-DSN-01의 반복
패턴(감사1·2 모두 해당)이므로, 개별 파일 수정에 더해 향후 양방향 ICD
요청을 처리할 때 반대쪽 사슬의 회신을 재사용하지 말고 정식 요청으로
받으라는 지적을 함께 남긴다.

검증: "입력:" 3경로 중 2건 적법, 1건 부적법(타 사슬 산출물 무단 인용,
감사1과 동일 패턴) 확인 — 결함 1건 발견, PAY track 수정 요청 발행.
