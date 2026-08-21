#!/usr/bin/env python3
"""K-SAT 4 Work Package 발행기 — SE 역할 Work(E-SE-WP)의 산출물.

규칙 v2.4: Work의 단위는 사람(역할)이다. 이 스크립트는 킥오프 시점에 확실한
필요만 — 각 역할이 다른 역할에게 넘겨야 하는 인수인계 패키지 — 를 발행한다
(계약된 개발 범위이므로 1절의 "확실한 필요" 조건을 충족). 시험·감사·통합에서
발견되는 필요(NCR 등)는 발행하지 않는다 — 그것은 발견될 때 올라온다.

조직 308명: SE 10 · 서브시스템 8×24(DSN4 ANL3 PRC2 MFG5 QA2 ASM3 TST3
LEAD1 DOC1) · AIT 25 · FAC 12 · SW 20 · GS 15 · HAR 10 · LV 8 · PA 10 · PM 6.
에이전트는 이 역할들을 나눠 맡는다(규칙 4절, 1:N).
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent   # examples/ksat4
BOARD = HERE / "board"
DELIV = HERE / "deliverables"
RUNS = HERE / "runlists"
REPO = HERE.parent.parent
REL = lambda p: p.relative_to(REPO).as_posix()

SUBS = [("STR", "구조"), ("TCS", "열제어"), ("EPS", "전력"), ("AOCS", "자세제어"),
        ("OBC", "탑재컴퓨터"), ("COMM", "통신"), ("PROP", "추진"), ("PAY", "탑재체")]
ASMS = ["A1", "A2", "A3", "A4"]

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
(담당 역할: {role} — owner에는 take 시 이 역할 이름을 쓴다)
"""

made = 0


def post(fid, id, title, parent, after, track, role, body):
    global made
    p = BOARD / f"{fid}.md"
    if p.exists():
        return
    p.write_text(TPL.format(id=id, title=title, parent=parent, after=after,
                            track=track, role=role, body=body), encoding="utf-8")
    made += 1


