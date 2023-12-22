from collections import UserDict
import pickle
import os


# Клас для представлення нотаток. Один екземпляр класу - одна нотатка, що має такі атрибути як заголовок, тіло нотатки та перелік тегів

class Note:
    def __init__(self, note_title, note_body):
        self.note_title = note_title
        self.note_body = note_body
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)

    def __str__(self):
        return f"Note name: {self.note_title}, note: {self.note_body},  tags: {'; '.join(p for p in self.tags)}"

# Клас в якому зберфгаються нотатки

class Notebook(UserDict):

    
    # метод додавання нотатки
    def add_note(self, note):
        if isinstance(note, Note):
            self.data[note.note_title] = note
            
            
    # метод пошуку нотаток по тегу
    def find_note_tag(self, tag):
        res = None
        res = []
        for note in self.data.values():
            if tag in note.tags:
                res.append(note)
        return res

    # метод пошуку фрагмету у тілі нотатки
    def search(self, query: str):
        results = []
        for note in self.data.values():
            if query.lower() in note.note_body.lower():
                results.append(note)
        return results
    
    # метод редагування тіла нотатки за назвою
    def edit_note(self, title, new_body):
        self.data[title].note_body = new_body

    # метод видалення нотатки за назвою
    def delete(self, title):
        self.pop(title, None)

    
    # метод збереження нотатки у файл
    def save_to_file(self, file):
        with open(file, 'wb') as fh:
            pickle.dump(self.data, fh)
    
    # метод завантаження нотаток з файлу
    def load_from_file(self, file):
        if not os.path.exists(file):
            return
        with open(file, 'rb') as fh:
            self.data = pickle.load(fh)

    # метот виводу усіх нотаток у зручному для читання форматі
    def show_all(self):
        if len(self.data) != 0:
            for note in self.data:
                print(self.data[note])
            pass