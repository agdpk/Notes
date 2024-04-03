class NoteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.model.load_notes()

        while True:
            self.view.display_menu()
            choice = self.view.get_input("Enter your choice: ")

            if choice == '1':
                title = self.view.get_input("Enter the title of the note: ")
                body = self.view.get_input("Enter the body of the note: ")
                self.model.add_note(title, body)
            elif choice == '2':
                self.model.list_notes()
            elif choice == '3':
                note_id = int(self.view.get_input("Enter the ID of the note you want to edit: "))
                new_title = self.view.get_input("Enter the new title: ")
                new_body = self.view.get_input("Enter the new body: ")
                self.model.edit_note(note_id, new_title, new_body)
            elif choice == '4':
                note_id = int(self.view.get_input("Enter the ID of the note you want to delete: "))
                self.model.delete_note(note_id)
            elif choice == '5':
                date = self.view.get_input("Enter the date in format YYYY-MM-DD: ")
                self.model.filter_notes(date)
            elif choice == '6':
                note_id = int(self.view.get_input("Enter the ID of the note you want to read: "))
                self.model.read_note(note_id)
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")