# 통신(COMM) EM 모듈 인도 문서
입력: examples/ksat5/deliverables/COMM/link-budget.md,
examples/ksat5/deliverables/COMM/transceiver-em.md (rev.2),
examples/ksat5/deliverables/COMM/antenna-design.md,
examples/ksat5/deliverables/COMM/bus-voltage-check.md

## 모듈 구성
1. UHF 트랜시버 EM 보드 — 송신 2W(33dBm) GMSK, 9.6kbps, 수신 LNA/복조 포함
2. UHF 디플로이어블 휩 안테나 4조(−Z 패널 장착)
3. 전원 인터페이스: PA는 액추에이터 레일(8.4V, 버스직결), 로직단은 5V 레일

## 통합·기능시험 결과 (COMM-05)
| 시험 항목 | 판정 기준 | 결과 |
|---|---|---|
| 링크버짓 재확인 | 마진 ≥ 6 dB | 6.3 dB (link-budget.md 계산치 유지, 부품 실측 전까지 해석치) |
| 5V 로직 레일 전압 유지(송신 중) | 정격(2.0A) 이내 | 0.52A 사용, 여유 74% 확인(bus-voltage-check.md) |
| 안테나 수납/전개 포락선 | STR ICD 범위 내 | 확인(antenna-design.md, STR 회신 기준) |
| 질량 | ≤ 1.2 kg 배분 | 트랜시버 0.55 + 안테나 0.15 + 하네스/체결 여유 0.50 = 1.20 kg (배분 한도 내, 여유 없음 — 후속 단계에서 경량화 검토 필요) |

## 인도 시점 잔여 리스크 (정직 공개, 미해결 상태로 이월)
1. **액추에이터 레일(8.4V) 분기 퓨즈 정격 미확정** — EPS-04(부하 스텝
   시험)에서 COMM 송신 펄스 파형을 실측 조건으로 포함해 재확인 예정
   (EPS 권고, bus-voltage-check.md §4).
2. **방전 말기(EOD 6.8V) 조건에서 PA 출력 저하 가능성** — 링크버짓
   마진이 0.3dB로 작아, 저전압 조건에서 실측 검증 필요(icd-eps-comm-power.md,
   transceiver-em.md rev.2 리스크 항목).
3. **질량 여유 0 kg** — 배분 1.2kg을 정확히 소진, 하네스 실측 시 초과
   가능성 있음.

이 항목들은 통합시험(AIT) 단계에서 실측 데이터가 모이는 대로 COMM
팀이 재검증한다 — "괜찮다"고 단정하지 않고 미해결로 명시해 인도한다.

## 산출물 목록 (본 모듈을 구성하는 COMM 산출물)
- examples/ksat5/deliverables/COMM/link-budget.md
- examples/ksat5/deliverables/COMM/transceiver-em.md
- examples/ksat5/deliverables/COMM/antenna-design.md
- examples/ksat5/deliverables/COMM/bus-voltage-check.md
- examples/ksat5/deliverables/COMM/icd-str-comm-footprint.md
- examples/ksat5/deliverables/COMM/icd-eps-comm-power.md

검증: 위 표의 4개 판정 항목 중 3개(링크버짓·5V레일·안테나 포락선)는
COMM-05 통합점검에서 통과 확인, 질량은 배분 한도 내이나 여유 0으로
조건부 통과. 미해결 리스크 3건은 §"인도 시점 잔여 리스크"에 명시해
AIT로 이월.
