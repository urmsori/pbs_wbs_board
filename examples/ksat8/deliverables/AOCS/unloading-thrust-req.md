# REQ-PROP-AOCS-추력 회신 — 모멘텀 언로딩 AOCS측 요구

입력: examples/ksat8/deliverables/AOCS/u1-dsn.md, examples/ksat8/board/REQ-PROP-AOCS-추력.md

- 휠 모멘텀 용량: 4기(3+1) 각 ≥25N·m·s, 언로딩 트리거 축당 20N·m·s(80%).
- 1회 언로딩 소요시간(계산): 20N·m·s ÷ 0.22N·m(PROP 회신 피치축 성분) ≈ 91초.
  PROP 제안 세션(10~20분) 충분히 초과 만족 — 최소펄스 50ms로도 미세조정 가능.
- 연간 언로딩 빈도(추정): 격주 1회(26회/년), SRP+SADA 축적률 기준 잠정치.
- 추력기-휠축 정렬 허용오차: ≤1.0°(토크 벡터 분해 오차 <5% 유지 조건).
- PROP 회신(4기 SPT급 200mN, 캔팅±20°, 명령 discrete on/off+duty)의 배치·명령
  인터페이스는 위 요구를 만족 — 추가 변경 요청 없음.

검증: 91초≪10~20분(PROP 세션), 정렬허용오차 1.0° PROP 캔팅브래킷 공차 내 반영 요청
