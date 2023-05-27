from scamp import *
from mingus.containers import Note

# Initialize a new SCAMP session
session = Session()
session.default_soundfont = './GeneralUser/my.sf2'

# Define chords
# Define a dictionary with chord names and their corresponding notes
chords = {
    "C": ["C-4", "E-4", "G-4"],
    "G": ["G-3", "B-3", "D-4"],
    "Am": ["A-3", "C-4", "E-4"],
    "Em": ["E-3", "G-3", "B-3"],
    "D": ["D-4", "F#-4", "A-4"],
    "A": ["A-4", "C#-4", "E-4"],
}

# Define chord progressions for each instrument for each section of the song
instrument_progressions = {
"drums": {
        "verse": {
            "C": 1,
            "G": 1.5,
            "Am": 0.5,
            "Em": 1,
        },
        "chorus": {
            "C": 1,
            "G": 1.5,
            "Am": 0.5,
            "Em": 1,
        },
    },
    "piano": {
        "verse": {
            "C": 1,
            "G": 1.5,
            "Am": 0.5,
            "Em": 1,
        },
        "chorus": {
            "C": 1,
            "G": 1.5,
            "Am": 0.5,
            "Em": 1,
        },
    },
    "violin": {
        "verse": {
            "C": 1,
            "G": 1.5,
            "Am": 0.5,
            "Em": 1,
        },
        "chorus": {
            "C": 1,
            "G": 1.5,
            "Am": 0.5,
            "Em": 1,
        },
    },
    "electric_guitar": {
        "verse": {
            "Em": 1,
            "G": 1.5,
            "D": 0.5,
            "A": 1,
        },
        "chorus": {
            "C": 1,
            "G": 1.5,
            "D": 0.5,
            "C": 1,
            "G": 1,
            "Em": 1,
        },
    },
}


def playPart(instrument_name, section_name, transposition = 0):
    instrument = session.new_part(instrument_name)
    # current_clock().tempo = int
    for chord_name, dur in instrument_progressions[instrument_name][section_name].items():
        print(f"Playing chord {chord_name} of {section_name} on {instrument_name} for {dur}")
        chord(chord_name, dur, instrument, 0.6, transposition)
        wait(dur)

def chord(chord_name, duration, instrument, volume = 0.6, transposition = 0):
    chord_pitches = getChordPitches(chord_name)
    instrument.play_chord(chord_pitches, volume, duration, blocking=False)


def getChordPitches(chord_name):
    chord_notes = [str(note) for note in chords[chord_name]]
    chord_pitches = []
    for note in chord_notes:
        chord_pitches.append(int(Note(note)))
    return chord_pitches


# For each instrument and their progressions, create an instrument part and play the chords
# session.fork(playPart, args=("piano", "verse"));
session.fork(playPart, args=("electric_guitar", "verse"));

session.wait_for_children_to_finish();

exit(0);

