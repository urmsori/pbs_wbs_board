# EPS → FSW 회신: 배터리 관리 파라미터
입력: examples/ksat6/deliverables/EPS/pcdu-design.md

- 충전 종지: 33.6 V(4.2V/cell), 테이퍼 컷오프 전류 0.05C
- 저전압 로드셰딩 1단계: 27.2 V(3.4V/cell) — 비필수 부하 차단
- 저전압 안전모드(임계): 26.4 V(3.3V/cell) — sysreq DoD≤25% 한계 초과 방지 여유
- 과온 충전금지: 32°C(재개 28°C), 저온 충전금지: 0°C 미만(sysreq TCS 배터리 0~30°C 범위 내)

검증: PCDU 배터리관리 임계값표 인용 회신, sysreq DoD≤25%·배터리 0~30°C 반영.
