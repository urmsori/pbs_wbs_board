# COMM-U1 설계 도면 검도

입력: examples/ksat8/deliverables/COMM/comm-u1-design.md, examples/ksat8/deliverables/COMM/comm-u1-linkbudget.md, examples/ksat8/deliverables/COMM/comm-u1-thermal.md

## 검도 항목·결과
| 항목 | 설계(comm-u1-design.md) | 해석 결과 | 판정 |
|---|---|---|---|
| 상시 전력 | 150W 이내 설계 | 링크버짓: SSPA 2W 정격이 150W 예산 내 | 정합 |
| 피크 전력 | 220W 이내 설계 | 열해석: 피크 10분 이내 열용량 완충 | 정합 |
| 발열 | (미명시) | 상시150W가 TCS 6kW 예산의 2.5% | 여유 확인 |
| 주파수 | 2087.5/2255.5MHz | 링크버짓 동일 주파수로 계산 | 정합 |
| 안테나 이득 3dBi(가정) | §5 잠정 가정 명기 | 링크버짓도 동일 가정 사용, 결과에
  "STR 실회신 시 재계산" 명기 | 조건부 승인 — STR 정정 대기 항목으로 이월 |

## 결함·이견
없음. 단 §5(안테나 배치) 잠정 가정은 RVW·RB 단계에서도 잠정임을 재확인
받아야 한다.

검증: 3개 산출물 수치(전력·주파수) 상호 정합, 안테나 가정 종속성은
이월 항목으로 명시.
