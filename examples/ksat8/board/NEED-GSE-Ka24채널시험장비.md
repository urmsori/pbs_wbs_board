---
id: NEED-GSE-Ka24채널시험장비
title: Ka 24채널 동시 페이로드 시험 장비(INT-TST-3 RF 종단간용)
status: DONE
parent: INT
source: AIT-RX-4
owner: GSE-03
deliverable: examples/ksat8/deliverables/GSE/scoe-ka24ch-reply.md
after: -
track: GSE
started: 2026-08-27 04:33:15
finished: 2026-08-27 04:33:15
---

왜: INT-TST-3(RF 종단간: TT&C+Ka 24채널 EIRP/NPR)은 위성 전체 형상
(도파관·하니스로 실제 연결된 PAY-HAR-안테나 체인)에서 TT&C S-band와
Ka 24채널을 **동시에** 종단간 검증해야 한다. GS module-fm.md의 IOT
계획(D6-D21 Ka 24채널 전수측정)과도 정합해야 하므로 지상 시험 단계에서
24채널을 동시에 구동·측정할 수 있는 장비가 필요하다.

## 재사용 판단
PAY module-fm.md·CAL/pay-u1-cal.md·FAC/pay-u1-fac.md 확인 결과, 컴팩트
레인지 RF 챔버 #1과 근접전계 안테나측정계·노이즈로딩 장비가 PAY-U1-TST
(패널 단품 baseline 확정, EIRP 52.43dBW/NPR 19.5dB)에 이미 쓰였다.
그러나 이는 **PAY 패널을 챔버에 단독 거치해 베이스라인을 확정한
모듈 단위 시험**이고, INT-TST-3은 **위성 통합형상(HAR 도파관·안테나
체결 후) 상태에서 24채널 동시 구동**이 필요해 근접전계 스캐너 1식으로는
동시성 요구를 충족하기 어렵다. 노이즈로딩 시험장비(NPR)는 대표채널
측정에 **재사용 가능**하다고 판단한다. 신규로 필요한 것은 24채널
동시 신호원/전력분배·다채널 동시 EIRP 측정이 가능한 확장 장비다.

요청: Ka 24채널 동시 구동 가능한 신호원/전력분배기+다채널 EIRP 측정
장비 가용 여부(컴팩트레인지 챔버 #1과 연동 가능 여부 포함). 신규 조달
시 필요 사양·소요 기간.
회신 산출물 제안: examples/ksat8/deliverables/GSE/scoe-ka24ch-reply.md
검증: Ka24채널 신호원/전력분배+동시측정 구성 완료, 채널간편차<0.3dB 합격
