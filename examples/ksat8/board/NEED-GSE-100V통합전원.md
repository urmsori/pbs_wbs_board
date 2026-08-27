---
id: NEED-GSE-100V통합전원
title: 100V 고전압 통합 전원 SCOE(INT-TST-2 15kW 통합부하시험용)
status: DONE
parent: INT
source: AIT-RX-2
owner: GSE-03
deliverable: examples/ksat8/deliverables/GSE/scoe-100v-reply.md
after: -
track: GSE
started: 2026-08-27 04:33:15
finished: 2026-08-27 04:33:15
---

왜: INT-TST-2(전기 100V·15kW 통합 부하시험)는 EPS 비행모델(PCU·배터리)에
PAY·PROP-EP·COMM·TCS 히터 부하를 동시에 물려 15kW급 통합 부하 프로파일
(PAY11,000+EP3,000+COMM220+히터200+HK, EPS module-fm.md 인용)을 실물로
인가·모니터링해야 한다. 위성 전체를 그라운드에서 급전·감시하려면 100V
고전압 인터페이스(제한전류·접지분리·비상차단 인터록 포함)를 갖춘 통합
전원 SCOE가 필요하다.

## 재사용 판단
EPS module-fm.md·CAL/eps-u1-cal.md·FAC/eps-u1-fac.md 확인 결과, 전기시험실
#1에 "15kW 부하뱅크"와 교정된 전자부하·DAQ가 상설돼 있다. 그러나 이는
**PCU를 전원(소스)으로 보고 전자부하로 흡수시키는 모듈 단위 부하시험
장비**이며, INT-TST-2는 반대로 **여러 비행 서브시스템(실부하)을 동시에
100V 버스에 물리는 통합 급전·감시 SCOE**가 필요해 용도가 다르다.
기존 DAQ(0.08%FS, 100kS/s, 12.8A/10ms 과도파형 포착 가능)는 통합시험
계측으로 **재사용 가능**하다고 판단해 신규 요청 범위에서 제외한다.
신규로 필요한 것은 고전압 통합 급전 인터페이스·인터록·다채널 전류
분기 모니터링 하드웨어다.

요청: 100V/15kW급 통합 전원 SCOE(비상차단 인터록, 채널별 전류 분기
모니터링 8채널 이상 — PAY/EP/COMM/히터/HK) 가용 여부. 신규 조달 시
필요 사양·조달 기간.
회신 산출물 제안: examples/ksat8/deliverables/GSE/scoe-100v-reply.md
검증: 100V/15kW SCOE 구성·교정 완료, 인터록<10ms·접지분리>100MΩ 합격
