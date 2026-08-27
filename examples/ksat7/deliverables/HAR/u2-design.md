# HAR-U2 신호·데이터 하니스 설계

입력: examples/ksat7/deliverables/SE/sysreq.md, examples/ksat7/deliverables/OBC/io-connector-pinmap.md

## ICD 상태
REQ-HAR-OBC 회신 접수(io-connector-pinmap.md) — 대기 없이 정식 데이터로
설계.

## OBC 인터페이스 (io-connector-pinmap.md 인용)
- 커넥터: MDM-51 (51핀, 우주급 D형 마이크로미니어처)
- SpW 5채널(LVDS 2쌍/채널, 20핀), CAN 2채널(4핀), MIL-STD-1553B 이중화
  1버스(6핀), 실드 접지 1핀(41번핀, 단일점 섀시 접지)

## 하니스 구성
- 케이블: SpW/CAN/1553 각 신호쌍 개별 트위스트 실드 페어(TSP), 전체
  번들을 편조 실드로 2중 차폐(개별 실드 + 오버롤 실드)
- 실드 접지: 개별 실드는 커넥터측 플로팅(1점 접지 방지 목적, 접지루프
  방지), 오버롤 실드는 MDM-51 41번핀·커넥터 쉘 360° 접지(단일점, 저저항
  본딩 <10mΩ, OBC 요구 반영)
- 배선 경로: 위성 구조 프레임 인접 라우팅, SAR 대전류 펄스 배선(HAR-U1)
  과 최소 이격거리 150mm 확보(EMC 상호간섭 저감)

## EMC 차폐 설계 목표 (sysreq.md HAR: EMC 차폐)
2중 실드(개별+오버롤) + 단일점 접지 + HAR-U1 이격 라우팅으로 SAR 펄스
스위칭 노이즈 결합을 최소화. 정량 검증은 HAR-U2-INS-01(EMC 차폐 검사)에서
수행.

검도 대상으로 HAR-U2-CHK-01에 전달.
