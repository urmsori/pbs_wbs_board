# STR-U1 중앙 실린더 설계

입력: examples/ksat8/deliverables/SE/sysreq.md (STR 1차모드≥30Hz, 질량≤380kg), examples/ksat8/deliverables/PROP/str-prop-tank-reply.md (탱크 습식1,363kg·트러니언4점·
축8.5g/횡4.5g), examples/ksat8/deliverables/SA/str-sa-load-reply.md (SA 180kg/윙·전개반력2,500N/3,000N·m·4점M10 PCD200mm),
examples/ksat8/deliverables/PAY/str-pay-mount-reply.md (중계기 총156.6kg·M6 50mm그리드·국부강성≥60Hz — STR-U2 패널 설계 입력,
U1 총 스택질량 산정에 반영)

## 형상
CFRP 스킨 + Al 허니컴 코어 샌드위치 중앙 실린더(Ø2.0m×H2.6m), 상/하 데크, 측판 4매,
발사체 인터페이스 링(하단).

## 인터페이스 반영
- 하부 데크: 이원추진제 탱크 2기(산화제846kg/연료517kg, 합계1,363kg 습식) 트러니언
  마운트 4점×2기, PROP 요구 국부강성(≥60Hz) 반영해 보강링(Ø600mm 산화제/Ø520mm 연료) 배치.
  설계하중은 PROP 회신치(축8.5g/횡4.5g)를 채택.
- 측판: SA 요크 마운트 4점 M10 PCD200mm ×2윙, 전개반력(축2,500N·모멘트3,000N·m) 국부보강.
- 상판: MECH-U1(반사판 전개기구) 장착 인터페이스, PAY 중계기 패널(STR-U2) 접속 프레임.
  PAY 중계기 총질량 156.6kg(78.3kg/패널) 확정 회신 반영해 상판 프레임 하중경로 확정.

## 질량 예산 (잠정, ANL-S 단계에서 확정)
| 부재 | 질량(kg) |
|---|---|
| 중앙 튜브(CFRP) | 62 |
| 상/하 데크(Al허니컴+보강링) | 78 |
| 측판 4매 | 54 |
| 트러니언 보강링·브래킷 | 28 |
| SA 요크 마운트 브래킷 | 12 |
| 체결류·인서트 | 10 |
| **합계** | **244** (목표≤260kg, 마진16kg) |

## 다음 단계
ANL-S(구조해석, 탱크·SA 집중질량 반영 1차모드)·ANL-T(열해석) 병행.
