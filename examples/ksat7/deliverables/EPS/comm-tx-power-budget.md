# COMM 송신 첨두 전력 배정 회신 (REQ-COMM-EPS)

입력: examples/ksat7/board/REQ-COMM-EPS.md, examples/ksat7/deliverables/EPS/pcdu-pulse-design.md

1) COMM 채널 첨두 DC 배정: **60W**, 지속시간 제한 없음(교신 패스당 최대 600s 연속 허용).
2) SAR 펄스(1.8kW/90s)와 동시 발생: **허용**. SAR 펄스는 슈퍼캡·배터리 하이브리드
   전용 경로로 공급되어 정상모선 부하 경로와 물리적으로 분리된다. 단, COMM 60W를
   포함한 정상모선 부하 총합이 EOL 소비예산 540W(sysreq)를 넘지 않아야 한다.
3) 모선 50V±5V 리플·과도 규격(HPA 전원단 설계용): 정상상태 리플 ≤200mVpp,
   0→60W 부하 스텝 시 전압편차 ≤±2%(≤1V), 정착시간 ≤5ms.

검증: 모선50V±5V·리플200mVpp·과도±2%/5ms 규격 회신, SAR 동시운용 조건부 허용
