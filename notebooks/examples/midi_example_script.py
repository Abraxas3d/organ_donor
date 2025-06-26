#!/usr/bin/env python3
"""
Example script demonstrating the MIDI Markov Chain system.

This script:
1. Loads a MIDI file
2. Analyzes it to extract notes and rests
3. Builds Markov chains for composition
4. Generates a new piece based on learned patterns
5. Saves the result to a new MIDI file
"""

from pathlib import Path
import sys
from typing import Dict, Any

# Import our domain classes (assuming they're in a file called midi_markov.py)
# from midi_markov import MarkovMidiGenerator


def main():
    """Main demonstration function"""
    
    # Initialize the system
    print("🎵 MIDI Markov Chain Composer")
    print("=" * 40)
    
    generator = MarkovMidiGenerator()
    
    # Check available MIDI ports
    print("\n📡 Available MIDI Ports:")
    input_ports, output_ports = generator.midi_interface.list_ports()
    print(f"Input ports: {input_ports}")
    print(f"Output ports: {output_ports}")
    
    # Load and analyze a MIDI file
    midi_file_path = get_midi_file_path()
    if not midi_file_path:
        return
    
    print(f"\n🔍 Analyzing MIDI file: {midi_file_path.name}")
    
    try:
        # Analyze the MIDI file
        analysis_results = generator.analyze_midi_file(midi_file_path)
        
        # Display analysis results
        print_analysis_results(analysis_results)
        
        # Generate new composition based on the first track with notes
        available_tracks = list(analysis_results.keys())
        if not available_tracks:
            print("❌ No tracks with notes found in MIDI file")
            return
        
        print(f"\n🎼 Generating new composition based on {available_tracks[0]}...")
        
        # Generate a new track
        new_track = generator.generate_composition(
            track_name=available_tracks[0],
            length=50  # Generate 50 musical events
        )
        
        print(f"✨ Generated track with {len(new_track.notes)} notes and {len(new_track.rests)} rests")
        
        # Save the generated composition
        output_path = midi_file_path.parent / f"generated_{midi_file_path.stem}.mid"
        generator.midi_interface.save_track_to_midi(new_track, output_path)
        
        print(f"💾 Saved generated composition to: {output_path}")
        
        # Optional: Play through MIDI if output port available
        if output_ports:
            play_option = input(f"\n🔊 Play through MIDI port '{output_ports[0]}'? (y/n): ")
            if play_option.lower() == 'y':
                play_generated_track(generator, new_track, output_ports[0])
        
    except Exception as e:
        print(f"❌ Error processing MIDI file: {e}")
        import traceback
        traceback.print_exc()


def get_midi_file_path() -> Path:
    """Get MIDI file path from user input or command line argument"""
    
    if len(sys.argv) > 1:
        # Use command line argument
        file_path = Path(sys.argv[1])
    else:
        # Ask user for file path
        file_input = input("\n📁 Enter path to MIDI file (or 'demo' for built-in example): ")
        
        if file_input.lower() == 'demo':
            # Create a simple demo MIDI file
            return create_demo_midi_file()
        else:
            file_path = Path(file_input)
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return None
    
    if file_path.suffix.lower() not in ['.mid', '.midi']:
        print(f"❌ Not a MIDI file: {file_path}")
        return None
    
    return file_path


def create_demo_midi_file() -> Path:
    """Create a simple demo MIDI file for testing"""
    import mido
    
    print("🎹 Creating demo MIDI file...")
    
    # Create a simple melody
    demo_path = Path("demo_melody.mid")
    
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    
    # Simple C major scale with some rests
    notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
    
    for i, note in enumerate(notes):
        # Note on
        track.append(mido.Message('note_on', channel=0, note=note, velocity=64, time=0))
        # Note off after a quarter note
        track.append(mido.Message('note_off', channel=0, note=note, velocity=64, time=480))
        
        # Add a rest every few notes
        if i % 3 == 2:
            track.append(mido.Message('note_on', channel=0, note=60, velocity=0, time=240))  # Rest
    
    mid.save(demo_path)
    print(f"✅ Demo file created: {demo_path}")
    
    return demo_path


def print_analysis_results(results: Dict[str, Any]):
    """Print formatted analysis results"""
    
    print("\n📊 Analysis Results:")
    print("-" * 30)
    
    for track_name, data in results.items():
        print(f"\n🎵 {track_name.upper()}:")
        print(f"  Notes: {data['notes']}")
        print(f"  Rests: {data['rests']}")
        print(f"  Kemeny Constant: {data['kemeny_constant']:.2f}")
        print(f"  Entropy: {data['entropy']:.3f}")
        
        # Show a sample of entropy timeline
        timeline = data['entropy_timeline']
        if timeline:
            print(f"  Entropy Timeline (first 5): {timeline[:5]}")


def play_generated_track(generator: 'MarkovMidiGenerator', track: 'Track', port_name: str):
    """Play the generated track through MIDI (simplified version)"""
    
    print(f"🔊 Playing through {port_name}...")
    
    try:
        generator.midi_interface.open_ports(output_name=port_name)
        
        if generator.midi_interface.output_port:
            # Simple playback - just send note on/off messages
            import time
            
            for note in track.notes[:10]:  # Play first 10 notes
                # Note on
                msg_on = mido.Message('note_on', 
                                    channel=0, 
                                    note=note.pitch, 
                                    velocity=note.velocity)
                generator.midi_interface.output_port.send(msg_on)
                
                # Wait for note duration
                time.sleep(min(note.duration, 0.5))  # Cap at 0.5 seconds
                
                # Note off
                msg_off = mido.Message('note_off', 
                                     channel=0, 
                                     note=note.pitch, 
                                     velocity=0)
                generator.midi_interface.output_port.send(msg_off)
                
                time.sleep(0.1)  # Small gap between notes
            
            print("✅ Playback complete")
        
    except Exception as e:
        print(f"❌ Playback error: {e}")


def interactive_mode():
    """Interactive mode for exploring the system"""
    
    generator = MarkovMidiGenerator()
    
    while True:
        print("\n" + "="*50)
        print("🎵 MIDI Markov Interactive Mode")
        print("="*50)
        print("1. Analyze MIDI file")
        print("2. Generate composition")
        print("3. List MIDI ports") 
        print("4. Create demo file")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            file_path = get_midi_file_path()
            if file_path:
                results = generator.analyze_midi_file(file_path)
                print_analysis_results(results)
        
        elif choice == '2':
            if not generator.note_chains:
                print("❌ No analyzed tracks available. Analyze a MIDI file first.")
                continue
            
            track_names = list(generator.note_chains.keys())
            print(f"Available tracks: {track_names}")
            track_name = track_names[0]  # Use first track
            
            length = int(input("Length of composition (default 20): ") or "20")
            
            new_track = generator.generate_composition(track_name, length)
            output_path = Path(f"generated_composition_{track_name}.mid")
            generator.midi_interface.save_track_to_midi(new_track, output_path)
            print(f"💾 Saved to: {output_path}")
        
        elif choice == '3':
            inputs, outputs = generator.midi_interface.list_ports()
            print(f"Input ports: {inputs}")
            print(f"Output ports: {outputs}")
        
        elif choice == '4':
            demo_path = create_demo_midi_file()
            print(f"Demo file created: {demo_path}")
        
        elif choice == '5':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_mode()
    else:
        main()
