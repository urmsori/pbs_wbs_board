# FM 비행품 제작 기록
입력: examples/ksat5/deliverables/AOCS/design-update-fm.md,
      examples/ksat5/deliverables/AOCS/icd-str-aocs-mass-footprint.md

design-update-fm.md 갱신 설계와 icd-str-aocs-mass-footprint.md 확정
질량·외형·체결 사양대로 비행품(FM) 제작을 완료했다.

## 제작 완료 품목
| 구성품 | 수량 | 시리얼/로트 | 실측 질량 | 판정 |
|---|---|---|---|---|
| 스타트래커(STT-1) | 1 | FM-STT-001 | 0.352 kg | 배분(0.35kg) 대비 +0.6%, 합격 |
| 관성센서(MEMS 자이로) | 1 | FM-IMU-001 | 0.198 kg | 합격 |
| 태양센서 | 2 | FM-SS-001/002 | 0.049 kg (개당) | 합격 |
| 리액션휠 | 3 | FM-RW-001~003 | 0.301 kg (개당) | 합격 |
| 마그네토토커 | 3 | FM-MTQ-001~003 | 0.099 kg (개당) | 합격 |

FM 총질량 실측: 1.998 kg (배분 2.000 kg 이내)

## SW 탑재
design-update-fm.md의 확보 슬루 guard band 강제 로직을 온보드 SW에
반영·탑재 완료(빌드 FM-SW-v1.1).

검증: FM 구성품별 실측 질량 합계(1.998 kg) ≤ AOCS 질량 배분(2.000 kg)
확인, 체결 홀 패턴이 icd-str-aocs-mass-footprint.md 사양과 일치함을
육안·게이지 검사로 확인.
