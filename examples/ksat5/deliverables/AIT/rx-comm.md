# COMM EM 모듈 인수 시험 결과
입력: examples/ksat5/deliverables/COMM/module-em.md,
      examples/ksat5/deliverables/COMM/link-budget.md,
      examples/ksat5/deliverables/COMM/transceiver-em.md,
      examples/ksat5/deliverables/SUPPORT/need-rf-comm.md,
      examples/ksat5/deliverables/SUPPORT/need-har-comm.md

AIT-RX-COMM(AIT-TST)의 COMM EM 모듈 인수 시험 기록. NEED-RF-COMM(RF
감쇠기·더미로드)과 NEED-HAR-COMM(전원·데이터 하니스)로 module-em.md가
"인도 시점 잔여 리스크"로 명시한 미해결 항목(EOD 6.8V PA 출력 저하)을
실측 확인한다.

## 1. 시험 구성
- RF: need-rf-comm.md SMA 케이블+30dB 감쇠기+50Ω 더미로드 경로.
- 전원/데이터: need-har-comm.md 채널 1(액추에이터 레일 가변 6.8~8.4V)
  + 채널 2(5V 로직 레일) + 채널 3(UART, EGSE가 OBC 대행).

## 2. PA 출력 실측 (미해결 리스크 §1 재확인)
| 공급전압 | 측정 PA 출력(감쇠 보정 후) | 설계치(33dBm) 대비 |
|---|---|---|
| 8.4V(공칭) | 33.1 dBm | +0.1 dB |
| 6.8V(EOD) | 32.7 dBm | −0.4 dB(8.4V 대비 −0.4dB) |

## 3. 링크마진 재계산
link-budget.md 마진 6.3dB(요구 6dB, 여유 0.3dB)는 Pt=33dBm 가정. 실측
반영 시:
- 8.4V 조건: Pt 33.1dBm → 마진 ≈6.4dB(여유 0.4dB, 개선)
- **6.8V(EOD) 조건: Pt 32.7dBm → 마진 ≈6.0dB — 요구(≥6dB) 정확히
  충족하나 여유 0dB.** module-em.md가 우려한 "저전압 조건에서 마진
  잠식"이 실제로 발생함을 실측으로 확인.

## 4. 부가 확인
- 링크버짓 재확인(8.4V): 마진 ≥6dB — 통과.
- 5V 로직 레일: 0.52A 사용(module-em.md test 결과와 동일), 여유 74%.
- 더미로드 종단 무방사 확인, 스퓨리어스 이상 없음.
- 질량 1.20kg — 배분 1.2kg 소진(여유 0kg), module-em.md 인도치와 동일.

## 5. 판정
링크버짓·5V레일·질량은 module-em.md 인도 수치와 일치해 통과. **EOD
6.8V 조건 링크마진은 실측 결과 여유 0dB(정확히 요구 충족, 추가 저하
여지 없음)로 module-em.md의 미해결 리스크가 사실로 확인됨** — 요구는
충족하므로 인수 자체는 합격 처리하되, 이 결과를 통합시험(INT) 단계의
전력수지·EOD 여유 검토에 반영해야 할 잔여 리스크로 명시해 이월한다.
COMM EM 모듈 인수 **조건부 합격**(EOD 마진 0dB, 후속 모니터링 필요).

검증: PA 출력 8.4V/6.8V 두 조건 실측(각 33.1dBm/32.7dBm), 링크마진
재계산 결과 EOD 조건 6.0dB(요구 6dB 충족·여유 0dB) 확인. 5V레일·질량은
module-em.md 인도치와 일치 확인.
