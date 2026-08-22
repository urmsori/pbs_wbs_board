# PAY 비행모델(FM) 인도 — 취합
입력: examples/ksat6/deliverables/PAY/telescope-optics.md, focal-plane-tdi.md, payload-electronics.md, optical-performance-test.md, str-interface-reply.md, eps-imaging-power-reply.md, tcs-thermal-confirm.md, obc-datarate-reply.md, examples/ksat6/deliverables/TCS/pay-thermal-confirmation.md, examples/ksat6/deliverables/OBC/reply-pay-storage-bandwidth.md

## 구성
망원경 광학계(구경300mm, f/7.8), TDI 초점면(32단, 10µm 픽셀), 탑재
전자부(비균일보정+2:1압축), 통합 성능시험 결과.

## sysreq 판정 (자기 항목)
| sysreq 항목 | 요구 | 실측/확정 | 판정 |
|---|---|---|---|
| 구경 | 300mm | 300mm(설계) | PASS |
| 초점면 | TDI | 32단 TDI, 라인율2,500/s | PASS |
| 기내 보정 | 요구 | FPN 2.1%→0.3%(optical-performance-test.md) | PASS |
| (참고) MTF/왜곡 | - | MTF 0.21~0.24, 왜곡0.07% | PASS |

## 완료된 인터페이스 협상 (ICD)
- REQ-PAY-TCS ↔ TCS: 초점면 안정도 ±0.5°C 요청 → TVAC 실측 구배1.6°C·
  히터21.7W로 달성 확인(pay-thermal-confirmation.md).
- REQ-PAY-OBC ↔ OBC: 데이터율100~115Mbps·SpW2링크·버퍼30GB 요청 → SpW
  200Mbps 여유·118GB 버퍼로 충족(reply-pay-storage-bandwidth.md).
- REQ-STR-PAY(수신) ↔ STR: 질량35kg·3점킨네마틱·각변위≤0.01° 회신 — 완료.
- REQ-EPS-PAY(수신) ↔ EPS: 촬영전력(첨두55W/평균35W/12분) 회신 — 완료.
- REQ-TCS-PAY(수신) ↔ TCS: ±0.5°C·구배≤2°C 수용 확인 — 완료.
- REQ-OBC-PAY(수신) ↔ OBC: 데이터율·SpW링크 회신 — 완료.

## 잠정 가정
EPS-01의 평균전력 가정(궤도전체 평균 20W)과 PAY 회신(촬영중 평균 35W)이
정의 기준(궤도평균 vs 촬영구간평균) 차이로 수치가 다르다 — eps-imaging-power-reply.md에서
정의 재확인을 요청했으나 폴링 종료 시점까지 EPS 측 재회신 없음. 잠정적으로
PAY 수치(촬영구간 평균 35W, 첨두55W, 듀티12%)를 정본으로 채택하고, EPS
전력예산 취합 시 궤도평균 환산(35W×12%+8W×88%≈11.2W)을 참고치로 병기한다.

검증: optical-performance-test.md MTF 0.21~0.24 ≥0.20, 왜곡0.07% ≤0.1% —
sysreq PAY 3항목(구경300mm·TDI·기내보정) 모두 PASS. 전 유닛(4건) DONE,
송신 REQ 2건·수신 REQ 4건 모두 회신 완료(1건 정의차 잠정가정 병기).
