# [PAY→TCS] 광학부 온도 안정성 수용 확인
입력: examples/ksat6/deliverables/PAY/telescope-optics.md

## 확인
TCS-01이 도출한 광학벤치 구배 ≤2°C, 궤도 1주기 내 변동 ≤±0.5°C는
telescope-optics.md §3에서 PAY가 독자 산출한 열변형 WFE 예산(12nm RMS →
±0.5°C, 감도계수 24nm/°C 가정)과 **정확히 일치**한다 — 수용 가능.

구배(≤2°C) 항목에 대해서는 PAY 광학계가 별도 구배 배분을 갖고 있지 않았으므로
신규로 수용: 구조 3점 킨네마틱 마운트(REQ-STR-PAY 회신 참조)로 국부 열구배가
경통에 굽힘을 유발하지 않는 설계를 전제로 한다.

**대안 수치 없음 — TCS-01 제시 값(±0.5°C, 구배≤2°C) 그대로 채택.**

검증: PAY 독자 WFE 예산(telescope-optics.md §3)과 TCS 열해석 결과가 ±0.5°C로
일치 — REQ-TCS-PAY 응답.
