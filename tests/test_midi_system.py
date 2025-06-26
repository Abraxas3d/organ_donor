#!/usr/bin/env python3
"""
Simple test script to verify the MIDI Markov system works.
Run this to test basic functionality.
"""

# First, let's create a minimal test to ensure our imports work
def test_imports():
    """Test that all required libraries are available"""
    print("🔧 Testing imports...")
    
    try:
        import mido
        print("✅ mido imported successfully")
    except ImportError as e:
        print(f"❌ mido import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        from pathlib import Path
        from dataclasses import dataclass
        from typing import List, Dict, Optional
        print("✅ Standard library imports successful")
    except ImportError as e:
        print(f"❌ Standard library import failed: {e}")
        return False
    
    return True


def test_midi_ports():
    """Test MIDI port detection"""
    print("\n🎹 Testing MIDI ports...")
    
    import mido
    
    try:
        input_ports = mido.get_input_names()
        output_ports = mido.get_output_names()
        
        print(f"📥 Input ports found: {len(input_ports)}")
        for port in input_ports:
            print(f"  - {port}")
        
        print(f"📤 Output ports found: {len(output_ports)}")
        for port in output_ports:
            print(f"  - {port}")
        
        return True
        
    except Exception as e:
        print(f"❌ MIDI port detection failed: {e}")
        return False


def create_test_midi():
    """Create a simple test MIDI file"""
    print("\n🎵 Creating test MIDI file...")
    
    import mido
    from pathlib import Path
    
    try:
        # Create a simple MIDI file
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        
        # Add some notes - simple melody
        notes = [60, 64, 67, 72, 67, 64, 60]  # C major arpeggio
        
        for note in notes:
            track.append(mido.Message('note_on', channel=0, note=note, velocity=64, time=0))
            track.append(mido.Message('note_off', channel=0, note=note, velocity=64, time=480))
        
        # Save test file
        test_path = Path("test_melody.mid")
        mid.save(test_path)
        
        print(f"✅ Test MIDI file created: {test_path}")
        print(f"📊 File size: {test_path.stat().st_size} bytes")
        
        return test_path
        
    except Exception as e:
        print(f"❌ Test MIDI creation failed: {e}")
        return None


def test_midi_loading(test_file):
    """Test loading and basic analysis of MIDI file"""
    print(f"\n📖 Testing MIDI file loading...")
    
    import mido
    
    try:
        # Load the test file
        mid = mido.MidiFile(test_file)
        
        print(f"✅ MIDI file loaded successfully")
        print(f"📏 Tracks: {len(mid.tracks)}")
        print(f"⏱️  Ticks per beat: {mid.ticks_per_beat}")
        print(f"🕐 Length: {mid.length:.2f} seconds")
        
        # Count messages
        total_messages = 0
        note_messages = 0
        
        for track in mid.tracks:
            for msg in track:
                total_messages += 1
                if msg.type in ['note_on', 'note_off']:
                    note_messages += 1
        
        print(f"📨 Total messages: {total_messages}")
        print(f"🎵 Note messages: {note_messages}")
        
        return True
        
    except Exception as e:
        print(f"❌ MIDI loading failed: {e}")
        return False


def test_basic_markov():
    """Test basic Markov chain functionality"""
    print(f"\n🔗 Testing basic Markov chain...")
    
    try:
        from collections import defaultdict
        import numpy as np
        
        # Simple transition counting
        sequence = [60, 64, 67, 64, 60, 64, 67, 72]
        transitions = defaultdict(lambda: defaultdict(int))
        
        for i in range(len(sequence) - 1):
            current = str(sequence[i])
            next_note = str(sequence[i + 1])
            transitions[current][next_note] += 1
        
        print("✅ Transition counting successful")
        print(f"📊 Unique states: {len(transitions)}")
        
        # Convert to probabilities
        probabilities = {}
        for state, next_states in transitions.items():
            total = sum(next_states.values())
            probabilities[state] = {
                next_state: count / total 
                for next_state, count in next_states.items()
            }
        
        print("✅ Probability calculation successful")
        
        # Simple entropy calculation
        total_entropy = 0.0
        for state, probs in probabilities.items():
            state_entropy = 0.0
            for prob in probs.values():
                if prob > 0:
                    state_entropy -= prob * np.log2(prob)
            total_entropy += state_entropy
        
        avg_entropy = total_entropy / len(probabilities) if probabilities else 0.0
        print(f"📈 Average entropy: {avg_entropy:.3f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Markov chain test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("🧪 MIDI Markov Chain System Test")
    print("=" * 40)
    
    tests_passed = 0
    total_tests = 5
    
    # Test 1: Imports
    if test_imports():
        tests_passed += 1
    
    # Test 2: MIDI ports
    if test_midi_ports():
        tests_passed += 1
    
    # Test 3: Create test file
    test_file = create_test_midi()
    if test_file:
        tests_passed += 1
        
        # Test 4: Load test file
        if test_midi_loading(test_file):
            tests_passed += 1
    
    # Test 5: Basic Markov functionality
    if test_basic_markov():
        tests_passed += 1
    
    # Summary
    print(f"\n{'='*40}")
    print(f"📊 Test Results: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! System is ready.")
        print("\nNext steps:")
        print("1. Save the domain model classes to 'midi_markov.py'")
        print("2. Save the example script to 'example.py'") 
        print("3. Run: python example.py --interactive")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    return tests_passed == total_tests


if __name__ == "__main__":
    main()
