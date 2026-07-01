def get_note_id(notes):
    # To return the Available ID for the next note
    if not notes:
        return 1
    
    return max(note["id"] for note in notes) + 1


def pause():
    input("\nPress Enter to continue...")