def phase(ph, ph_name, gate):
    """ph: 'E'/'F', gate: 이 페이즈 시작 게이트가 되는 after id."""
    runs = {}

    def run(agent, fid, deliv, title):
        runs.setdefault(agent, []).append(
            f"{fid}\t{REL(BOARD / (fid + '.md'))}\t{deliv}\t{title}")

    for sub, sub_name in SUBS:
        t = sub
        d = DELIV / sub
        d.mkdir(parents=True, exist_ok=True)
        agent = f"haiku-{sub.lower()}-{ph.lower()}"
        pid = f"{ph}-{sub}"
        # 서브시스템 페이즈 취합(LEAD) — 부모 역할
        lead_after = f"{ph}-{sub}-T3" if ph == "E" else f"{ph}-{sub}-T2"
        post(pid + "-L1", f"{pid}-L1", f"{sub_name} {ph_name} 취합·판정", f"{ph}-PHASE",
             lead_after, t, f"{sub}-LEAD-01",
             f"{sub_name} 팀의 {ph_name} 결과(시험 보고까지)를 취합해 판정을 남긴다.\n"
             f"산출물: {REL(d / f'summary-{ph.lower()}.md')}")
        # 설계
        n_dsn = 4 if ph == "E" else 2
        for k in range(1, n_dsn + 1):
            asm = ASMS[k - 1]
            body = (f"{sub_name} 조립체 {asm}의 {'설계 패키지' if ph == 'E' else '설계 갱신(EM 결과 반영)'}. "
                    f"해석·구매·제작 역할들이 이 산출물을 입력으로 쓴다.\n"
                    f"산출물: {REL(d / f'dsn-{asm.lower()}-{ph.lower()}.md')}")
            after = f"E-SE-ICD-{sub}" if ph == "E" else f"E-PHASE, E-{sub}-L1"
            fid = f"{pid}-D{k}"
            post(fid, fid, f"{sub_name} {asm} {'설계' if ph == 'E' else 'FM 설계갱신'}",
                 pid + "-L1", after, t, f"{sub}-DSN-{k:02d}", body)
            run(agent, fid, REL(d / f"dsn-{asm.lower()}-{ph.lower()}.md"), f"{asm} 설계")
        dsn_all = ", ".join(f"{pid}-D{k}" for k in range(1, n_dsn + 1))
        # 해석 (EM만 3건)
        if ph == "E":
            for k, name in [(1, "구조 해석"), (2, "열 해석"), (3, "전력·EMC 해석")]:
                fid = f"{pid}-N{k}"
                post(fid, fid, f"{sub_name} {name}", pid + "-L1", dsn_all, t,
                     f"{sub}-ANL-{k:02d}",
                     f"설계 패키지 4건을 입력으로 {name}을 수행해 마진을 보고한다.\n"
                     f"산출물: {REL(d / 'anl-em.md')} (해석 역할 3명이 같은 파일에 절을 덧붙인다)")
                run(agent, fid, REL(d / "anl-em.md"), name)
        # 구매
        for k in range(1, 3):
            fid = f"{pid}-P{k}"
            post(fid, fid, f"{sub_name} {'부품 구매' if ph == 'E' else '비행부품 구매'} {k}",
                 pid + "-L1", dsn_all, t, f"{sub}-PRC-{k:02d}",
                 f"설계 BOM의 {'개발용' if ph == 'E' else '비행 등급'} 부품 발주·입고 기록.\n"
                 f"산출물: {REL(d / f'parts-{ph.lower()}.md')} (구매 2명이 같은 파일에 덧붙인다)")
            run(agent, fid, REL(d / f"parts-{ph.lower()}.md"), "부품 구매")
        # 제작 (EM 5 = A1..A4 + 치구, FM 4)
        n_mfg = 5 if ph == "E" else 4
        for k in range(1, n_mfg + 1):
            target = "치구" if (ph == "E" and k == 5) else f"조립체 {ASMS[min(k, 4) - 1]}"
            dep = f"{pid}-P{1 if k <= 2 else 2}" + (f", {pid}-D{min(k, n_dsn)}" if True else "")
            extra = f", {pid}-N1" if ph == "E" and k <= 4 else ""
            fid = f"{pid}-M{k}"
            bl = d / f"build-{ASMS[min(k, 4) - 1].lower()}-{ph.lower()}.md"
            post(fid, fid, f"{sub_name} {target} {'시제 제작' if ph == 'E' else '비행품 제작'}",
                 pid + "-L1", dep + extra, t, f"{sub}-MFG-{k:02d}",
                 f"{target}의 제작 기록을 빌드로그에 남긴다.\n산출물: {REL(bl)}")
            run(agent, fid, REL(bl), f"{target} 제작")
        # 검사
        for k, dep in [(1, f"{pid}-M1, {pid}-M2"), (2, f"{pid}-M3, {pid}-M4")]:
            fid = f"{pid}-Q{k}"
            post(fid, fid, f"{sub_name} {'공정 검사' if ph == 'E' else '수락 검사'} {k}",
                 pid + "-L1", dep, t, f"{sub}-QA-{k:02d}",
                 f"제작품의 치수·워크맨십 검사 판정을 빌드로그에 덧붙인다.\n"
                 f"산출물: {REL(d / f'build-a{k}-{ph.lower()}.md')}")
            run(agent, fid, REL(d / f"build-a{k}-{ph.lower()}.md"), "검사")
        # 조립 (EM 3, FM 2)
        n_asm = 3 if ph == "E" else 2
        for k in range(1, n_asm + 1):
            fid = f"{pid}-S{k}"
            post(fid, fid, f"{sub_name} 조립 {k}단계", pid + "-L1",
                 f"{pid}-Q1, {pid}-Q2" if k == 1 else f"{pid}-S{k-1}", t,
                 f"{sub}-ASM-{k:02d}",
                 f"조립 {k}단계 기록.\n산출물: {REL(d / f'build-a1-{ph.lower()}.md')}")
            run(agent, fid, REL(d / f"build-a1-{ph.lower()}.md"), f"조립 {k}")
        # 시험 (EM: 절차/수행/보고, FM: 수행/보고) — 수행은 공용 시설 슬롯 게이트
        si = SUBS.index((sub, sub_name))
        slot = f"{ph}-FAC-V{si % 4 + 1}" if si < 4 else f"{ph}-FAC-T{si % 4 + 1}"
        if ph == "E":
            post(f"{pid}-T1", f"{pid}-T1", f"{sub_name} 기능시험 절차", pid + "-L1",
                 f"{pid}-S3", t, f"{sub}-TST-01",
                 f"시험 절차서.\n산출물: {REL(d / 'test-em.md')}")
            run(agent, f"{pid}-T1", REL(d / "test-em.md"), "시험 절차")
            post(f"{pid}-T2", f"{pid}-T2", f"{sub_name} 기능시험 수행", pid + "-L1",
                 f"{pid}-T1, {slot}", t, f"{sub}-TST-02",
                 f"시설 슬롯({slot})을 기다려 수행한다 — 공용 자원 게이트.\n"
                 f"산출물: {REL(d / 'test-em.md')}")
            run(agent, f"{pid}-T2", REL(d / "test-em.md"), "시험 수행")
            post(f"{pid}-T3", f"{pid}-T3", f"{sub_name} 시험 보고", pid + "-L1",
                 f"{pid}-T2", t, f"{sub}-TST-03",
                 f"결과 정리와 판정.\n산출물: {REL(d / 'test-em.md')}")
            run(agent, f"{pid}-T3", REL(d / "test-em.md"), "시험 보고")
        else:
            post(f"{pid}-T1", f"{pid}-T1", f"{sub_name} 수락시험 수행", pid + "-L1",
                 f"{pid}-S{n_asm}, {slot}", t, f"{sub}-TST-01",
                 f"수락 수준 시험(시설 슬롯 {slot} 게이트).\n산출물: {REL(d / 'test-fm.md')}")
            run(agent, f"{pid}-T1", REL(d / "test-fm.md"), "수락시험")
            post(f"{pid}-T2", f"{pid}-T2", f"{sub_name} 수락시험 보고", pid + "-L1",
                 f"{pid}-T1", t, f"{sub}-TST-02",
                 f"판정 보고.\n산출물: {REL(d / 'test-fm.md')}")
            run(agent, f"{pid}-T2", REL(d / "test-fm.md"), "수락 보고")
        # 형상 문서
        post(f"{pid}-C1", f"{pid}-C1", f"{sub_name} 형상문서 갱신", pid + "-L1",
             f"{pid}-T3" if ph == "E" else f"{pid}-T2", t, f"{sub}-DOC-01",
             f"도면·이력 정리.\n산출물: {REL(d / f'cfg-{ph.lower()}.md')}")
        run(agent, f"{pid}-C1", REL(d / f"cfg-{ph.lower()}.md"), "형상문서")

    # 지원 조직 (support runlist 하나로)
    sup = f"haiku-sup-{ph.lower()}"
    dsup = DELIV / "support"
    dsup.mkdir(parents=True, exist_ok=True)
    for i in range(1, 5):
        for code, fac_name in [("V", "진동시험 슬롯"), ("T", "열진공 슬롯")]:
            fid = f"{ph}-FAC-{code}{i}"
            post(fid, fid, f"{fac_name} {i} 준비·운용", f"{ph}-PHASE", gate, "FAC",
                 f"FAC-{(i if code == 'V' else i + 4):02d}",
                 f"공용 시설 슬롯 — 서브시스템 시험 수행의 선행이다.\n"
                 f"산출물: {REL(dsup / f'fac-{ph.lower()}.md')}")
            run(sup, fid, REL(dsup / f"fac-{ph.lower()}.md"), fac_name)
    n_sw = 10
    for i in range(1, n_sw + 1):
        fid = f"{ph}-SW-{i:02d}"
        post(fid, fid, f"비행SW {'모듈' if ph == 'E' else '통합·검증'} {i}", f"{ph}-PHASE",
             f"E-OBC-D1" if ph == "E" else "E-PHASE", "SW",
             f"SW-{(i if ph == 'E' else i + 10):02d}",
             f"비행 소프트웨어 {i}.\n산출물: {REL(dsup / f'sw-{ph.lower()}.md')}")
        run(sup, fid, REL(dsup / f"sw-{ph.lower()}.md"), "비행SW")
    n_gs = 8 if ph == "E" else 7
    for i in range(1, n_gs + 1):
        fid = f"{ph}-GS-{i:02d}"
        post(fid, fid, f"지상국 {'구축' if ph == 'E' else '운용 리허설'} {i}", f"{ph}-PHASE",
             gate, "GS", f"GS-{(i if ph == 'E' else i + 8):02d}",
             f"지상국 {i}.\n산출물: {REL(dsup / f'gs-{ph.lower()}.md')}")
        run(sup, fid, REL(dsup / f"gs-{ph.lower()}.md"), "지상국")
    n_har = 8 if ph == "E" else 6
    for i in range(1, n_har + 1):
        fid = f"{ph}-HAR-{i:02d}"
        post(fid, fid, f"하니스 {'설계·제작' if ph == 'E' else '비행품'} {i}", f"{ph}-PHASE",
             gate, "HAR", f"HAR-{(i if ph == 'E' else i + 4):02d}",
             f"하니스 {i}.\n산출물: {REL(dsup / f'har-{ph.lower()}.md')}")
        run(sup, fid, REL(dsup / f"har-{ph.lower()}.md"), "하니스")
    for i in range(1, 5):
        fid = f"{ph}-LV-{i:02d}"
        post(fid, fid, f"발사체 연계 {i}", f"{ph}-PHASE", gate, "LV",
             f"LV-{(i if ph == 'E' else i + 4):02d}",
             f"발사체 인터페이스 {i}.\n산출물: {REL(dsup / f'lv-{ph.lower()}.md')}")
        run(sup, fid, REL(dsup / f"lv-{ph.lower()}.md"), "발사체 연계")
    for i in range(1, 4):
        fid = f"{ph}-PM-{i:02d}"
        post(fid, fid, f"{ph_name} 마일스톤 리뷰 {i}", f"{ph}-PHASE", gate, "PM",
             f"PM-{(i if ph == 'E' else i + 3):02d}",
             f"리뷰 회의록 {i}.\n산출물: {REL(dsup / f'pm-{ph.lower()}.md')}")
        run(sup, fid, REL(dsup / f"pm-{ph.lower()}.md"), "리뷰")
    # AIT (수행은 sonnet 담당 — runlist에 넣지 않는다: 정합 실검사·NCR 발견 역할)
    subs_l1 = ", ".join(f"{ph}-{s}-L1" for s, _ in SUBS)
    for i, nm in enumerate(["전기 통합", "기능 통합", "환경 통합"], 1):
        fid = f"{ph}-AIT-{i}"
        post(fid, fid, f"{ph_name} {nm} 시험", f"{ph}-PHASE",
             subs_l1 if i == 1 else f"{ph}-AIT-{i-1}", "AIT",
             f"AIT-{(i if ph == 'E' else i + 12):02d}",
             f"서브시스템 산출물 전체의 정합을 실제로 대조한다. 불일치는 NCR\n"
             f"게시글로 올린다(발견되는 필요).\n산출물: {REL(dsup / f'ait-{ph.lower()}.md')}")
    # 페이즈 취합 (SE)
    post(f"{ph}-PHASE", f"{ph}-PHASE", f"{ph_name} 판정", "K4",
         f"{ph}-AIT-3" + ("" if ph == "E" else ""), "SE", "SE-01",
         f"{ph_name} 전체 판정.\n산출물: {REL(DELIV / f'{ph.lower()}-decision.md')}")

    RUNS.mkdir(parents=True, exist_ok=True)
    for agent, lines in runs.items():
        (RUNS / f"{agent}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    BOARD.mkdir(parents=True, exist_ok=True)
    phase("E", "EM", "E-SE-WP")
    phase("F", "FM", "E-PHASE")
    print(f"게시글 {made}건 발행. 총 {len(list(BOARD.glob('*.md')))}건, "
          f"runlist {len(list(RUNS.glob('*.txt')))}개.")


if __name__ == "__main__":
    main()
