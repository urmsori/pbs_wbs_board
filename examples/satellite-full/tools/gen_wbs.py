#!/usr/bin/env python3
"""K-SAT 2 상세 개발 보드의 WBS 골격 생성기 — Work F002의 산출물.

규칙 1절: "PBS의 큰 골격이나 WBS의 일부가 처음부터 정해져 있어도 된다.
정해진 부분은 시작할 때 게시글들로 미리 올려 두면 된다." 이 스크립트가
그 '미리 올려 두기'를 수행한다: 형상 3(EM/QM/FM) × 서브시스템 8 ×
조립체 6 × 잎 Work(형상별 12~16)의 OPEN 게시글과, 조립체 산출물 스텁,
에이전트용 실행목록(runlist)을 만든다.

생성 구조 (레벨 = 트리 깊이, 규칙 4절 레벨-등급):
  L0 F000 루트(claude) → L1 형상 EM/QM/FM(claude) → L2 서브시스템(sonnet 취합)
  → L3 조립체(sonnet 취합) → L4 잎 Work(haiku 수행)

사용법: python3 examples/satellite-full/tools/gen_wbs.py
멱등: 이미 있는 게시글 파일은 덮어쓰지 않는다.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent   # examples/satellite-full
BOARD = HERE / "board"
DELIV = HERE / "deliverables"
RUNS = HERE / "runlists"
REPO = HERE.parent.parent
REL = lambda p: p.relative_to(REPO).as_posix()

PHASES = [
    ("EM", "EM 형상 — 엔지니어링 모델", "F002"),
    ("QM", "QM 형상 — 인증 모델", "EM"),
    ("FM", "FM 형상 — 비행 모델", "QM"),
]

SUBSYSTEMS = [
    ("STR", "구조계"), ("TCS", "열제어계"), ("EPS", "전력계"), ("AOCS", "자세제어계"),
    ("OBC", "탑재컴퓨터"), ("COMM", "통신계"), ("PROP", "추진계"), ("PAY", "탑재체"),
]

ASSEMBLIES = {
    "STR": [("MF", "메인프레임"), ("PN", "외부패널"), ("SEP", "분리장치"), ("BR", "브래킷류"), ("HG", "전개힌지"), ("MC", "사출가공품")],
    "TCS": [("HT", "히터"), ("ML", "MLI 단열재"), ("RD", "라디에이터"), ("TS", "서미스터"), ("HP", "히트파이프"), ("TC", "온도조절기")],
    "EPS": [("SA", "태양전지판"), ("BT", "배터리"), ("PC", "전력조절기"), ("PD", "배전기"), ("PB", "전원보드"), ("HN", "전력하니스")],
    "AOCS": [("ST", "별추적기"), ("GY", "자이로"), ("RW", "반작용휠"), ("MT", "자기토커"), ("SS", "태양센서"), ("CB", "제어보드")],
    "OBC": [("PR", "프로세서보드"), ("MM", "대용량메모리"), ("IO", "IO보드"), ("WD", "감시회로"), ("SW", "비행소프트웨어"), ("BP", "백플레인")],
    "COMM": [("TR", "S대역 트랜시버"), ("AN", "안테나"), ("DP", "다이플렉서"), ("RF", "RF케이블"), ("TX", "고속송신기"), ("LG", "저이득안테나")],
    "PROP": [("TH", "추력기"), ("TK", "추진제탱크"), ("PL", "배관"), ("VV", "밸브"), ("PS", "압력센서"), ("FV", "충전밸브")],
    "PAY": [("CM", "광학카메라"), ("DT", "검출기"), ("IP", "영상처리보드"), ("CL", "교정장치"), ("DC", "데이터압축기"), ("FC", "포커스기구")],
}

WORKS = {
    "EM": [("req", "요구 할당"), ("concept", "개념 설계"), ("design", "상세 설계"),
           ("stress", "구조·강도 해석"), ("thermal", "열 해석"), ("parts", "부품 선정"),
           ("iface", "인터페이스 정의"), ("proto", "시제 제작"), ("proc", "기능시험 절차"),
           ("test", "기능시험"), ("perf", "성능 측정"), ("fix", "문제점 조치"),
           ("pdr", "설계검토 자료"), ("report", "EM 결과보고")],
    "QM": [("upd", "설계 갱신"), ("buy", "인증부품 구매"), ("recv", "입고 검사"),
           ("fab", "제작"), ("asm", "조립"), ("wkm", "워크맨십 검사"),
           ("vib", "진동시험"), ("shk", "충격시험"), ("tvac", "열진공시험"),
           ("emc", "EMC 시험"), ("burn", "수명·번인시험"), ("ncr", "비적합 처리"),
           ("data", "시험데이터 분석"), ("cdr", "인증검토 자료"),
           ("cfg", "형상문서 갱신"), ("qrep", "인증보고")],
    "FM": [("buy", "비행부품 구매"), ("recv", "입고 검사"), ("fab", "제작"),
           ("asm", "조립"), ("insp", "정밀 검사"), ("avib", "수락 진동시험"),
           ("atvac", "수락 열진공시험"), ("fperf", "최종 성능시험"),
           ("bake", "세척·베이크아웃"), ("mass", "질량특성 측정"),
           ("dpak", "인도문서 작성"), ("arev", "수락검토")],
}

TPL = """---
id: {id}
title: {title}
status: OPEN
parent: {parent}
owner: -
deliverable: -
after: {after}
track: {track}
started: -
finished: -
---

