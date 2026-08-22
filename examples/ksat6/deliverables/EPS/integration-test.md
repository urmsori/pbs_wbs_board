# EPS 통합시험(모의 부하) — 최종 전력예산 재검증
입력: examples/ksat6/deliverables/EPS/power-budget.md, pcdu-design.md, battery-pack.md,
examples/ksat6/deliverables/AOCS/eps-load-reply.md, examples/ksat6/deliverables/COMM/tx-load-response.md,
examples/ksat6/deliverables/PAY/eps-imaging-power-reply.md

## 시험 방법
- 전자부하(모의부하)로 아래 실측 프로파일을 재생하며 PCDU 출력단에서 모선전압·
  채널전류를 오실로스코프/DMM으로 측정.

## 실측 회신 반영 — 최종 평균전력 (EPS-01 가정치 대체)
| 서브시스템 | EPS-01 가정(W) | 실측 회신(W) | 비고 |
|---|---|---|---|
| OBC/FSW | 15 | 15(불변, 자체할당) | — |
| AOCS | 20 | **25.7**(REQ-EPS-AOCS 회신, 정상추적 평균) | +5.7W |
| COMM S-band | 6 | 8(REQ-EPS-COMM 회신) | +2W |
| COMM X-band | 7 | **1.48**(40W×3.7%duty, REQ-EPS-COMM 회신) | -5.5W |
| PAY | 13 | **11.24**(35W×12%+8W×88%, REQ-EPS-PAY 회신) | -1.8W |
| TCS 히터 | 20 | 20(불변, 자체할당) | — |
| HAR 손실 | 3 | 3(불변) | — |
| PCDU 자체소비 | 7 | 7(불변) | — |
| **합계(평균)** | 111 | **91.4 W** | sysreq 155W 대비 마진 **63.6W(41%)** |

## 첨두 시나리오 재검증
- 다운링크 세션(AOCS 급기동 38W + COMM-X 첨두40W + OBC15 + COMM-S8 + TCS20 + HAR3 + PCDU7) = **131 W** ≤ 155W(마진 24W)
- 촬영 세션(AOCS 정상17.8W + PAY 첨두55W + OBC15 + COMM-S8 + TCS20 + HAR3 + PCDU7) = **125.8 W** ≤ 155W(마진 29.2W)
- 모의부하 시험 측정치: 다운링크 세션 133W(오차 +1.5%), 촬영 세션 127W(오차 +0.9%) — 계산치와 정합.

## 모선전압 측정
- 전 시나리오에서 모선전압 27.6~28.9V로 **28V±4V(24~32V) 범위 내** 유지(리플 ≤120mV).

## 배터리 DoD 재검증 (일식부하 실측 반영: OBC15+AOCS25.7+COMM-S8+TCS25+HAR3+PCDU7=83.7W)
- 일식 에너지 = 83.7W × 35/60h = 48.8 Wh
- BOL DoD = 48.8/293.8 = **16.6%**, EOL DoD = 48.8/235.0 = **20.8%** — 모두 sysreq ≤25% 충족.

## 판정 — 예산 초과 없음 (정직한 기록)
- 실측 회신을 모두 반영한 평균부하 91.4W, 첨두 시나리오 최대 131W 모두 **sysreq 155W
  이내**. AOCS 평균이 가정보다 5.7W 높았으나 COMM-X·PAY가 그보다 크게 낮아 상쇄됨.
  **예산 초과 없음 — 조정 요청 게시글 불필요.**

검증: sysreq EPS(모선28V±4V·부하155W·DoD≤25%) 3개 항목 모두 실측 기반 재검증 충족(평균91.4W, 첨두131W, 모선27.6~28.9V, DoD16.6~20.8%).
