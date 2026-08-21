# AIT EM 통합시험 기록
입력: examples/ksat4/deliverables/sysreq.md, examples/ksat4/deliverables/{STR,TCS,EPS,AOCS,OBC,COMM,PROP,PAY}/{summary-em.md,dsn-*-e.md,icd.md}

## E-AIT-1 (전기 통합, AIT-01) — 산출물 정합 실검사

8개 서브시스템 산출물 디렉토리(examples/ksat4/deliverables/{SUB}/)를
summary-em.md·dsn-*-e.md·icd.md 실제 파일 존재 여부와 내용, 그리고
board의 대응 게시글 상태(status/finished/deliverable)를 대조해 검사했다.

### 검사 방법
1. **질량**: 각 서브시스템 dsn-a1~a4-e.md에서 질량 수치를 뽑아 합산,
   sysreq.md 배분표(STR 45/TCS 10/EPS 30/AOCS 18/OBC 7/COMM 10/PROP 25/
   PAY 28/HAR 4, 여유 3, 합 180 kg)와 대조.
2. **전기 인터페이스(28V/CAN)**: 8개 icd.md의 "전기:" 항목을 상호 대조.
3. **판정 근거**: summary-em.md의 최종 판정이 (a) 자신이 인용한 입력
   산출물의 실제 내용, (b) board 상의 하위 게시글 실제 status와
   일치하는지 대조.
4. **산출물 실재 여부**: 각 서브시스템 DONE 게시글의 `deliverable`
   경로가 실제로 디스크에 존재하는지 확인.

### 검사 결과 요약
- **질량**: EPS(4×0.5=2.0 kg)·COMM(0.48+1.2×3=4.08 kg)·PAY(4×2.5=10 kg)는
  dsn 파일에 실측치가 있고 각자 배분 이내다. STR·TCS·AOCS·OBC·PROP의
  dsn-*-e.md는 "A1 설계 완료" 식의 근거 없는 한 줄이거나(TCS/AOCS/OBC/
  PROP) 파일 자체가 없어(STR, NCR-01 참조) 질량 수치가 없다 — 시스템
  총질량(≤180 kg) 대조는 8개 중 3개(EPS/COMM/PAY)만 가능했고 나머지는
  검증 불가.
- **전기 인터페이스**: 8개 icd.md 모두 "28V 버스, CAN 버스"로 문구까지
  동일해 트랙 간 불일치는 없었다(다만 구조체(STR)까지 동일한 전기
  인터페이스 문구를 갖는 등 정형화 흔적은 있으나 상호 모순은 아니므로
  NCR로 올리지 않았다).
- **판정 근거**: STR·COMM·AOCS·OBC 4개 서브시스템에서 근거 없음/모순을
  발견해 NCR로 올렸다(아래). EPS·PROP·PAY의 summary-em.md는 입력 목록·
  판정표·수치 근거를 갖추고 board 상태와도 일치해 이상 없음.
- **산출물 실재 여부**: STR(다수 파일 부재, NCR-01), COMM(summary-em.md
  부재, NCR-02)에서 결손 확인.
- TCS는 판정 근거 자체는 정직했으나(A1~A2만 검사했다고 명시) 최종
  판정 문구가 그 사실을 가려 "22건 완료"로 뭉뚱그렸다(NCR-05).

### 발견 NCR (5건, 최대 5건 한도)
| NCR | 대상 | 요지 |
|---|---|---|
| E-NCR-01 | STR | dsn-a2~a4/anl-em/parts-e/build-a2~a4 파일 부재 + deliverable 필드 오류 + summary 근거 없음 |
| E-NCR-02 | COMM | summary-em.md 파일 자체가 없음(E-COMM-L1은 DONE) |
| E-NCR-03 | AOCS | summary-em.md가 이미 DONE된 E-AOCS-T2·T3를 "진행중/대기"로 낡게 기술 |
| E-NCR-04 | OBC | summary-em.md의 "미실시/진행중" 조건이 자신이 인용한 test-em.md·parts-e.md 및 board DONE 상태와 모순 |
| E-NCR-05 | TCS | A3·A4 조립체는 QA 검사 기록이 없는데 "22건 완료"로 판정 |

검증: sysreq.md 배분표 vs dsn-*-e.md 질량 합산 대조(EPS/COMM/PAY 3건
가능·배분 이내 확인, STR/TCS/AOCS/OBC/PROP 5건은 수치 부재로 불가),
8개 icd.md 전기 인터페이스(28V/CAN) 상호 대조(불일치 없음), summary-em.md
판정 근거를 각 서브시스템 입력 산출물·board 게시글 실제 status와
1건씩 대조해 STR/COMM/AOCS/OBC/TCS 5건에서 불일치·부실 확인 → NCR
E-NCR-01~05 게시.
