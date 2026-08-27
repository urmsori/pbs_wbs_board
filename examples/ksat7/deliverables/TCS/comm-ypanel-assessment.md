입력: examples/ksat7/board/FIX-TCS-COMM-YPANEL.md, examples/ksat7/deliverables/AIT/int-tst-4.md,
examples/ksat7/deliverables/COMM/comm-u1-anl-t.md, examples/ksat7/deliverables/TCS/unit1-thermal-design.md,
examples/ksat7/deliverables/TCS/tvac-test.md, examples/ksat7/deliverables/SE/sysreq.md

# COMM -Y측판 국부 열점 — TCS 통합열모델 재평가 회신 (FIX-TCS-COMM-YPANEL)

## 재확인 수치
- 통합 열해석(int-tst-4): COMM-U1 SSPA 베이스플레이트 +51.6°C(-Y측판, 위성
  공유 라디에이터·인접기기 실배치 반영).
- sysreq TCS 대역(-15~+45°C)은 문면상 **SAR 송수신기** 기준(sysreq.md "TCS:
  SAR 송수신기 첨두 열부하 관리(-15~+45°C)")이며, TCS-U1 히트파이프4식·
  라디에이터0.35㎡는 REQ-TCS-PAY 회신치(270W×5s×18회/궤도, T/R모듈
  베이스플레이트 0.30㎡)를 입력으로 그 SAR T/R모듈 전용 경로로 설계·TVAC
  실측 검증됐다(tvac-test.md, 고온+43.5°C≤+45°C). COMM-U1 SSPA는 이
  TCS-U1 전용 열수송 경로에 포함되지 않는 별도 발열원 — -Y측판 국부값은
  TCS-U1 자체 설계 판정 범위(SAR 경로) 밖의 인접 열점이다.
- COMM 부품 자체 정격(85°C) 마진 33.4°C 유지(int-tst-4 확인), HAR 인접 도체
  65.5°C≤정격200°C 여유 확인 — 하드웨어 손상·성능저하 경로 없음.

## 판단 1: 하드웨어 조치 필요 여부
**불필요.** 근거:
1. 열점이 TCS-U1의 SAR 전용 히트파이프/라디에이터 설계 범위(sysreq TCS 대역
   적용 대상) 밖의 COMM 부품이며, 그 부품 자체 정격 마진(33.4°C)이 충분하다.
2. TCS-U1 자체 하드웨어(히트파이프4식·라디에이터0.35㎡·MLI·히터3채널)는
   이미 TVAC 4사이클 실측으로 sysreq 전항목 충족이 확정된 형상(RB 승인·CM
   배포 완료)이며, -Y측판 국부값 해소를 위해 이 형상을 재설계하면 이미
   검증된 열마진(고온 여유1.5°C)을 흔들 위험이 있고 실이득이 없다.
3. MLI 개구부·히트파이프 라우팅 변경은 인접 COMM 발열원의 근본 원인(SSPA
   Tx 듀티)을 줄이지 못해 국부값을 부분적으로만 낮추며, 하드웨어 재작업
   비용·일정 대비 COMM 판정에 영향이 없다(int-tst-4: "COMM sysreq 항목은
   부품정격 기준"이라 통신성능 PASS 불변).

## 판단 2: AIT 운용 이관(텔레메트리 감시+송신 듀티 제한) 타당성
**타당하다고 판단, 승인.** 근거: 원인이 COMM SSPA 자체 Tx 듀티에 있으므로
운용 절차(듀티 제한)로 직접 제어 가능하고, 기존 서미스터 채널로 상시 감시가
가능해 하드웨어 변경 없이 재현 가능한 통제 수단이다. TCS-U1 하드웨어는
변경 불요.

## 추가 권고
1. 운용 절차서에 SSPA 베이스플레이트 임계치 이단(경보 +48°C / 듀티제한 액션
   +50°C)를 명시해 33.4°C 마진 내에서도 조기 개입 기준을 두도록 COMM·FSW
   팀에 권고.
2. 리스크 등록부 유지(운용 이관, CLOSED 아님) — 차기 설계 블록에서 -Y측판
   공유 라디에이터 구간의 국부 방열 여유(개구부 배치)를 COMM과 공동
   재검토할 것을 장기 권고 항목으로 남긴다(현 FM 형상 변경 불요와는 별개).
3. TCS-U1 자체 sysreq 판정(고온+43.5°C·저온-13.8°C·배터리+7.5~9.2°C·
   히터38.6W)은 본 검토로 영향받지 않음 — module-fm.md 판정 유지.

검증: 통합열해석+51.6°C(COMM부품, TCS-U1 SAR전용경로 밖)·부품마진33.4°C 재확인,
TCS-U1 하드웨어 조치 불요·AIT 운용이관(감시+듀티제한) 타당 승인
