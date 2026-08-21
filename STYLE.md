# Style

This book teaches music theory to programmers by making each idea audible and
inspectable. It should read like a capable friend sitting next to you at the
keyboard: someone who knows where the lesson is going, tells you plainly what
you're about to hear, and is honest when the result is subtle or when they got
it wrong the first time.

Earlier versions of this guide were mostly a list of things not to do. That
produced prose with no filler and no life in it: correct, careful, and cold. A
ban list defines the floor. This guide is about the ceiling. Everything below
that says "do this" matters more than everything that says "avoid that."

## The target voice

Here is the register to write in. Read it before writing anything else.

> Stack twelve pure fifths and you land almost exactly seven octaves up.
> Almost. Multiply by `3/2` twelve times and you overshoot by about a quarter
> of a semitone: nothing at all on one chord, and a disaster once you want to
> play in all twelve keys. That gap is the *Pythagorean comma*, and every
> tuning system ever built is a decision about where to hide it.

Five things are doing the work there. A two-word sentence sets the rhythm. The
reader is the subject of the first clause. The number is specific enough to
check. The stakes arrive before the terminology. And the last clause tells you
why the rest of the lesson exists.

Compare the version that guide-by-prohibition produces:

> A tuning system chooses which frequency relationships remain exact and where
> small discrepancies will appear. Pure fifths make a tempting foundation:
> multiply a frequency by `3/2` twelve times and the resulting pitch comes
> close to seven octaves above the start. It does not arrive exactly.

Nothing in it is wrong. Nobody is in it.

## Six things to do

These are the mandates. `tests/test_book_draft.py` measures most of them, and a
lesson that fails those checks is not finished.

### 1. Use contractions

Write "you'll hear," "doesn't," "here's," "that's," "isn't." Reserve the full
form for emphasis, where the extra syllable is doing something: "This does
not work, and the reason is interesting." Contractions are the single loudest
signal of whether prose was written for a person or filed for a record.

### 2. Put a person in the sentence

At least once per paragraph, make the reader or the writer the grammatical
subject. Watch for paragraphs where every sentence starts with "The" or "A"
followed by an abstract noun; that pattern is the surest sign the prose has
drifted into documentation.

> **Instead of:** The program schedules six evenly spaced attacks.
>
> **Write:** You get six evenly spaced attacks.

> **Instead of:** Provenance belongs beside the score data.
>
> **Write:** Write the edition, page, system, and measure into the score, even
> though Sonic Pi will never read them.

### 3. Ask the reader something

Every lesson should contain at least one real question: one that asks the
reader to predict a sound, guess which of two things changed, or notice what
the code cannot tell them. Put the question before the answer, and give them a
sentence of room to think.

> Both chords contain C, E, and G. So why does only one of them sound
> finished?

A question that you answer in the same breath is decoration. Don't write those.

### 4. Vary the sentence length

Every section needs at least one sentence under eight words. Long sentences
carry comparison and cause; short ones let a consequence land. A page of
fourteen-word sentences is grammatical and inert.

> The seed guarantees that your run matches the printed output. Until you
> delete an `rrand` call. Then every later draw shifts, and the comparison you
> thought you were making quietly becomes a different one.

### 5. Name the surprise

Every lesson has a moment where the sound contradicts what a programmer would
reasonably expect: a visual step that isn't a constant pitch step, a chord
that's correct on paper and dead in the air, a seed that stops reproducing.
Find that moment and say so in those words. It's the reason the lesson exists.

### 6. Commit to what the reader will hear

State the result in the present indicative. "The third shimmers." "The bass
drops out and the chord loses its floor." "You'll lose the click of each
onset."

This is a rule about honesty, not against it. See the next section.

## Uncertainty lives in one place, not in every sentence

Most of this book has not yet been auditioned in Sonic Pi by a human. That is
true, it matters, and readers deserve to know it. But that fact belongs in the
`status:` field and in the standard callout at the top of each lesson, not
smeared across every claim as *may*, *is expected to*, *tends to*, or *remains
a listening judgement*.

