# FSW 통신·탑재 관리 SW 설계

입력: examples/ksat6/deliverables/SE/sysreq.md, examples/ksat6/deliverables/FSW/architecture.md, examples/ksat6/deliverables/OBC/io-board.md

## 명령/텔레메트리 처리
- 상향(S-band 64kbps): CCSDS TC 프레임 수신·인증·명령 디스패치.
- 하향(S-band 2Mbps 상태 / X-band 150Mbps 영상): CCSDS TM 프레임 생성,
  우선순위 큐(비상 TM > 상태 HK > 영상 벌크).

## 탑재체 시퀀서
- 관측 시퀀스 업로드(지상 명령) → 시각 동기 실행 → SpW 채널로 영상 수신
  → OBC-MEM 버퍼 영역(mem-board.md "탑재체 영상 버퍼 118GB")에 저장
  → 다운링크 큐 등록.

## FDIR / 밸브류 액추에이터 안전 로직
- PROP 등 유닛의 밸브·액추에이터 명령은 이 태스크가 중계하며, 명령 실행 전
  인터록(사전조건: 압력·온도 범위, 이중 확인 명령) 검사를 수행한다.
- PROP으로부터 밸브 로직 요구가 도착하면 이 설계에 반영·회신한다(별도
  REQ-PROP-FSW 게시글 발행 시 처리).

## 검증 케이스(총 6건)
1. TC 프레임 수신·인증 정상 처리
2. TC 인증 실패 시 명령 폐기
3. TM 큐 우선순위(비상>HK>영상) 준수
4. 탑재체 시퀀스 시각 동기 실행 오차 <100ms
5. 밸브 명령 인터록 미충족 시 명령 거부
6. 다운링크 큐 오버플로 시 저우선순위 데이터 드롭, 비상 TM 무손실

검증: 위 6개 케이스를 FSW-VV 통합검증에서 프로세서 시뮬레이터로 재현·확인(교차참조).
