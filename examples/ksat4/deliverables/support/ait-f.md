# AIT FM 통합시험 기록
입력: examples/ksat4/deliverables/sysreq.md, examples/ksat4/deliverables/e-decision.md,
examples/ksat4/deliverables/support/ait-e.md,
examples/ksat4/deliverables/{STR,TCS,EPS,AOCS,OBC,COMM,PROP,PAY}/{summary-fm.md,test-fm.md,dsn-*-f.md}

## F-AIT-1 (전기 통합, AIT-13) — EM 이관 리스크 종결 여부 검사

e-decision.md의 FM 이관 리스크 2건을 실제로 재검했다.
1. TCS·EPS·AOCS·OBC·COMM·PROP·PAY 7팀: anl-em 구조/열 마진 **수치** 없음 → FM
   설계갱신(F-\*-D\*)에서 수치 필수 기재.
2. TCS·AOCS·OBC·PROP 4팀: 설계 질량 실측치 미기재 → FM에서 질량표 필수.

### 검사 방법
8개 서브시스템 dsn-a1-f.md·dsn-a2-f.md를 전부 열어 (a) 질량(kg) 수치
기재 여부, (b) 구조/열 마진 수치 기재 여부, (c) 기재된 질량 합계를
sysreq.md 배분표(STR 45/TCS 10/EPS 30/AOCS 18/OBC 7/COMM 10/PROP 25/
PAY 28/HAR 4, 여유 3, 합 180 kg)와 대조했다. summary-fm.md의 판정이
위 dsn 수치·board 상태와 정합하는지도 함께 대조했다.

### 검사 결과
| SUB | 질량(dsn-*-f.md) | 구조/열 마진(dsn-*-f.md) | 비고 |
|---|---|---|---|
| STR | 2.5+2.5=5.0 kg (수치 있음) | 1.5 / 25°C (수치 있음) | summary-fm.md는 "전체 구조 질량 12.8 kg"이라 적으나 dsn 합계(5.0kg)·parts-f/build-*-f 어디에도 12.8의 근거가 없다(패널 외 프레임·브래킷 미itemize라는 EM 잔여 리스크와 동일 원인으로 추정). 배분(45kg) 이내이므로 예산 위반은 아니나 수치 자체는 미검증 — NCR 4건 한도로 이번에는 게시하지 않고 잔여 리스크로 기록. |
| TCS | **없음**(파일이 사실상 빈 파일) | **없음** | EM 리스크 1·2 모두 미해소. F-NCR-01 게시 |
| EPS | 0.52+0.48=1.00 kg (수치 있음) | 1.85/1.42, 1.92/1.38 (수치 있음) | EM 리스크 해소됨(EM에서도 이미 해소 대상이었음) |
| AOCS | **없음**("설계 완료" 텍스트뿐) | **없음** | EM 리스크 1·2 모두 미해소 + summary-fm.md 판정문 자체 모순("EM 단계 진입 가능"). F-NCR-02 게시 |
| OBC | **없음**("예정" TBD) | **없음**("예정" TBD) | EM 리스크 1·2 모두 미해소 + summary-fm.md가 TBD 항목을 "✓완료"로 판정(모순), 최종 판정 문장 자체가 없음. F-NCR-03 게시 |
| COMM | 0.48+0.52=1.00 kg (수치 있음) | 35%/25% (수치 있음) | EM 리스크 해소됨 |
| PROP | 2.5+2.5=5.0 kg (수치 있음) | 15%/10% (수치 있음) | EM 리스크 해소됨(EM에서 질량 미기재였던 4팀 중 유일하게 완전 해소) |
| PAY | **없음**(EM엔 있었으나 FM에서 삭제됨 — 퇴행) | **없음**(EM부터 없었음) | EM 리스크 2(질량)는 EM 때는 없던 문제였는데 FM에서 새로 발생(퇴행), 리스크 1(마진)은 여전히 미해소. summary-fm.md의 "26.8/28kg"은 PAY 어느 산출물에도 근거가 없음(배분 대비 여유가 8팀 중 가장 적은 수치라 위험도가 높음). F-NCR-04 게시 |

- **질량 합계 vs sysreq 배분(c)**: TCS·AOCS·OBC 3팀이 질량 수치 자체가
  없어 시스템 총질량(≤180 kg) 전수 검증은 여전히 불가능하다(EM과
  동일한 결론). PAY는 summary-fm.md 값(26.8kg)을 신뢰하면 배분(28kg)
  이내지만 근거가 없어 신뢰할 수 없다. 검증 가능한 4팀(STR 5.0~12.8/
  EPS 1.00/COMM 1.00/PROP 5.0)은 모두 배분 이내다.