One clear disclosure is more honest than four hundred mumbled ones. Hedging
every sentence doesn't make the book more truthful; it makes it impossible for
a reader to tell a subtle effect from a broken setup from a false claim.

So: assert in the body text. Then, where a claim genuinely depends on the
listener's room, speakers, or register, say that specifically and once.

> **Instead of:** The ratio-built version is expected to have less internal
> motion around its third; the equal-tempered version may carry a faint
> shimmer. Those expectations still require audition.
>
> **Write:** Listen to the third, not the whole chord. In the ratio-built
> triad it sits still. In the equal-tempered one it shimmers, because that
> third is 14 cents sharp of a pure 5:4 and the two tones keep drifting in and
> out of phase. If you hear nothing on the first pass, you're not doing it
> wrong: on small speakers this difference lives close to the floor.

When a lesson is auditioned and moves to `tested`, you remove one callout
instead of re-editing forty sentences.

## Voice and person

**Second person is the default.** "You" is a specific adult at a keyboard. Use
it to direct attention and to hand over the work.

**First person singular is available for authorial decisions.** Choices about
what to include, what to leave out, and what order to teach things in are real,
documentable, and yours to own.

> I've kept the bass out of this example because it hides the third.

**First person singular is not available for sensory claims** until a human has
actually listened and written it down. Do not invent confusion, surprise, or a
changed opinion about a sound. That is the one hard line, and it is the reason
the previous rule exists in the narrow form it does.

> Once a listening log supports it: My first note on the tritone said "broken."
> After slowing the example I changed it to "unfinished," and the settings that
> made the difference audible are in the caption.

**First person plural means programmers as a group.** "We already know why a
good data model makes later operations easier to see." It never means the
writer steering the reader.

Bare imperatives are good: "Press Run." "Slow the tempo until both patterns
separate." Put enough around them that the reader knows what the action is for.

Present tense governs explanation. Past tense is for a real drafting or
listening event.

## Lead the reader

Give the reader a reason to care before you give them a definition. Establish
the situation, name the question, then move into code or terminology.

Don't leave an inference stranded between paragraphs. If a change in the code
alters the sound, say how. If the next lesson depends on this one, build the
bridge rather than appending a bare cross-reference.

Guidance is not cajoling. Tell the reader what to listen for, where an error is
likely, and how to read the result. Don't congratulate them, warn them that a
topic is hard, or pretend the work is easier than it is.

Warmth is allowed. Reassurance that costs nothing is not: "you're not doing it
wrong, this one is genuinely quiet" is useful, and "great work!" is not.

## Unity and shape

Each lesson has one governing idea, and the title, opening, example, listening
directions, explanation, and exercise all serve it. Material that belongs to
another lesson goes there.

Paragraphs need unity too. The first sentence sets a subject; the rest develop
it far enough to be useful. Short paragraphs are fine for emphasis, but a run of
terse declarations reads like notes to self.

Transitions should carry thought, not just sequence. "Because the durations stay
fixed, the new attack is the only thing that could have changed the sound" beats
"Next, change the synth."

Section headings should say what the section is about. "Why twelve fifths miss
the octave" tells a reader scanning the page what they're about to learn; "Why
it works" tells them which slot they're in. Keep the underlying rhythm of the
lesson, vary the labels.

## Clarity

Choose familiar words where they're exact. Put the actor near the verb. Name the
object instead of pointing at it with "this" or "it."

Watch nominalisation. Words ending in *-tion*, *-ment*, *-ness*, and *-ity* pile
up fast in technical writing, and each one buries a verb. "The tempering
discrepancy buys a large structural advantage" wants to be "tempering costs you
pure thirds and buys you all twelve keys."

Cut throat-clearing, inflated claims, duplicate qualifiers, and abstractions with
no example under them. Keep the sentence that tells the reader why the example
exists.

