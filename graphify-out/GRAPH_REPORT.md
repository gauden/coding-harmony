# Graph Report - .  (2026-08-18)

## Corpus Check
- Corpus is ~32,976 words - fits in a single context window. You may not need a graph.

## Summary
- 325 nodes · 270 edges · 72 communities (49 shown, 23 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 15 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Course Architecture
- Book Generation Pipeline
- Publishing and Audience
- Scales and Tension
- Performance and Refactoring
- Drafting Workflow
- Keys and Modulation
- Notation and Transcription
- Legal Score Sources
- Polyphonic Voice Scheduling
- Ruby Language Essentials
- Sonic Pi API
- Production Phases
- Transcription Validation
- Quarto Output Formats
- Source Provenance
- Diatonic Harmony
- Staff Coordinate Systems
- Audio Filter
- Secondary Dominants
- Prose Style Rules
- Dual Licensing
- Meter and Syncopation
- Duration and Feel
- Ear Training Harnesses
- Voicing and Voice Leading
- Cadences and Periods
- Musical Form
- Ear Transcription
- Bass Line Design
- Drum Grid Programming
- Arrangement and Space
- Canon and Imitation
- Capstone Score Model
- Publishing Workflow
- First Sonic Pi Sound
- Pitch Arithmetic
- Beat Scheduling
- Harmonic Series
- Consonance and Beating
- Tuning Systems
- Sound Envelopes
- Pitch Classes
- Octaves and Register
- Enharmonic Spelling
- Blues Harmony
- Audio Generation Script
- Setup Demonstration
- Field Notes Voice
- Executable Examples
- Book Visual Identity
- Audio Publishing
- Pentatonic Melody
- Fractional Rhythm
- Tuplets
- Interval Measurements
- Interval Ear Dictionary
- Melody Identity
- Motivic Development
- Grand Staff Texture
- Score Decoding Checks
- Transcription Debugging
- Modal Mixture
- Ruby Syntax Validation
- Code Extraction
- Prose Linting
- Lesson Scaffolding
- Sonic Pi Interface
- Sonic Pi Installation
- Concise Prose
- Music Glossary
- Exercise Solutions

## God Nodes (most connected - your core abstractions)
1. `Music Theory Through Sonic Pi Course` - 17 edges
2. `main()` - 7 edges
3. `Preface` - 7 edges
4. `Ruby for Non-Rubyists` - 6 edges
5. `Sonic Pi Cheat Sheet` - 6 edges
6. `Four-Pass Transcription Pipeline` - 6 edges
7. `parse_syllabus()` - 5 edges
8. `Music Theory Through Sonic Pi` - 5 edges
9. `Quarto Music Theory Book` - 5 edges
10. `Sources and Licences` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Sound First, Name Second` --semantically_similar_to--> `Sound First, Name Second`  [INFERRED] [semantically similar]
  curriculum/music_theory_through_sonic_pi.html → index.qmd
- `Music Is Data` --semantically_similar_to--> `Music Is Data`  [INFERRED] [semantically similar]
  curriculum/music_theory_through_sonic_pi.html → index.qmd
- `Score and Renderer Separation` --semantically_similar_to--> `Score and Renderer Separation`  [INFERRED] [semantically similar]
  curriculum/music_theory_through_sonic_pi.html → index.qmd
- `Draft-Test-Observe-Rewrite Loop` --semantically_similar_to--> `Confusion Is Data`  [INFERRED] [semantically similar]
  curriculum/plan.html → notes/field-notes.md
- `Chapter List Check` --conceptually_related_to--> `Syllabus as Single Source of Truth`  [INFERRED]
  .github/workflows/publish.yml → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Thirteen-Part Course Spine** — curriculum_music_theory_through_sonic_pi_part_0_getting_a_sound_out, curriculum_music_theory_through_sonic_pi_part_1_why_sound_has_structure, curriculum_music_theory_through_sonic_pi_part_2_pitch_space, curriculum_music_theory_through_sonic_pi_part_3_rhythm_and_meter, curriculum_music_theory_through_sonic_pi_part_4_intervals, curriculum_music_theory_through_sonic_pi_part_5_scales_and_keys, curriculum_music_theory_through_sonic_pi_part_6_chords_and_harmony, curriculum_music_theory_through_sonic_pi_part_7_melody_phrase_and_form, curriculum_music_theory_through_sonic_pi_part_8_reading_notation, curriculum_music_theory_through_sonic_pi_part_9_transcription, curriculum_music_theory_through_sonic_pi_part_10_texture_and_arrangement, curriculum_music_theory_through_sonic_pi_part_11_chromatic_harmony, curriculum_music_theory_through_sonic_pi_part_12_capstones [EXTRACTED 1.00]
- **Ordered Book Development Phases** — curriculum_plan_phase_0_scaffold, curriculum_plan_phase_1_parts_0_to_3, curriculum_plan_phase_2_parts_4_to_7, curriculum_plan_phase_3_parts_8_to_11, curriculum_plan_phase_4_capstones_and_book_pass, curriculum_plan_phase_5_publish [EXTRACTED 1.00]
- **Book Output Formats** — quarto_html_output, quarto_pdf_output, quarto_epub_output [EXTRACTED 1.00]
- **Temporal Organization System** — parts_03_rhythm_and_meter_12_durations_fractions_fractional_durations, parts_03_rhythm_and_meter_13_bars_accent_that_makes_meter_audible_meter_by_accent, parts_03_rhythm_and_meter_14_rests_dots_ties_rests_dots_and_ties, parts_03_rhythm_and_meter_15_syncopation_grid_syncopation_grid, parts_03_rhythm_and_meter_16_swing_microtiming_swing_and_microtiming, parts_03_rhythm_and_meter_17_tuplets_3_against_2_tuplets [INFERRED 0.85]
- **Scale and Key System** — parts_05_scales_and_keys_21_major_scale_step_formula_major_step_formula, parts_05_scales_and_keys_22_scale_degrees_pull_toward_home_scale_degree_tendency, parts_05_scales_and_keys_23_minor_family_minor_family, parts_05_scales_and_keys_24_modes_over_drone_modes, parts_05_scales_and_keys_25_circle_fifths_data_structure_circle_of_fifths [INFERRED 0.85]
- **Harmonic Progression System** — parts_06_chords_and_harmony_26_triads_stacked_thirds_triads, parts_06_chords_and_harmony_27_inversions_voicing_inversion_and_voicing, parts_06_chords_and_harmony_28_diatonic_chords_roman_numerals_diatonic_chords, parts_06_chords_and_harmony_29_cadences_are_punctuation_cadences, parts_06_chords_and_harmony_30_seventh_chords_tension_seventh_chords, parts_06_chords_and_harmony_31_voice_leading_optimisation_problem_voice_leading_optimization [INFERRED 0.85]
- **Four-Pass Transcription Stages** — parts_09_transcription_43_four_pass_pipeline_structure_pass, parts_09_transcription_43_four_pass_pipeline_rhythm_pass, parts_09_transcription_43_four_pass_pipeline_contour_pass, parts_09_transcription_43_four_pass_pipeline_exact_pitch_expression_pass [EXTRACTED 1.00]
- **Voice Separation Dimensions** — parts_10_texture_and_arrangement_50_register_timbre_space_voice_separation, parts_10_texture_and_arrangement_50_register_timbre_space_register_envelope_panning, parts_10_texture_and_arrangement_50_register_timbre_space_reverb_echo_depth [EXTRACTED 1.00]
- **Structured Capstone Score Checks** — parts_12_capstones_56_capstone_b_melody_accompaniment_three_part_score, parts_12_capstones_56_capstone_b_melody_accompaniment_shared_timeline, parts_12_capstones_56_capstone_b_melody_accompaniment_metric_integrity, parts_12_capstones_56_capstone_b_melody_accompaniment_chord_note_validation [EXTRACTED 1.00]

## Communities (72 total, 23 thin omitted)

### Community 0 - "Course Architecture"
Cohesion: 0.08
Nodes (28): Music Theory Through Sonic Pi Course, Parallel Ear Training Track, Course Event Model, Music Is Data, Part 0: Getting a Sound Out, Part 10: Texture and Arrangement, Part 11: Chromatic Harmony, Part 12: Capstones (+20 more)

### Community 1 - "Book Generation Pipeline"
Cohesion: 0.25
Nodes (13): lesson_path(), main(), parse_syllabus(), A lesson file with the syllabus notes carried across as a planning block., Turn an HTML fragment into readable plain text., 11. Pentatonic: the scale with no wrong notes' -> 'pentatonic-scale-no-wrong-…, Extract parts and lessons from the tracker HTML., render_chapters() (+5 more)

### Community 2 - "Publishing and Audience"
Cohesion: 0.18
Nodes (11): Chapter List Check, Quarto HTML Render, GitHub Pages Deployment, Publish Job, Sonic Pi Snippet Syntax Check, Single-Source Multi-Format Book, Music Theory Through Sonic Pi, Programmers Who Cannot Read Music (+3 more)

### Community 3 - "Scales and Tension"
Cohesion: 0.20
Nodes (10): Major Scale Step Formula, Scale Constructor, Scale-Degree Tendency, Tonic Resolution, Minor Family, Scale Array Diff, Characteristic Degree, Modes (+2 more)

### Community 4 - "Performance and Refactoring"
Cohesion: 0.20
Nodes (10): Amplitude, Articulation, and Onset Offset, Performance Event Schema, Performance-Shaped Renderer, Score-Strict Renderer, Future-Reader README, Repeated Helper Extraction, Reusable Music Library, Score-to-Code Capability (+2 more)

### Community 5 - "Drafting Workflow"
Cohesion: 0.22
Nodes (9): Build Plan, Draft-Test-Observe-Rewrite Loop, Lesson Template, Publish from Day One, Quarto Toolchain, Two-Tier Code Validation, Confusion Is Data, Field Notes (+1 more)

### Community 6 - "Keys and Modulation"
Cohesion: 0.22
Nodes (9): Accidental as Bar-Scoped Override, Key Signature Default, Resolved MIDI Number, Pitch Resolver, Current Key State, Perceived New Tonic, Pivot Chord, Roman Numeral as Relative Address (+1 more)

### Community 7 - "Notation and Transcription"
Cohesion: 0.25
Nodes (8): Notation Decoding Order, Score Data Before Sound Design, Contour and Anchor-Pitch Pass, Exact Pitch and Expression Pass, Four-Pass Transcription Pipeline, Rhythm-Only Pass, Tempo, Meter, and Phrase Pass, Greppable Uncertainty Marker

### Community 8 - "Legal Score Sources"
Cohesion: 0.25
Nodes (8): IMSLP Scans, Legal Music Sources, MuseScore Community Arrangements, Mutopia Public-Domain Scores, Source and Licence Inventory, Source Measure Provenance, Notation and Interpretation Separation, Score-Faithful Encoding

### Community 9 - "Polyphonic Voice Scheduling"
Cohesion: 0.25
Nodes (8): Deterministic Voice Scheduling, Per-Voice Score Data, Sync and Cue Alignment, One Process per Voice, Motivic, Imitative, Cadential, and Harmonic Annotations, Automatic Voice Alignment, Independent Voice Encoding, Two-Voice Polyphony Capstone

### Community 10 - "Ruby Language Essentials"
Cohesion: 0.29
Nodes (7): Ruby Blocks, Sonic Pi define, each and map, Ruby Keyword Arguments, Sonic Pi Rings, Ruby for Non-Rubyists, Ruby Symbols

### Community 11 - "Sonic Pi API"
Cohesion: 0.29
Nodes (7): Sonic Pi Effects API, Sonic Pi Envelope API, Sonic Pi Music Helpers, Sonic Pi Randomness API, Sonic Pi Cheat Sheet, Sonic Pi Sound API, Sonic Pi Time API

### Community 12 - "Production Phases"
Cohesion: 0.29
Nodes (7): LilyPond Notation Diagrams, Phase 0: Scaffold, Phase 1: Parts 0 to 3, Phase 2: Parts 4 to 7, Phase 3: Parts 8 to 11, Phase 4: Capstones and Book Pass, Phase 5: Publish

### Community 13 - "Transcription Validation"
Cohesion: 0.29
Nodes (7): Bar-Total Assertion, Range Assertion and Large-Leap Review, Transcription Validation, Chord-to-Sounding-Note Validation, Per-Bar Metric Integrity, Shared Timeline, Melody, Bass, and Inner-Harmony Score

### Community 14 - "Quarto Output Formats"
Cohesion: 0.29
Nodes (7): Accessible Syntax Highlighting, Audio Lua Filter, EPUB Output, Generated Chapter Manifest, HTML Output, Quarto Music Theory Book, PDF Output

### Community 15 - "Source Provenance"
Cohesion: 0.33
Nodes (6): Edition-Level Provenance, IMSLP, MuseScore, Mutopia, Sources and Licences, Third-Party Material Provenance

### Community 16 - "Diatonic Harmony"
Cohesion: 0.33
Nodes (6): Adjacent-Key Note Sharing, Circle of Fifths, Diatonic Chords, Roman-Numeral Progression Engine, Chord-Tone Skeleton, Nonharmonic Tones

### Community 17 - "Staff Coordinate Systems"
Cohesion: 0.33
Nodes (6): Diatonic Staff Step, Printed Note to Sonic Pi Translation, Treble Staff Coordinate System, One-Octave Treble Cheat Sheet, Bass Clef Offset, Middle C Between Staves

### Community 18 - "Audio Filter"
Cohesion: 0.60
Nodes (3): file_exists(), handle(), up_to_root()

### Community 19 - "Secondary Dominants"
Cohesion: 0.40
Nodes (5): Chromatic F-Sharp, Secondary Dominant, Temporary Tonic, Tonicised Progression, V/V in C Major

### Community 20 - "Prose Style Rules"
Cohesion: 0.40
Nodes (5): Banned Prose Constructions, Banned Vocabulary Patterns, Editable Style Policy, Prose Lint Rules, Voice Rules

### Community 21 - "Dual Licensing"
Cohesion: 0.50
Nodes (4): CC BY-NC-SA 4.0, Dual Licensing, MIT License, Think Python

### Community 22 - "Meter and Syncopation"
Cohesion: 0.50
Nodes (4): Bar Duration Assertion, Meter by Accent, Clave Bit Array, Syncopation Grid

### Community 23 - "Duration and Feel"
Cohesion: 0.50
Nodes (4): Rests, Dots, and Ties, Sustained Event Model, Humanization Jitter, Swing and Microtiming

### Community 24 - "Ear Training Harnesses"
Cohesion: 0.50
Nodes (4): Adaptive Weighting, Drill Harness, Chord-Quality Trainer, Triads

### Community 25 - "Voicing and Voice Leading"
Cohesion: 0.50
Nodes (4): Inversion and Voicing, Voice Near, Four Independent Lines, Voice-Leading Optimization

### Community 26 - "Cadences and Periods"
Cohesion: 0.50
Nodes (4): Cadence Ear Drill, Cadences, Antecedent and Consequent, Period Form

### Community 27 - "Musical Form"
Cohesion: 0.50
Nodes (4): ABA Call Sequence, Form Assembly from Sections and Transition, Sections as Functions, Varied Return with Arguments

### Community 28 - "Ear Transcription"
Cohesion: 0.50
Nodes (4): Interval-Based Transcription, Melodic Dictation over a Drone, Slowed Source Recording, Tonic Anchor

### Community 29 - "Bass Line Design"
Cohesion: 0.50
Nodes (4): Approach and Passing Notes, Independent Bass Rhythm, Root Bass, Walking Bass

### Community 30 - "Drum Grid Programming"
Cohesion: 0.50
Nodes (4): Amplitude Accent and Late-Hi-Hat Pocket, One-Instrument-at-a-Time Groove Transcription, One Array per Drum, Sixteen-Step Drum Grid

### Community 31 - "Arrangement and Space"
Cohesion: 0.50
Nodes (4): Register, Envelope, and Panning, Reverb and Echo Depth Placement, Sparse, Dense, and Wide Arrangements, Voice Separation

### Community 32 - "Canon and Imitation"
Cohesion: 0.50
Nodes (4): Canon, Delayed Entry, Self-Harmonising Melody, Imitative Transposition

### Community 33 - "Capstone Score Model"
Cohesion: 0.50
Nodes (4): Pitch, Rhythm, Articulation, Dynamics, and Phrase Data, Expressive Monophonic Renderer, Measure References and Uncertain Passages, Solo Melody Capstone

### Community 34 - "Publishing Workflow"
Cohesion: 0.67
Nodes (3): GitHub Pages, Local PDF and EPUB Build, Publish Workflow

### Community 35 - "First Sonic Pi Sound"
Cohesion: 0.67
Nodes (3): Lesson 1: Hello, Sound, Instrument Substitution, Sonic Pi Minimum API

### Community 36 - "Pitch Arithmetic"
Cohesion: 0.67
Nodes (3): Melody Transformations, Lesson 2: Notes Are Integers, Pitch Arithmetic

### Community 37 - "Beat Scheduling"
Cohesion: 0.67
Nodes (3): Sonic Pi Deterministic Scheduler, Symbolic Beat Time, Lesson 3: Time Is Beats, Not Seconds

### Community 38 - "Harmonic Series"
Cohesion: 0.67
Nodes (3): Additive Timbre, Harmonic Series, Lesson 4: One Note Is Many Notes

### Community 39 - "Consonance and Beating"
Cohesion: 0.67
Nodes (3): Acoustic Beating, Lesson 5: Consonance Is Small Whole Numbers, Small Whole-Number Frequency Ratios

### Community 40 - "Tuning Systems"
Cohesion: 0.67
Nodes (3): Twelve-Tone Equal Temperament, Just Intonation, Lesson 6: Twelve Notes, One Compromise

### Community 41 - "Sound Envelopes"
Cohesion: 0.67
Nodes (3): ADSR Envelope, Articulation Vocabulary, Lesson 7: The Envelope Is the Instrument

### Community 42 - "Pitch Classes"
Cohesion: 0.67
Nodes (3): Chromatic Browser, Pitch Class Modulo 12, Lesson 8: Twelve Pitch Classes

### Community 43 - "Octaves and Register"
Cohesion: 0.67
Nodes (3): Lesson 9: Octaves as Address Space, Musical Register, Register-Based Arrangement

### Community 44 - "Enharmonic Spelling"
Cohesion: 0.67
Nodes (3): Enharmonic Equivalence, Pitch Spelling Field, Lesson 10: Sharps, Flats, and Spelling

### Community 45 - "Blues Harmony"
Cohesion: 0.67
Nodes (3): Nonfunctional Dominant Sevenths, Numeral-Based Transposition, Twelve-Bar Blues

### Community 47 - "Setup Demonstration"
Cohesion: 1.00
Nodes (3): E Minor Pentatonic Demo, Bass Live Loop, Tune Live Loop

### Community 48 - "Field Notes Voice"
Cohesion: 0.67
Nodes (3): Field Notes Voice, No Encouragement Tone, Read-Aloud Lesson Test

### Community 49 - "Executable Examples"
Cohesion: 0.67
Nodes (3): Fresh-Buffer Examples, Reproducible Randomness, Executable Sound Claims

## Knowledge Gaps
- **180 isolated node(s):** `check-code.sh script`, `extract-code.sh script`, `lint-prose.sh script`, `new-lesson.sh script`, `GitHub Pages` (+175 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **23 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `check-code.sh script`, `extract-code.sh script`, `lint-prose.sh script` to the rest of the system?**
  _180 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Course Architecture` be split into smaller, more focused modules?**
  _Cohesion score 0.07936507936507936 - nodes in this community are weakly interconnected._