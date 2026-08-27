# AIT 수령검사 — AOCS·PAY (rx-4)

입력: examples/ksat7/deliverables/AOCS/module-fm.md, examples/ksat7/deliverables/PAY/module-fm.md,
examples/ksat7/deliverables/PAY/u2-pulse-test.md

## AOCS 수령
- 지향정확도(3σ) 0.0183°≤0.02°(마진8.5%), 요스티어링±4.0°, 안정도0.00251°/s≤0.003°/s
  (마진16.3%) — sysreq AOCS 3항목 전부 실측(HIL) 충족.
- STR ICD(정렬기준면 수직도·열드리프트7.3arcsec≤배분12.6arcsec, 안테나1차모드37.2Hz≫4.0Hz)
  확인 — 단, 이 37.2Hz는 STR rev.1 잠정해석치(안테나38kg 가정)였고, STR rev.2 최종 실측은
  36.1Hz(72kg 반영). 4.0Hz 요구 대비 여전히 압도적 마진(36.1Hz≫4.0Hz)이므로 AOCS 판정에는
  영향 없음 — 재확인만 기록.

## PAY 수령
- SAR 첨두펄스부하 1.79kW/90.4s(공차내), NESZ -19.6dB≤-19dB — sysreq PAY 2항목 PASS.
- **질량 38↔72kg 불일치 원인 확인**: REQ-STR-PAY 회신치가 안테나 실측질량 72.0kg, 3점 킨매틱
  PCD400mm 8-M8임을 원문에서 직접 확인. STR 초기 설계가정(38kg)과의 괴리 82.9%가 rev.1 1차모드
  미충족(30.4Hz)의 근본원인이었고, STR rev.2가 이 72.0kg·PCD400mm/8-M8을 반영해 재설계·
  재제작(36.1Hz 달성)했음을 PAY 측 수치와 대조 확인 — **수치 일치, 불일치 해소 확인**.
- ICD 6건(EPS·HAR·TCS·MECH·STR·OBC·FSW) 전량 수치 회신 완료, 잠정 없음.
- **1.8kW 펄스 시험 방법**: u2-pulse-test.md는 PAY-U2 자체 시험(CAL 교정 실험실 전원 기준)으로,
  EPS 실 배터리·PCDU를 통한 위성 통합 전력경로 시험은 아님 — EPS rx-2 소견과 동일하게 INT
  통합 실증 필요(→ INT-TST-2).

## 재사용 판단
- AOCS·PAY 자체 판정 재확인: 기존 HIL·펄스시험 장비 재사용, 신규 불요.
- PAY-EPS 통합 1.8kW 실증: rx-2에서 이미 NEED-GSE-PULSE로 판단(중복 발행 방지, source는
  rx-2로 통일).

## 판정
AOCS·PAY sysreq 전항목 충족 재확인. 질량 38↔72kg 불일치는 PAY 실측치와 STR rev.2 반영치가
정확히 일치함을 확인하여 **해소 확인 완료**. 1.8kW 통합 실증은 INT-TST-2로 이관.
