# 지상국·운용(GS) 비행모델 인도
입력: examples/ksat6/deliverables/GS/station-compatibility.md, examples/ksat6/deliverables/GS/ops-procedures.md, examples/ksat6/deliverables/GS/initial-ops-30day.md, examples/ksat6/deliverables/COMM/link-budget.md

## sysreq.md 판정 (GS 자기 항목)
> GS: 2개소 적합성, 초기운용 30일 계획, 비상 절차.

| 항목 | 요구 | 결과 | 판정 |
|---|---|---|---|
| 2개소 적합성 | 2개소가 COMM 요구(S/X-band EIRP·G/T) 충족 | GS-1·GS-2 모두 스펙상 요구 상회(각 +0.5~1dB) 확인, 5종 시험항목 정의 | **충족** (단, 원 링크의 S-band 하향 저마진은 지상국 여유로도 완전 해소되지 않음 — 아래 참조) |
| 초기운용 30일 계획 | D+0~D+30 일별 활동·성공기준 | initial-ops-30day.md 5구간 계획 | **충족** |
| 비상 절차 | 통신두절 등 비상 대응 | ops-procedures.md 비상절차 4종 | **충족** |

## 구성
1. 지상국 적합성 계획·시험(station-compatibility.md) — GS-1/GS-2 스펙·시험 5항목.
2. 운용 절차서(ops-procedures.md) — 정상 패스 5단계, 비상 4종.
3. 초기운용 30일 계획(initial-ops-30day.md) — D+0~D+30 5구간.

## COMM 링크 마진 이월 기록 (정직 기록)
- COMM 링크버짓(link-budget.md)·RF통합시험 실측 결과 S-band 하향 마진이
  **+0.94dB로 1dB 미만**임을 그대로 이어받아, 운용 절차에 앙각 15° 이상만
  신뢰 수신하도록 반영했다(ops-procedures.md 3항). 지상국 스펙 여유(+0.5dB)를
  더해도 완전히 해소되지 않는 구조적 마진 부족이며, 초기운용 D+2~D+7 구간에서
  실측 CRC 오류율로 재확인하도록 계획에 반영했다(initial-ops-30day.md).
- X-band 하향은 마진 +5.96dB로 양호, 2개소 모두 150Mbps 처리량 시험 통과 가능.

## 발행/수신 REQ 요약
- GS가 별도로 발행한 타 트랙 REQ는 없다(입력이 모두 COMM 자체 산출물이므로
  같은 인도 내 순서 종속(after)만으로 충분 — 규칙 4절: 필요 없는 REQ를
  만들지 않음).
- 수신 REQ 없음(타 트랙이 GS 트랙에 요청한 건 없음, 최종 폴링 6회 확인).

검증: 3개 항목이 sysreq.md 자기 항목을 인용해 판정되었고, COMM에서 이월된
마진 부족(S-band 하향)을 숨기지 않고 운용절차·초기운용계획에 반영했음을 확인.
