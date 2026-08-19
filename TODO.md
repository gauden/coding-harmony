# Book First Draft

This file is the durable checklist for the first complete manuscript pass. A new
session should read this file and `DEVELOPMENT.md` before editing prose.

## Phase 1: Baseline and acceptance tests

- [x] Inventory the 58 lesson files, front matter, appendices, build scripts, and style rules.
- [x] Establish a resumable Codex goal for the complete first draft.
- [x] Define automated first-draft acceptance tests before manuscript changes.
- [x] Run the tests once and record the expected red baseline.
- [x] Build the repository knowledge graph and record the curriculum dependencies.

## Phase 2: Draft the manuscript

- [x] Draft Lessons 1-20 (Parts 0-4) from top to bottom.
- [x] Draft Lessons 21-41 (Parts 5-8) from top to bottom.
- [x] Draft Lessons 42-58 (Parts 9-12) from top to bottom.
- [x] Revise the preface and setup chapter to match the completed manuscript.
- [x] Complete the Ruby guide, cheatsheet, solutions, glossary, and sources appendices.

## Phase 3: Integration and editing

- [x] Run a dedicated continuity edit across all lesson boundaries.
- [x] Check term introductions, data representations, helper names, and cross-references.
- [x] Apply the house voice in `STYLE.md` across all prose.
- [x] Confirm every optional exercise has a useful solution or an explicit open-ended note.

## Phase 4: Verification

- [x] Pass `uv run pytest`.
- [x] Pass `scripts/lint-prose.sh`.
- [x] Pass `scripts/check-code.sh` with zero Ruby syntax failures.
- [x] Render the Quarto HTML book and inspect the build for broken links or markup.
- [x] Record any checks requiring Sonic Pi or external tooling as deferred manual QA.

## Phase 5: Handoff

- [x] Update `README.md` status from scaffold to complete first draft.
- [x] Update `DEVELOPMENT.md` with final word counts, checks, and remaining second-draft work.
- [x] Mark every phase above complete.

## Follow-up: front-page AI disclosure

- [x] Add a regression test for a prominent disclosure before the first preface section.
- [x] Add the AI-generated draft, hand-rewrite, and testing warning to the front page.
- [x] Invite pull requests while setting the limited-response expectation.
- [x] Pass tests and prose lint, then render and inspect the revised front page.
