## Clone the repo

```git clone https://github.com/Abraxas3d/organ_donor.git```

```cd organ_donor```

## Install dependencies and setup environment

```poetry install```

## Start Jupyter Lab

```poetry run jupyter lab```

## Core Entities Envisioned and Implemented

MidiAnalyzer: Extracts notes, rests, and timing from MIDI streams

MarkovChain: Builds transition tables for notes, durations, and rests

EntropyAnalyzer: Sliding window entropy analysis for musical structure

PerformanceEngine: Real-time MIDI I/O and live generation

CompositionGenerator: Creates new MIDI from learned patterns

## Core Dataclasses

Note & Rest: Clean dataclasses for musical events

Track: Encapsulates a complete musical sequence

TransitionTable: Markov chain with entropy metrics

## Core Analyzers

MidiEventExtractor: Handles the tricky timing logic for notes AND rests

MarkovChainBuilder: Creates transition tables for notes, durations, content

EntropyAnalyzer: Your sliding window entropy analysis

MidiComposer: Generates new music from learned patterns

## North Star Features

Type hints throughout for clarity

Dataclasses for clean data structures

Pathlib instead of hardcoded strings

Async-ready design (will add later)

Separation of concerns - each class has one responsibility

## Innovations

✅ Rest duration analysis - crucial for natural feel

✅ Multiple Markov chains (notes, durations, content)

✅ Kemeny constants for phrase length

✅ Entropy analysis with sliding windows

✅ Real-time MIDI I/O capability

## MIDI Markov Chain Composition System - Function Summary 26 June 2025

## Core Domain Classes

### `Note`
**Purpose**: Represents a single musical note with timing information
- **Properties**: pitch (MIDI note number), velocity, start_time, duration, channel
- **Key insight**: Captures both the note AND how long it's held (crucial for live feel)

### `Rest` 
**Purpose**: Represents silence/breathing between notes
- **Properties**: start_time, duration
- **Key insight**: The "breath" of live performance - what makes algorithmic music feel human

### `Track`
**Purpose**: A complete musical sequence combining notes and rests
- **Properties**: name, notes list, rests list, timing metadata
- **Key insight**: Preserves the relationship between sound and silence

### `TransitionTable`
**Purpose**: Markov chain probabilities with musical analysis metrics
- **Properties**: transition probabilities, kemeny_constant, entropy
- **Key insight**: Not just "what note comes next" but also musical structure analysis

## Analysis Classes

### `MidiEventExtractor`
**Purpose**: Converts MIDI files into our domain model (Notes + Rests)
- **Key method**: `extract_track()` - analyzes MIDI timing to detect note durations AND rest durations
- **Critical insight**: Uses timestamp tracking to calculate when notes end and rests begin
- **Why important**: Most MIDI analysis ignores rests - we preserve the "breathing" of live performance

### `MarkovChainBuilder` 
**Purpose**: Creates transition tables from musical sequences
- **`build_note_chain()`**: What note typically follows what note
- **`build_duration_chain()`**: What note/rest duration typically follows what duration  
- **`build_content_chain()`**: Combined sequence of notes AND rests (preserves musical phrasing)
- **Key insight**: Three separate Markov chains capture different aspects of musical performance

### `EntropyAnalyzer`
**Purpose**: Analyzes musical complexity and structure using sliding windows
- **`analyze_track_entropy()`**: Measures how "surprising" or "predictable" music is over time
- **Key insight**: Musical entropy reveals phrase structure, climaxes, and compositional patterns
- **Applications**: Could identify verse/chorus structure, development sections, cadences

## Generation Classes

### `MidiComposer`
**Purpose**: Creates new compositions from learned Markov patterns
- **`generate_track()`**: Creates new musical sequence using three Markov chains
- **Key insight**: Combines note choices, duration patterns, AND rest patterns for realistic output
- **Sampling strategy**: Uses probability-based selection to create variations while preserving style

### `MidiInterface`
**Purpose**: Handles all MIDI file I/O and real-time MIDI communication
- **`load_midi_file()`**: Converts MIDI files to our Track objects
- **`save_track_to_midi()`**: Converts Track objects back to playable MIDI files
- **`list_ports()`**: Finds connected MIDI devices (pipe organs, synthesizers, etc.)
- **Real-time capability**: Can send generated music directly to MIDI instruments

## Orchestration Class

### `MarkovMidiGenerator`
**Purpose**: Main application that coordinates all components
- **`analyze_midi_file()`**: Complete analysis pipeline (extract → build chains → calculate entropy)
- **`generate_composition()`**: Single track generation
- **`generate_multi_track_composition()`**: Multiple track generation preserving instrument separation
- **`save_with_organ_stops()`**: Specialized output for pipe organ with different stops
- **`save_multi_track_composition_with_sustaining_instruments()`**: Uses strings, woodwinds, brass for clear duration perception

## Key Insights & Design Decisions

### Why Three Markov Chains?
1. **Note chain**: Captures melodic/harmonic patterns
2. **Duration chain**: Captures rhythmic patterns  
3. **Content chain**: Captures phrasing (when to breathe/rest)

### Why Sustaining Instruments?
- **Piano problem**: Piano is percussive - notes decay immediately, making duration analysis impossible
- **Solution**: Use violin, cello, flute, organ - instruments that sustain notes for their full duration
- **Result**: You can actually HEAR whether the algorithm preserved timing patterns

### Why Rest Detection Matters?
- **Live performance**: Human musicians breathe, pause, phrase naturally
- **Algorithmic music**: Often sounds robotic because it lacks these micro-pauses
- **Our approach**: Preserves the original "breathing" patterns in generated music

### Critical Input File Requirements
- **Must have actual rests**: Files with perfectly connected notes (like Bach.mid) won't teach rest patterns
- **Multi-track preferred**: Separate instruments allow for richer harmonic analysis
- **Natural performance**: Files from live recordings capture human timing nuances

## Workflow Summary

1. **Analyze** → `analyze_midi_file()` extracts notes, rests, builds three Markov chains
2. **Generate** → Uses probability tables to create new sequences with realistic timing
3. **Output** → Saves as MIDI with sustaining instruments for clear duration perception
4. **Verify** → Open in GarageBand/DAW to hear if the "breathing" feels natural

## Future Enhancements

- **Real-time performance**: Connect MIDI keyboard for live interaction with algorithms
- **Entropy-based structure**: Use entropy analysis to create formal musical structures
- **Multiple style learning**: Analyze different composers/genres for style transfer
- **Live parameter control**: Real-time adjustment of Markov chain probabilities during performance





