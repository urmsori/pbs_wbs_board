# SA 3윙 힌지 인터페이스 회신 (REQ-MECH-SA)

입력: examples/ksat7/board/REQ-MECH-SA.md, examples/ksat7/deliverables/SA/panel-design.md,
examples/ksat7/deliverables/MECH/sa-hinge-icd.md

① 윙당 패널 질량·관성: 질량 **7.6kg/윙**(설계 목표 ≤8kg 이내), 힌지축 기준
   회전관성 **I ≈ 10.1 kg·m²**(패널 길이 2.0m, 균일분포 가정 m·L²/3).
② 요구 회전강성·백래시: 귀 팀 회신(8000 N·m/rad, sysreq 1차모드≥0.5Hz 판정에
   사용한 값)과 **일치 확인**, 백래시 요구 ≤0.05°(귀 팀 제시치 수용).
③ 힌지 장착 볼트 패턴/좌표: 귀 팀 제안(4점 M6, PCD 80mm, 윙 뿌리 대칭축 기준
   ±40mm) **그대로 확정**, 패널측 브래킷 동일 패턴으로 설계 반영.

검증: 패널 질량7.6kg/윙·관성10.1kg·m² 회신, 힌지강성·볼트패턴 상호 확정(수치 일치)
