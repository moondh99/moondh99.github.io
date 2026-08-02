#!/usr/bin/env python3
"""브리프 준수 체크. 실행: python3 .orca/check_structure.py"""
import re, sys, pathlib

HTML = pathlib.Path(__file__).parent.parent / "index.html"
s = HTML.read_text(encoding="utf-8")

STEPS = ["문제 정의", "리서치·가설", "기획 프로세스", "결과·임팩트"]
# 브리프 §2 금지 조합 + 팔레트 밖 하드코딩 색상 (토큰 var() 만 허용)
ALLOWED_HEX = {
    "#f7f7f5", "#ffffff", "#1d2320", "#5b645f", "#67706a", "#e3e6e2",
    "#0e6e5c", "#e3f0ec", "#eef1ee", "#3d4642",
    "#121614", "#1a201d", "#e7ebe8", "#a4ada7", "#8b958f", "#2a322e",
    "#3fbba0", "#1c2f2a", "#232a26", "#c3cbc6",
}

fails = []

# 1) Featured Projects 4건 각각 4단 서사, 순서 고정
projects = re.findall(r'<article class="proj"[^>]*>.*?</article>', s, re.S)
assert projects, "no .proj articles found"
if len(projects) != 4:
    fails.append(f"Featured Projects 4건이어야 하는데 {len(projects)}건")
for i, a in enumerate(projects, 1):
    title = re.search(r"<h3>(.*?)<", a).group(1)
    got = [re.sub(r"<.*?>", "", d).strip() for d in re.findall(r"<dt>(.*?)</dt>", a, re.S)]
    got = [re.sub(r"^\d\d", "", g).strip() for g in got]
    if got != STEPS:
        fails.append(f"프로젝트 {i} ({title}) 서사 순서 불일치: {got}")

# 2) 정량 수치는 chips 로 먼저 스캔 가능해야 함 (chips 가 dl 보다 앞)
for i, a in enumerate(projects, 1):
    ci, di = a.find('class="chips"'), a.find('<dl class="pa">')
    if ci == -1 or di == -1 or ci > di:
        fails.append(f"프로젝트 {i}: chips 가 dl.pa 보다 앞에 있어야 함")

# 3) 팔레트 밖 색상 하드코딩 금지 (rgba() 그림자는 예외)
for hexv in set(re.findall(r"#[0-9a-fA-F]{6}\b", s)):
    if hexv.lower() not in ALLOWED_HEX:
        fails.append(f"팔레트 밖 색상 하드코딩: {hexv}")

# 4) h1 은 정확히 1개
n_h1 = len(re.findall(r"<h1[\s>]", s))
if n_h1 != 1:
    fails.append(f"h1 은 1개여야 하는데 {n_h1}개")

# 5) 브레이크포인트는 600px 하나만 (브리프 §4)
bps = set(re.findall(r"@media\s*\(max-width:\s*(\d+)px\)", s))
if bps - {"600"}:
    fails.append(f"허용되지 않은 브레이크포인트: {sorted(bps - {'600'})}")

# 6) 320px 오버플로 가드 — 뷰포트 320 - .wrap 좌우 패딩 48 = 콘텐츠 272px
NARROW = 320 - 48
for track in re.findall(r"minmax\((\d+)px", s):
    if int(track) > NARROW:
        fails.append(f"minmax({track}px) 가 320px 화면 콘텐츠 폭 {NARROW}px 초과")
for cols in re.findall(r"grid-template-columns:\s*([^;}]+)", s):
    fixed = [int(x) for x in re.findall(r"(\d+)px", cols)]
    if fixed and sum(fixed) > NARROW:
        fails.append(f"고정 컬럼 합 {sum(fixed)}px 가 {NARROW}px 초과: {cols.strip()}")

# 7) 접근성 기본 — skip link, main, 섹션 aria-labelledby
if 'href="#main"' not in s or 'id="main"' not in s:
    fails.append("skip-to-content 링크 또는 #main 대상 없음")
for sec in re.findall(r"<section\b[^>]*>", s):
    if "aria-labelledby" not in sec:
        fails.append(f"aria-labelledby 없는 section: {sec}")

if fails:
    print("FAIL")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print(f"OK — 프로젝트 {len(projects)}건 4단 서사, 팔레트 준수, h1 1개")
