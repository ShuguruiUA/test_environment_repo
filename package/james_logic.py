from package.note_book import *
from package.addressbook import *
import os
from rich.console import Console
from rich.table import Table


notebook = Notebook()
addressbook = AddressBook()


note_file = './data/notebook.dat'
phone_file = './data/phonebook.dat'

table_notes = Table(title='[italic #FF6C00]List of notes :heavy_check_mark:', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
table_notes.add_column('Title', justify='center', style='#FF6C00', no_wrap=True, min_width=16)
table_notes.add_column('Note', justify='center', style='#FF6C00', min_width=60)
table_notes.add_column('Tags', justify='center', style='#FF6C00', min_width=16)
console = Console()




def save():
    if not os.path.exists('./data/'):
        os.makedirs('./data/')
        Notebook.save_to_file(notebook, note_file)
        AddressBook.saved_to_file(addressbook, phone_file)
    else:
        Notebook.save_to_file(notebook, note_file)
        AddressBook.saved_to_file(addressbook, phone_file)
    # print(f'notebook file {note_file} saved successfuly')


def load():
    Notebook.load_from_file(notebook, note_file)
    AddressBook.load_from_file(addressbook, phone_file)
    # print(f'notebook file {note_file} loaded successfuly')


def create_note():
    note_title = input("Note's title: ")
    note_body = input("Note's info: ")
    note_title = Note(note_title, note_body)
    while True:
        tag_adder = input("Note's tag: ")
        if tag_adder.startswith('e'):
            break
        else:
            note_title.add_tag(tag_adder)
    notebook.add_note(note_title)
    
"""    id_counter = 0
    x = id_counter
    note_title = input("Note's title: ")

    if note_title in notebook:
        print('This name already exist, please choose another one')
        
    else:

        note_body = input("Note's info: ")

        x = Note(note_title, note_body)

        while True:
            tag_adder = input("Note's tag: ")
            if tag_adder.startswith('e'):
                break
            else:
                x.add_tag(tag_adder)
        notebook.add_note(x)
        id_counter += 1"""


def show_notes():
    for v in notebook.values():
        table_notes.add_row(v.note_title, v.note_body,
                            '\n'.join(p for p in v.tags))
    console.print(table_notes)
    
def find_tag():
    s = input('Enter a tag that you want to find: ')
    for item in notebook.find_note_tag(s):
        print(item)
        
    
#Логіка телефонної книги має бути тут

def create_contact():
    name = input('Enter the name: ')
    name = Record(name)
    phone = input('Enter the phone in format "1234567890": ')
    name.add_phone(phone)
    birthday = input('Enter  birthday in format DD.MM.YYYY: ')
    name.add_birthday(birthday)
    email = input('Enter the contact email: ')
    name.add_email(email)
    address = input('Enter the address: ')
    name.add_address(address)
    addressbook.add_record(name)
    
def show_contacts():
    for value in addressbook.values():
        print(value)
    
def find_phone():
    s = input('Enter a phone that you want to find: ')
    for item in addressbook.value(s):
        print(item) 

def remove_phone():


if __name__ == "__main__":
    pass
