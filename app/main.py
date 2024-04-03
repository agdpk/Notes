from app.controller import NoteController
from app.model import NoteModel
from app.view import NoteView

if __name__ == '__main__':
    model = NoteModel()
    view = NoteView()
    controller = NoteController(model, view)
    controller.run()