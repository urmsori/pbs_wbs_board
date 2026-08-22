# EPS → COMM 회신: X-band 송신 첨두전력 허용치
입력: examples/ksat6/deliverables/EPS/pcdu-design.md

- 배정 가능 첨두전력 상한: **70 W**(28V±4V 모선, 듀티 ≤10%/궤도 가정 — REQ-EPS-COMM 회신으로 재확인 예정)
- 허용 첨두전류: 24V 기준 2.92A, 채널 퓨즈 정격 **4A**(약 1.4배 마진) → RF 출력 잠정 10W(효율 30~35% 가정 시 DC 입력 ≈29~33W) 사용 시 여유 충분, duty 제약 없음(퓨즈 열정격 내).
- 실제 X-band 송신 프로파일(첨두전류·듀티)이 확정되면 REQ-EPS-COMM으로 회신 바란다 — EPS-04 통합시험에서 실측 검증한다.

검증: PCDU 채널표(COMM X-band 4A/70W) 인용 회신.
