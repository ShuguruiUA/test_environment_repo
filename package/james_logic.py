from package.note_book import *
from package.addressbook import *
import os
from rich.console import Console
from rich.table import Table


notebook = Notebook()
addressbook = AddressBook()
console = Console()

note_file = './data/notebook.dat'
phone_file = './data/phonebook.dat'

def Notes_Table():
    global table_notes
    table_notes = Table(title='[italic #FF6C00]Table of notes :heavy_check_mark:', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
    table_notes.add_column('Title', justify='center', style='#FF6C00', no_wrap=True, min_width=16)
    table_notes.add_column('Note', justify='center', style='#FF6C00', min_width=60)
    table_notes.add_column('Tags', justify='center', style='#FF6C00', min_width=16)

def Record_Table():
    global table_record
    table_record = Table(title='[italic #FF6C00]Table of records :heavy_check_mark:', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
    table_record.add_column('Name', justify='center', style='#FF6C00', min_width=16)
    table_record.add_column('Phone', justify='center', style='#FF6C00', min_width=12)
    table_record.add_column('Birthday', justify='center', style='#FF6C00', min_width=12)
    table_record.add_column('Email', justify='center', style='#FF6C00', min_width=12)
    table_record.add_column('Address', justify='center', style='#FF6C00', min_width=10)


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


def show_notes():
    Notes_Table()
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
    Record_Table()
    for el in addressbook.values():
        if not el in addressbook:
            table_record.add_row(el.name.value,'\n'.join(str(t) for t in el.phones), el.birthday.value, el.email.value, el.address.value)
    console.print(table_record)

        
def find_record():
    name = input('Input contact name: ')
    print(addressbook.find_record(name))
        
def add_phone():
    name = input('Input contact name: ')
    if name in addressbook:
        phone = input('Enter the phone in format "1234567890": ')
        if phone in addressbook[name]:
            return print(f'Phone {phone} is present in {name}\'s contacts')
        else:
            
            addressbook[name].additonal_info(addressbook[name].phones, Phone(phone))
            return print(f'Phone {phone} was successfully added to {name}\'s contact')
            
    else:
        return print(f'{name}\'s contact does not exist in phone book, please create it first')
        # Record.add_phone(addressbook(name), phone)
    # for v in addressbook.values():
    #    if name == v.name.value:
    #     _ = addressbook[name]
    #     phone = input('Enter the phone in format "1234567890": ')
    #     Record.add_phone(_ , phone) 
        
    
def find_phone():
    name = input('Input contact name: ')
    for v in addressbook.values():
       if name == v.name.value:
            _ = addressbook[name]
            s = input('Enter a phone that you want to find: ')
            _res =  Record.find_phone(_, s)
            print(_res)
       else:
           print(f'{name} not found in the records')
           
def delete_contact():
    name = input('Enter the name: ')
    if not name in addressbook:
        return f'contact {name} is not found'
    contact = addressbook.delete(name)
    return print(f'contact {contact} was deleted')

def remove_phone():
    name = input('Enter your name: ')
    if not name in addressbook:
        return print(f'There is no {name} in phonebook')
    name_ = addressbook[name]
    s = input('Enter a phone number that you want to delete: ')
    res_ = Record.find_phone(name_, s)
    if res_:
        Record.remove_phone(addressbook[name], str(res_))
        return print(f'Phone number {res_} was successfuly removed from {name}\'s contact')
    return print(f'Phone number {s} not belongs to {name}\'s contact ')
    
if __name__ == "__main__":
    pass
