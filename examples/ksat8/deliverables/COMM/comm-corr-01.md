# COMM-CORR-01 — FSW·OBC 잠정회신 정정 공지

입력: examples/ksat8/deliverables/COMM/comm-u1-fm-package.md

REQ-FSW-COMM-TMTC·REQ-OBC-COMM-IF의 잠정 자답(fsw-tmtc-reply.md,
obc-if-reply.md)을 COMM-U1 확정치와 대조했다.

- OBC 잠정 가정(1553B 이중버스·콜드스탠바이)은 **확정치와 일치** — 정정
  불필요. TM은 32워드/1Hz 프레임, TC는 16워드/10cmd/s로 구체화됨(OBC가
  참고).
- FSW 잠정 가정 중 "레인징-TM/TC 주파수분할 공존"은 **부정확** — 확정치는
  동일 캐리어 결합변조(레인징 부반송파 억압)다. FSW는 TC 검증규칙 설계
  시 이 정정을 반영 바람.
- FSW의 CRC/2단계확인/순번검사 항목은 COMM 트랜스폰더 범위 밖(OBC-FSW
  프로토콜 계층)이라 COMM이 확인·정정할 수 없음 — 해당 팀 자체 판단 필요.

검증: OBC 가정 일치(정정 불필요), FSW 레인징 공존 방식 1건 정정 통지.
