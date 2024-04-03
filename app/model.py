import datetime
import json
import random


class NoteModel:
    def __init__(self):
        self.notes = []

    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, title, body):
        note_id = random.randint(1, 100000)
        while any(note['id'] == note_id for note in self.notes):
            note_id = random.randint(1, 100000)

        new_note = {
            'id': note_id,
            'title': title,
            'body': body,
            'date and time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notes.append(new_note)
        self.save_notes()
        print("Note saved")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note['id']}, Title: {note['title']}")

    def edit_note(self, note_id, new_title, new_body):
        note_found = False
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = new_title
                note['body'] = new_body
                note['date and time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note_found = True
                break

        if not note_found:
            print("Note not found.")
        else:
            self.save_notes()
            print("Change saved")

    def delete_note(self, note_id):
        note_found = False
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Note deleted")
                note_found = True
                break

        if not note_found:
            print("Note not found")

    def filter_notes(self, date):
        filtered_notes = [note for note in self.notes if note['date and time'].split()[0] == date]
        if filtered_notes:
            for note in filtered_notes:
                print(f"ID: {note['id']}, Title: {note['title']}")
        else:
            print("No notes found for this date.")

    def read_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                print(
                    f"ID: {note['id']}\nTitle: {note['title']}\nBody: {note['body']}\nDate and Time: {note['date and time']}")
                break
        else:
            print("Note not found.")