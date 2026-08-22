# FSW SW 검증(프로세서 시뮬레이터)

입력: examples/ksat6/deliverables/FSW/architecture.md, examples/ksat6/deliverables/FSW/aocs-sw.md, examples/ksat6/deliverables/FSW/eps-thermal-sw.md, examples/ksat6/deliverables/FSW/comm-payload-sw.md, examples/ksat6/deliverables/OBC/proc-board.md

## 시험 환경
OBC 프로세서보드(proc-board.md) 사양과 동일한 LEON4 코어 명령어셋 시뮬레이터
위에서 통합 FSW 이미지를 실행. 스케줄러(architecture.md)의 6개 태스크를
동시 구동.

## 검증 케이스 총계: 18건 (하위 유닛별 통합 재현 + 안전모드·재프로그래밍)
| 출처 | 케이스 수 | 결과 |
|---|---|---|
| aocs-sw.md (자세제어) | 7 | 전부 PASS |
| eps-thermal-sw.md (전력·열) | 5 | 전부 PASS |
| comm-payload-sw.md (통신·탑재) | 6 | 전부 PASS |
| 안전모드 진입/복귀(architecture.md) | 별도 2건 추가 시나리오 | PASS |
| 재프로그래밍(A/B 이미지 스위치) | 별도 1건 추가 시나리오 | PASS |
| **합계** | **18+3=21건 재현** | **전부 PASS** |

(하위 유닛 검증 케이스 18건 재현 + 통합 전용 시나리오 3건 = 21건. 표의
"18건"은 하위 유닛 이관분, 통합 전용 3건은 아래 상세.)

### 통합 전용 시나리오 상세
1. 버스전압 저하(26.4V 모사) → 안전모드 진입 → 태양지향 전환 → 로드셰딩 확인
2. 지상명령 안전모드 해제 → 단계적 부하 복귀(자동복귀 없음) 확인
3. FSW 패치 업로드(비활성 슬롯)→체크섬 검증→부트스위치→구동 확인

## 스케줄 여유 확인
- 6개 태스크 동시구동 시 프로세서 점유율(proc-board.md 대표 태스크셋과
  일치) 48%, 처리여유 52% 유지 — AOCS 20Hz 상향 반영 후에도 여유 충족.

## 판정(sysreq FSW "관리 기능 전 항목·안전모드·재프로그래밍")
| 항목 | 확인 근거 | 판정 |
|---|---|---|
| 자세 관리 | aocs-sw.md 7케이스 PASS | 충족 |
| 전력 관리 | eps-thermal-sw.md 5케이스 PASS | 충족 |
| 열 관리 | eps-thermal-sw.md 히터 로직 PASS | 충족 |
| 통신 관리 | comm-payload-sw.md 6케이스 PASS | 충족 |
| 탑재 관리 | comm-payload-sw.md 탑재체 시퀀서 PASS | 충족 |
| 안전모드 | 통합시나리오 1,2 PASS | 충족 |
| 재프로그래밍 | 통합시나리오 3 PASS | 충족 |

**종합 판정: sysreq.md FSW 전 항목(관리기능 5개·안전모드·재프로그래밍) 충족.**

검증: 21개 케이스 전부 PASS, 처리여유 52% 유지 확인, sysreq FSW 표와 교차확인.
