# [PAY→STR] 탑재체 장착 인터페이스·열변형 허용치 회신
입력: examples/ksat6/deliverables/PAY/telescope-optics.md, payload-electronics.md

## 질량·인터페이스
- 탑재체 총질량(망원경+초점면+전자부): **약 35 kg**(발사질량 예산 150kg의
  ~23%, sysreq 마진 20% 관리 대상)
- 장착: **3점 등정력학(kinematic, bipod) 마운트**, 볼트원 지름 260mm,
  각 점 2×M6(합 6개), 예압은 STR 해석 결과에 따름.

## 열변형 허용치 (광축 정렬 보존)
- 마운트 인터페이스 각변위: **≤0.01°(36 arcsec)**
- 마운트 인터페이스 병진변위: **≤10 µm**
(운용 온도범위 전체에 걸쳐, telescope-optics.md §2 정렬오차 배분 15nm WFE에
대응하는 구조 스택업 여유를 반영한 값 — REQ-TCS-PAY 회신의 광학벤치 구배
≤2°C 전제와 함께 적용)

검증: 3점 킨네마틱 마운트가 위 각변위/변위 허용치를 만족하도록 STR 해석에
반영 요청 — REQ-STR-PAY 응답.
