# 수령검사 — RF·탑재·운용(COMM/GS/AOCS/PAY)
입력: examples/ksat6/deliverables/COMM/module-fm.md, examples/ksat6/deliverables/GS/module-fm.md, examples/ksat6/deliverables/AOCS/module-fm.md, examples/ksat6/deliverables/PAY/module-fm.md

## 수령 확인
| 모듈 | 핵심 수치(인도 문서 인용) | 수령 판정 |
|---|---|---|
| COMM | S-band하향마진+0.94dB(<1dB, 빠듯), X-band마진+5.96dB, 버퍼여유6.7% | 수령, 마진 2건 정직 기록됨 |
| GS | GS-1/GS-2 스펙상회, S-band 저마진 앙각≥15° 운용절차 반영 | 수령, COMM 마진 이관 확인 |
| AOCS | 지향정확도0.034°(≤0.05°), 지향안정도0.0028°/s(≤0.005°/s) | 이상 없음 |
| PAY | 구경300mm·MTF0.21~0.24·왜곡0.07%, 질량35kg, EPS 평균전력 정의차 잠정 | 수령, 정의차 1건 미결 인지 |

## 통합시험 필요 장비 판단(근거 기반)

1. **AOCS-COMM 연동 시험 장비 — 필요, NEED 발행**
   COMM module-fm.md의 안테나 사양은 X-band 1기, **빔폭 ±11°**로
   좁다(150Mbps 다운링크). AOCS module-fm.md의 지향정확도 0.034°는
   빔폭 대비 충분한 여유가 있으나, 이는 정적 지향 성능일 뿐 실제
   다운링크 패스 중 자세기동(궤도상 지향 갱신)이 X-band 빔 지향에
   미치는 영향은 모듈 단위 시험(COMM RF통합시험, AOCS HIL시험)
   어디에서도 결합 검증되지 않았다 — AOCS 자세기동과 COMM RF 링크를
   동시에 구동·계측할 수 있는 연동 시험 장비(회전 포지셔너 + RF
   링크 모니터, AOCS 명령 인터페이스 연동)가 시스템 통합시험에
   새로 필요하다. → NEED-자세연동RF시험장비 발행(source: AIT-RX-4).

2. **S-band 감쇠 교정 장비 — 필요, NEED 발행**
   COMM module-fm.md가 S-band 하향 마진을 **+0.94dB(1dB 미만)**로
   정직하게 기록했고, GS module-fm.md도 이 저마진이 지상국 스펙
   여유(+0.5dB)를 더해도 완전히 해소되지 않는다고 명시했다. 이렇게
   빠듯한 마진은 시스템 레벨 종단간 시험(INT-TST-3)에서 교정
   추적성이 있는 감쇠기·전력계로 재확인해야 신뢰할 수 있다 — 모듈
   단계 RF통합시험 장비만으로는 0.1dB 단위 교정 이력이 확인되지
   않는다. → NEED-S밴드감쇠교정장비 발행(source: AIT-RX-4).

3. **EPS-PAY 평균전력 정의 차이** — 장비 필요 아님. PAY module-fm.md의
   "잠정 가정"(궤도평균 20W vs 촬영구간평균 35W)은 계측기·치구가
   아니라 정의·판정 기준의 문제이므로 INT-TST-2(전기 통합·전력)에서
   시스템 레벨 실측으로 직접 닫는다(4단계 참조). NEED 미발행.

## 재사용 판단
- PAY 리프팅·정렬 치구는 AIT-RX-1(STR 수령)에서 이미 NEED로 발행
  판단했으므로 여기서 중복 발행하지 않는다(같은 필요, 다른 관점에서
  재확인만 함 — STR 인터페이스 회신과 PAY 자체 질량 35kg이 일치).
- GS 지상국 장비 자체는 AIT 통합시험 범위 밖(원격지 시설)이므로
  NEED 대상 아님 — GS는 이미 자체 스펙으로 적합성 확인 완료.
- AOCS HIL 시험 장비(hil-test.md 사용)는 AOCS 자체 폐루프 시뮬레이터이며
  시스템 레벨에서는 실제 반작용휠·마그네토커가 장착되므로 재사용 불가 —
  INT-TST-1에서 실기 정렬 확인으로 대체(추가 장비 불필요, 광학 정렬
  장비로 충분).

검증: COMM·GS·AOCS·PAY module-fm.md의 판정표를 각 1개씩 인용해 수령
수치 일치 확인, AOCS-COMM 연동 장비·S밴드 감쇠교정장비 2건의 필요를
module-fm.md 원문(빔폭±11°, 마진+0.94dB) 근거로 판단해 NEED 발행,
EPS-PAY 정의차는 장비 아님을 판별해 INT-TST-2로 이관.
