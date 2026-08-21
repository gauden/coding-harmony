# Development Record

## Resume protocol

When the user says `resume`, read `TODO.md`, this file, `STYLE.md`, and
`git status --short`. Continue from the first unticked item without regenerating
or overwriting completed prose. Run the focused tests for the files being changed
before advancing to the next phase. If every phase in `TODO.md` is ticked, report
that state and work from the "Still owed" list at the bottom of it.

Read Lessons 1 and 6 before writing any prose. `STYLE.md` describes the voice;
those lessons are the voice, and where the two seem to disagree the lessons win.

## Goal

*Music Theory Through Sonic Pi*: 58 sequential lessons, the front matter, and
five appendices, written so that a programmer who cannot read a note will
actually keep reading. The manuscript must hold together top to bottom while
staying honest that no example has been auditioned in Sonic Pi.

## Roles

- Coordinator: root Codex agent. Owns scope, tests, integration, progress records,
  and final verification.
- Writers: parallel agents assigned non-overlapping lesson ranges after the
  curriculum map is complete.
- Editor: a dedicated agent used after the draft ranges are integrated. Owns
  continuity and style findings; the coordinator owns final application and QA.

## Acceptance criteria

- Exactly 58 lesson files remain in curriculum order.
- Every lesson has `status: draft`, at least three sections, a numbered set of
  variations to try, substantive prose, and a non-placeholder Ruby example.
  Section headings name their own lesson; the suite requires at least 25 distinct
  heading patterns across the book and caps any generic title at 20 lessons.
- Every lesson clears the voice checks in `tests/test_book_draft.py`:
  contractions, second person, a real question, sentence-length variation, hedge
  density, the em dash budget, and the contrast-formula cap.
- Lesson lengths vary with the material. The suite rejects a manuscript where
  every lesson is written to the same size.
- No generated syllabus planning callout or `TODO` placeholder remains in a lesson.
- Prose clears `scripts/lint-prose.sh`.
- Extracted Ruby clears `ruby -c` through `scripts/check-code.sh`.
- Quarto can render the HTML edition without an error.
- Any example not executed inside Sonic Pi remains honestly labelled as requiring
  manual sound QA; `draft` is not silently promoted to `tested`.

## Session log

### 2026-08-21

- Measured the second draft's voice before changing anything. Over 41,160 words
  of lesson prose with code stripped: zero verbal contractions, 8 question marks
  across 58 lessons, 567 hedges, 26% of sentences opening on an article, and 108
  uses of "rather than" or "instead of" where the banned "not X but Y" had been.
  All 58 lessons shared one heading signature, one code block and a 724-1011
  word band. Recorded the diagnosis in `plan.html`.
- Identified the cause as specification rather than execution. `STYLE.md` was a
  ban list with no positive model, and `tests/test_book_draft.py` hard-coded
  `REQUIRED_HEADINGS` plus a word floor into every lesson, so the template was a
  passing test rather than a habit.
- Rewrote `STYLE.md` around six mandates with worked before/after pairs, and
  replaced the form tests with voice tests measuring contractions, second
  person, article-led sentences, questions, sentence-length variation, hedge
  density, em dash budget and contrast-formula reflex, plus anti-uniformity
  checks on heading patterns and lesson length. Baseline: 9 voice checks red, 10
  structural invariants green.
- Wrote the preface, setup chapter and Lessons 1-7 by hand as the reference
  corpus, on the principle that an agent given rules produces avoidance while an
  agent given instances produces prose.
- Ran six parallel rewrite lanes against those exemplars. Three completed
  (Lessons 8-25 and the five appendices); three hit a session limit partway, and
  the coordinator finished Lessons 35-37, 45-46 and 57-58 directly.
- Verified every lane independently rather than trusting its report, including
  diffing all Ruby blocks against their pre-rewrite versions to confirm that
  only the intended code changes landed.
- Final measurements across the 58 lessons: 422 contractions, 76 questions, 8
  hedges, 15% article openings, 15% of sentences under 8 words, lengths from 627
  to 1331 words with a standard deviation of 180, and 58 distinct heading
  patterns out of 58.
