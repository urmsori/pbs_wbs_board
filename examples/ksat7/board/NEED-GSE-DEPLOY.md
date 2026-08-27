---
id: NEED-GSE-DEPLOY
title: SAR 2단+SA 3윙 통합형상 동시 중력보상 설비
status: OPEN
parent: INT
source: AIT-RX-1
track: GSE
owner: -
deliverable: -
after: -
started: -
finished: -
---

MECH-U1(SAR 2단 전개기구, 안테나 실측72.0kg)과 MECH-U2(SA 힌지×3윙, 패널7.6kg/윙)의 전개
시험은 각각 유닛 단독 형상(FAC-MECH 단독 예약)으로만 수행됐다. INT-TST-1(rev.2 실측 재확인)
단계에서 위성 통합 형상 전체(SAR 안테나 2단 붐 완전전개 + SA 3윙 동시전개)를 지지할 수
있는 중력보상(지상 1g 환경에서 궤도상 0g 전개거동 모사) 설비가 필요하다. 두 기구가 근접
배치되어 전개 간섭(clearance) 확인도 함께 요구된다.

요구 사양(안):
- 지지용량: 안테나측 72.0kg(2단 붐 최대 전개 반경 기준 모멘트 포함) + SA 3윙 합계 22.8kg
  (7.6kg×3, 윙별 독립 오프로드)
- 오프로드 포인트: 최소 4점(안테나 2단 각 1점 이상) + SA 힌지별 오프로드 트롤리 3식
- 전개 중 실시간 위치 트래킹(간섭 확인용, 두 기구 최소 이격거리 기록)

재사용 불가 판단 근거: 기존 유닛레벨 오프로드 지그는 각 기구 단독 질량·리치 기준으로
설계되어, 통합형상 전체를 동시 지지할 지지점 수·용량이 부족하다고 판단(개별 기구 지그의
합산이 아니라 통합형상 전용 지그 설계 필요).

산출물 제안: examples/ksat7/deliverables/GSE/deploy-offload-confirmation.md
검증: 요청 사양 대비 확보 설비(지지용량·오프로드포인트수) 회신
