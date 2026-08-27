# OBC 모듈 비행모델(FM) 인도 — 취합

입력: examples/ksat7/deliverables/OBC/obc-storage-design.md, structural-analysis.md,
thermal-analysis.md, design-check.md, review-a-electrical.md, review-b-reliability.md,
rb-decision.md, iqc.md, mfg.md, cln.md, ins.md, functional-test.md,
comm-interface-spec.md, io-connector-pinmap.md, examples/ksat7/deliverables/SE/sysreq.md

## OBC-U1(OBC·2TB 저장부) 직능 체인
| 단계 | Work | 산출물 | 상태 |
|---|---|---|---|
| 설계 | OBC-U1-DSN(+REV) | obc-storage-design.md | DONE |
| 구조해석 | OBC-U1-ANL-S | structural-analysis.md | DONE |
| 열해석 | OBC-U1-ANL-T | thermal-analysis.md | DONE |
| 도면검도 | OBC-U1-CHK | design-check.md | DONE |
| 검토(전기) | OBC-U1-RVW-A | review-a-electrical.md | DONE |
| 검토(신뢰성) | OBC-U1-RVW-B | review-b-reliability.md | DONE |
| 검토회 | OBC-U1-RB | rb-decision.md | DONE |
| CM배포(서비스) | CM-OBC-U1 | CM/obc-u1-release.md | DONE |
| 구매(서비스) | PUR-OBC-U1 | PUR/obc-u1-parts.md | DONE |
| 입고검사 | OBC-U1-IQC | iqc.md | DONE |
| 제작조립 | OBC-U1-MFG | mfg.md | DONE |
| 세척 | OBC-U1-CLN | cln.md | DONE |
| 최종검사 | OBC-U1-INS | ins.md | DONE |
| 교정(서비스) | CAL-OBC-U1 | CAL/obc-u1-cal.md | DONE |
| 기능시험 | OBC-U1-TST | functional-test.md | DONE |

## 외부 인터페이스 협상 결과
- PAY(REQ-OBC-PAY, 발신): 스팟 첨두3.2Gbps/평균1.1Gbps, 스트립맵 첨두
  1.2Gbps/평균450Mbps, SpW 4채널 — 회신 지연으로 잠정치(1.2Gbps·2채널)로
  최초 설계, 실회신 도착 후 OBC-U1-DSN-REV로 정정(3.6Gbps·5채널). 확정.
- COMM(REQ-COMM-OBC, 수신): SpW 850Mbps, 재생버퍼 256Mbit, 언더런마진
  15% 회신. 확정.
- HAR(REQ-HAR-OBC, 수신): MDM-51 커넥터, SpW5/CAN2/1553B1 핀맵, 실드접지
  41번핀 회신. 확정.

## sysreq.md OBC 항목 최종 판정
| 항목 | 요구 | 실측(OBC-U1-TST) | 판정 |
|---|---|---|---|
| 처리여유 | ≥50% | 51.6% | 충족 |
| 저장용량 | 원시 2TB | 2.01TB | 충족 |
| 인터페이스 | SpW/CAN | 1553×1·CAN×2·SpW×5 全PASS | 충족 |

**종합: sysreq.md OBC 3개 항목 전부 충족. M-OBC 인도 가능.**

## 잠정 사항의 최종 처리
- SAR 원시데이터율(REQ-OBC-PAY): 8회×20초 폴링 중 회신 도착 → 정정
  게시글(OBC-U1-DSN-REV)로 기록대역폭 1.2→3.6Gbps, SpW 2→5채널 반영,
  기능시험(케이스3)에서 3.55Gbps 실측 재확인.

검증: 15개 유닛 Work 전부 DONE, 외부 인터페이스 3건(PAY·COMM·HAR) 전부
확정, sysreq OBC 3항목 전부 충족 재확인(기능시험 실측치 기준).
