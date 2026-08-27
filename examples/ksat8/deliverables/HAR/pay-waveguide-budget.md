# REQ-PAY-HAR-도파관 회신 — TWTA-안테나 간 도파관 손실 예산

입력: examples/ksat8/board/REQ-PAY-HAR-도파관.md,
examples/ksat8/deliverables/HAR/u2-design.md

## 회신 (HAR-U2 설계 기준, 잠정 — PAY 플랜지 규격·STR 실경로 확정 전)
- 경로장: 편도 2.0m(TWTA 출력부→중앙 실린더 관통부→안테나 급전부)
- 굴곡: 90° 3회
- 플랜지 접속: 4개소(양단 2개소+중간 분기 2개소)
- 삽입손실 배분: 직선 0.30dB + 굴곡 0.15dB + 플랜지 0.12dB = **0.57dB**
- VSWR(잠정): 플랜지·굴곡 포함 경로 전체 ≤1.15:1(대표 Ka-band 도파관
  경로 관행치)

## 판정
삽입손실 0.57dB ≤ sysreq HAR 상한 0.8dB **충족**(0.23dB 마진). 본
수치는 HAR-U2-DSN-01 잠정 가정(REQ-HAR-PAY-RF·REQ-HAR-STR-경로 회신
대기 타임아웃) 기준이며, PAY 플랜지 규격·STR 실제 경로 확정 시
재계산해 정정 회신할 수 있다.

검증: 삽입손실 0.57dB≤0.8dB(sysreq HAR 상한) 회신, TWTA 필요출력 역산
입력으로 사용 가능(잠정 조건부)