- **EM 이관 리스크 종결 여부**: **미종결**. 리스크 1(마진 수치)은
  7팀 중 EPS·COMM·PROP 3팀만 해소, TCS·AOCS·OBC·PAY 4팀 미해소.
  리스크 2(질량 수치)는 4팀(TCS·AOCS·OBC·PROP) 중 PROP만 해소,
  TCS·AOCS·OBC 3팀 미해소 + PAY 1팀 신규 퇴행.

### 발견 NCR (4건, 최대 4건 한도)
| NCR | 대상 | 요지 |
|---|---|---|
| F-NCR-01 | TCS | dsn-a1/a2-f.md 질량·마진 수치 전무(EM 리스크 미해소), summary-fm.md가 근거 없이 PASS 판정 |
| F-NCR-02 | AOCS | dsn-a1/a2-f.md 질량·마진 수치 전무(EM 리스크 미해소), summary-fm.md 판정문 자체 모순("EM 단계 진입 가능") |
| F-NCR-03 | OBC | dsn-a1/a2-f.md가 "예정"(TBD)뿐인데 summary-fm.md는 "✓완료"로 판정(모순), 최종 판정 문장 부재 |
| F-NCR-04 | PAY | dsn-a1/a2-f.md 질량 수치가 EM 대비 퇴행(삭제)되었고 마진은 여전히 없음, summary-fm.md의 26.8/28kg이 근거 없음 |

검증: 8개 dsn-a1/a2-f.md 실측(질량·마진 수치 유무), sysreq.md 배분표
대조(검증 가능 4팀은 배분 이내), summary-fm.md 판정을 각 dsn 수치·
board 상태와 1건씩 대조해 TCS/AOCS/OBC/PAY 4건에서 EM 이관 리스크
미해소 또는 판정 모순 확인 → F-NCR-01~04 게시(4건, 한도 소진). STR의
12.8kg 근거 불명은 NCR 한도 초과로 이번 라운드에서는 게시하지 않고
위 표에 잔여 리스크로 기록.

## F-AIT-2 (기능 통합, AIT-14) — test-fm.md·summary-fm.md 정합 검사

### 검사 방법
8개 서브시스템의 test-fm.md(수락시험 절차·수행·보고)와 summary-fm.md의
시험 관련 판정 문구를 상호 대조하고, 대응하는 board 게시글
(F-\*-T1·F-\*-T2)의 실제 status가 두 문서의 서술과 일치하는지 확인했다
(post.py done이 존재하지 않는 산출물 경로를 거부하므로 파일 실재는
도구가 보증 — 내용의 정합만 사람이 확인).

### 검사 결과
- **board 상태 대조**: 8개 서브시스템의 F-\*-T1·F-\*-T2 16개 게시글
  전부 status: DONE이고, 이는 각 test-fm.md("수락시험 완료"·"수락 보고
  완료")·summary-fm.md(시험 항목 완료/PASS/합격)의 서술과 일치한다.
  불일치 없음.
- **판정 근거**: STR·TCS·EPS·COMM·PROP 5개 서브시스템은 summary-fm.md의
  시험 관련 판정이 test-fm.md 내용·board 상태와 정합하고 근거도
  구체적이다(예: PROP "수락시험 실시 및 보고 완료 — 모든 성능 요구사항
  만족", COMM "수락시험 합격").
- AOCS("EM 단계 진입 가능" 판정문 모순)와 OBC(설계갱신 항목이
  TBD("예정")인데 "✓완료"로 판정, 최종 판정 문장 부재)의 summary-fm.md
  판정 근거 문제는 F-AIT-1 검사에서 이미 발견되어 F-NCR-02·F-NCR-03으로
  게시했다(대상 파일이 동일한 summary-fm.md이므로 중복 게시하지
  않는다). 두 서브시스템의 test-fm.md 자체(T1·T2 완료 서술)와 board
  상태는 서로 일치해 기능시험 결과 자체에는 새로운 불일치가 없다.
- PAY의 summary-fm.md "26.8/28kg" 근거 불명 문제(F-NCR-04)도 질량
  수치 문제이지 기능시험(test-fm.md) 서술과는 무관 — test-fm.md·
  board 상태는 일치한다.

### 판단
test-fm.md·summary-fm.md·board 상태 3자 대조에서 **기능시험 정합
자체는 8개 서브시스템 전부 이상 없음**을 확인했다. AOCS·OBC·PAY의
summary-fm.md 판정 근거 문제는 F-AIT-1에서 이미 NCR로 포착된 사안과
동일 파일·동일 결함이므로 F-AIT-2 범위에서 새 NCR을 만들지 않는다.
새로 발견된 NCR이 없으므로 F-AIT-2는 여기서 종결한다.

검증: 8개 서브시스템 test-fm.md·summary-fm.md·board(F-\*-T1/T2 16건)
3자 대조 — 시험 완료 서술과 board 상태 불일치 없음 확인, 판정 근거
문제(AOCS·OBC·PAY)는 F-NCR-02~04와 동일 사안이라 중복 게시 없이
교차 참조. 신규 NCR 없음 → done.
