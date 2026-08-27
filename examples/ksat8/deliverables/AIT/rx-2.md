# AIT-RX-2 전력·전개·열·추진(EPS/SA/TCS/PROP) 인도 수령·판정

입력: examples/ksat8/deliverables/EPS/module-fm.md,
examples/ksat8/deliverables/SA/module-fm.md,
examples/ksat8/deliverables/TCS/module-fm.md,
examples/ksat8/deliverables/PROP/module-fm.md

## 판정
| 트랙 | sysreq 항목 | 인도 문서 판정 |
|---|---|---|
| EPS | 100V±2V·15kW배전·이클립스2.4kWh | 98.4~101.7V·14,420W 실증·2.44kWh — 충족 |
| SA | EOL16kW·1차모드≥0.1Hz | 16,120W(마진0.75%)·0.118Hz — 충족 |
| TCS | 방열6kW·작동-10~+60°C | 부하5.04kW/용량6.3kW·TVAC실측-9~+52°C — 충족 |
| PROP | Δv 2,250m/s | 1,500+750=2,250m/s 정확 일치 — 충족 |

## 이월 항목
4개 트랙 module-fm.md 모두 "잠정 가정으로 남은 입력 없음"을 명시했다.
SA의 EOL 마진(0.75%)은 module-fm.md가 "운용 단계 관찰 항목"으로
못박아 INT 재작업 대상이 아니다. TCS의 TWTA 6kW 방열은 통합 열시험
(INT-TST-4)에서 개별시험(패널 단위 TVAC)과 다른 통합 열부하 조건으로
재확인한다(신규 확인 항목이지 이월 리스크는 아님). 세부 기록 요청 불요
— REQ 발행 없음.

검증: EPS·SA·TCS·PROP sysreq 항목 전량 인도 문서 기준 충족 확인, 이월
리스크 없음(SA 마진 관찰 항목 1건은 운용 단계로 명시 이관)
