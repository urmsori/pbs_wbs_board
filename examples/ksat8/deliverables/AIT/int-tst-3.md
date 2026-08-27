# INT-TST-3 통합시험3 — RF 종단간(TT&C + Ka 24채널 EIRP/NPR)

입력: examples/ksat8/deliverables/AIT/rx-3.md, examples/ksat8/deliverables/AIT/rx-4.md,
examples/ksat8/deliverables/AIT/int-tst-1.md,
examples/ksat8/deliverables/GSE/scoe-ka24ch-reply.md,
examples/ksat8/deliverables/COMM/module-fm.md, examples/ksat8/deliverables/PAY/module-fm.md,
examples/ksat8/deliverables/GS/module-fm.md

## 시험 구성
INT-TST-1에서 확정된 통합 형상(HAR-PAY 도파관 어댑터 조치 완료, 총손실
0.62dB)으로 컴팩트레인지 챔버 #1 + GSE Ka 24채널 신호원/전력분배·동시
측정 장비(scoe-ka24ch-reply.md)를 사용해 RF 종단간 시험을 수행한다.

## 1) TT&C S-band 종단간
COMM module-fm.md 확정치(상향2087.5MHz/하향2255.5MHz, 안테나 배치
±90°무차폐) 그대로 통합 형상에서 재확인:
- 하향 EIRP 실측 **4.78dBW**(목표5.0dBW 대비-0.22dB, 모듈시험4.8dBW와
  0.02dB 이내 일치) — **PASS**
- 레인징 턴어라운드비 240/221 정합 재확인 — **PASS**

## 2) Ka 24채널 EIRP/NPR 종단간
- 24채널 동시 구동, EIRP 실측 **52.01~52.57dBW**(모듈시험
  52.05~52.61dBW 대비 전 채널 균일하게 -0.04dB — INT-TST-1 어댑터
  삽입손실과 정합) — 요구 ≥52dBW 대비 전 채널 **PASS**(최소마진
  0.01dB, 채널1 한정 마진 타이트 — 궤도상 열화 여유 관찰 권고로 GS
  운용 단계 이관)
- 대표 4채널 NPR 실측 **18.6~19.2dB**(모듈시험 18.7~19.3dB 대비
  -0.1dB, 어댑터 반사손실 영향 미미) — 요구≥18dB 대비 **PASS**

## GS IOT 계획과의 정합
GS module-fm.md의 IOT 30일 계획(D6-D21 Ka 24채널 전수측정, 목표
52dBW±0.5dB) 입력값을 본 시험의 통합 형상 실측치(52.01~52.57dBW)로
갱신 필요 — GS 트랙 자체 정정 게시글 대상으로 기록만 남긴다(본 Work가
GS 문서를 직접 수정하지 않음).

## GS Ka IOT 시험국 이월 항목과의 관계
본 시험은 지상 AIT용 GSE 장비(scoe-ka24ch-reply.md, 컴팩트레인지 챔버
#1)로 수행하는 **지상 통합시험**이며, GS module-fm.md가 언급한 "Ka IOT
시험국"은 **발사 후 궤도상시험(IOT) 운용 단계**의 별도 지상국이다. 두
설비는 별개이므로 INT-TST-3은 Ka 시험국 확보 여부와 무관하게 완결
된다. REQ-AIT-GS-Ka시험국은 계속 OPEN 상태로 두고 운용 단계(GS IOT
착수 전) 전제조건으로 명시 이관한다(module-fm.md의 이관 지시와 일치).

검증: TT&C 하향EIRP4.78dBW(모듈치와 0.02dB이내 일치)·Ka24채널EIRP
52.01~52.57≥52dBW 전채널PASS·NPR18.6~19.2≥18dB PASS — 어댑터 삽입손실
반영해도 sysreq COMM·PAY 항목 전량 통합형상에서 재충족
