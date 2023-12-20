from note_book import Note, Notebook
from addressbook import AddressBook
import os
notebook = Notebook()
addressbook = AddressBook()


note_file = './data/notebook.dat'
phone_file = './data/phonebook.dat'


def operation_commands():
    pass


def save():
    if not os.path.exists('./data/'):
        os.makedirs('./data/')
        Notebook.save_to_file(notebook, note_file)
    else:
        Notebook.save_to_file(notebook, note_file)
    # print(f'notebook file {note_file} saved successfuly')


def load():
    Notebook.load_from_file(notebook, note_file)
    # print(f'notebook file {note_file} loaded successfuly')


def create_note():
    id_counter = 0
    x = id_counter
    y = input("Note's title: ")
    z = input("Note's info: ")

    x = Note(y, z)

    while True:
        tag_adder = input("Note's tag: ")
        if tag_adder.startswith('e'):
            break
        else:
            x.add_teg(tag_adder)
    notebook.add_note(x)
    id_counter += 1


if __name__ == "__main__":
    pass
