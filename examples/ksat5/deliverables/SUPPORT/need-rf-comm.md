# COMM EM 모듈 인수 시험용 RF 감쇠기·더미로드
입력: examples/ksat5/deliverables/COMM/transceiver-em.md,
      examples/ksat5/deliverables/COMM/icd-eps-comm-power.md

NEED-RF-COMM(AIT-TST) 요청에 대한 치구/기타 담당 인도물. transceiver-em.md
§인터페이스 커넥터 정의(SMA(f), PA 출력 2W/33dBm)와 §리스크(EOD 6.8V
PA 출력 저하 우려, 링크버짓 마진 0.3dB)를 반영한 RF 계측 구성.

## 구성품
| 항목 | 사양 | 용도 |
|---|---|---|
| RF 케이블 | SMA(m)-SMA(m), 50Ω, 저손실 | 모듈 SMA(f) 포트 ↔ 감쇠기 연결 |
| 감쇠기 | 30dB, 정격 5W(33dBm=2W 대비 여유), SMA(m/f) | 전력계/스펙트럼분석기 입력 정격(통상 +20~+30dBm) 이내로 감쇠 |
| 더미로드 | 50Ω, 정격 5W, SMA(m) | 방사 없이 종단 측정(실내 무방사 시험용) |
| 전력계/센서 어댑터 | SMA(f), 감쇠기 후단 접속 | 감쇠 후 실효 출력 역산(감쇠기 표시값 보정) 측정 |

## 측정 시나리오
1. 8.4V 공칭 공급 → PA 송신 → 감쇠기 30dB 경유 → 전력계로 실측 →
   30dB 보정해 PA 출력(목표 33dBm=2W) 산출
2. 액추에이터 레일 EOD 6.8V 공급 → 동일 경로로 재측정 → 8.4V 대비
   출력 저하량 산출, 링크버짓 마진 0.3dB 잠식 여부 판정
3. 더미로드 종단 구성으로 무방사 상태에서 정상 송신 확인(실내 규정
   준수), 필요 시 스펙트럼분석기로 스퓨리어스 확인

검증: NEED-RF-COMM 요청의 SMA 케이블+33dBm급 감쇠기+50Ω 더미로드,
8.4V/6.8V 두 조건 측정 구성이 위 구성품·시나리오와 일치함을 확인.
transceiver-em.md PA 출력(2W/33dBm) 대비 감쇠기 정격(5W) 여유 확인.
