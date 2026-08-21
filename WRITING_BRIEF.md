# Manuscript Writing Brief

Read `STYLE.md` first, and read Lessons 1 and 6 after it. Those two are the
reference corpus: the guide describes the voice, but the lessons are the voice,
and when the two seem to disagree the lessons win. This file settles the
manuscript-wide choices that several writers have to make the same way.

## Lesson contract

Preserve each lesson's YAML title, subtitle, part, and concepts. Set `status` to
`draft`; do not claim `tested` until a human has worked through the lesson in
Sonic Pi. Remove the generated planning callout after its promises appear in the
lesson.

Give every lesson these five movements, in this order. **Name each heading for
what that section of that lesson is about.** The previous draft used one fixed
set of five titles across all 58 lessons and read like a filing system;
`tests/test_book_draft.py` now requires at least 25 distinct heading patterns
across the book and caps any generic title at 20 lessons.

1. **The problem, and why you'd care.** Put a specific sound or compositional
   problem in the reader's head. Bring the term in after the sound.
2. **A program to run.** A fresh-buffer Sonic Pi program, with comments that
   explain musical intent. Say what the reader will hear, directly below it.
3. **Two or three controlled edits.** Explain why each comparison isolates the
   idea, and point at an audible feature without dictating a verdict.
4. **The explanation.** Connect the sound to theory and to a programmer's
   existing model of data, functions, state or concurrency. This is where the
   lesson's named surprise belongs.
5. **One finite exercise.** Its answer lives in the solutions appendix. Say what
   the reader is making, why the constraint reveals the idea, and how they'll
   recognise a result that worked.

Immediately after the YAML front matter, include the shared status callout:

```
{{< include ../../_not-yet-auditioned.qmd >}}
```

That callout is where the draft's uncertainty lives. Because it's there, the
body text asserts what the reader will hear in the present indicative. Do not
hedge individual claims; see the honesty section in `STYLE.md`.

Length follows the material, and the book must not be uniform. Most lessons run
750 to 950 words. Some ideas deserve 500 and some deserve 1,400, and the suite
checks that both extremes exist and that the spread is real. The automated floor
is 350 words.

## Code contract

- Target Sonic Pi 5.0.0 and Ruby syntax accepted by `ruby -c`.
- Every block runs in a fresh buffer unless it starts with
  `# ...continued from above` and the prose says so.
- Use `use_random_seed 42` before any random choice.
- Keep the score as data and rendering in a function once a lesson needs either
  abstraction. Do not introduce a helper before the text explains its inputs.
- Prefer note symbols while spelling has musical meaning and integers while
  arithmetic is the point.
- Pick the synth that can actually show the phenomenon. A sine has one partial,
  which makes it right for beating between near-unisons and useless for anything
  that depends on partials lining up. When the choice is load-bearing, say so in
  the prose.
- If an exercise asks the reader to remove a random call, hoist every random
  draw into a named variable first. Deleting a call renumbers the seeded stream
  and silently breaks the comparison the seed was there to protect.
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
part has passed since its introduction. At a lesson boundary, show what the new
idea can explain that the previous representation could not. Use cross-references
when they help the reader recover a prerequisite; link to the relative `.qmd`
file.

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
