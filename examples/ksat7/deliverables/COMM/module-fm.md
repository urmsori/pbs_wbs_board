# COMM 모듈 비행모델 인도 요약

입력: examples/ksat7/deliverables/SE/sysreq.md, COMM-U1/U2 전 유닛 산출물 일체

## sysreq.md 판정 대상 (인용)
COMM: **S-band 64k/2M, X-band 800Mbps(DVB-S2)**

## COMM-U1 (X-band 800Mbps 송신계, DVB-S2)
- 설계: 32APSK 5/6, 180.6Msps, 예측 링크마진 +8.9dB(comm-u1-dsn.md) — ICD 3건
  (OBC/STR/EPS) 전부 실회신 반영(SpW850Mbps·버퍼256Mbit / -Y측판3.0kg·시야±70° /
  첨두DC60W배정)
- 구조·열: 국부1차모드118Hz≫35Hz, 베이스플레이트52°C(정격85°C대비마진33°C) —
  TCS 통합열해석 재확인 리스크 승계(INT 단계)
- 검토회(RB): 승인(조건 2건 반영·기록)
- 제작: PUR 6품목 발주 → IQC 전량합격 → MFG 조립완료(라벨조건 반영) → CLN(NIC8.2<10) →
  INS(질량3.02kg≈배정3.0kg)
- **RF시험(TST) 실측: 링크마진 +5.4dB (예측+8.9dB 대비 -3.5dB 열화, 원인 4건 정직 기록:
  RF출력-0.4dB·안테나이득-0.7dB·구현손실-1.0dB·GS G/T-1.4dB)**
- 판정: **X-band 800Mbps 실측 충족 (PASS, 마진 양수)**

## COMM-U2 (S-band TT&C, 헤리티지)
- 제작: PUR 1식 발주 → IQC 합격 → MFG 장착·배선완료 → CLN(NIC7.6<10) → INS(전항목합격)
- 시험(TST) 실측: **업링크 64.0kbps / 다운링크 2.00Mbps**, BER 규격이내
- 판정: **S-band 64k/2M 실측 충족 (PASS)**

## 서비스 요청 결과
CM 1건(형상배포 COMM-U1-BL-001), PUR 2건(U1 6품목/U2 1식 발주완료), CAL 2건(X-band/
S-band 장비 교정확인), PA 1건(U1 TST 입회, 이상없음) — 전부 완료.

## ICD 협상 (송신 REQ 3건)
REQ-COMM-OBC/STR/EPS 전부 회신 완료(8×20s 폴링 내 도착, 잠정가정 불필요).
수신 REQ(타 track→COMM): 없음(모니터링 결과 무).

## 리스크 승계 (INT 단계)
1. TCS 통합 열해석 재확인 필요(comm-u1-anl-t.md — 위성 공유 라디에이터 국부 7°C 초과 가능성)
2. EPS 정상모선 총부하 540W EOL 이내 여부는 전력예산 통합 시 재확인 필요(COMM 단독 43.7W는 배정60W 이내)

검증: sysreq.md COMM 항목(S-band 64k/2M, X-band 800Mbps DVB-S2) — COMM-U1
실측마진+5.4dB, COMM-U2 실측 64.0kbps/2.00Mbps로 전부 실측 수치 충족(PASS).
