"""Acceptance tests for the manuscript.

Two kinds of check live here. Structural tests keep the curriculum intact: 58
lessons in order, a worked solution for every exercise, a populated glossary.
Voice tests measure the prose against the mandates in STYLE.md.

The voice tests exist because the previous suite hard-coded five section
headings and a word floor into every lesson, and got 58 lessons of identical
shape as a result. A test that pins the form produces uniformity; these pin the
qualities that make prose readable and leave the form free.
"""

import re
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSONS = sorted((ROOT / "parts").glob("*/*.qmd"))
NARRATIVE = [ROOT / "index.qmd", ROOT / "setup.qmd", *LESSONS]

AUTHOR = "GPT 5.6 Sol at High Reasoning and Claude Opus 5"

# Weasel words that let a sentence avoid saying what the reader will hear.
# "can" and "whether" are deliberately absent: both have honest uses.
HEDGES = re.compile(
    r"\b(may|might|tends? to|is expected to|are expected to|presumably|"
    r"possibly|perhaps|arguably|somewhat)\b",
    re.IGNORECASE,
)
CONTRACTION = re.compile(
    r"\b\w+(?:'(?:s|t|re|ve|ll|d|m))\b(?<!\bit's)|"
    r"\b(?:don|doesn|didn|isn|aren|wasn|weren|can|won|couldn|shouldn|wouldn|"
    r"hasn|haven|hadn)'t\b|\b(?:you|we|they|it|that|there|here|I)'\w+",
    re.IGNORECASE,
)


def front_matter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "missing YAML front matter"
    return match.group(1)


def body(text: str) -> str:
    return text.split("---\n", 2)[-1]


def prose(text: str) -> str:
    """Body text with code blocks, callouts, and headings removed."""
    stripped = re.sub(r"^```.*?^```", "", body(text), flags=re.S | re.M)
    stripped = re.sub(r"^:::.*$", "", stripped, flags=re.M)
    stripped = re.sub(r"^#+ .*$", "", stripped, flags=re.M)
    stripped = re.sub(r"\{\{< include .*? >\}\}", "", stripped)
    return stripped


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in parts if len(s.split()) > 2]


def contractions(text: str) -> list[str]:
    """Verbal contractions only. Possessives like `chord's` do not count."""
    found = re.findall(r"\b(\w+)'(s|t|re|ve|ll|d|m)\b", text, re.IGNORECASE)
    verbal = []
    for stem, suffix in found:
        if suffix == "s" and stem.lower() not in {
            "it", "that", "here", "there", "what", "he", "she", "who", "let",
        }:
            continue  # possessive
        verbal.append(f"{stem}'{suffix}")
    return verbal