- Fixed seven substantive defects found by reading: the `:sine` demonstrations
  in Lessons 6 and 22, the seeded-randomness comparison in Lesson 16, the
  parallel cadences and uneven seam in Lesson 29, the bass-tenor unison in
  Lesson 31, the scale-degree cluster in Lesson 25, and the missing printed bars
  in Lesson 41. Removed an invented first-person recollection from Lesson 46.
- Linkified 116 cross-references. One bug worth recording: the first pass also
  rewrote "Lesson 1" inside `setup.qmd`'s YAML title, and because a title
  propagates to the sidebar, that single link produced an unresolved-target
  warning on all 64 other pages. Front matter is now excluded.
- Final checks: 19 pytest tests pass, prose lint is clean across 72 files, all
  83 extracted Ruby snippets clear syntax, `git diff --check` is clean, and
  Quarto renders all 65 HTML pages with zero warnings. A static scan of the
  built book found no broken local links, the status callout present on all 58
  lesson pages, and the joint author string on all 65.

### 2026-08-20

- Began the second-draft expository rewrite with a red acceptance test for the
  new voice. Replaced the former brevity-led style guide with guidance on
  clarity, unity, humanity, rhythm, concrete detail, and reader orientation.
- Queried the existing curriculum graph before editing. The result confirmed the
  sound-to-data progression and the score/renderer split as the conceptual spine
  to preserve through the rewrite.
- Split the 58 lessons into three non-overlapping rewrite ranges while revising
  the preface, setup chapter, reference appendices, README, and contributor brief
  in the coordinator pass. Ruby blocks remain unchanged pending syntax checks.
- Completed the expository pass across all 65 reader-facing source files. The
  manuscript now contains 62,244 regex-counted words, including 48,257 across
  the 58 lessons and 8,216 in the worked solutions.
- Ran an independent read-only editorial audit, corrected its prose/code and
  continuity findings, then added regression coverage for ten solution contracts.
  The auditor's final verification returned GO with no remaining blocker.
- Corrected the disclosure to match the actual workflow: the manuscript is
  AI-generated, under revision and independent testing, and no human-authored
  edition is claimed. Removed unsupported personal listening history.
- Final automated checks: nine pytest tests pass, prose lint is clean across 71
  files, all 83 extracted Ruby snippets clear syntax, and `git diff --check` is
  clean.
- Quarto rendered all 65 HTML pages. Browser inspection found no horizontal or
  code overflow on the preface, representative early/middle/late lessons, and
  solutions appendix. A complete static scan found no missing local targets,
  empty links, empty titles, or author-metadata mismatches.
- Resumed the transparent-authorship milestone and found that Quarto's
  `book.author` metadata labelled the title page but did not propagate to every
  chapter. Added project-wide author metadata and a regression assertion for it.
- Rebuilt all 65 HTML pages and confirmed that every page contains the exact
  `GPT 5.6 Sol at High Reasoning` author metadata. The rendered book contains no
  former CC/MIT book-licence links, copyright line, or `LICENSE.md` reference.
- Final validation: seven pytest tests pass, prose lint is clean across 70 files,
  all 83 extracted Ruby snippets clear syntax, and `git diff --check` is clean.

### 2026-08-19

- Set the global Quarto author to `GPT 5.6 Sol at High Reasoning`, removed the
  book licence file and all book-level licence/copyright presentation, and kept
  third-party source-rights guidance separate. Seven pytest tests pass and prose
  lint is clean.
- The required full rebuild, inspection, commit, and push remain pending because
  the Codex execution approval service reported its usage limit. Resume after
  2026-08-20 07:30 Europe/Malta and continue from the sole unticked TODO item.
- Added a warning callout at the top of `index.qmd` identifying the manuscript as
  AI-generated and under testing. Its former hand-rewrite wording was corrected
  during the later agent-written expository pass.
- Linked the warning directly to the repository pull-request page and recorded
  the author's limited capacity for individual replies.
- Added a regression test requiring the disclosure to appear before the first
  preface section. Final checks: six pytest tests pass, prose lint is clean, and
  `git diff --check` is clean.
- Rendered `_book/index.html` and confirmed Quarto emitted a titled warning
  callout with the disclosure and pull-request link before the preface body.

### 2026-08-18

- Inventoried 58 outline lessons, five appendices, and two front-matter chapters.
- Measured 14,352 words across the book sources; most lessons are about 200-word
  generated stubs.
- Read the project constitution, `STYLE.md`, Quarto configuration, and validation
  scripts.
