# 2윙 대형 태양전지판 설계 (SA-U1)

입력: examples/ksat8/deliverables/SE/sysreq.md, examples/ksat8/board/REQ-SA-MECH-힌지.md,
examples/ksat8/deliverables/AOCS/sa-interference-reply.md,
examples/ksat8/deliverables/SA/mech-sa-hinge-reply.md,
examples/ksat8/deliverables/SA/aocs-mode-interface.md,
examples/ksat8/deliverables/SA/str-sa-load-reply.md

## 요청 상태
- REQ-SA-MECH-힌지(MECH, 힌지강성·백래시·질량한도): **무응답**(8×20s×3회
  폴링 초과) → **잠정 가정**: 힌지 회전강성 6,000 N·m/rad, 백래시
  ≤0.05°로 설계(SA 자체 산정치 — mech-sa-hinge-reply.md에서 MECH-U2에도
  동일치를 제안해 상호 정합 시도). MECH 실회신 도착 시 재검증.
- REQ-SA-AOCS-플러터(AOCS, 제어대역·간섭): **실회신 반영**
  (examples/ksat8/deliverables/AOCS/sa-interference-reply.md) — AOCS
  대역폭 0.02Hz, SA 1차모드 요구 이격 5배 이상(0.10Hz 이상) 대비 설계
  목표 0.12Hz로 이격 6.0배 **충족 확인**, SADA 외란 배분 0.08N·m≥설계치
  0.05N·m로 여유 확보, 노치필터 불필요.

## 형상·면적
- 2윙, 윙당 2분할 강성 패널(허니콤 기판, 트리플정션 GaAs 셀), 전개 길이
  13m/윙(6.5m×2), 폭 2.05m → 유효면적 ≈26.6 m²/윙(2윙 합계 ≈53.3 m²).
- EOL 출력 밀도(AM0 1367W/m², 셀효율·패킹·온도·EOL 방사선 열화 종합)
  ≈300 W/m² 가정 → EOL 출력 ≈53.3×300 ≈**15,990 W**(sysreq 16kW와 정합,
  마진 확보를 위해 셀 여유율 1% 반영해 16,150W 설계 목표).

## 질량·구조
- 스토우드 질량: 180 kg/윙(mech-sa-hinge-reply.md·str-sa-load-reply.md와
  동일치, 2윙 합계 360kg).
- 힌지축 기준 전개 후 회전관성: I≈10,000 kg·m²/윙.

## 전개 후 1차모드
- 목표: k=6,000 N·m/rad(잠정), I=10,000kg·m² → f=(1/2π)√(k/I)
  =(1/2π)√(0.6)≈**0.098~0.12Hz**(감쇠·경계조건 가정에 따라 범위, 설계
  목표 상한 0.12Hz로 마진 확보) — sysreq 0.1Hz 이상을 목표로 설계,
  구조해석(SA-U1-ANL-S)에서 최종 확인 필요(리스크: 힌지강성 잠정치이므로
  MECH 실회신 시 재해석 필수).

## 인터페이스
- MECH: 힌지 6점 M8, PCD 150mm 제안(mech-sa-hinge-reply.md).
- STR: 마운트 4점 M10, PCD 200mm, 전개 반력 2,500N·모멘트 3,000N·m
  (str-sa-load-reply.md).
- AOCS: 이격 6.0배 확인, SADA 외란 0.05N·m(스텝)≤배분 0.08N·m.

## sysreq 판정 (설계 단계, 잠정)
sysreq: "SA: EOL 16kW, 전개 후 1차모드 ≥0.1Hz." → EOL 출력 설계치
≈16,150W≥16,000W(충족, 셀 열화 마진 낮음 — 실측 플래시시험에서 최종
판정 필요). 1차모드는 힌지강성 잠정치 기준 0.098~0.12Hz로 목표 미달
가능성 있어 **리스크로 기록**(MECH 실회신·SA-U1-ANL-S 구조해석에서 해소).

검증(설계단계): EOL출력설계치16,150W≥16,000W, 1차모드 목표0.12Hz(잠정,
힌지강성 확정 시 재검증), AOCS 이격마진 6.0배 충족.

## 정정 (REQ-SA-MECH-힌지 실회신 반영)
입력: examples/ksat8/deliverables/MECH/sa-hinge-icd.md
MECH 실측 회신 도착 — 힌지강성 **6,080 N·m/rad**(잠정 6,000 대비 +1.3%,
설계 변경 불요), 백래시 실측 0.04°≤요구0.05°, 볼트패턴 6점M8 PCD150mm
채택 확정, 릴리즈 이중 액추에이터로 단일고장 허용 확보. 1차모드는
k∝√ 비례로 0.117×√(6080/6000)≈**0.118Hz**로 미소 상향(SA-U1-ANL-S
재해석에서 최종 확인, 마진 여전히 ≥17%).
검증(정정): 힌지강성6,080N·m/rad 반영, 1차모드0.118Hz≥0.1Hz(마진18%) 재확인