def heading_signature(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"^## (.+)$", body(text), re.MULTILINE))


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def ruby_blocks(text: str) -> list[str]:
    pattern = re.compile(
        r"^```(?:ruby|\{\.ruby[^}]*\})\s*$\n(.*?)^```\s*$",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.findall(text)


def report(failures: list[str], label: str) -> None:
    assert not failures, f"{label}\n  " + "\n  ".join(failures)


# ---------------------------------------------------------------------------
# Structure
# ---------------------------------------------------------------------------


def test_curriculum_keeps_exactly_58_lessons() -> None:
    assert len(LESSONS) == 58
    assert [int(path.name.split("-", 1)[0]) for path in LESSONS] == list(range(1, 59))


def test_every_lesson_is_a_substantive_draft() -> None:
    """Each lesson teaches, demonstrates, prompts a variation, and sets work.

    Deliberately silent about what those sections are called. The old suite
    named them and every lesson came out the same shape.
    """
    failures: list[str] = []
    for path in LESSONS:
        text = path.read_text(encoding="utf-8")
        metadata = front_matter(text)
        problems: list[str] = []

        if not re.search(r"^status:\s*(draft|tested)\s*$", metadata, re.MULTILINE):
            problems.append("status is not draft or tested")
        if "Planned, from the syllabus" in text:
            problems.append("generated planning callout remains")
        if re.search(r"\bTODO\b", text):
            problems.append("TODO placeholder remains")

        blocks = ruby_blocks(text)
        if not blocks or all(not b.strip() or b.strip() == "# TODO" for b in blocks):
            problems.append("no substantive Ruby example")
        if len(re.findall(r"^## ", body(text), re.MULTILINE)) < 3:
            problems.append("fewer than three sections")
        if not re.search(r"^\d+\.\s", body(text), re.MULTILINE):
            problems.append("no numbered variation to try")

        count = word_count(text)
        if count < 350:
            problems.append(f"only {count} words; expected at least 350")

        if problems:
            failures.append(f"{path.relative_to(ROOT)}: {'; '.join(problems)}")
    report(failures, "lessons are not substantive drafts:")


def test_lessons_are_not_all_one_template() -> None:
    """Section headings must describe their lesson, not fill a slot.

    Before this test, 58 of 58 lessons carried the identical five headings.
    """
    signatures = {heading_signature(p.read_text(encoding="utf-8")) for p in LESSONS}
    assert len(signatures) >= 25, (
        f"only {len(signatures)} distinct heading patterns across 58 lessons; "
        "headings should name what the section teaches"
    )

    generic = {"the idea", "run this", "why it works", "take it further"}
    overused = [
        heading
        for heading in generic
        if sum(
            1
            for p in LESSONS
            if heading in [h.lower() for h in heading_signature(p.read_text(encoding="utf-8"))]
        )
        > 20
    ]
    assert not overused, f"generic headings used in more than 20 lessons: {overused}"


def test_lesson_length_varies_with_the_material() -> None:
    counts = [word_count(p.read_text(encoding="utf-8")) for p in LESSONS]
    assert min(counts) < 700, (
        f"shortest lesson is {min(counts)} words; some ideas need less room"
    )
    assert max(counts) > 1100, (
        f"longest lesson is {max(counts)} words; some ideas need more room"
    )
    assert statistics.pstdev(counts) > 110, (
        f"length spread is only {statistics.pstdev(counts):.0f} words; "
        "every lesson is being written to the same size"
    )


# ---------------------------------------------------------------------------
# Voice, per STYLE.md
# ---------------------------------------------------------------------------


def test_prose_uses_contractions() -> None:
    """STYLE.md mandate 1. The previous draft contained zero in 41,000 words."""
    failures = []
    for path in NARRATIVE:
        found = contractions(prose(path.read_text(encoding="utf-8")))
        if len(found) < 3:
            failures.append(f"{path.relative_to(ROOT)}: {len(found)} contractions")
    report(failures, "prose reads too formally (STYLE.md: use contractions):")


def test_prose_addresses_the_reader() -> None:
    """STYLE.md mandate 2. Put a person in the sentence."""
    failures = []
    for path in NARRATIVE:
        text = prose(path.read_text(encoding="utf-8"))
        second_person = len(re.findall(r"\b(you|your|you'\w+)\b", text, re.IGNORECASE))
        if second_person < 8:
            failures.append(f"{path.relative_to(ROOT)}: 'you' appears {second_person} times")
    report(failures, "prose does not address the reader (STYLE.md: put a person in the sentence):")


def test_prose_does_not_open_every_sentence_with_an_article() -> None:
    """A page of 'The X is...' sentences is documentation, not teaching."""
    failures = []
    for path in NARRATIVE:
        opened = sentences(prose(path.read_text(encoding="utf-8")))
        if len(opened) < 10:
            continue
        articles = sum(1 for s in opened if re.match(r"(The|A|An)\s", s))
        share = articles / len(opened)
        if share > 0.35:
            failures.append(
                f"{path.relative_to(ROOT)}: {share:.0%} of sentences open with an article"
            )
    report(failures, "prose leads with abstract nouns (STYLE.md: put a person in the sentence):")


def test_every_lesson_asks_the_reader_something() -> None:
    """STYLE.md mandate 3. The previous draft had 8 question marks in 58 lessons."""
    failures = []
    for path in LESSONS:
        if "?" not in prose(path.read_text(encoding="utf-8")):
            failures.append(str(path.relative_to(ROOT)))
    report(failures, "lessons never ask the reader anything (STYLE.md: ask the reader something):")


def test_sentence_length_varies() -> None:
    """STYLE.md mandate 4. Every section needs one sentence under eight words."""
    failures = []
    for path in NARRATIVE:
        lengths = [len(s.split()) for s in sentences(prose(path.read_text(encoding="utf-8")))]
        if not lengths:
            continue
        short = sum(1 for n in lengths if n < 8)
        if short < 2:
            failures.append(
                f"{path.relative_to(ROOT)}: {short} sentences under 8 words "
                f"(mean {statistics.mean(lengths):.1f})"
            )
    report(failures, "prose has no rhythm (STYLE.md: vary the sentence length):")


def test_claims_about_sound_are_not_hedged() -> None:
    """STYLE.md: uncertainty lives in the status callout, not in every sentence."""
    failures = []
    for path in NARRATIVE:
        found = HEDGES.findall(prose(path.read_text(encoding="utf-8")))
        if len(found) > 3:
            failures.append(f"{path.relative_to(ROOT)}: {len(found)} hedges {sorted(set(found))}")
    report(failures, "claims are hedged (STYLE.md: commit to what the reader will hear):")


def test_em_dashes_stay_within_budget() -> None:
    """One per file. Not zero: banning it outright flattened every aside."""
    failures = []
    for path in NARRATIVE:
        count = prose(path.read_text(encoding="utf-8")).count("—")
        if count > 1:
            failures.append(f"{path.relative_to(ROOT)}: {count} em dashes")
    report(failures, "em dash budget exceeded (STYLE.md allows one per lesson):")


def test_contrast_formulas_are_not_a_reflex() -> None:
    """Banning 'not X but Y' produced 108 'rather than's. Cap the substitute too."""
    failures = []
    for path in NARRATIVE:
        text = prose(path.read_text(encoding="utf-8"))
        count = len(re.findall(r"\b(rather than|instead of)\b", text, re.IGNORECASE))
        if count > 2:
            failures.append(f"{path.relative_to(ROOT)}: {count} contrast formulas")
    report(failures, "contrast formulas used as filler (STYLE.md: handle with care):")


# ---------------------------------------------------------------------------
# Front matter, back matter, attribution
# ---------------------------------------------------------------------------


def test_front_and_back_matter_have_no_placeholders() -> None:
    paths = [ROOT / "index.qmd", ROOT / "setup.qmd", *(ROOT / "appendix").glob("*.qmd")]
    failures = [
        str(path.relative_to(ROOT))
        for path in paths
        if re.search(r"\bTODO\b|Planned, from the syllabus", path.read_text(encoding="utf-8"))
    ]
    assert not failures, f"placeholders remain in: {', '.join(failures)}"


def test_solutions_cover_every_lesson() -> None:
    text = (ROOT / "appendix" / "solutions.qmd").read_text(encoding="utf-8")
    numbers = [int(value) for value in re.findall(r"^###\s+(\d+)\.", text, re.MULTILINE)]
    assert numbers == list(range(1, 59))


def test_glossary_is_populated() -> None:
    text = (ROOT / "appendix" / "glossary.qmd").read_text(encoding="utf-8")
    assert "*Empty." not in text
    assert len(re.findall(r"^###\s+", text, re.MULTILINE)) >= 30


def test_preface_opens_with_ai_draft_warning() -> None:
    text = (ROOT / "index.qmd").read_text(encoding="utf-8")
    prefix = body(text)
    warning = prefix.find("::: {.callout-warning")
    first_section = prefix.find("\n## ")

    assert 0 <= warning < first_section
    disclosure = prefix[:first_section]
    assert "AI-generated" in disclosure
    assert "revised and independently tested" in disclosure
    assert "No human-authored edition is claimed" in disclosure
    assert "https://github.com/gauden/coding-harmony/pulls" in disclosure


def test_ai_draft_has_global_author_and_no_book_licence() -> None:
    config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    sources = (ROOT / "appendix" / "sources.qmd").read_text(encoding="utf-8")

    assert re.search(rf'^author:\s*"{re.escape(AUTHOR)}"\s*$', config, re.MULTILINE)
    assert f'  author: "{AUTHOR}"' in config
    assert "page-footer:" not in config
    assert not (ROOT / "LICENSE.md").exists()
    assert "## Licence" not in readme
    assert "LICENSE.md" not in readme
    assert "CC BY-NC-SA" not in sources
    assert "MIT License" not in sources

    for path in [ROOT / "index.qmd", ROOT / "setup.qmd", *LESSONS,
                 *(ROOT / "appendix").glob("*.qmd")]:
        metadata = front_matter(path.read_text(encoding="utf-8"))
        match = re.search(r"^author:\s*(.+)$", metadata, re.MULTILINE)
        assert match is None or AUTHOR in match.group(1)


def test_style_guide_leads_with_positive_mandates() -> None:
    """STYLE.md must specify a voice, not only prohibit one."""
    style = (ROOT / "STYLE.md").read_text(encoding="utf-8").lower()
    for mandate in (
        "use contractions",
        "put a person in the sentence",
        "ask the reader something",
        "vary the sentence length",
        "name the surprise",
        "commit to what the reader will hear",
    ):
        assert mandate in style, f"STYLE.md is missing the mandate: {mandate}"

    assert "the target voice" in style, "STYLE.md must model the voice, not just describe it"
    banned = style.index("## banned vocabulary")
    mandates = style.index("## six things to do")
    assert mandates < banned, "positive mandates must come before the ban list"


def test_worked_solutions_match_their_exercise_contracts() -> None:
    text = (ROOT / "appendix" / "solutions.qmd").read_text(encoding="utf-8")
    required_evidence = {
        "two distinct rhythms": "second pattern `[0.5, 0.5, 1, 0.25, 0.25, 0.5, 1]`",
        "tie crosses beat four": "G4 begins at beat 3.5",
        "enharmonic interval tests": "C-C-sharp as an augmented unison",
        "tendency tones resolve by semitone": "[43,47,53,62]` to `[43,48,52,60]",
        "contour is rebuilt": "contour = [60,60,62,62,64,64,62,60]",
        "period fits eight events": "common five-event opening",
        "decorations have harmonic context": "C5 at beat 3.5",
        "middle C is coordinate zero": "middle C at coordinate 0",
        "accidentals use letter-octave scope": "key = [event[:letter], event[:octave]]",
        "secondary dominant has explicit voice leading": "F-sharp3 rises to G3",
    }
    missing = [name for name, snippet in required_evidence.items() if snippet not in text]
    assert not missing, "solution regressions remain: " + ", ".join(missing)
