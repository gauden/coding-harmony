# Music Theory Through Sonic Pi

Music theory for people who already write code.

The audience is programmers who are at ease with arrays, functions, and threads,
and who cannot read a note. [Sonic Pi](https://sonic-pi.net/) is the laboratory.
Each lesson takes one musical idea, encodes it as data, plays it, and asks you to
change something and listen to what happened.

This is not the Sonic Pi tutorial. That one teaches programming and uses music as
the reward. Here the programming is assumed, and Ruby idioms get a one-line note
the first time they appear.

## Status

Early. The syllabus and the build plan are written. The lessons are not.

## What is here

Both files are self-contained HTML. Clone the repo and open them in a browser.

| File | What it is |
|---|---|
| [`curriculum/music_theory_through_sonic_pi.html`](curriculum/music_theory_through_sonic_pi.html) | The syllabus. 58 lessons across 13 parts, with progress tracking and search. |
| [`curriculum/plan.html`](curriculum/plan.html) | How the site and book get built. Toolchain, repository layout, lesson template, audio workflow, writing standard, five phases. Interactive, with a notes export. |

## Where it is going

The lessons will be Quarto `.qmd` files, which are Markdown with a YAML header.
One source tree renders to a GitHub Pages site and to PDF and EPUB for the book.
Every example that produces sound gets a recording next to it on the website.

## Requirements

Sonic Pi 4 or later, from [sonic-pi.net](https://sonic-pi.net/). Check that
`play 60` makes a noise and you are ready to start. Headphones or decent speakers
will do more for your progress than any other purchase, because half of this
course is hearing small differences.

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
