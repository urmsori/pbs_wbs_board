# PAY 초점면 조립체 (TDI)
입력: examples/ksat6/deliverables/PAY/telescope-optics.md

## 1. 검출기·TDI 파라미터
- 픽셀 피치: 10µm (telescope-optics.md §1 회절스팟 5.2µm와 정합)
- 교차궤도 화소수: 6,000px → 스와스 ≈18km (GSD 3m 기준)
- TDI 단수: 32단 (SNR 이득 √32≈5.7배)
- 라인율: 2,500 line/s (telescope-optics.md §4 지상속도 산출과 동일)
- 라인적분시간: 400µs/line, TDI 32단 실효적분시간 ≈12.8ms
- 비트심도: 12bit/px

## 2. 초점면 열안정도 요구 (인용)
telescope-optics.md §3에서 산출한 **±0.5°C**(촬영 구간 초점면/광학벤치)를
그대로 채택 — REQ-PAY-TCS로 TCS 팀에 요청됨.

## 3. 원시 데이터율 (인용·확정)
6,000px × 12bit × 2,500/s = **180 Mbps**(판) — telescope-optics.md §4와 일치.
PAY-03(전자부)의 압축·출력 데이터율 설계 입력.

검증: TDI 32단·라인율 2,500/s 조합이 GSD 3m·SNR 목표를 만족(telescope-optics.md
§1 회절스팟 대비 픽셀 정합), 열안정도 요구를 광학계 예산과 동일하게 유지.
