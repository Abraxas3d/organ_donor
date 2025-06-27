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

