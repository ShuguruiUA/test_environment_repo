from package.note_book import *
from package.addressbook import *
import os
from rich.console import Console
from rich.table import Table
from datetime import date, datetime, timedelta
from package.clean import run_func

# Створення екземплярів класів

notebook = Notebook()
addressbook = AddressBook()
console = Console()

note_file = './data/notebook.dat'
phone_file = './data/phonebook.dat'


# Визначення таблиць для нотаток і контактів

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

# Методи для збереження та завантаження нотаток і адресної книги
def save():
    if not os.path.exists('./data/'):
        file_dir = os.mkdir('./data/')
        file = open(file_dir / 'notebook.bin', 'a')
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



################################ Нотатки

# метод створення нотатки
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

# метод виводу усіх збережених нотаток у формі таблиці
def show_notes():
    Notes_Table()
    for v in notebook.values():
        table_notes.add_row(v.note_title, v.note_body,
                            '\n'.join(p for p in v.tags))
    console.print(table_notes)

# метод пошуку нотатки за тегом    
def find_tag():
    s = input('Enter a tag that you want to find: ')
    for item in notebook.find_note_tag(s):
        print(item)

# метод редагування тіла нотатки        
def edit_note():
    title = input('What note do you want to edit? Enter note title: ')
    if title in notebook.data:
        new_body = input('Enter new note text: ')
        notebook.edit_note(title, new_body)
        print(f"Note '{title}' body has been updated.")
    else:
        print(f"Note '{title}' not found in the notebook.")


   
################################ Адресна книга

# метод ствогення нового контакту
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

# метод виводу збереженних контактів у формі таблиці    
def show_contacts():
    Record_Table()
    for el in addressbook.values():
        if not el in addressbook:
            table_record.add_row(el.name.value,'\n'.join(str(t) for t in el.phones), el.birthday.value, el.email.value, el.address.value)
    console.print(table_record)

# метод пошуку контакту за ім'ям      
def find_record():
    name = input('Input contact name: ')
    print(addressbook.find_record(name))

# метод додавання телефону до існуючого контакту?        
def add_phone():
    name = input('Input contact name: ')
    if name in addressbook:
        phone = input('Enter the phone in format "1234567890": ')
        addressbook[name].additonal_info(addressbook[name].phones, Phone(phone))
        return print(f'Phone {phone} was successfully added to {name}\'s contact')
        # if phone in addressbook[name]:
        #     return print(f'Phone {phone} is present in {name}\'s contacts')
        # else:
            
            # addressbook[name].additonal_info(addressbook[name].phones, Phone(phone))
            # return print(f'Phone {phone} was successfully added to {name}\'s contact')
            
    else:
        return print(f'{name}\'s contact does not exist in phone book, please create it first')
        # Record.add_phone(addressbook(name), phone)
    # for v in addressbook.values():
    #    if name == v.name.value:
    #     _ = addressbook[name]
    #     phone = input('Enter the phone in format "1234567890": ')
    #     Record.add_phone(_ , phone) 
        
# метод пошуку контакту за номером телефону   
def find_phone():
    phone_number = input('Enter a phone number to find: ')
    
    found_contacts = []
    for name, contact in addressbook.items():
        if any(phone.value == phone_number for phone in contact.phones):
            found_contacts.append(contact)

    if found_contacts:
        console = Console()
        table = Table(title=f'Contacts with phone number {phone_number}', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
        table.add_column('Name', justify='center', style='#FF6C00', no_wrap=True, min_width=16)
        table.add_column('Phone', justify='center', style='#FF6C00', no_wrap=True, min_width=12)
        table.add_column('Birthday', justify='center', style='#FF6C00', no_wrap=True, min_width=12)
        table.add_column('Email', justify='center', style='#FF6C00', no_wrap=True, min_width=12)
        table.add_column('Address', justify='center', style='#FF6C00', no_wrap=True, min_width=10)

        for contact in found_contacts:
            table.add_row(contact.name.value, ', '.join(str(phone.value) for phone in contact.phones),
                          contact.birthday.value if contact.birthday else 'N/A', contact.email.value if contact.email else 'N/A',
                          contact.address.value if contact.address else 'N/A')

        console.print(table)
    else:
        print(f'No contacts found with phone number {phone_number}.')

# метод видалення контакту за ім'ям          
def delete_contact():
    name = input('Enter the name: ')
    if not name in addressbook:
        return f'contact {name} is not found'
    contact = addressbook.delete(name)
    return print(f'contact {contact} was deleted')

# метод твидалення номеру телефону з контакту
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

# метод додавання електронної пошти котакту
def add_email():
    name = input('Enter the name: ')
    if name in addressbook:
        email = input('Enter the email in format "example@example.com": ')
        record: Record = addressbook.find_record(name)
        record.add_email(email)
        return print(f"{email} for contact {name} added")
    else:
        return print(f"Contact not found. Please try again")

# метод додавання адреси контакту
def add_address():
    name = input('Enter the name: ')
    if name in addressbook:
        address = input('Enter the address')
        record: Record = addressbook.find_record(name)
        record.add_address(address)
        return print(f"{address} for contact {name} added")
    else:
        return print(f"Contact not found. Please try again")

# метод додавання дня народження контакту
def add_birthday():
    name = input('Enter the name: ')
    if name in addressbook:
        birthday = input('Enter the birthday in format dd.mm.yyyy')
        record: Record = addressbook.find_record(name)
        record.add_birthday(birthday)
        return print(f"{birthday} for contact {name} added")
    else:
        return print(f"Contact not found. Please try again")

# метод редагування телефону контакту
def edit_phone():
    name = input('Enter the name: ')
    if name in addressbook:
        old_phone = input('Enter the number phone for change')
        new_phone = input('Enter the new phone')
        record: Record = addressbook.find_record(name)
        record.edit_phone(old_phone, new_phone)
        return print(f"{old_phone} was changed {new_phone} for contact {name}")
    else:
        return print(f"Contact not found. Please try again")

# метод, що виводити інформацію про найближці дня народження за вказаинй період
def uncoming_birthdays():
    days = int(input('Enter the check period in days: '))
    if days > 0:
        if addressbook.find_birthdays_in_days(days):
            for record, days_until_birthday in addressbook.find_birthdays_in_days(days):
                print(f"{record.name.value}'s birthday in {days_until_birthday} days: {record.birthday.value}")
        else:
            print('No uncoming birthdays.')   
    else:
        print('The number of days can only be positive. Try again')


################################ Сортувальник
        
def clean():
    path = input('Enter path: ')
    run_func(path)
        
    
if __name__ == "__main__":
    pass