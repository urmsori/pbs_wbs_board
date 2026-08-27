# HAR 모듈 비행모델 인도 요약

입력: examples/ksat8/deliverables/HAR/u1-*.md, u2-*.md, pay-waveguide-budget.md,
examples/ksat8/deliverables/SE/sysreq.md

## sysreq.md HAR 항목 대비 판정
> HAR: 100V 절연·대전류, 도파관 손실 ≤0.8dB.

| 판정 항목 | 기준 | 실측/결과 | 판정 |
|---|---|---|---|
| 100V 절연저항 | (EPS 요구 ≥10MΩ@500VDC 인용) | 242~245MΩ (u1-inspection.md) | 충족 |
| 100V 대전류 전압강하 | ≤1%(내부 공학기준, sysreq는 % 미규정) | 주버스 0.24%, 분기 0.20~0.79% (u1-inspection.md) | 충족 |
| 도파관 손실 | ≤0.8dB | 0.58dB (u2-inspection.md) | 충족 |

## 유닛별 요약

### HAR-U1 100V 전력 하니스
설계 풀체인: DSN→ANL-T(줄열, 최고 도체온도 85°C≤절연정격200°C)/ANL-E
(절연내력·전압강하)→CHK(EPS 정식 회신 대조)→RVW-A(전기)/RVW-B(열·
절연)→RB(조건부 확정)→CM 배포. 제작: PUR→IQC→MFG→CLN. 검사:
INS(절연저항 242~245MΩ·전압강하 0.20~0.79%).
- ICD: REQ-HAR-EPS-배전 발행(설계 착수와 동시), 최초 8×20초 폴링
  타임아웃 → 잠정 가정(채널 30A, 이격 3mm/4mm)으로 설계·해석 진행.
  이후 EPS 정식 회신 접수(주버스 150A 일치, 분기 채널 8~20A로 잠정치
  보다 여유, 이격 요구 1.5mm/2.0mm) — CHK 단계에서 대조, 재설계 불요
  (잠정치가 더 보수적).
- REQ-HAR-OBC-핀맵: 착수와 동시 발행, RB 확정 후 정식 회신(OBC-CONN-
  J1/J2, 32+16채널, 실드접지 4핀) 접수 — 별도 정정 Work(HAR-U1-ICD-OBC-01)
  로 반영, 설계 변경 불요(리스크 해소).
- 커넥터 p/n: 잠정(PCU-PWR-J1) → PUR 발주 시 정식 MIL-DTL-38999
  시리즈 III로 대체(PUR-HAR-U1, IQC 확인 완료).
- PA 입회(PA-HAR-U1): 8×20초 폴링에도 회신 없어 입회 미확인 상태로
  INS 진행(**미해소 리스크** — 최종 폴링에서 재확인).

### HAR-U2 도파관·RF 하니스
설계 축약체인: DSN→CHK→RB(RVW 생략, 위험도 낮음 판단)→PUR→IQC→MFG→
INS(삽입손실 0.58dB≤0.8dB).
- ICD: REQ-HAR-PAY-RF·REQ-HAR-STR-경로 착수와 동시 발행, 최초 8×20초
  폴링 타임아웃 → 잠정 가정(편도2.0m, 90°×3, 플랜지4개소, WR-28
  상당)으로 설계·제작·검사 진행.
  - PAY 수신 요청(REQ-PAY-HAR-도파관, PAY→HAR)에 잠정 설계치로 회신
    (삽입손실 0.57dB, pay-waveguide-budget.md).
  - PAY 정식 회신(REQ-HAR-PAY-RF, WR-42/28포트, 손실배분 0.8dB 전량
    HAR 보유 인정) 지연 접수 — 경로·굴곡·손실 예산은 일치(재계산
    불요)하나 **플랜지 형식(WR-28 상당→WR-42) 불일치** 확인
    (HAR-U2-ICD-PAY-01, u2-pay-reconcile.md). 전기 성능(손실)은 이미
    실측 검증되어 유효하나, 물리적 체결 정합은 INT 단계 확인 필요.
  - REQ-HAR-STR-경로: **최종 폴링까지 회신 없음** — 잠정 경로(구조
    관통부 위치 미확정)로 제작·검사 완료. STR 정식 회신 접수 시 실제
    관통부 위치 대조 필요(**미해소 리스크**).

## 리스크·후속조치 (통합(INT) 단계 이관)
1. HAR-U2 도파관 플랜지 물리 정합: 제작에 사용한 WR-28 상당 플랜지와
   PAY 정식 규격 WR-42의 체결 정합을 INT 단계에서 확인, 불일치 시
   어댑터/재발주.
2. PA 입회 미확인(PA-HAR-U1): 정식 입회 회신 접수 시 입회 기록을
   u1-inspection.md에 소급 반영.
3. STR 라우팅 정식 회신 미접수(REQ-HAR-STR-경로): 구조 관통부 실제
   위치 확정 시 HAR-U1/U2 경로 물리 배치를 INT 단계에서 재확인.
4. HAR-U1 스위칭 과도전압 실측: u1-review-b.md 권고에 따라 통합시험
   단계에서 EMI 실측 권고.

## 산출물 목록
examples/ksat8/deliverables/HAR/{u1-design, u1-thermal-analysis,
u1-electrical-analysis, u1-drawing-check, u1-review-a, u1-review-b,
u1-review-board, u1-obc-reconcile, u1-iqc, u1-mfg, u1-cleaning,
u1-inspection, pay-waveguide-budget, u2-design, u2-drawing-check,
u2-review-board, u2-pay-reconcile, u2-iqc, u2-mfg, u2-inspection}.md
