# PA 표본감사 1 — REQ-HAR-PAY-RF 회신 "입력:" 경로 적법성 대조 (v3.2)

감사는 표본 감사이므로 불시 열람이 본질이다(4절 예외).

## 감사 대상
examples/ksat8/deliverables/PAY/waveguide-route-spec.md — HAR팀이 자기 사슬
(parent=M-HAR)에서 발행한 요청 `REQ-HAR-PAY-RF`(HAR→PAY, 도파관 플랜지·포트
규격 요청)의 회신. 작성자: PAY-DSN-01.

## "입력:" 경로 대조
산출물 머리의 "입력:" 3개 경로를 `REQ-HAR-PAY-RF`의 취합 사슬
(REQ-HAR-PAY-RF → M-HAR → R00) 기준으로 하나씩 대조했다.

| 경로 | 만든 Work | 그 Work의 parent | 적법성 판정 |
|---|---|---|---|
| examples/ksat8/deliverables/PAY/u1-dsn.md | (PAY 자체 산출물, PAY-U1-DSN 등) | M-PAY | 응답자(PAY) 자기 팀 산출물 — **적법**(자기 track) |
| examples/ksat8/board/REQ-HAR-PAY-RF.md | REQ-HAR-PAY-RF 자신 | — | 보드 게시글(공용 기록) — **적법**(예외) |
| examples/ksat8/deliverables/HAR/pay-waveguide-budget.md | `REQ-PAY-HAR-도파관`(PAY→HAR, parent: **M-PAY**, track: HAR) | M-PAY | **부적법** — 아래 상세 |

### 부적법 판정 상세
`pay-waveguide-budget.md`는 REQ-HAR-PAY-RF(parent=M-HAR)의 취합 사슬 위에
있지 않다. 이 파일을 만든 Work `REQ-PAY-HAR-도파관`은 parent가 **M-PAY**로,
PAY팀이 별도로 HAR에 낸 요청(PAY→HAR, "TWTA-안테나 간 도파관 손실 예산 요청")의
회신이다 — 즉 **M-PAY 취합 사슬에 속한 산출물**이지 REQ-HAR-PAY-RF(M-HAR
사슬)의 것이 아니다. 적법 경로 5가지(자기 팀·after·자기 사슬 회신·source·
보드) 중 어느 것에도 해당하지 않는다:
- 자기 팀(track) 산출물 아님(만든 이는 track: HAR)
- after로 받은 것 아님(REQ-HAR-PAY-RF의 after: -)
- REQ-HAR-PAY-RF의 취합 사슬(parent가 M-HAR)에서 발행한 요청의 회신 아님
  — `REQ-PAY-HAR-도파관`의 parent는 M-PAY
- REQ-HAR-PAY-RF를 낳은(source) Work의 산출물 아님(source: HAR-U2-DSN-01)

PAY-DSN-01이 같은 사람(역할)으로 두 요청(HAR→PAY와 PAY→HAR)을 동시에
처리하면서, 자신이 이미 알고 있던 반대쪽 회신 수치(도파관 삽입손실
0.57dB·굴곡 90°×3·경로장 2.0m)를 정식 요청 절차 없이 그대로 가져다 썼다.
결과 수치 자체(WR-42, 28포트, 손실배분 0.8dB)는 HAR 실측(0.57dB)과
모순되지 않으나, 이 경로는 도구가 재검증을 촉발하지 못하는 **보이지
않는 종속**이다 — HAR/pay-waveguide-budget.md가 나중에 갱신되어도
waveguide-route-spec.md는 자동으로 재검토 대상이 되지 않는다.
(`tools/build_board_view.py` 실행 결과에서도 동일 경고 확인:
"REQ-HAR-PAY-RF가 요청 없이 남의 산출물을 읽었다: …pay-waveguide-budget.md")

## 감사 결과
**결함 발견.** 산출물 위조는 아니다(수치는 정확하고 상호 모순 없음) — 다만
정식 요청 경로를 거치지 않고 인접 사슬의 정보를 재사용한 기록 절차 위반이다.
원인은 PAY(대상 track) 자신의 산출물 작성 방식이므로, PAY track으로 수정
요청(source=본 감사 AUDIT-1)을 발행한다: REQ-HAR-PAY-RF의 회신에서 해당
경로를 제거하거나, PAY가 HAR에 정식 요청(REQ-PAY-HAR-경로재확인 등)을 올려
회신을 받은 뒤 그 회신을 "입력:"에 적어야 한다.

검증: "입력:" 3경로 중 2건 적법(자기팀·보드게시글), 1건 부적법(타 사슬
산출물 무단 인용) 확인 — 결함 1건 발견, PAY track 수정 요청 발행.
