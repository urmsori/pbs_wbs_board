---
id: REQ-PAY-HAR-도파관
title: "[PAY→HAR] 도파관 경로·손실 예산 요청"
status: DONE
parent: M-PAY
source: M-PAY
owner: HAR-DSN-01
deliverable: examples/ksat8/deliverables/HAR/pay-waveguide-budget.md
after: -
track: HAR
started: 2026-08-27 03:49:56
finished: 2026-08-27 03:49:56
---

sysreq HAR은 도파관 손실 ≤0.8dB를 규정한다. PAY-U1 설계(DSN)가 TWTA 출력단
에서 안테나 급전까지의 링크 예산(EIRP 52dBW/채널 달성을 위한 TWTA 필요
출력 역산)을 확정하려면 HAR의 실제 도파관 경로(길이·굴곡수)와 채널별
삽입손실·VSWR을 알아야 한다.
산출물 제안: examples/ksat8/deliverables/HAR/pay-waveguide-budget.md —
TWTA-안테나 간 도파관 경로 삽입손실(dB, 채널별 또는 대표치)·VSWR·경로장.
검증: 삽입손실 ≤0.8dB(sysreq HAR 상한) 회신 확인, TWTA 필요출력 역산에 반영
검증: 삽입손실 0.57dB<=0.8dB 회신(잠정, PAY/STR정식회신시 재계산 가능)
