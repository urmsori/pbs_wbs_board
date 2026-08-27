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

## 정정 확인 (PAY-CORR-02 재취합)
PAY track이 수정 요청(PAY-CORR-02)을 DONE 처리했다(산출물
examples/ksat8/deliverables/PAY/corr-02-record.md). 그 수정 기록과 현재
twta-heat-layout.md 실물을 대조해 재확인한다.

- **경로 수정**: twta-heat-layout.md "입력:" 줄에서 부적법 경로
  (examples/ksat8/deliverables/TCS/pay-thermal-capability.md)가 제거되고,
  남은 두 경로(examples/ksat8/deliverables/PAY/u1-dsn.md — 자기 track,
  examples/ksat8/board/REQ-TCS-PAY-발열.md — 보드 게시글)만 남았음을 파일
  실물에서 직접 확인 — **적법**.
- **서술 정합**: 판정 기준 서술이 "sysreq TCS 방열배분(6kW/24채널=250W/
  채널)"로 재작성되어, 제거된 경로(TCS 확약 6.3kW)에 대한 직접 인용 없이
  자기 사슬(sysreq, after=REQ) 안에서 판정이 성립하도록 고쳐졌음을 확인.
- **잔여 서술 관찰(경미, 재수정 불요)**: 문서 하단 "검증:" 줄이 여전히
  "262W(TCS확약)"라는 옛 수치 표현을 남기고 있다 — 본문 수치(210W,
  마진40W, 250W 배분 기준)와는 정합하고("입력:" 경로 적법성에는 영향
  없음, 검증 줄은 도구의 입력추적 대상이 아님), 다만 서술 잔재이므로
  정직하게 기록만 남긴다. 결함 재발이 아니라 표현 정리 수준이라 별도
  수정 요청은 발행하지 않는다.
- **판정 불변 확인**: 회신 결론(채널당 210W, 24채널 5,040W, 배치도)은
  수정 전후 동일.
- **도구 재검증**: `python3 tools/build_board_view.py examples/ksat8/board`
  재실행 결과 REQ-TCS-PAY-발열 관련 "보이지 않는 종속" 경고 **소멸** 확인.
- **재발방지 서술**: corr-02-record.md에 감사1과 동일한 재발방지 원칙
  (반대쪽 사슬 회신 미인용, sysreq/자기 track으로 대체)이 명시되어
  타당하다고 판단한다.

검증: PAY-CORR-02 반영 확인 — twta-heat-layout.md "입력:" 2경로 전건
적법, 판정 불변, build_board_view 경고 소멸, 잔여 서술 1건(검증줄 옛
수치) 정직기록(결함 아님) — 정정 종결.
