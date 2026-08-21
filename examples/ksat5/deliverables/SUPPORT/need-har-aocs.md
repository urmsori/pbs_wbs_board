# AOCS EM 모듈 인수 시험용 시험 하니스
입력: examples/ksat5/deliverables/AOCS/module-em.md,
      examples/ksat5/deliverables/AOCS/icd-str-aocs-mass-footprint.md

NEED-HAR-AOCS(AIT-TST) 요청에 대한 하니스 기술자 인도물. module-em.md §2
확정 인터페이스가 인용하는 icd-str-aocs-mass-footprint.md 커넥터/하니스
인출면 열을 반영해 아래 10채널 시험 하니스를 제작한다.

## 채널/핀맵 표
| 채널 | 구성품 | 인출면 | 트렁크 경로 | 커넥터(모듈측/EGSE측) | 케이블 길이 |
|---|---|---|---|---|---|
| 1 | 스타트래커(STT-1) | 후면(–배플 반대면) | –Z 패널 트렁크 | D-Sub15M / D-Sub15F | 1.8 m |
| 2 | MEMS 자이로 | 측면 1면 | –Z 패널 트렁크 | Micro-D9M / Micro-D9F | 1.6 m |
| 3 | 태양센서 #1 | 후면(패널 관통) | –Z 패널 트렁크 | Micro-D9M / Micro-D9F | 1.7 m |
| 4 | 태양센서 #2 | 후면(패널 관통) | –Z 패널 트렁크 | Micro-D9M / Micro-D9F | 1.7 m |
| 5~7 | 리액션휠 X/Y/Z | 축 반대면(휠 배면), 직교 3축 개별 인출 | 축별 개별 트렁크(합류 없음) | Micro-D25M / Micro-D25F | 2.2 m (축당) |
| 8~10 | 마그네토토커 X/Y/Z | 로드 중앙부 측면, 직교 3축 개별 인출 | 축별 개별 트렁크(합류 없음) | Micro-D9M / Micro-D9F | 2.0 m (축당) |

## 배선 규칙
–Z 패널 트렁크(채널 1~4, 관성/태양센서)는 단일 하니스 다발로 합류시켜
EGSE 브레이크아웃 박스 1포트로 취합하고, 리액션휠·마그네토토커 6채널은
직교 3축 배치를 그대로 반영해 축별 개별 커넥터로 EGSE에 인출한다(트렁크
합류 금지 — module-em.md §2 장착 배치와 불일치 방지).

검증: NEED-HAR-AOCS 표의 5개 구성품·인출면·수량(스타트래커1, 자이로1,
태양센서2, 리액션휠3, 마그네토토커3 = 총 10채널)과 위 채널표가 1:1
일치함을 확인. –Z 트렁크 합류(1~4) vs 축별 개별 인출(5~10) 구분이
icd-str-aocs-mass-footprint.md 배치 개요와 일치함을 확인.
