#!/usr/bin/env python3
"""Report STYLE.md voice metrics for one or more prose files."""
import re, sys, statistics, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tests"))
from test_book_draft import prose, sentences, contractions, HEDGES, word_count, heading_signature

for arg in sys.argv[1:]:
    p = pathlib.Path(arg); raw = p.read_text(); t = prose(raw)
    s = sentences(t)
    art = sum(1 for x in s if re.match(r"(The|A|An)\s", x))
    short = sum(1 for x in s if len(x.split()) < 8)
    you = len(re.findall(r"\b(you|your|you'\w+)\b", t, re.I))
    flags = []
    if len(contractions(t)) < 3: flags.append("CONTRACTIONS")
    if you < 8: flags.append("YOU")
    if s and art/len(s) > 0.35: flags.append("ARTICLES")
    if "?" not in t and "/parts/" in str(p.resolve()): flags.append("QUESTION")
    if short < 2: flags.append("SHORT-SENTENCES")
    if len(HEDGES.findall(t)) > 3: flags.append("HEDGES")
    if t.count("—") > 1: flags.append("EMDASH")
    if len(re.findall(r"\b(rather than|instead of)\b", t, re.I)) > 2: flags.append("CONTRAST")
    if "/parts/" in str(p.resolve()):
        if len(re.findall(r"^## ", raw.split('---',2)[-1], re.M)) < 3: flags.append("SECTIONS")
        if not re.search(r"^\d+\.\s", raw.split('---',2)[-1], re.M): flags.append("NO-NUMBERED-LIST")
        if word_count(raw) < 350: flags.append("TOO-SHORT")
    print(f"{'FAIL' if flags else 'ok  '} {p.name:52} w={word_count(raw):4} you={you:3} "
          f"con={len(contractions(t)):2} short={short:2} art={art/len(s)*100 if s else 0:3.0f}% "
          f"hedge={len(HEDGES.findall(t)):2} {' '.join(flags)}")
