# [PAY→OBC] 탑재체 데이터율·SpW 링크 수 회신
입력: examples/ksat6/deliverables/PAY/telescope-optics.md, focal-plane-tdi.md, payload-electronics.md

## 데이터율
- 초점면 원시 출력(판코로매틱): **180 Mbps**(focal-plane-tdi.md §3)
- 멀티스펙트럼 포함 시 원시: **230 Mbps**
- 온보드 압축(~2:1) 후 영상 다운로드 데이터율: **평균 100 Mbps / 버스트
  115 Mbps**(촬영 세션 중, payload-electronics.md 인용)

## SpW 링크 요구
- **영상 다운로드용 SpW 1개 링크**: 지속 처리율 ≥150 Mbps 여유 요청(버스트
  115Mbps에 30% 마진).
- **명령/상태용 SpW 1개 링크**(분리): 저속(≤2Mbps), 영상 링크와 물리적으로
  분리해 영상 버스트 중 명령 지연 방지.
- 합계 **SpW 2링크** 요청.

## 메모리 버퍼
- 궤도당 촬영시간 12분(REQ-EPS-PAY 회신 참조) × 압축후 100Mbps ≈ 72Gb ≈
  **9GB/궤도**. 다운링크 지연(최대 2~3궤도) 대비 128GB 중 **≥30GB**를 탑재체
  영상버퍼로 할당 요청.

검증: REQ-PAY-OBC(당사 발신)와 상호 정합 — 동일 수치(100~115Mbps)로 회신,
REQ-OBC-PAY 응답.
