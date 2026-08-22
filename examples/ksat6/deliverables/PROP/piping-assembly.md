# 배관·밸브 조립 기록
입력: examples/ksat6/deliverables/PROP/tank-acceptance.md, examples/ksat6/deliverables/PROP/thruster-acceptance.md, examples/ksat6/deliverables/PROP/propellant-budget.md

## 조립 순서
1. 탱크(수락 S/N 확인) → 충전/배출 밸브 → 압력변환기 체결(토크 스펙 준수).
2. 래치밸브(이중) 체결, 절연저항 측정(≥10MΩ) 후 배선.
3. 배관 4분기(외경6mm 튜브, 곡률반경≥25mm 확보) → 스러스터 4기(대각쌍 배치,
   thruster-acceptance.md 배정대로 S/N01·03 / S/N02·04) 체결.
4. 전 이음부 토크 재확인, 육안 검사.

## FSW 인터페이스 반영
래치밸브 이중코일 배선을 FSW 요구(REQ-PROP-FSW, 펄스폭 50ms 구동)에 맞춰
코일 저항·전류 스펙으로 배선했다. FSW 팀의 최종 로직 확인은 REQ-PROP-FSW
완료 후 통합시험(INT)에서 함께 검증한다.

## 확인
장착 좌표는 STR REQ(REQ-PROP-STR) 확정치를 반영 대기 중이며, 배관 경로는
propellant-budget.md 산정치(총길이 1.6m, 클리어런스 30mm)로 임시 라우팅했다 —
STR 확정 좌표가 다르면 배관 재라우팅 필요(변경 범위: 클리어런스 30mm 이내면
무변경).

검증: 전 이음부 토크 실측 스펙 이내, 절연저항 실측 ≥10MΩ, 육안검사 이상없음.
가압·누설 실측은 PROP-05에서 별도 수행.
