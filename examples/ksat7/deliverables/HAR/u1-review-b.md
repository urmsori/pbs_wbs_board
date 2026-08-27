# HAR-U1 검토의견 B (열/EMC)

입력: examples/ksat7/deliverables/HAR/u1-thermal-analysis.md, u1-drawing-check.md

## 검토
- 줄열 해석: 단열 근사(보수적)로도 도체 최고온도 65.5°C, 절연정격 200°C
  대비 134.5°C 여유 — 충분.
- 접지/차폐: 편조 실드 + SPG 접지 계획 확인. 최종 EMC 차폐 실측은
  HAR-U2-INS-01 단계(EMC 차폐 검사)로 이관되나, U1도 동일 편조 실드
  적용이므로 설계상 문제 없음. 단, U1 자체의 차폐 실측이 INS 항목에
  명시적으로 없어 향후 통합시험(INT) 단계 EMC 확인 권고.

## 의견
열/EMC 관점 승인. 권고사항 1건(위 통합시험 단계 U1 차폐 실측 권고)을
module-fm.md 리스크로 기록할 것.
