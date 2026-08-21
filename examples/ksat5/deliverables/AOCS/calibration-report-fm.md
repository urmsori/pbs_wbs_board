# FM 센서·액추에이터 교정 결과
입력: examples/ksat5/deliverables/AOCS/fabrication-record-fm.md,
      examples/ksat5/deliverables/AOCS/design-update-fm.md

fabrication-record-fm.md 제작 완료품(FM-STT-001, FM-IMU-001,
FM-RW-001~003, FM-MTQ-001~003)에 대한 교정 결과.

| 구성품 | 교정 항목 | 결과 |
|---|---|---|
| STT-001 | 광축 정렬 기준교정(장착면 대비) | 잔차 0.008° (설계 정렬공차 0.015° 이내) |
| IMU-001 | 바이어스/스케일팩터 교정 | 바이어스 0.02°/h, 스케일팩터 오차 0.05% |
| RW-001~003 | 토크상수 교정 | 편차 ≤1.2%(축간) |
| MTQ-001~003 | 자기모멘트 교정 | 편차 ≤1.5%(축간) |

design-update-fm.md의 조정된 EKF/PD 게인(목표 결정오차 0.13°/제어오차
0.28°)을 상기 교정치로 재계산해 SW 파라미터 테이블에 반영·탑재
완료(빌드 FM-SW-v1.1 파라미터 갱신).

검증: STT 정렬 잔차(0.008°) ≤ 설계 정렬공차(0.015°) 확인, 전 구성품
교정 편차가 설계 여유(design-update-fm.md 목표치) 이내임을 확인.
