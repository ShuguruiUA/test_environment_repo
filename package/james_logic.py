from package.note_book import *
from package.addressbook import *
import os
from rich.console import Console
from rich.table import Table


notebook = Notebook()
addressbook = AddressBook()


note_file = './data/notebook.dat'
phone_file = './data/phonebook.dat'

table_notes = Table(title='List of notes')
table_notes.add_column('Title', justify='center', style='cyan', no_wrap=True)
table_notes.add_column('Note', justify='full', style='cyan')
table_notes.add_column('Tags', justify='right', style='cyan')
console = Console()


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

    if y in notebook:
        print('This name already exist, please choose another one')
    else:

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


def show_notes():
    for v in notebook.values():
        table_notes.add_row(v.note_title, v.note_body,
                            '; '.join(p for p in v.tags))
    console.print(table_notes)


if __name__ == "__main__":
    pass
