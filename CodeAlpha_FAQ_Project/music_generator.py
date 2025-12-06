# --- START OF music_generator.py CODE (Task 3) ---

# Import necessary modules from the music21 library
from music21 import stream, note, chord, tempo

def generate_and_save_music():
    """
    Generates a simple musical phrase (C major scale) and saves it as a MIDI file.
    """
    
    # 1. Create the main stream (the container for the music)
    s = stream.Stream()
    s.append(tempo.MetronomeMark(number=120)) # Set the tempo to 120 BPM

    # 2. Define the melody (C major scale)
    # The format is Note Name followed by Octave Number (e.g., 'C4' is Middle C)
    c_major_scale = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    
    print("--- 🎶 Music Generation Tool (Task 3) ---")
    print(f"Generating a simple C major sequence...")

    # 3. Add notes to the stream
    for pitch_name in c_major_scale:
        # Create a quarter note (duration=1.0) for the current pitch
        new_note = note.Note(pitch_name, quarterLength=1.0) 
        s.append(new_note)

    # 4. Save the generated music to a file
    output_filename = 'generated_music_task3.mid'
    try:
        # The .write('midi') command saves the music file
        s.write('midi', fp=output_filename)
        print(f"\n✅ Success! Music saved to: {output_filename}")
        print("You can open this .mid file with any music player or notation software.")
        
    except Exception as e:
        print(f"\n❌ An error occurred during file saving: {e}")
        print("Check if music21 is installed correctly.")


# Run the generation function
if __name__ == "__main__":
    generate_and_save_music()

# --- END OF music_generator.py CODE ---