Technical vocabulary earns its place. Define a term in the sentence where it
first becomes useful, then use it consistently.

## Musical terms

Italicise a term at first use, then set it plain, and define it in the sentence
itself:

> A *tritone* splits the octave into two equal spans of six semitones. In a
> dominant seventh chord, that perfectly balanced interval creates a distinctly
> unbalanced desire to move.

Then go back to the sound. A new name should sharpen what the reader hears, not
interrupt it.

## Concreteness

Prefer the instance to the claim. "Play 220 Hz against 330 Hz and listen for the
slow pulse between them" beats "consider the perfect fifth."

Every claim about sound must be checkable by running the snippet next to it. Say
what can vary between synths, speakers, registers, and listening levels, and say
it once, specifically.

## Constructions to handle with care

**Contrast formulas.** "Not X, but Y" hides the real assertion, and so do
"rather than" and "instead of" when they become reflexes. State the misconception
only when the reader is likely to hold it, then explain why the better account
fits. If a paragraph has two of these, one is padding.

**Rhetorical triplets.** Three items when the subject has three parts. Never a
third item for cadence alone.

**Em dashes.** One per lesson, maximum. Use it when the interruption carries
meaning a comma or colon would lose. The budget exists because the mark is a
known tic; the budget is not zero because the mark is genuinely useful.

## Banned vocabulary

delve, crucial, unlock, harness (as a verb), leverage (as a verb), robust,
seamless, powerful, elegant (as praise), of course, obviously, dive in, deep
dive, game-changer, at its core, it's worth noting, let's.

These replace explanation with posture. `scripts/lint-prose.sh` catches them.
It can't tell whether a paragraph has earned the reader's attention.

Note what is no longer banned: contractions, questions, em dashes in moderation,
and the writer's own first person. Those were casualties of an earlier pass and
they cost more than they saved.

## Tone

Treat the reader as capable and new to the subject. When a topic is fiddly,
identify what makes it fiddly and offer a way to take it apart.

Avoid bureaucratic exercise language. "The target is," "the structural constraint
is," and "the finished file should contain" turn a musical experiment into
compliance work.

> **Instead of:** Generate a Markdown table for positions -2 through 10. Include
> coordinate, line-or-space classification, letter, octave, Sonic Pi symbol, and
> MIDI integer.
>
> **Write:** Build yourself the reference card you'd actually want taped to the
> monitor: positions -2 to 10, with the letter, octave, Sonic Pi symbol, and MIDI
> number for each. Print it. You'll use it for the whole of Part 8.

Write so the sound is interesting. Point at something audible: the edge of an
attack, the pull of a leading tone, the hole a rest leaves, the way a bass note
changes what a chord is.

## Code

Comments carry teaching that belongs beside a line. If a comment restates the
line, cut it.

```ruby
play :c4, release: 4    # the long tail overlaps the next note
```

Any example using randomness starts with `use_random_seed 42`, so the printed
output, the recording, and the reader's run agree. If an exercise asks the reader
to remove a random call, draw every random value into a named variable first, so
that removing one from use doesn't renumber the rest of the stream.

Examples run as written in a fresh buffer. If an example depends on earlier code,
say so and mark the block `# ...continued from above`.

Choose the synth that can actually show the phenomenon. A pure sine has one
partial, which makes it right for beating between near-unisons and wrong for
anything that depends on partials lining up. Say in the prose why the synth was
chosen when the choice is load-bearing.

Examples target the Sonic Pi version pinned in `setup.qmd`. When that pin moves,
run `scripts/check-code.sh --deep` before editing examples.

## Before marking a lesson `tested`

Read it aloud and rewrite whatever resists a natural speaking rhythm. Then run
the lesson from a clean Sonic Pi buffer, making each requested change in turn.
Record what the program does, what the sound suggests, and where the instructions
leave room for a wrong reading.

Recording follows that pass. Audio made from a moving lesson becomes a second
draft the prose has already left behind.
