from models import Note
from file_handler import load_notes, save_notes
from utils import get_note_id
from dataclasses import asdict


def create_note():
    notes = load_notes()

    title = input("Enter title: ").strip()
    content = input("Enter content: ").strip()

    note = Note(id=get_note_id(notes), title=title, content=content)

    notes.append(asdict(note))
    # or
    # notes.append(note.__dict__)     # Convert object → dictionary

    save_notes(notes)

    print("Note created successfully.")


def view_notes():
    notes = load_notes()

    if not notes:
        print("No notes found!")
        return

    print(f"\n{' Notes ':-^30}")

    for note in notes:
        print("ID       : ", note["id"])
        print("Title    : ", note["title"])
        print("Content  : ", note["content"])
        print("-" * 40)


def edit_note():
    notes = load_notes()

    if not notes:
        print("No notes found!")
        return

    note_id = int(input("Enter the note ID: "))

    for note in notes:
        if note["id"] == note_id:
            print("Current information of notes: ")
            print("ID       : ", note["id"])
            print("Title    : ", note["title"])
            print("Content  : ", note["content"])
            print("-" * 30)

            note["title"] = input("Enter new title: ")
            note["content"] = input("Enter new Content: ")

            save_notes(notes)
            print("Note updated successfully.")
            return
        
    print("Note not found!")


def delete_note():
    notes = load_notes()

    if not notes:
        print("No notes found!")
        return

    note_id = int(input("Enter note ID: "))

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully.")
            return
        
        print("Note not found!")


def search_note():
    notes = load_notes()

    if not notes:
        print("No notes found!")
        return

    keyword = input("Enter keyword: ").lower()
    found = False

    for note in notes:
        if(keyword in note["title"].lower() or keyword in note["content"].lower()):
            print(f"\nID    : {note['id']}")
            print(f"Title   : {note['title']}")
            print(f"Content : {note['content']}")

            found = True

        if not found:
            print("Note not found!")
