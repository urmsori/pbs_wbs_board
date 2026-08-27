# AIT-RX-1 구조·기구·하니스(STR/MECH/HAR) 인도 수령·판정

입력: examples/ksat8/deliverables/STR/module-fm.md,
examples/ksat8/deliverables/MECH/module-fm.md,
examples/ksat8/deliverables/HAR/module-fm.md

## 판정
| 트랙 | sysreq 항목 | 인도 문서 판정 |
|---|---|---|
| STR | 질량≤380kg, 1차모드≥30Hz | 349.7kg(마진8%), 31.8Hz(마진6%) — 충족 |
| MECH | 반사판2기·SA힌지2윙 전개, 단일고장허용 | 전개시험/기능시험 실측 확인 — 충족 |
| HAR | 100V절연·대전류, 도파관손실≤0.8dB | 242~245MΩ·전압강하≤0.79%·0.58dB — 충족 |

## HAR 이월 리스크 처리
HAR module-fm.md「리스크·후속조치」4건 중 INT 단계로 명시 이관된 것은
1항(HAR-PAY 도파관 플랜지 물리 정합)뿐이다. 세부 실측 도면이 인도
문서에 없어 REQ-AIT-HAR-플랜지실측(track: HAR, source: 본 Work)을
발행했으나 8×20초 폴링(160초) 동안 회신이 없었다(HAR 팀 에이전트
종료). **REQ-AIT-HAR-플랜지실측은 OPEN으로 남기고, 인도 문서 범위
내에서만 판정한다**: HAR module-fm.md가 "전기 성능(손실)은 이미 실측
검증되어 유효, 물리적 체결 정합은 INT 단계 확인 필요"라고 명시했으므로
INT-TST-1에서 실물 체결 시도로 직접 확인하고, 부적합 시 어댑터
현장 조치를 INT-TST-1에서 별도 기록한다(module-fm.md 이관 지시와 일치).
나머지 3건(PA 입회 미확인·STR 라우팅 회신 미접수·EMI 실측 권고)은
HAR 자체 기록 유지 항목으로 INT 재작업 대상이 아니다(STR module-fm.md에
대응 리스크 언급 없어 정상 진행으로 판단).

검증: STR·MECH·HAR sysreq 항목 전량 인도 문서 기준 충족 확인, HAR
이월 리스크 1건은 REQ-AIT-HAR-플랜지실측 OPEN 상태로 INT-TST-1에 이관
