입력: examples/ksat8/deliverables/OBC/obc-design.md, examples/ksat8/deliverables/OBC/obc-anl-elec.md, examples/ksat8/deliverables/OBC/obc-anl-therm.md, examples/ksat8/deliverables/COMM/obc-if-reply.md, examples/ksat8/deliverables/PAY/obc-tm-reply.md

# OBC 도면·설계 검도

## 정정 1 — PAY TM 배정 (잠정 → 확정)
obc-design.md §2는 REQ-OBC-PAY-TM 회신 전 채널당 ~108점(24채널 ≈2,600점)
을 잠정 가정했다. 실제 회신(examples/ksat8/deliverables/PAY/obc-tm-reply.md)은
**채널당 15점×24 + 공통40 = 총 400점**이다. TM 예산표를 아래로 정정한다.

| 구분 | 원 배정(잠정) | 확정 배정 | 근거 |
|---|---|---|---|
| PAY | 2,600 | **400** | REQ-OBC-PAY-TM 회신 |
| 여유(마진) | 1,000 | **3,200** | 확정치 반영 후 여유 증가 |
| 그 외(EPS/TCS/PROP/AOCS/COMM/OBC자체) | 4,400 | 4,400 | 변경 없음(OBC가 개별 요청하지 않은 자체 견적, sysreq 상위요약 근거) |
| **합계(용량 상한)** | 8,000 | 8,000 | sysreq TM 8,000점은 처리 **용량** 요구이며 실사용점수가 이보다 적어도 요구 충족 |

## 정정 2 — TT&C 인터페이스
COMM 회신(obc-if-reply.md)은 COMM-U1 설계 미확정으로 **잠정**임을 재확인.
1553B 버스·1Hz 프레임 가정은 obc-design.md §3과 정합하나, COMM-U1이
확정되면 재검도가 필요하다(module-fm.md에 미결 항목으로 기록).

## 검도 결과
- 치수·공차: obc-design.md의 커넥터·레지스터 오프셋 정의는 내부
  일관성 있음(중복 없음).
- 열/전자 해석(anl-elec/anl-therm)과 설계 정합 확인.
- 위 정정 1은 확정, 정정 2는 잠정 유지(추후 정정 예정) — RVW 단계로 진행.

검증: PAY TM 배정 400점으로 정정, 마진 3,200점 확보(용량요구 8,000점 충족).
