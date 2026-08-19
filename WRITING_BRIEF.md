# First-Draft Writing Brief

Read `STYLE.md` first. This file settles manuscript-wide choices that several
writers must make the same way.

## Lesson contract

Preserve each lesson's YAML title, subtitle, part, and concepts. Set `status` to
`draft`; do not claim `tested` until a human has worked through the lesson in
Sonic Pi. Remove the generated planning callout after its promises appear in the
lesson.

Keep these headings, in this order:

1. `The idea`: put a specific sound or compositional problem in the reader's
   head. Introduce the term after the sound when possible.
2. `Run this`: provide a fresh-buffer Sonic Pi program with comments that explain
   musical intent. Describe the audible result directly below it.
3. `Change one thing`: give two or three bounded edits and say what difference to
   hear. Numbered lists work well here.
4. `Why it works`: connect the sound to theory and to a programmer's existing
   model of data, functions, state, or concurrency.
5. `Take it further`: give one finite exercise whose answer can live in the
   solutions appendix. State the target sound or structural constraint.

Aim for 650 to 900 words per lesson. The automated floor is 550 words so short
topics can stay short. A first draft should be specific enough to edit, without
padding to meet a quota.

## Code contract

- Target Sonic Pi 5.0.0 and Ruby syntax accepted by `ruby -c`.
- Every block runs in a fresh buffer unless it starts with
  `# ...continued from above` and the prose says so.
- Use `use_random_seed 42` before any random choice.
- Keep the score as data and rendering in a function once a lesson needs either
  abstraction. Do not introduce a helper before the text explains its inputs.
- Prefer note symbols while spelling has musical meaning and integers while
  arithmetic is the point.
- Represent pitch class as `note % 12`.
- Represent a reusable event as a hash with `:note`, `:start`, `:duration`, and
  optional `:amp`. Use `:duration` consistently rather than alternating with
  `:length` or `:dur` in prose-facing data.
- Use `play_events` for the general event renderer and `play_phrase` for a simple
  sequential array. Small local helpers may have narrower names.
- Leave `audio=""` in a Quarto Ruby fence when no recording exists. Do not invent
  audio filenames.

## Continuity

Assume only earlier lessons. Briefly restate a representation when more than one
part has passed since its introduction. Use cross-references only when they help
the reader recover a prerequisite; link to the relative `.qmd` file.

The conceptual progression is:

`sound -> pitch/time data -> acoustics -> pitch classes -> rhythm -> intervals ->
scales/keys -> harmony -> melody/form -> notation -> transcription -> arrangement
-> chromatic harmony -> capstones`

Keep notation out of the teaching surface before Part 8. Note names such as
`:c4` are Sonic Pi addresses, not staff-reading exercises.

## Editorial honesty

Code may clear Ruby syntax without producing the intended sound. Keep every file
at `draft` and record Sonic Pi auditioning as manual QA. Do not fabricate source
citations, recordings, listening results, or claims that an example was tested.
