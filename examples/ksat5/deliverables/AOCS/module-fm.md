# 자세제어(AOCS) FM 모듈 인도 문서
입력: examples/ksat5/deliverables/AOCS/design-update-fm.md,
      examples/ksat5/deliverables/AOCS/fabrication-record-fm.md,
      examples/ksat5/deliverables/AOCS/calibration-report-fm.md,
      examples/ksat5/deliverables/AOCS/acceptance-test-fm.md

SE-01(M2-AOCS)의 "EM 결과·승계 리스크를 반영한 자세제어 FM 모듈 인도"
요청에 대한 AOCS 팀의 인도물.

## 1. EM 대비 변경 사항
- EKF/PD 게인 미세조정으로 지향오차 여유 확대(design-update-fm.md)
- RISK-RAIL(공유 액추에이터 레일 동시부하) 대응: 확보 슬루 guard band를
  SW 강제 조건화(여유<5s 시 슬루 자동 취소·이월) — acceptance-test-fm.md에서
  정상 동작 확인

## 2. 제작·교정
- 비행품 전 품목 제작 완료, 총질량 1.998 kg (배분 2.000 kg 이내,
  fabrication-record-fm.md)
- 스타트래커 광축 정렬 잔차 0.008°(설계 공차 0.015° 이내), 전 구성품
  교정 완료(calibration-report-fm.md)

## 3. 수락시험 결과
종합 지향오차 0.45°(SYS-REQ 요구 ≤0.5° 충족, EM 0.47° 대비 개선),
guard band 강제 로직으로 RISK-RAIL 최악조건(동시부하 ≈2.08A) 발생을
SW 레벨에서 차단함을 확인(acceptance-test-fm.md).

## 4. 인도 판정
질량·전력·지향정확도 요구를 모두 충족하고, EM에서 승계한 공유 레일
리스크에 대한 SW 대응이 시험으로 검증되었으므로 FM 모듈 인도 가능.
최종 위성구조체 장착 검증은 INT2(AIT, FM 통합) 범위.

검증: 하위 Work(FM-AOCS-01~04) 전건 DONE, acceptance-test-fm.md의
종합 지향오차(0.45°)가 SYS-REQ(≤0.5°) 이내임을 확인.
