# PROP 추진 비행모델 인도
입력: examples/ksat6/deliverables/PROP/propellant-budget.md, examples/ksat6/deliverables/PROP/tank-acceptance.md, examples/ksat6/deliverables/PROP/thruster-acceptance.md, examples/ksat6/deliverables/PROP/piping-assembly.md, examples/ksat6/deliverables/PROP/leak-test.md, examples/ksat6/deliverables/STR/interface-prop.md

## 구성
단일추진제(하이드라진) 시스템: 탱크 1기(수락 완료) + 래치밸브 2 + 스러스터
4기(수락 완료, 대각 배치 2조) + 배관(수락된 부품으로 조립 완료) + 압력변환기.
탱크 장착점·배관 경로는 STR 확정 좌표(interface-prop.md)로 최종 반영.

## sysreq.md PROP 행 수치 판정
| 항목 | sysreq 요구 | 실측/산출 | 판정 |
|---|---|---|---|
| Δv | 15 m/s(3년) | 추진제 탑재 1.8kg (소요 0.89kg, 마진 100%) | 충족 |
| 배관 누설 | ≤1×10⁻⁶ scc/s | 전체 계통 24h 압력강하법 9.2×10⁻⁷ scc/s | 충족(마진 8%) |

## 인터페이스 이행 기록
- REQ-PROP-STR(STR): DONE — 장착점·배관 경로 볼륨 STR 확정, 요청 조건
  (클리어런스30mm·곡률반경25mm) 충족 확인.
- REQ-PROP-FSW(FSW): DONE — 밸브 구동·잠금 로직(이중코일 펄스구동 50ms·안전모드
  인터록·연속구동시간 제한·위치 텔레메트리) 4개 요구항목을 FSW가 1:1 반영 확인
  (examples/ksat6/deliverables/FSW/reply-prop-valve-logic.md).

검증: sysreq.md PROP 행(Δv 15m/s, 누설 1e-6 scc/s 이하) 전 항목 실측 충족.
STR·FSW 인터페이스 모두 상대 팀 확인 완료.
