import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSONS = sorted((ROOT / "parts").glob("*/*.qmd"))
REQUIRED_HEADINGS = (
    "## The idea",
    "## Run this",
    "## Change one thing",
    "## Why it works",
    "## Take it further",
)


def front_matter(text: str) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "missing YAML front matter"
    return match.group(1)


def ruby_blocks(text: str) -> list[str]:
    pattern = re.compile(
        r"^```(?:ruby|\{\.ruby[^}]*\})\s*$\n(.*?)^```\s*$",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.findall(text)


def test_curriculum_keeps_exactly_58_lessons() -> None:
    assert len(LESSONS) == 58
    assert [int(path.name.split("-", 1)[0]) for path in LESSONS] == list(range(1, 59))


def test_every_lesson_is_a_substantive_draft() -> None:
    failures: list[str] = []
    for path in LESSONS:
        text = path.read_text(encoding="utf-8")
        metadata = front_matter(text)
        problems: list[str] = []
        if not re.search(r"^status:\s*draft\s*$", metadata, re.MULTILINE):
            problems.append("status is not draft")
        if "Planned, from the syllabus" in text:
            problems.append("generated planning callout remains")
        if re.search(r"\bTODO\b", text):
            problems.append("TODO placeholder remains")
        missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
        if missing:
            problems.append(f"missing headings: {', '.join(missing)}")
        blocks = ruby_blocks(text)
        if not blocks or all(not block.strip() or block.strip() == "# TODO" for block in blocks):
            problems.append("no substantive Ruby example")
        words = re.findall(r"\b[\w'-]+\b", text)
        if len(words) < 550:
            problems.append(f"only {len(words)} words; expected at least 550")
        if problems:
            failures.append(f"{path.relative_to(ROOT)}: {'; '.join(problems)}")
    assert not failures, "\n" + "\n".join(failures)


def test_front_and_back_matter_have_no_placeholders() -> None:
    paths = [ROOT / "index.qmd", ROOT / "setup.qmd", *(ROOT / "appendix").glob("*.qmd")]
    failures = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if re.search(r"\bTODO\b|Planned, from the syllabus", text):
            failures.append(str(path.relative_to(ROOT)))
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
    body = text.split("---\n", 2)[-1]
    warning = body.find('::: {.callout-warning')
    first_section = body.find("## How the lessons work")

    assert 0 <= warning < first_section
    assert "AI-generated" in body[:first_section]
    assert "revised and independently tested" in body[:first_section]
    assert "No human-authored edition is claimed" in body[:first_section]
    assert "under revision and testing" in body[:first_section]
    assert "under human rewrite" not in body[:first_section]
    assert "https://github.com/gauden/coding-harmony/pulls" in body[:first_section]
    assert "Individual responses may be" in body[:first_section]
    assert "limited" in body[:first_section]


def test_ai_draft_has_global_author_and_no_book_licence() -> None:
    config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    sources = (ROOT / "appendix" / "sources.qmd").read_text(encoding="utf-8")

    assert re.search(
        r'^author:\s*"GPT 5\.6 Sol at High Reasoning"\s*$',
        config,
        re.MULTILINE,
    )
    assert '  author: "GPT 5.6 Sol at High Reasoning"' in config
    assert "page-footer:" not in config
    assert not (ROOT / "LICENSE.md").exists()
    assert "## Licence" not in readme
    assert "LICENSE.md" not in readme
    assert "Copyright 2026" not in readme
    assert "CC BY-NC-SA" not in sources
    assert "MIT License" not in sources

    for path in [ROOT / "index.qmd", ROOT / "setup.qmd", *LESSONS, *(ROOT / "appendix").glob("*.qmd")]:
        metadata = front_matter(path.read_text(encoding="utf-8"))
        match = re.search(r"^author:\s*(.+)$", metadata, re.MULTILINE)
        assert match is None or "GPT 5.6 Sol at High Reasoning" in match.group(1)


def test_second_draft_uses_an_expository_voice() -> None:
    style = (ROOT / "STYLE.md").read_text(encoding="utf-8")
    required_principles = (
        "lead the reader",
        "unity",
        "rhythm",
        "humanity",
        "concrete detail",
    )
    missing = [principle for principle in required_principles if principle not in style.lower()]
    assert not missing, f"STYLE.md is missing expository principles: {', '.join(missing)}"

    repeated_protocol = (
        "After each edit, restore the original before trying the next one. "
        "This keeps the comparisons independent. Write one sentence about the change"
    )
    offenders = [
        str(path.relative_to(ROOT))
        for path in LESSONS
        if repeated_protocol in path.read_text(encoding="utf-8")
    ]
    assert not offenders, "canned lab-protocol prose remains in: " + ", ".join(offenders)


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
