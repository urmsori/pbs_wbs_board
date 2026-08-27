# HAR-U2 신호·데이터 하니스 도면 검도

입력: examples/ksat7/deliverables/HAR/u2-design.md, examples/ksat7/deliverables/OBC/io-connector-pinmap.md

## 검도 항목
1. 핀맵 대조: MDM-51 51핀 중 SpW20+CAN4+1553B6+실드1 = 31핀 사용, OBC
   회신표(35핀 사용+실드)와 표기 상 예비 4핀 차이 확인 — 예비 핀 표기
   차이는 문서상 정정(예비 4핀 포함 시 35핀), 실사용 배선 핀수는 OBC
   회신과 일치. 이상 없음.
2. 실드 접지: 41번핀 단일점 접지, 개별 실드 플로팅(접지루프 방지) —
   OBC EMC 요구와 일치.
3. 라우팅: HAR-U1(대전류 펄스) 대비 150mm 이격 — EMC 상호간섭 저감
   설계 타당.

## 판정
검도 통과, 이견 없음. RB 단계로 송부(RVW 생략 — 축약 체인).
