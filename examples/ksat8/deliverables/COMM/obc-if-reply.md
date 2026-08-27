입력: examples/ksat8/deliverables/SE/sysreq.md

# COMM → OBC 회신: TT&C 인터페이스 [잠정]

**주의(잠정)**: COMM 트랙(M-COMM)이 자기 설계 체인(COMM-U1) 진행 중으로
8×20초 폴링 내 정식 회신이 오지 않아, OBC 리드가 sysreq.md의 TT&C
요약(S-band 상시·레인징)에 근거해 잠정 회신한다. COMM-U1 트랜스폰더
설계가 확정되면 정정 게시글로 갱신한다.

1. TM/TC 버스: MIL-STD-1553B(§obc-design.md와 동일 계열 가정), 전기규격은
   OBC 표준 인터페이스를 따른다고 가정.
2. TM 프레임: S-band 상시 하향, 프레임 전송률은 OBC TM 8,000점 처리와
   정합되는 1Hz 기준 프레임 가정.
3. TC 프레임: 콜드 이중화 가정(OBC 이중화 방식과 동일 계통 분리).

검증: sysreq TT&C 요약과 정합. 정식 COMM-U1 회신 대기 중(잠정).
