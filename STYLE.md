# Style

This book teaches music theory to programmers by making each idea audible and
inspectable. Its prose should feel like an informed person at the next desk:
clear about where the lesson is going, candid about what caused confusion, and
interested in the sound itself. Economy still counts, but economy is not
starvation. A reader needs enough context to connect one fact to the next.

The principles below draw on the durable lessons of William Zinsser's *On
Writing Well*: clarity, simplicity, unity, humanity, rhythm, concrete detail,
and the confidence to sound like a person rather than an institution. They are
standards for judgement, not a machine for shortening sentences.

## Lead the reader

Begin each section by giving the reader a reason to care about the idea in
front of them. Establish the situation, name the question, then move into code
or terminology. A definition lands better after the reader knows what problem
it solves.

Do not leave an inference stranded between paragraphs. If a change in the code
alters the sound, explain the connection in ordinary language. If the next
lesson depends on this one, show the bridge rather than appending a bare
cross-reference.

Guidance is different from cajoling. Tell the reader what to listen for, where
an error is likely to arise, and how to interpret the result. Do not praise,
scold, cheer, or pretend the work is easier than it is.

## Voice and humanity

**First person singular only for documented human observation or a real authorial
decision.** Confusion, surprise, and changed judgement can help the reader see an
idea, but an AI drafting pass must never invent them. Until a human listening log
supports an experience, describe the comparison the reader can make instead.

> My first listening note called the tritone "broken." After slowing the example,
> I revised that description to "unfinished" and recorded the settings that made
> the distinction audible.

**Second person for the reader.** "You" addresses a specific adult at a
keyboard. Use it to orient attention, not to manufacture intimacy.

> Play 220 Hz against 330 Hz. The roughness falls away before the ratio has a
> name, so begin with the sound and return to the numbers afterward.

**First person plural only for programmers as a group.** "We" means people who
already write code. It does not mean the writer steering the reader through an
exercise.

> We already know why a good data model makes later operations easier to see.

Bare imperatives suit direct instructions: "Press Run." "Slow the tempo until
both patterns separate." Around those instructions, supply enough explanation
that the reader understands the purpose of the action and the meaning of its
result.

Never use "let's". Present tense governs explanations. Past tense is available
for a genuine drafting or listening experience.

## Unity and shape

Each lesson has one governing idea. The title, opening, code example, listening
directions, explanation, and exercise should all serve it. Interesting material
that belongs to another lesson should move there.

Each paragraph also needs unity. Its first sentence establishes a subject; the
remaining sentences develop that subject far enough to be useful. Paragraphs
may be short for emphasis, but a sequence of terse declarations feels like
notes left for the author rather than exposition written for a reader.

Transitions should carry thought as well as chronology. Prefer a causal bridge
such as "Because the durations stay fixed, the new attack is the only source of
the change" to administrative language such as "Next, change the synth."

## Clarity and simplicity

Choose familiar words where they are exact. Put the actor near the verb. Name
the object instead of referring vaguely to "this" or "it." When a sentence
contains two important ideas, decide whether one depends on the other; make
that relation visible or give each idea its own sentence.

Remove clutter that delays meaning: throat-clearing, inflated claims, duplicate
qualifiers, and abstractions with no example beneath them. Do not remove the
sentence that tells the reader why the example exists.

Technical vocabulary is welcome when it earns its place. Define the term in
the sentence where it first becomes useful, then use it consistently.

## Rhythm and sound

Read the prose aloud. Sentence length should vary with the thought: a longer
sentence can carry a comparison or unfold a cause; a short one can let the
consequence land. Repeated sentence openings and repeated paragraph shapes
flatten the voice even when every sentence is grammatical.

Prefer verbs that move. Prefer nouns that can be pictured, played, counted, or
heard. Music gives the prose its own supply of motion, contrast, arrival, and
silence. Use that material instead of promotional adjectives.

## Constructions to handle with care

**Contrast formulas.** "Not X, but Y" often hides the real assertion. State the
misconception only when the reader is likely to hold it, then explain why the
better account fits the evidence.

**Rhetorical triplets.** Three items are appropriate when the subject has three
parts. Do not add a third item for cadence alone.

**Em dashes.** The house style prefers a full stop, comma, or colon. Use an em
dash only when its interruption carries meaning that those marks would lose.

**Rhetorical questions.** Ask only when the pause does work. A question should
invite the reader to predict a sound, inspect the code, or recall an earlier
idea before the answer appears.

## Banned vocabulary

delve, matters, crucial, unlock, harness (as a verb), leverage (as a verb),
robust, seamless, powerful, elegant (as praise), simply, just, of course,
obviously, dive in, deep dive, game-changer, at its core, it's worth noting,
let's.

These words are banned because they tend to replace explanation with posture.
`scripts/lint-prose.sh` catches them. It cannot tell whether a paragraph has
earned the reader's attention.

## Tone

Treat the reader as capable and new to the subject. Do not congratulate them,
warn them that a topic is difficult, or use briskness as proof of seriousness.
When a topic is fiddly, identify the source of the difficulty and offer a way
to separate its parts.

Avoid bureaucratic exercise language. "The target is," "the structural
constraint is," and "the finished file should contain" often make a musical
experiment sound like compliance work. State what the reader is making, why
the constraint reveals the idea, and how they can tell whether the result
worked.

Write so that the sound is interesting. Description should direct attention to
something audible: the edge of an attack, the pull of a leading tone, the gap
left by a rest, or the way a bass note changes the identity of a chord.

## Musical terms

Italicise a term at first use, then set it plain. Define it in the sentence
itself:

> A *tritone* divides the octave into two equal spans of six semitones. In a
> dominant seventh chord, that balanced interval creates a distinctly
> unbalanced desire to move.

Return from the definition to the example. A new name should sharpen what the
reader hears, not interrupt it.

## Concreteness

Prefer the instance to the claim. "Play 220 Hz against 330 Hz and listen for the
slow pulse between them" gives the reader more than "consider the perfect
fifth." Use concrete detail to make an abstraction testable.

Every claim about sound must be checkable by running the nearby snippet. Tell
the reader what can vary between synths, speakers, registers, or listening
levels. Distinguish an observed result from an expected result until a human has
auditioned the code.

## Code

Comments carry teaching that belongs beside a line. If a comment restates the
line, cut it.

```ruby
play :c4, release: 4    # the long tail overlaps the next note
```

Any example using randomness starts with `use_random_seed 42`, so the printed
output, recording, and reader's run agree.

Examples run as written in a fresh buffer. If an example depends on earlier
code, say so in the prose and mark the block `# ...continued from above`.

Examples target the Sonic Pi version pinned in `setup.qmd`. When that pin moves,
run `scripts/check-code.sh --deep` before editing examples.

## Before marking a lesson `tested`

Read it aloud and rewrite the passages that resist a natural speaking rhythm.
Then run the lesson from a clean Sonic Pi buffer, making each requested change
in turn. Record what the program does, what the sound suggests, and where the
instructions leave room for a wrong interpretation.

Recording follows this pass. Audio made from a moving lesson soon becomes a
second draft that the prose has left behind.