- Started a persistent Codex goal for a complete, resumable first draft.
- Began a graph-based curriculum analysis. Initial scan: 83 relevant files,
  about 32,976 corpus words, no sensitive files skipped.
- Added first-draft acceptance tests before changing lesson prose.
- Added a minimal `uv` project with pytest and ran the red baseline: the lesson
  structure test and placeholder test fail for the expected outline content;
  the exact-58-lessons invariant passes.
- Built the pre-draft curriculum graph in `graphify-out/`: 325 nodes, 270 edges,
  and 72 labelled communities. The graph health check reported five dangling
  endpoint edges; no endpoints were missing and no edges collapsed. Treat this
  graph as a map of the scaffold that existed before parallel drafting began.
- Assigned three non-overlapping drafting lanes: Lessons 1-20, 21-41, and 42-58.
- Writer A completed Lessons 1-20 at 552-594 acceptance-test words and handed
  them to the dedicated editor for expansion and continuity work.
- Writer B completed Lessons 42-58 at 634-727 shell-counted words. All 17 Ruby
  blocks clear syntax; Sonic Pi sound and concurrent timing remain manual QA.
- Populated the glossary and sources ledger, and expanded the Ruby and Sonic Pi
  reference appendices. The solutions appendix is now assigned as a separate
  58-exercise pass.
- The solutions pass is complete: 58 worked entries and 5,837 words, with finite
  structural checks for open-ended listening and source-dependent exercises.
- Editor Stage 2A completed Lessons 42-58 and the reference appendices. Those
  lessons now span 650-773 words; renderer names and event keys match the shared
  conventions. Fresh Ruby syntax checks passed for all 37 blocks in that scope.
- The manuscript acceptance suite currently passes all five tests while the final
  range validation and continuity edit continue.
- Writer C handed off Lessons 21-41 at 609-685 regex-counted words. The full
  five-test suite passed, and all Ruby fences in that range cleared `ruby -c`.
- A fresh whole-book extraction produced 81 Ruby snippets; all 81 cleared syntax.
- The full house-style linter currently passes across 71 prose files.
- Revised the preface, setup chapter, and README against the finished manuscript.
  They distinguish syntax checks from Sonic Pi auditioning and no longer describe
  the book as an unwritten scaffold.
- The dedicated editor completed a final pass across Lessons 21-41, both writing
  boundaries, and all 58 solutions. Event keys, renderer names, source caveats,
  prerequisite order, and exercise-solution agreement were checked together.
- Extended code extraction to cover `setup.qmd`. The final extraction contains 83
  Ruby snippets, all of which clear `ruby -c`.
- Final manuscript size is 49,618 regex-counted words: 38,776 in the 58 lessons,
  with individual lessons ranging from 609 to 773 words, and 5,958 in solutions.
- Final automated checks: five pytest tests pass; prose lint is clean across 71
  files; `git diff --check` is clean.
- Quarto rendered 65 HTML pages to `_book/`. A local-target scan found zero
  missing relative links or assets, and no generated TODO/planning placeholders
  or empty HTML links were found.

## Current state

The third-draft voice rewrite is complete. Every item in Phases 1 to 4 of
`TODO.md` is ticked. All lessons remain honestly marked `draft` until a human
runs them in Sonic Pi and checks their listening claims; each one now says so in
a callout at the top of the page rather than by hedging its prose.

## Second-draft and manual QA

- Run every lesson from a clean buffer in Sonic Pi 5.0.0. Record runtime errors,
  timing behaviour, balance, and whether each sound description matches the
  result. Revise before changing any status to `tested`.
- Give extra timing attention to multi-loop and canon material in Lessons 47 and
  51, and compare the notation/transcription examples in Lessons 38-46 with exact
  printed or recorded sources.
- Verify setup shortcuts and output-device guidance on each supported platform.
- Replace the candidate-source worksheet only when an exact artifact and its
  edition-level licence evidence have been selected.
- Record audio after the corresponding lesson has passed the human test. Empty
  `audio=""` attributes are deliberate until then.
- Render and inspect PDF and EPUB editions when those formats enter scope. The
  completed verification in this pass covers HTML.
- The graph in `graphify-out/` maps the pre-draft scaffold and reports five
  dangling endpoints. Rebuild it only when a post-draft content graph is useful.
