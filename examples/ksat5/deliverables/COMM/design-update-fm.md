# COMM FM 설계 갱신
입력: examples/ksat5/deliverables/COMM/module-em.md,
examples/ksat5/deliverables/AIT/rx-comm.md,
examples/ksat5/deliverables/COMM/link-margin-fix.md,
examples/ksat5/deliverables/COMM/antenna-design.md (rev.2),
examples/ksat5/deliverables/COMM/transceiver-em.md (rev.2)

## EM 대비 변경 사항
1. **안테나 피드망**: 4소자 급전선 길이·결합 임피던스 재조정
   (link-margin-fix.md 방안A) — 형상·질량·장착 인터페이스 변경 없음,
   위상오차 ±5°→±2°, EOD 링크마진 6.0dB(여유0)→7.5dB(여유1.5dB).
2. **트랜시버 전원**: rev.2(PA 액추에이터 레일 8.4V 직결, 로직단만
   5V 레일) 그대로 승계 — EM 인수시험에서 5V 레일 여유 74% 확인됨.
3. **미변경 항목**: 질량(트랜시버 0.55kg+안테나 0.15kg=0.70kg,
   구조체결·하네스 포함 총 1.20kg 배분 유지), 커넥터·기구 인터페이스
   (icd-str-comm-footprint.md 규격 그대로 — STR ICD 재협상 불필요).

## 승계 이월 리스크 처리 현황
- EOD 링크마진 0dB → RISK-LINK로 해소(여유 1.5dB 확보), FM 방사패턴
  실측 재확인은 COMM-FM-04(수락시험)에서 수행.
- 액추에이터 레일 동시부하(RISK-RAIL) → EPS 주관 진행 중(미완료).
  COMM 몫으로 송신 펄스 시간프로파일 회신 완료(req-rail-comm-tx-timing.md).
  본 설계 갱신에서는 전류 수치 변경이 없으므로 대기 없이 진행하되,
  RISK-RAIL 최종 퓨즈 정격이 나오면 그 값으로 COMM-FM-03(수락검사) 시
  재확인이 필요할 수 있음을 명시해 이월한다.

## FM 제작 착수 조건
설계 수치(전원·안테나·기구) 전항 확정 — COMM-FM-02(비행품 제작) 착수
가능.

검증: EM 대비 변경분(안테나 피드망만)이 형상·질량·인터페이스에
영향 없음을 확인, 링크마진 개선치는 link-margin-fix.md 재계산과
일치. RISK-RAIL 미확정 항목은 미해결로 명시(낙관 판정 금지).
