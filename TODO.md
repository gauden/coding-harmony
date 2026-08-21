# Third draft: the approachable voice

The first draft built the manuscript. The second gave it an expository register
that turned out to be correct and cold. This one fixes the voice at its source
and rewrites the book against it.

Read this file and `DEVELOPMENT.md` before editing. Earlier phases are archived
at the bottom.

## Phase 1: Fix the specification

- [x] Diagnose the voice problem with measurements over the lesson corpus, and
      record the findings in `plan.html`.
- [x] Rewrite `STYLE.md` from a ban list into a positive specification: a worked
      model of the target voice, six mandates, and before/after pairs.
- [x] Move the draft's uncertainty out of the prose and into one shared status
      callout, `_not-yet-auditioned.qmd`.
- [x] Replace the form-pinning tests with voice tests. Confirm a red baseline on
      the nine voice checks and green on the structural invariants.
- [x] Restore the em dash at one per file; drop the bans that only redirected a
      reflex into "rather than".
- [x] Update `WRITING_BRIEF.md` to the new lesson contract.
- [x] Credit Claude Opus 5 alongside GPT 5.6 Sol in the global attribution.

## Phase 2: Write the reference corpus by hand

- [x] Rewrite the preface and setup chapter.
- [x] Rewrite Lessons 1-7 as the exemplars every later lesson is written against.
- [x] Fix Lesson 6, which demonstrated tuning with the one synth that removes the
      phenomenon it was demonstrating.

## Phase 3: Rewrite the rest against those exemplars

- [x] Lessons 8-17 (Parts 2-3), including the Lesson 16 seeded-randomness defect.
- [x] Lessons 18-25 (Parts 4-5).
- [x] Lessons 26-37 (Parts 6-7), including the Lesson 29 parallel-motion cadences
      and the Lesson 31 bass-tenor unison.
- [x] Lessons 38-46 (Parts 8-9), including text staff diagrams and four actual
      printed bars for Lesson 41.
- [x] Lessons 47-58 (Parts 10-12), including wiring the three capstones onto the
      phrase from `setup.qmd`.
- [x] The five appendices, preserving all ten tested solution contracts.

## Phase 4: Integration

- [x] Turn the 47 bare "Lesson N" mentions into working links.
- [x] Pass `uv run pytest` on all nineteen checks.
- [x] Pass `scripts/lint-prose.sh`.
- [x] Pass `scripts/check-code.sh` with zero Ruby syntax failures.
- [x] Render the HTML book and inspect early, middle, late and appendix pages.
- [x] Update `README.md`, `CHANGELOG.md` and `DEVELOPMENT.md`.

## Still owed, and not part of this draft

- [ ] Engraved staff figures for Part 8. The text diagrams added in Lessons 38,
      39 and 41 are a stopgap, not notation.
- [ ] Reference recordings. 60 `audio=""` attributes are still empty, which
      leaves every listening claim unfalsifiable for the reader.
- [ ] A human audition of every lesson in Sonic Pi 5.0.0, which is the only
      thing that can move a lesson from `draft` to `tested`.
- [ ] Part openers. Thirteen short bridges would give the book a sense of
      movement that 58 separate lessons cannot.

## Archived

Phases from the first draft and the second-draft expository pass are recorded in
the session log in `DEVELOPMENT.md`. Every item in both was completed.
