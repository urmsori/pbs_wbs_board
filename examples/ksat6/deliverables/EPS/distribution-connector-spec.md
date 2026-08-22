# EPS → HAR 회신: 배전 출력 커넥터·채널 전류정격
입력: examples/ksat6/deliverables/EPS/pcdu-design.md

PCDU 배전 출력은 채널별 Micro-D 커넥터(9/15/25핀, 채널표 참조)이며, 채널별
첨두전류(24V 기준)는 pcdu-design.md 표와 동일: OBC 0.63A, AOCS 2.92A,
COMM-S 0.33A, COMM-X 2.92A, PAY 2.71A, TCS 히터 3채널 합계 0.92A.
주버스 총 첨두전류 6.29A(151W/24V), 모선 28V±4V.
케이블 게이지는 이 전류값과 하니스 길이로 HAR 팀이 sysreq "전원선 전압강하
≤2%" 기준으로 산정해 달라 — EPS 쪽 여유는 채널 퓨즈 정격(1.4~1.5배 마진)까지다.

검증: PCDU 채널전류표 인용 회신, sysreq HAR 전압강하 ≤2% 판정은 HAR 팀 몫으로 명시.
