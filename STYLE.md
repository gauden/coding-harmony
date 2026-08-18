# Style

The rules the prose in this book follows. They exist because the failure mode of
technical writing for beginners is encouragement, and encouragement reads as
condescension to the audience this book is for.

Anyone writing here, human or otherwise, follows these.

## Voice

**First person plural.** The "we" means the writer and the reader working
through the same problem at the same time. It is the voice of someone sitting
next to you at the keyboard rather than lecturing from the front.

> We build a tone by stacking sine partials, then take one away and listen to
> what changed.

Not "you build a tone", which instructs from above, and not "the reader builds a
tone", which is a report on someone else's afternoon.

**Bare imperatives are fine for direct instructions.** "Install Sonic Pi." "Press
Run." "Slow the tempo until both patterns are audible." These are short, neutral,
and carry no subject at all. Reaching for "we press Run" where "press Run" will
do adds a word and a small false note.

**Second person survives for what belongs to the reader.** Their ear, their code,
their `drills.rb`, their judgement. "Your ear will disagree with the arithmetic
here" is honest. "You will find this exciting" is not.

**Never "let's".** It is the register of a children's television presenter and it
undoes everything else on this page.

**Never the editorial "we" that means only the author.** No "we have shown", no
"we will see in a later chapter". If the writer alone did something, say so
plainly or leave it out.

Present tense throughout. Active voice.

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

delve, matters, crucial, journey, unlock, harness (as a verb), leverage (as a
verb), robust, seamless, powerful, elegant (as praise), simply, just, of course,
obviously, dive in, deep dive, game-changer, at its core, it's worth noting,
let's.

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
