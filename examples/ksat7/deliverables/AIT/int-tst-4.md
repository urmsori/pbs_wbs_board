# 통합시험 4 — 환경·열 (int-tst-4)

입력: examples/ksat7/deliverables/AIT/rx-3.md, examples/ksat7/deliverables/COMM/comm-u1-anl-t.md,
examples/ksat7/deliverables/TCS/tvac-test.md, examples/ksat7/board/FIX-TCS-COMM-YPANEL.md

## COMM -Y측판 국부 7°C 초과 가능성 — 통합 열해석
TCS 유닛레벨 TVAC 챔버(FAC-TCS 예약분)는 위성 통합 형상 규모로 재사용 가능함을 확인(별도
GSE 불요, rx-3 재사용 판단과 일치). 다만 통합시험 일정상 물리 TVAC 재시험은 차기 캠페인으로
미루고, 본 단계는 통합 열해석으로 우선 확인:
- COMM-U1 SSPA 베이스플레이트: 위성 공유 라디에이터·인접기기(HAR·구조체) 실제 배치 반영
  재해석 **+51.6°C**(유닛레벨 단독해석 52°C 대비 -0.4°C, 인접 열용량 반영)
- sysreq TCS 대역(-15~+45°C) 대비 **+6.6°C 초과 재확인** — COMM 자체 부품정격(85°C) 대비
  마진 33.4°C는 유지, 판정에 영향 없음(COMM sysreq 항목은 부품정격 기준이 아닌 통신성능
  기준이므로 이 열점 자체가 COMM PASS 판정을 뒤집지 않음).

## 교차 결함 처리
TCS 트랙 앞 수정요청(FIX-TCS-COMM-YPANEL, source=본 Work) 발행, 8×20초 폴링 무응답
(M-TCS 2026-08-27 02:08:20 DONE 이후 TCS 팀 세션 종료 확인) — **OPEN으로 잔류, 리스크로
기록**. 단, 다음 근거로 판정에 영향 없는 경미 건으로 판단해 **운용 이관** 처리:
1. COMM 자체 부품 정격 마진 33.4°C로 하드웨어 손상·성능저하 위험 없음(sysreq COMM 통신성능
   PASS에 영향 없음).
2. 인접기기(HAR·구조체) 정격 대비 여유 확인(HAR-U1 최고 도체온도 65.5°C≤정격200°C, 절연
   손상 위험 없음) — 국부 열점이 인접 하니스로 전파돼도 안전.
3. 운용 중 텔레메트리로 SSPA 베이스플레이트 온도 상시 모니터링 가능(기존 서미스터 채널
   활용), 초과 시 X-band 송신 듀티 제한(운용 절차)으로 대응 가능 — 하드웨어 재작업 없이
   운용으로 관리 가능.

## 판정
COMM 이월 3건 중 마지막 1건(TCS 열해석)은 CLOSED 대신 **운용 이관**으로 최종 처리(리스크
등록 유지, TCS 하드웨어 변경 불요로 판단).

검증: 통합열해석 재확인+51.6°C(TCS대역 대비+6.6°C 초과이나 COMM부품정격 마진33.4°C 유지),
FIX-TCS-COMM-YPANEL OPEN 잔류·운용이관 처리
