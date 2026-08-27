입력: examples/ksat8/deliverables/SE/sysreq.md

# COMM → FSW 회신: TT&C 프로토콜·TC 검증 규칙 [잠정]

**주의(잠정)**: COMM 트랙이 자기 설계 체인 진행 중으로 8×20초 폴링 내
정식 회신이 오지 않아, FSW 리드가 sysreq.md 요약(S-band 상시·레인징)과
표준 위성 TT&C 관행에 근거해 잠정 회신한다. COMM-U1 확정 후 정정한다.

1. 프로토콜: CCSDS TC/TM 스페이스 패킷 가정, 프레임 동기어는 표준
   CCSDS ASM(0x1ACFFC1D) 가정.
2. TC 검증 규칙: CRC-16 체크섬, 크리티컬 명령(추력기 점화·모드 전환 등)은
   2단계 확인(무장→실행) 필수, 순번 검사로 재전송 중복 실행 방지,
   거부 시 NAK TM 프레임 회신.
3. 레인징: PN 레인징 신호와 TM/TC는 주파수 분할로 공존(레인징 채널
   별도 서브캐리어) 가정.

검증: sysreq TT&C 요약과 정합. 정식 COMM-U1 회신 대기 중(잠정).
