# Music Theory Through Sonic Pi

Music theory for people who already write code.

The audience is programmers who are at ease with arrays, functions, and threads,
and who cannot read a note. [Sonic Pi](https://sonic-pi.net/) is the laboratory.
Each lesson takes one musical idea, encodes it as data, plays it, and asks for one
change so we can hear what the change did.

This is not the Sonic Pi tutorial. That one teaches programming and uses music as
the reward. Here the programming is assumed, and Ruby idioms get a one-line note
the first time they appear.

The prose is first person plural and deliberately unencouraging. The rules are in
[`STYLE.md`](STYLE.md).

## Status

Early. The syllabus, the build plan, and the book scaffold are done. The lessons
are not written yet.

The book renders to a website, a PDF, and an EPUB from one Markdown source.
`scripts/gen_book.py` generates the chapter list and one stub per lesson from the
syllabus, so the syllabus stays the single source of truth for what exists.

## What is here

The two planning documents are self-contained HTML. Clone the repo and open them
in a browser.

| File | What it is |
|---|---|
| [`curriculum/music_theory_through_sonic_pi.html`](curriculum/music_theory_through_sonic_pi.html) | The syllabus. 58 lessons across 13 parts, with progress tracking and search. |
| [`curriculum/plan.html`](curriculum/plan.html) | How the site and book get built. Toolchain, repository layout, lesson template, audio workflow, writing standard, five phases. Interactive, with a notes export. |
| [`STYLE.md`](STYLE.md) | The prose rules, starting with the voice. |

## Building it

Lessons are Quarto `.qmd` files, which are Markdown with a YAML header. Every
example that produces sound gets a recording next to it on the website.

```bash
quarto render
```

That produces `_book/` with the site, the PDF, and the EPUB. Needs
[Quarto](https://quarto.org/) and, for the PDF, `quarto install tinytex`.

## Requirements

Sonic Pi 5.0.0, from [sonic-pi.net](https://sonic-pi.net/). Every example is
written and recorded against that version. Check that `play 60` makes a noise and
we are ready to start.

Headphones or decent speakers do more for progress here than any other purchase,
because half of this course is hearing small differences.

## Licence

Two licences, following the arrangement Allen Downey uses for
[Think Python](https://github.com/AllenDowney/ThinkPython).

**Code** is [MIT](https://mit-license.org/). The Sonic Pi examples, the scripts,
the filters, and the build configuration. Copy any snippet into your own work,
including work you sell.

**Text** is [CC BY-NC-SA
4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). The lesson prose, the
curriculum, the diagrams, and the audio. Share and adapt it non-commercially,
with attribution, under the same terms.

Full terms in [`LICENSE.md`](LICENSE.md). Public-domain scores and recordings
used as transcription material carry their own licences and are listed with their
sources.

Copyright 2026 Gauden Galea.
