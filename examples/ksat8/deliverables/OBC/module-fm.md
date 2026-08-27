입력: examples/ksat8/deliverables/OBC/obc-design.md, examples/ksat8/deliverables/OBC/obc-anl-elec.md, examples/ksat8/deliverables/OBC/obc-anl-therm.md, examples/ksat8/deliverables/OBC/drawing-check.md, examples/ksat8/deliverables/OBC/review-01.md, examples/ksat8/deliverables/OBC/review-02.md, examples/ksat8/deliverables/OBC/rb-disposition.md, examples/ksat8/deliverables/OBC/iqc-report.md, examples/ksat8/deliverables/OBC/obc-mfg.md, examples/ksat8/deliverables/OBC/obc-asy.md, examples/ksat8/deliverables/OBC/obc-ins.md, examples/ksat8/deliverables/OBC/obc-tst.md, examples/ksat8/deliverables/COMM/obc-if-reply.md, examples/ksat8/deliverables/PAY/obc-tm-reply.md, examples/ksat8/deliverables/CM/obc-baseline.md, examples/ksat8/deliverables/PUR/obc-parts.md

# OBC 비행모델 인도 (module-fm)

## 요약
이중화 위성관리컴퓨터(OBC) 비행모델 2식(주/예비)을 설계→해석→검도→
검토회→제작→조립→검사→시험의 전체 체인으로 완성했다.

## sysreq 대조
- TM 8,000점 처리: 시험(obc-tst.md)에서 8,000점 상당 프레임 드롭 0건
  확인 — 실사용 배정은 드로잉체크(drawing-check.md) 확정치 기준 4,800점
  (PAY 400점 정정 반영, 마진 3,200점 별도) — **용량 요구 충족**.
- TC 2,000점 처리: 처리 정상, 오류 프레임 100% 거부 확인 — 충족.
- 이중화: FMEA 단일고장점 없음(obc-anl-elec.md), 실측 절체 420ms
  (≤500ms) — 충족.

## 외부 인터페이스 회신 반영
- REQ-OBC-COMM-IF: COMM-U1 설계 미확정으로 **잠정** 회신
  (COMM/obc-if-reply.md, sysreq 요약 근거) 사용 — RVW2(review-02.md)가
  조건부 통과로 지정한 재검토 항목. **미결(추후 정정 예정)**.
- REQ-OBC-PAY-TM: PAY로부터 실측 회신(PAY/obc-tm-reply.md, 채널당15점
  ×24+공통40=400점) 수신 — drawing-check.md에서 원 설계(obc-design.md)의
  잠정치(2,600점)를 **정정**했다.

## 서비스 요청 처리 결과 (재취합 — v2.9 취합 순서 정정)
REQ-OBC-CM-REL(형상관리 배포, → CM/obc-baseline.md, 베이스라인
OBC-U1-BL-001)·REQ-OBC-PUR(부품 구매, → PUR/obc-parts.md, PO 4건 발주)
모두 최초 module-fm 취합(2026-08-27 04:06:19) **이후**에 서비스 부서가
회신을 완료했다(각각 04:05:38, 04:06:39). 규칙 4절(취합 순서)에 따라
M-OBC를 재취합해 finished를 갱신한다 — 부모(M-OBC)의 finished가 항상
모든 자식보다 늦어야 하므로.

## PBS 구성
설계 7건(DSN·ANLE·ANLT·CHK·RVW1·RVW2·RB) + 제작 4건(IQC·MFG·ASY·INS) +
시험 1건(TST) = OBC-U1 12건 산출물, 인터페이스 회신 반영.

검증: TM/TC 처리 용량·이중화 절체 시간 시험으로 sysreq 수치 충족 확인.
COMM 인터페이스는 잠정 — COMM-U1 확정 시 정정 게시글 예정.
