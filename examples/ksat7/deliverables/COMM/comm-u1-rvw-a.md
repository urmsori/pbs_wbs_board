# COMM-U1 검토의견 A (전기·RF)

입력: examples/ksat7/deliverables/COMM/comm-u1-dsn.md, comm-u1-chk.md

## 검토
- 링크버짓 예측 마진 +8.9dB — 32APSK 5/6 전제, LDPC 프레임 오버헤드 반영됨(구현손실1.0dB
  포함) 확인. 적정.
- DC전력 43.7W < EPS 배정 60W(마진 27%) — 배정 대비 여유 충분, EPS 상호배제 조건(정상모선
  총합 540W EOL 이내)은 EPS 전력예산 통합에서 재확인 필요(COMM 단독으로는 충족).
- 지적사항: 커넥터 라벨 폰트 확대(CHK 지적) — 경미, 제작 단계 반영 조건부 승인.

판정: 전기/RF 관점 조건부 승인(경미 지적 1건, 제작 시 반영).
