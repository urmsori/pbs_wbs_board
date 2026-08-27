# PAY-CORR-01 수정 기록 — waveguide-route-spec.md 입력 경로 정정

입력: examples/ksat8/deliverables/PA/audit-1-req-har-pay-rf.md, examples/ksat8/board/PAY-CORR-01.md

## 결함
AUDIT-1이 지적한 대로, REQ-HAR-PAY-RF 회신(examples/ksat8/deliverables/PAY/
waveguide-route-spec.md, parent: M-HAR)의 "입력:"이 별도 사슬(REQ-PAY-HAR-도파관,
parent: M-PAY)의 회신 examples/ksat8/deliverables/HAR/pay-waveguide-budget.md를
정식 요청 없이 인용해 "보이지 않는 종속"이었다.

## 조치 — 이미 수정됨(선행 조치)
본 감사 요청이 올라오기 전, PAY-DSN-01(PAY-IF-01 재분배 전 원 작업자)이 동일
결함을 자체 점검 과정에서 발견해 이미 수정을 완료했다. waveguide-route-spec.md의
"입력:" 줄에서 examples/ksat8/deliverables/HAR/pay-waveguide-budget.md 경로를
제거하고, 본문의 손실배분 서술도 "PAY-U1-DSN 링크예산의 설계치(sysreq 상한
0.8dB)"로 재작성해 타 사슬 수치에 대한 의존 서술을 없앴다(HAR 실측이 이보다
낮다면 그 차이는 HAR 측 여유로 남긴다는 서술로 대체).

현재 waveguide-route-spec.md 입력 줄(수정 후, 확인):
```
입력: examples/ksat8/deliverables/PAY/u1-dsn.md,
examples/ksat8/board/REQ-HAR-PAY-RF.md
```
두 경로 모두 적법(자기 트랙 산출물 · 보드 게시글).

## 커밋 근거
git을 쓰지 않는 저장소 운용 방식이라 커밋 해시는 없다 — 수정은 파일 자체의
현재 상태로 확인된다(위 발췌). 재발 방지: 향후 반대쪽 사슬(타 track parent)의
요청에 답할 때는 자기 track 산출물과 그 요청 게시글만 인용하고, 자신이 별도로
발행한 상대 요청의 회신은 인용하지 않는다.

검증: waveguide-route-spec.md "입력:" 경로 2건 전부 적법(자기 트랙·보드 게시글) 재확인
