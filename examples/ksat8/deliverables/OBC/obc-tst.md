입력: examples/ksat8/deliverables/OBC/obc-ins.md, examples/ksat8/deliverables/CAL/obc-cal-cert.md, examples/ksat8/deliverables/FAC/obc-fac-booking.md

# 비행모델 기능·이중화 절체 시험

1. **TM 처리 시험**: 시뮬레이터로 8,000점 상당 TM 프레임(고속 33%/저속
   67% 비율, drawing-check.md 확정 배분 기준) 주입 → 전량 정상 수집·
   순환버퍼 기록 확인, 프레임 드롭 0건.
2. **TC 처리 시험**: 2,000점 상당 TC 프레임(CRC 오류 포함 스트레스
   케이스) 주입 → 정상 명령 100% 수락, 오류 프레임 100% 거부(NAK) 확인.
3. **이중화 절체 시험**: 주 유닛 워치독 강제 무응답(3회) 주입 → 예비
   유닛 절체 개시, 절체 소요시간 실측 **420ms**(요구 ≤500ms 충족).
4. 절체 전 크리티컬 상태(모드·TC 순번) EEPROM 스냅샷 복원 확인 —
   절체 후 상태 연속성 유지.

검증: TM 8,000점 프레임 드롭 0, TC 처리 정상, 절체 420ms(≤500ms 요구
충족).
