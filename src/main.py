from note_manager import(
    create_note,
    view_notes,
    edit_note,
    delete_note,
    search_note
)

from utils import pause


def menu():
    print(f"{'\n     Personal Knowledge Base     \n':=^100}")

    while True:
        print("--- Menu ---")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Edit Note")
        print("4. Delete Note")
        print("5. Search Note")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            create_note()

        elif choice == "2":
            view_notes()

        elif choice == "3":
            edit_note()

        elif choice == "4":
            delete_note()

        elif choice == "5":
            search_note()

        elif choice == "6":
            print("Thank you for using the application.")
            break

        else:
            print("Invalid choice.")

        
        pause()


if __name__ == "__main__":
    menu()
