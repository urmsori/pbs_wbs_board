입력: examples/ksat7/deliverables/PROP/unit1-ins.md, examples/ksat7/deliverables/CAL/prop-u1-calibration.md,
examples/ksat7/deliverables/FAC/prop-u1-facility.md, examples/ksat7/deliverables/PROP/unit1-review-board.md,
examples/ksat7/deliverables/SE/sysreq.md

# PROP-U1 점화·누설시험

sysreq 판정: Δv25m/s, 홀추력기300W급.

## 누설시험 (점화 전)
- 배관계 전 용접부·플랜지 헬륨리크시험: 최대검출 <5e-9 atm·cc/s(합격기준
  1e-8 이내), 24시간 압력유지 압력강하 <0.3%(합격).

## 점화시험 (진공챔버, 추력측정대)
- 정격점 300W(300V/1.0A) 점화 성공, 실측 추력 19.8mN, 비추력(Isp) 1,485s
  (설계가정 1,500s 대비 -1%, 오차범위 내).
- 점화 안정성: 10회 점화-정지 사이클 전부 정상, 램프업 2.8s·램프다운 3.1s
  (설계가정 3s와 정합).

## Δv 재검증
- 실측 Isp 1,485s로 재계산: 충전량 1.0kg 기준 mp 전량 소모 시 Δv ≈
  1,485×9.80665×ln(280/279.0) ≈ 25.9m/s(sysreq 25m/s 대비 여유 0.9m/s, 3.6%).
  CHK 권고치(충전1.0kg)가 실측 Isp 반영 후에도 sysreq 충족.

## 판정
Δv 실측기준 25.9m/s≥25m/s(sysreq, 여유3.6%), 300W/300V/1.0A 점화 정상,
누설 전 항목 합격.

검증: 실측Isp1,485s 기준 Δv25.9m/s≥25m/s(여유3.6%), 300W점화 10사이클 정상,
누설<5e-9(합격)
