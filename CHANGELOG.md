# Changelog

This file records reader-visible changes to *Music Theory Through Sonic Pi*.

## 21 August 2026

### Changed

- Rewrote the whole book, all 58 lessons plus the preface, setup chapter and
  five appendices, in an approachable voice. The previous draft was accurate and
  cold: across 41,000 words of lesson prose it contained no verbal contractions
  at all, eight question marks in 58 lessons, and 567 hedges, with a quarter of
  every sentence opening on "The" or "A". It now has 422 contractions, 76
  questions, 8 hedges, and 15%.
- Replaced the house style guide's ban list with a positive specification: a
  worked model of the target voice and six mandates, each measured by the test
  suite. The old guide prohibited praise, questions, em dashes and the writer's
  own first person, which defined a floor and never described a ceiling.
- Moved the draft's honest uncertainty out of the prose and into one status
  callout at the head of every lesson. The body text now says what a reader will
  hear, in the present indicative. One clear disclosure replaces several hundred
  hedged ones, and it comes off in a single edit when a lesson is auditioned.
- Gave every lesson section headings that name its own subject. All 58 lessons
  previously shared one set of five titles, one code block and a 724-1011 word
  band; lengths now run 627 to 1331 words, and all 58 heading patterns differ.
- Rebuilt the three capstones on the E minor pentatonic phrase from the setup
  chapter, so the book ends by returning to the eight notes it opened with.
- Turned 116 cross-references into working links.
- Credited Claude Opus 5 alongside GPT 5.6 Sol at High Reasoning.

### Fixed

- Lesson 6 demonstrated just against equal-tempered intonation using `synth
  :sine`. A sine has a single partial, and the audible difference between those
  tunings comes almost entirely from beating between coincident upper partials,
  so the example removed the phenomenon it existed to show. Its closing
  paragraph also had the reasoning inverted. It now uses `:saw` and gives beat
  rates the reader can count against.
- Lesson 22 had the same fault: a drone lesson whose claims depend on partials
  interacting, demonstrated with sines. Now `:tri`.
- Lesson 16 warned that a seed reproduces a comparison only while the order of
  random calls holds, then asked the reader to delete two `rrand` calls and
  compare against the original. All draws are now hoisted into named variables
  and amplitude is disabled by a multiplier, so the stream never renumbers.
- Lesson 29's four cadences moved in strict parallel octaves and fifths, with
  the tonic a register above every other chord, so arrival was confounded with a
  register jump. Two of the four endings also carried a doubled IV at the seam
  that the other two did not. Hand-written voicings and a common seam replace
  both faults.
- Lesson 31's well-led progression put bass and tenor in unison, dropping the
  texture to three voices in a lesson about four independent lines. The unison
  is now the lesson: the cost function prefers it, a collisions check rejects
  it, and the repaired voicing turns out to contain parallel fifths of its own.
- Lesson 25 fed `play_chord` the first three degrees of a scale, so the twelve
  triads walking the circle of fifths were actually C-D-E clusters.
- Lesson 41 was titled "Decode four printed bars" and contained no printed bars,
  which made its exercise impossible from the book alone. Lessons 38, 39 and 41
  now carry monospace staff diagrams, marked as scaffolding rather than
  notation, and Lesson 41's bars match its Ruby exactly.
- Removed an invented first-person recollection from Lesson 46.

## 20 August 2026

### Changed

- Began a complete expository rewrite of the preface, setup chapter, 58 lessons,
  and five appendices. The revision keeps the curriculum and runnable examples
  intact while giving the reader more context, connection, and guidance.
- Recast the house style around clarity, unity, humanity, sentence rhythm, and
  concrete musical detail. Brevity remains an editorial tool rather than the
  governing voice.
- Expanded the setup and reference guides so instructions explain their purpose,
  likely failure modes, and connection to the book's score-and-renderer model.
- Reworked all 58 solution entries to explain the governing approach before the
  implementation details and to distinguish structural checks from evidence that
  still requires listening or source comparison.
- Corrected prose descriptions in Lessons 13 and 38 where the former text did not
  match the unchanged program output.
- Replaced the inaccurate promise of a complete hand rewrite with a precise
  disclosure: this is an AI-generated manuscript under revision and independent
  testing, and no human-authored edition is claimed.

### Fixed

- Corrected prose-to-code mismatches involving interval ratios, envelopes, swing,
  staff coordinates, voicings, secondary dominants, and validation examples.
- Repaired ten worked solutions whose former answers missed an exercise
  condition, including the cross-bar tie, enharmonic interval cases, two-pattern
  rhythm exercise, accidental scope, tendency-tone resolution, and decoration
  timeline.
- Replaced unsupported listening results and invented autobiographical claims
  with testable expectations that remain explicitly unauditioned.
