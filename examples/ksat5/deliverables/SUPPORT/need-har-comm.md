# COMM EM 모듈 인수 시험용 전원·데이터 시험 하니스
입력: examples/ksat5/deliverables/COMM/transceiver-em.md,
      examples/ksat5/deliverables/COMM/icd-str-comm-footprint.md

NEED-HAR-COMM(AIT-TST) 요청에 대한 하니스 기술자 인도물. transceiver-em.md
§"인터페이스 커넥터 정의"·§"기구 포락선"이 명시한 90mm 변 일렬 배치
(RF·전원2핀×2·UART, −X 데크 모서리 인출 방향)를 반영.

## 채널 구성
| 채널 | 신호 | 커넥터(모듈측/EGSE측) | 사양 | 비고 |
|---|---|---|---|---|
| 1 | 액추에이터 레일 전원 2핀 | 2핀 EPS 표준 준용 / EGSE 가변전원 단자 | 6.8~8.4V 가변, PA 전용, 0.6~0.74A | EOD 조건 재현용 독립 공급 |
| 2 | 5V 로직 레일 전원 2핀 | 2핀 EPS 표준 준용 / EGSE 정전압 단자 | 5V, ~0.12A | 액추에이터 레일과 독립 공급 |
| 3 | UART 데이터 | 데이터 커넥터(OBC 인터페이스 규격) / USB-UART 브리지 | 3.3V TTL, OBC 대행 | EGSE가 OBC 대신 링크상태·텔레메트리 송수신 |

RF(SMA) 채널은 NEED-RF-COMM 하니스로 별도 처리(본 하니스는 전원·데이터
2계통만 취급).

## 배선/인출 규격
90mm 변의 일렬 배치(RF·전원×2·데이터) 순서를 그대로 따라 트렁크를
구성하고, −X 데크 모서리 인출 방향에 맞춰 케이블 여유 길이 1.2m로
EGSE 브레이크아웃 박스까지 인출한다. 액추에이터 레일과 5V 로직 레일은
물리적으로 분리된 커넥터로 서로 다른 EGSE 전원 채널에 연결해 두 레일을
독립 가변할 수 있도록 한다(EOD 6.8V 시험 시 액추에이터 레일만 낮추고
5V 로직 레일은 정격 유지 가능해야 함).

검증: NEED-HAR-COMM 요청의 전원 2핀×2(액추에이터 6.8~8.4V 가변, 5V
로직) + UART 3.3V TTL 1채널 구성이 위 채널표와 일치함을 확인.
transceiver-em.md 인출 위치·방향과 일치함을 확인.
