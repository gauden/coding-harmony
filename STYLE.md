# Style

The rules the prose in this book follows. They exist because the failure mode of
technical writing for beginners is encouragement, and encouragement reads as
condescension to the audience this book is for.

Anyone writing here, human or otherwise, follows these.

## Voice

**First person singular for the writer.** This book is a record of one person
learning music theory, so it says "I". Field notes, not a textbook handed down.
Where I was confused, the text says I was confused.

> I expected the tritone to sound broken. It sounds unresolved, which is a
> different thing, and it took me three attempts to hear the difference.

**Second person for the reader.** "You" throughout. The reader is a specific
person at a keyboard, addressed directly.

> Play 220 Hz against 330 Hz. Your ear will call one of these pairs smooth
> before you know why.

**First person plural only for programmers as a group.** "We" means people who
already write code, which is the shared ground this book stands on. It does not
mean the writer and the reader doing an exercise together.

> It forces us to sit through an exposition of what a loop is.

Not "we now build a scale", which is the textbook plural this book avoids.

**Bare imperatives are fine for direct instructions.** "Install Sonic Pi."
"Press Run." "Slow the tempo until both patterns are audible." Short, neutral,
no subject at all.

**Never "let's".** It is the register of a children's television presenter and it
undoes everything else on this page.

Present tense throughout, except when recounting what happened during drafting.
Active voice.

## Sentences

Cut every word that carries no weight. Write the sentence, then remove a quarter
of it. This is Zinsser's rule and it survives contact with everything.

Vary sentence length. A short sentence after two long ones is the only
punctuation trick that always works.

## Constructions to avoid

**"Not X, but Y."** Say Y. If X needs correcting, correct it in its own
sentence.

**Rhetorical triplets.** Three items because three sounds rhythmic is padding.
Three items because there are three is fine.

**Em dashes.** A full stop or a comma almost always does the job. Use one only
when the alternative is genuinely worse.

**Rhetorical questions.** Ask a question only when the reader is meant to answer
it before reading on.

## Banned vocabulary

delve, matters, crucial, unlock, harness (as a verb), leverage (as a verb),
robust, seamless, powerful, elegant (as praise), simply, just, of course,
obviously, dive in, deep dive, game-changer, at its core, it's worth noting,
let's.

"Journey" is deliberately absent from that list. The book describes itself as a
record of one, and banning a word the framing depends on would be silly.

`scripts/lint-prose.sh` greps for these and reports file and line. It catches
drift; it does not catch bad writing.

## Tone

No encouragement. The reader is an adult who chose to be here. Do not tell them
something is exciting, do not congratulate them for finishing a lesson, and do
not warn them that the next part is hard.

No apologising for the material. If a topic is genuinely fiddly, say what makes
it fiddly and move on.

Write so that the sound is interesting. That is the whole persuasion budget.

## Musical terms

Italicise a term at first use, then set it plain forever after. Define it in the
sentence itself, not in a trailing parenthesis:

> A *tritone* splits the octave exactly in half, and it is the interval that
> makes a dominant seventh demand resolution.

Not:

> Play the tritone (an interval of six semitones).

## Concreteness

Prefer the instance to the claim. "Play 220 Hz against 330 Hz and rate the
result" beats "consider the perfect fifth". The reader can generalise; they
cannot un-hear a specific example.

Every claim about how something sounds must be checkable by running the snippet
directly above it.

## Code

Comments carry the teaching. If a comment restates the line, cut it.

```ruby
play :c4, release: 4    # long tail, so the next note overlaps this one
```

Not:

```ruby
play :c4, release: 4    # plays c4 with release of 4
```

Any example using randomness starts with `use_random_seed 42`, so the printed
output, the recording, and the reader's run agree.

Examples run as written, in a fresh buffer, with nothing above them. If an
example depends on earlier code, say so in the prose and mark the block
`# ...continued from above`.

Examples target the Sonic Pi version pinned in `setup.qmd`. When that pin moves,
run `scripts/check-code.sh --deep` before anything else.

## Before marking a lesson `tested`

Read it aloud. Anything you stumble over gets rewritten. This finds more
problems than any other check, and it takes four minutes.

Recording comes after this, never before. Audio made from a lesson that is still
moving has to be made again.
