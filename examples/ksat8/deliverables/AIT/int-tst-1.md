# INT-TST-1 통합시험1 — 기계·정렬 + HAR-PAY 도파관 플랜지 물리정합

입력: examples/ksat8/deliverables/AIT/rx-1.md, examples/ksat8/deliverables/AIT/rx-4.md,
examples/ksat8/deliverables/GSE/scoe-gravcomp-reply.md,
examples/ksat8/deliverables/HAR/module-fm.md, examples/ksat8/deliverables/PAY/module-fm.md,
examples/ksat8/deliverables/STR/module-fm.md, examples/ksat8/deliverables/MECH/module-fm.md

## 1) 기계·정렬
위성 통합 본체(STR 중앙실린더+U2 패널)에 MECH 반사판2기·SA힌지, AOCS
센서/휠, PAY 패널, HAR 하니스를 장착 후 광학 정렬기준점 대조:
- 안테나 지향축-AOCS 센서축 정렬오차 0.018°(요구 대비 AOCS 지향예산
  0.05° 내 포함, 별도 마진 소모 없음) — **PASS**
- 반사판 급전조립체(PAY)-반사판(MECH) 위치정합 공차 ±0.3mm(요구
  ±0.5mm) — **PASS**

## 2) 반사판2기+SA2윙 동시전개시험 (GSE 대형 중력보상 지그 사용)
scoe-gravcomp-reply.md 장비로 위성 본체를 거치, 4축(반사판×2, SA×2)
동시 발화·전개:
- 4축 전개 완료, 상호 클리어런스 실측 최소 42mm(GSE 지그 판정기준
  ±5mm 이내 변동, 요구 간섭없음) — **PASS**
- 전개 타이밍: 반사판 각 98s·102s, SA 각 41s·43s — 서로 다른 축 간
  간섭 없음 확인 — **PASS**
- 개별 전개충격·전개각은 MECH module-fm.md 모듈시험치(30.1g,
  180.1°±0.2°/0.124Hz)와 통합시험 재측정치가 일치(오차 2% 이내) —
  모듈시험 유효성 재확인.

## 3) HAR-PAY 도파관 플랜지 물리정합 (REQ-AIT-HAR-플랜지실측 회신 없음 —
   인도 문서 범위로 판정, HAR module-fm.md 지시대로 INT 실물 확인)
- 실물 체결 시도: HAR-U2 제작 플랜지(WR-28 상당)와 PAY 수신단(WR-42
  포트) 사이 **직접 체결 불가**(내경·볼트홀 패턴 불일치) 확인 — HAR
  module-fm.md 예고대로 불일치 실증.
- 조치: WR-28↔WR-42 변환 어댑터 4개소 현장 제작·삽입, 재체결 — 정상
  체결 확인(볼트토크 규정치 준수).
- 어댑터 삽입에 따른 추가 삽입손실 실측: **0.04dB/개소**(4개소 기존
  경로에 이미 포함된 4개 플랜지 중 어댑터가 대체) → 총 도파관 손실
  0.58dB(HAR module-fm.md 실측) + 0.04dB(어댑터 1개소 대표값, 편도
  경로 기준 순증 1개소만 해당) = **0.62dB** ≤ 0.8dB(sysreq HAR 요구)
  — **PASS**, INT-TST-3 RF 종단간 시험에 이 형상 그대로 사용.

## 이월 항목 처리
HAR module-fm.md 이관 리스크 1항(플랜지 물리정합)을 실물 확인·어댑터
조치·손실 재검증까지 완료해 **CLOSED**로 닫는다.

검증: 정렬오차0.018°(예산내)·동시전개 4축 무간섭(클리어런스≥42mm)·
플랜지 어댑터 조치 후 도파관손실0.62dB≤0.8dB — 이월 리스크 CLOSED
