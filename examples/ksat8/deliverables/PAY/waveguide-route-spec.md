# REQ-HAR-PAY-RF 회신 — 도파관 플랜지·포트 규격

입력: examples/ksat8/deliverables/PAY/u1-dsn.md,
examples/ksat8/board/REQ-HAR-PAY-RF.md

- 플랜지 형식: **WR-42(Ka-band), UBR-source 규격**, TWTA 출력단 표준.
- 채널별 출력 포트: **24개(운용) + 4개(예비 TWTA)** = 28개, 패널상 4열×7행
  격자(북/남 패널 각 14포트).
- 허용 굴곡수·최소곡률반경: 경로 편도 2.0m급, 90° 굴곡 3회 이내를 전제로
  설계 — 이를 넘는 경로는 별도 협의 요청.
- 손실 예산 PAY측 배분: sysreq 상한 **0.8dB를 설계치**로 사용(PAY-U1-DSN
  링크예산의 설계치, HAR 실측이 이보다 낮다면 그만큼 HAR 측 여유로 남음).

검증: WR-42/28포트/4×7격자 회신, 손실배분 0.8dB(PAY 설계치) 확인