{body}
"""


def write_post(fname, **kw):
    p = BOARD / fname
    if p.exists():
        return 0
    p.write_text(TPL.format(**kw), encoding="utf-8")
    return 1


def main():
    BOARD.mkdir(parents=True, exist_ok=True)
    RUNS.mkdir(parents=True, exist_ok=True)
    n = 0
    for ph, ph_title, ph_after in PHASES:
        # L1 형상 게시글 — 취합자는 claude(상위 등급). after에 서브시스템 취합을 걸어
        # 도구(post.py)가 취합 순서를 기계적으로 지키게 한다.
        subs_ids = ", ".join(f"{ph}-{s}" for s, _ in SUBSYSTEMS)
        n += write_post(
            f"{ph}-phase.md", id=ph, title=ph_title, parent="F000",
            after=f"{ph_after}, {subs_ids}" if ph != "EM" else f"{ph_after}, {subs_ids}",
            track="SAT",
            body=f"최종 위성 형상의 {ph} 단계. 서브시스템 취합이 모두 끝나면 형상 수준"
                 f" 통합·시험 결과를 취합한다. 산출물: {REL(DELIV / ph / 'report.md')}",
        )
        for sub, sub_title in SUBSYSTEMS:
            sid = f"{ph}-{sub}"
            asm_ids = ", ".join(f"{sid}-{a}" for a, _ in ASSEMBLIES[sub])
            gate = ph_after if ph != "EM" else "F002"
            # L2 서브시스템 취합 (sonnet)
            n += write_post(
                f"{sid}-subsystem.md", id=sid, title=f"{ph} {sub_title} 취합",
                parent=ph, after=asm_ids, track=sub,
                body=f"{ph} 단계 {sub_title}의 조립체 산출물을 취합해 판정을 남긴다."
                     f" 산출물: {REL(DELIV / ph / sub / 'summary.md')}",
            )
            runlist = []
            for asm, asm_title in ASSEMBLIES[sub]:
                aid = f"{sid}-{asm}"
                deliv = DELIV / ph / sub / f"{asm.lower()}-{asm_title_slug(asm_title)}.md"
                deliv.parent.mkdir(parents=True, exist_ok=True)
                if not deliv.exists():
                    deliv.write_text(
                        f"# {asm_title} ({ph}/{sub}) — 조립체 산출물\n\n"
                        f"잎 Work들이 결과를 한 줄씩 덧붙이고, 조립체 취합 Work가 판정을 남긴다.\n\n",
                        encoding="utf-8",
                    )
                works = WORKS[ph]
                last = None
                for i, (slug, wtitle) in enumerate(works, 1):
                    wid = f"{aid}-{i:02d}"
                    after = last if last else gate
                    n += write_post(
                        f"{wid}-{slug}.md", id=wid,
                        title=f"{asm_title} {wtitle}", parent=aid, after=after,
                        track=sub,
                        body=f"{ph}/{sub_title}/{asm_title}의 잎 Work. 결과를 조립체 산출물"
                             f" 파일에 한 줄 덧붙인다. 산출물: {REL(deliv)}",
                    )
                    runlist.append(f"{wid}\t{REL(BOARD / (wid + '-' + slug + '.md'))}\t{REL(deliv)}\t{wtitle}")
                    last = wid
                # L3 조립체 취합 (sonnet) — after: 마지막 잎
                n += write_post(
                    f"{aid}-assembly.md", id=aid, title=f"{asm_title} 취합·판정",
                    parent=sid, after=last, track=sub,
                    body=f"잎 Work {len(works)}건의 결과를 검토해 조립체 판정을 산출물"
                         f" 파일 머리에 남긴다. 산출물: {REL(deliv)}",
                )
            (RUNS / f"{sid}.txt").write_text("\n".join(runlist) + "\n", encoding="utf-8")
    print(f"게시글 {n}건 생성 (이미 있던 파일은 건너뜀). 총 {len(list(BOARD.glob('*.md')))}건.")


def asm_title_slug(title):
    return "asm"


if __name__ == "__main__":
    main()
