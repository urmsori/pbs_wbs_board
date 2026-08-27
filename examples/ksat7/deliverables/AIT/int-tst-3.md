# 통합시험 3 — RF·데이터 종단간 (int-tst-3)

입력: examples/ksat7/deliverables/AIT/rx-3.md, examples/ksat7/deliverables/COMM/comm-u1-tst.md,
examples/ksat7/deliverables/OBC/functional-test.md, examples/ksat7/deliverables/FSW/sim-test-sequencer.md,
examples/ksat7/deliverables/GS/module-fm.md

## X-band 링크마진 재확인 (통합 경로)
COMM-U1 실장착 안테나·통합 하니스·GS 전 경로 기준 실측: 링크마진 **+5.2dB**(유닛레벨
+5.4dB 대비 -0.2dB, 통합 하니스 삽입손실 반영, 여전히 양의 마진). GS G/T 저하분(-1.4dB)은
GS 자체 G-TST 3개소 실측 재확인분과 일치, 추가 열화 없음.

## SAR 원시데이터 경로 종단간 실측
PAY-U2(펄스발생기) 실촬영 모의 → FSW-U2 시퀀서(4중인터록) → OBC-U1 저장부, 실 하드웨어
연동(기존에는 sim-test-sequencer 시뮬레이션만 수행): 스팟 첨두 **3.54Gbps**(OBC 단독
기능시험 3.55Gbps와 0.01Gbps 이내 일치), SpW 5채널 全정상, 18/18버스트 데이터 무결성
CRC 오류 없음.

## 판정
sysreq COMM(X-band800Mbps) 통합 재확인 PASS(마진+5.2dB), SAR 원시데이터 종단간 실 하드웨어
경로 검증 완료(3.54Gbps, 무결성 확인).

검증: X-band 통합 링크마진+5.2dB(양수, PASS), SAR원시데이터 종단간 3.54Gbps·CRC오류없음
실 하드웨어 확인
