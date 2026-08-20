# Music Theory Through Sonic Pi

Music theory for people who already write code.

The audience is programmers who are at ease with arrays, functions, and threads
and who cannot read a note. [Sonic Pi](https://sonic-pi.net/) is the laboratory.
Each lesson takes one musical idea, encodes it as data, plays it, and asks you to
change one input and listen again.

This is a music-theory course rather than a general Sonic Pi tutorial.
Programming is assumed. Ruby idioms receive a short explanation when they first
appear and a fuller reference in the appendices.

The book uses a field-notes voice: first person for the writer, second person for
the reader, with no motivational filler. The rules are in [`STYLE.md`](STYLE.md).

## Status

The complete first draft is present: 58 lessons across 13 parts, the preface and
setup chapter, five reference appendices, and worked entries for all 58 optional
exercises. Every lesson is marked `draft`.

The rendered draft is globally attributed to **GPT 5.6 Sol at High Reasoning**.
It is being tested and completely rewritten by hand before any human-authored
edition is claimed.

`draft` means the planned lesson has substantive prose and a Ruby example, and
the extracted Ruby clears syntax checks. It does not mean the examples have been
auditioned end to end in Sonic Pi. Timing, synth balance, Sonic Pi API behaviour,
and listening claims remain manual QA. Lessons move to `tested` only after a
human works through them from a cold start and the prose is revised from field
notes. Recordings are added after that pass; empty `audio=""` attributes are
intentional in the draft.

The syllabus remains the source of truth for lesson order and titles.
`scripts/gen_book.py` regenerates the chapter manifest and can scaffold a newly
added lesson. It is not part of ordinary prose editing.

## What is here

| File | What it is |
|---|---|
| [`index.qmd`](index.qmd) | Preface, course method, working rhythm, and status model. |
| [`setup.qmd`](setup.qmd) | Sonic Pi version, first sound, window orientation, and reader workflow. |
| [`curriculum/music_theory_through_sonic_pi.html`](curriculum/music_theory_through_sonic_pi.html) | The 58-lesson syllabus and searchable course map. |
| [`curriculum/plan.html`](curriculum/plan.html) | Build, audio, testing, and publication decisions. |
| [`appendix/`](appendix/) | Ruby guide, Sonic Pi cheat sheet, solutions, glossary, and sources ledger. |
| [`STYLE.md`](STYLE.md) | House voice and prose constraints. |
| [`WRITING_BRIEF.md`](WRITING_BRIEF.md) | Lesson, code, and continuity contracts for contributors. |
| [`TODO.md`](TODO.md) | Durable first-draft and integration checklist. |
| [`DEVELOPMENT.md`](DEVELOPMENT.md) | Resume protocol, session record, checks, and deferred QA. |

The two curriculum documents are self-contained HTML. Clone the repository and
open them in a browser; their local progress state does not alter the manuscript.

## Reading it

Install Sonic Pi 5.0.0 and begin with [`setup.qmd`](setup.qmd). Lessons are meant
to run in order because the data model grows across parts. Run each code block in
a fresh buffer unless it declares a continuation. Make the *Change one thing*
edits separately, then attempt *Take it further* before opening the corresponding
solution.

Headphones or speakers with usable bass response help when comparing small
differences. Keep playback at a comfortable level during repeated ear drills.

## Building and checking it

Lessons are Quarto `.qmd` files. The project is configured to produce a website,
PDF, and EPUB from the same sources.

```bash
quarto render --to html
```

The HTML build writes to `_book/`. PDF output also needs TinyTeX, installed with
`quarto install tinytex`.

Run the automated manuscript checks before proposing a change:

```bash
uv run pytest
scripts/lint-prose.sh
scripts/extract-code.sh
scripts/check-code.sh
```

These checks cover structure, placeholders, house-style patterns, and Ruby
syntax. They cannot confirm that Sonic Pi accepts every call or that an example
sounds as described.

## Contributing and resuming

Read [`TODO.md`](TODO.md) and [`DEVELOPMENT.md`](DEVELOPMENT.md) before choosing
work. `DEVELOPMENT.md` records the current phase and the manual checks still
owed. Read [`WRITING_BRIEF.md`](WRITING_BRIEF.md) before changing a lesson, then
apply [`STYLE.md`](STYLE.md) to prose.

Keep lesson status at `draft` unless you personally run the complete lesson in
Sonic Pi from a clean state, record field notes, and revise the lesson from that
attempt. Do not invent audio filenames, source details, or runtime results. Keep
score data separate from rendering logic and preserve the shared event keys
`:note`, `:start`, and `:duration`.

For a resumed Codex session, say `resume`. The durable protocol is at the top of
[`DEVELOPMENT.md`](DEVELOPMENT.md).
