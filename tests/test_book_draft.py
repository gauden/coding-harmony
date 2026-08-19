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
    assert "tested and completely rewritten by hand" in body[:first_section]
    assert "https://github.com/gauden/coding-harmony/pulls" in body[:first_section]
    assert "limited capacity to respond" in body[:first_section]
