---
id: REQ-HAR-PAY-RF
title: 도파관 경로 요구·플랜지 규격 요청 (도파관·RF 하니스 설계용)
status: DONE
parent: M-HAR
source: HAR-U2-DSN-01
owner: PAY-DSN-01
deliverable: examples/ksat8/deliverables/PAY/waveguide-route-spec.md
after: -
track: PAY
started: 2026-08-27 03:55:18
finished: 2026-08-27 03:55:18
---

HAR-U2(도파관·RF 하니스)를 설계하려면 PAY 중계기(TWTA·스위치 매트릭스)
출력단에서 안테나 급전부까지의 도파관 경로 요구와 플랜지 규격을 알아야
한다. sysreq.md: 24채널, 채널당 EIRP 52dBW, 도파관 손실 ≤0.8dB(HAR
항목).
요청: 중계기 출력 도파관 플랜지 형식·규격(예: WR-band, UBR/PBR),
채널별 출력 포트 위치·개수, 경로상 허용 굴곡 수·최소 곡률반경, 손실
예산 중 PAY 측 배분(있다면).
산출물 제안: examples/ksat8/deliverables/PAY/waveguide-route-spec.md
검증: WR-42, 28포트(4x7격자), 손실배분0.8dB(HAR실측0.57dB 이내)
