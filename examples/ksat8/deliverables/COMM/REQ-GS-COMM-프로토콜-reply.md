# COMM → GS 회신: TT&C 주파수·변조·레인징 계획

입력: examples/ksat8/deliverables/COMM/comm-u1-design.md

1. **주파수**: 상향(명령) 2087.5 MHz(대역 2025.0–2110.0MHz 내 지정,
   대역폭 ≤1.5MHz) / 하향(TM) 2255.5 MHz(대역 2200.0–2290.0MHz 내 지정,
   대역폭 ≤4MHz).
2. **변조**: 명령 PCM/PSK/PM(부반송파 16kHz, 2kbps) / TM PCM/PSK/PM
   (부반송파 65.536kHz, 상시 4kbps·버스트 8kbps).
3. **레인징**: PN 코드(CCSDS 표준, 주 코드 2²²−1) + 코히런트 턴어라운드비
   240/221. 레인징은 TM/TC와 동일 캐리어 결합변조.
4. **EIRP·G/T 예상치**: 안테나는 LGA(반구 커버리지) 가정 시 보어사이트
   이득 약 3dBi, SSPA 출력은 상시 150W/피크 220W 전력 배정 내에서 2W급
   (33dBm)으로 설계 예정 — 관제소 링크버짓용 잠정치. EIRP ≈ 33dBm+3dB−
   급전선손 1dB ≈ 35dBm(약 5dBW). 정밀치는 §5 링크버짓 해석(COMM-ANL-RF-01)
   완료 후 갱신.

검증: comm-u1-design.md §1(주파수·변조·레인징)과 정합.
