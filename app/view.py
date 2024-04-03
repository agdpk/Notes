class NoteView:
    def display_menu(self):
        print("Menu:")
        print("1. Add a new note")
        print("2. List all notes")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Filter notes by date")
        print("6. Read a note")
        print("7. Exit")

    def get_input(self, message):
        return input(message)