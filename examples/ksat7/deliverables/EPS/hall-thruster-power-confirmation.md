# 홀추력기 300W 공급 확약 (REQ-PROP-EPS)

입력: examples/ksat7/board/REQ-PROP-EPS.md, examples/ksat7/deliverables/PROP/thruster-operating-profile.md

PROP 회신(REQ-EPS-PROP)에 따라 추력 운전은 SAR 촬영과 상호 배타 운용이며
정상상태 300W/1.0A, 램프 3s이다. EOL 공급예산 620W·소비예산 540W(sysreq) 내에서
SAR 비촬영 구간의 정상모선 부하는 300W(추력)를 포함해도 예산 이내로 확인.
모선 50V±5V 기준 300W는 6.0A(50V 기준)로 주배전 정격(핀당 40A) 대비 여유 충분.

판정: **가능**. 추력기 가동 구간 300W 연속 공급을 모선 50V±5V로 확약.

검증: 300W/6.0A 연속공급이 EOL 소비예산540W 이내에서 가능함을 확인
