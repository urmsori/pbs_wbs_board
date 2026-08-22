---
id: INT-TST-3
title: 통합시험 — RF·데이터 종단간
status: DONE
parent: INT
source: -
owner: AIT-TST-01
deliverable: examples/ksat6/deliverables/AIT/int-tst-3-rf-e2e.md
after: NEED-S밴드감쇠교정장비, NEED-자세연동RF시험장비
track: AIT
started: 2026-08-22 01:45:04
finished: 2026-08-22 01:46:13
---

시스템 레벨에서 S-band/X-band 링크와 OBC-COMM-PAY 데이터 경로를 종단간
검증해야 하며, COMM module-fm.md가 정직 기록한 S-band 하향 저마진
(+0.94dB)과 X-band 버퍼 여유(6.7%), 자세기동-X-band 빔 연동 미검증
항목을 이 시험에서 닫거나 운용 제약으로 이관해야 한다. 이를 위해
교정 감쇠기·전력계와 자세연동 RF 시험 장비(AIT-RX-4에서 발견된 필요)가
갖춰져야 시작할 수 있다.
산출물: RF·데이터 종단간 시험 기록(md).
검증: S밴드마진+0.91dB(모듈+0.94dB와 0.03dB 이내 재확인)→앙각≥15° 운용제약 추인, 자세기동중 X밴드 RSSI±1dB/BER≤1e-5 PASS(신규종결), 버퍼여유6.6%(모듈6.7%와 일치)→GS 운용모니터링 이관
