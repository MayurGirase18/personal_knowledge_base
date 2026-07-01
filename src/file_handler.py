import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "notes.json"


def load_notes():
    # Load all notes from the JSON file
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    

def save_notes(notes):
    # Save all notes to the JSON file
    with open(DATA_FILE, "w") as file:
        json.dump(notes, file, indent=4)