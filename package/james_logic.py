from package.note_book import Notebook, Note
from package.addressbook import AddressBook, Record, Phone
import os
from rich.console import Console
from rich.table import Table
from package.clean import run_func

# кольори для лого
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Створення екземплярів класів

notebook = Notebook()
addressbook = AddressBook()
console = Console()

note_file = './notebook.bin'
phone_file = './phonebook.bin'

#Декоратор помилок

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args)
        except Exception as e:
            return e
        else:
            return result
    return inner

# Визначення таблиць для нотаток і контактів

@input_error
def Notes_Table():
    global table_notes
    table_notes = Table(title='[italic #FF6C00]Table of notes :heavy_check_mark:', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
    table_notes.add_column('Title', justify='center', style='#FF6C00', no_wrap=True, min_width=16)
    table_notes.add_column('Note', justify='center', style='#FF6C00', min_width=60)
    table_notes.add_column('Tags', justify='center', style='#FF6C00', min_width=16)

@input_error
def Record_Table():
    global table_record
    table_record = Table(title='[italic #FF6C00]Table of records :heavy_check_mark:', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
    table_record.add_column('Name', justify='center', style='#FF6C00', min_width=16)
    table_record.add_column('Phone', justify='center', style='#FF6C00', min_width=12)
    table_record.add_column('Birthday', justify='center', style='#FF6C00', min_width=12)
    table_record.add_column('Email', justify='center', style='#FF6C00', min_width=12)
    table_record.add_column('Address', justify='center', style='#FF6C00', min_width=10)

# функціяи для збереження та завантаження нотаток і адресної книги
@input_error
def save():
    if not os.path.isfile(note_file) or not os.path.isfile(phone_file):
     
        file = open('./notebook.bin', 'a')
        file2 = open('./phonebook.bin', 'a')
        Notebook.save_to_file(notebook, note_file)
        AddressBook.saved_to_file(addressbook, phone_file)
    else:
        Notebook.save_to_file(notebook, note_file)
        AddressBook.saved_to_file(addressbook, phone_file)
    # print(f'notebook file {note_file} saved successfuly')

@input_error
def load():
    if not os.path.isfile(note_file) or not os.path.isfile(phone_file):
        file = open('./notebook.bin', 'a')
        file2 = open('./phonebook.bin', 'a')
    else: 
        Notebook.load_from_file(notebook, note_file)
        AddressBook.load_from_file(addressbook, phone_file)




################################ Нотатки

# функція створення нотатки
@input_error
def create_note():
    new_note_title = input("Note's title: ")
    new_note_title = new_note_title.capitalize()
    if not new_note_title in notebook:
        note_body = input("Note's info: ")
        new_note_title = Note(new_note_title, note_body)
        while True:
            tag_adder = input("Note's tag (type 'e' for exit): ")
            if tag_adder.startswith('e'):
                break
            else:
                new_note_title.add_tag(tag_adder)
        notebook.add_note(new_note_title)

        return print(f'Note {new_note_title.note_title} was added successfuly')
    return print(f'Note with {new_note_title} already exists')

# функція виводу усіх збережених нотаток у формі таблиці
@input_error
def show_notes():
    Notes_Table()
    for v in notebook.values():
        table_notes.add_row(v.note_title, v.note_body,
                            ', '.join(p for p in v.tags))
    console.print(table_notes)

# функція пошуку нотатки за тегом
@input_error    
def find_tag(tag_to_find):
    tag_to_find = input('Enter a tag that you want to find: ')
    found_notes = []
    for note in notebook.find_note_tag(tag_to_find):
        found_notes.append(note)

    if found_notes:
        console = Console()
        table = Table(title=f'Notes with tag: {tag_to_find}', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
        table.add_column('Title', justify='center', style='#FF6C00', no_wrap=True, min_width=16)
        table.add_column('Note', justify='center', style='#FF6C00', no_wrap=True, min_width=60)
        table.add_column('Tags', justify='center', style='#FF6C00', no_wrap=True, min_width=16)

        for note in found_notes:
            table.add_row(note.note_title, note.note_body, ', '.join(note.tags))

        console.print(table)
    else:
        print(f'No notes found with tag: {tag_to_find}.')

# функція редагування тіла нотатки
@input_error        
def edit_note():
    title = input('What note do you want to edit? Enter a note title: ')
    if title in notebook.data:
        new_body = input('Enter new note text: ')
        notebook.edit_note(title, new_body)
        print(f"Note '{title}' body has been updated.")
    else:
        print(f"Note '{title}' not found in the notebook.")

# функція видалення нотатки за ім'ям
@input_error
def delete_note():
    note_title = input('Which note title do you want to delete? Enter a note title: ')
    if note_title in notebook.data:
        notebook.delete(note_title)
        return print(f'Note with title "{note_title}" successfuly deleted')
    else:
        return print(f'Note with title "{note_title}" does not exists')

   
################################ Адресна книга

# функція ствогення нового контакту
@input_error
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

# функція виводу збереженних контактів у формі таблиці
@input_error    
def show_contacts():
    Record_Table()
    for el in addressbook.values():
        if not el in addressbook:
            table_record.add_row(el.name.value,'\n'.join(str(t) for t in el.phones), el.birthday.value, el.email.value, el.address.value)
    console.print(table_record)

# функція пошуку контакту за ім'ям   
@input_error   
def find_record():
    name = input('Input contact name: ')
    record = addressbook.find_record(name)

    if record:
        console = Console()
        table = Table(title=f'Contact Details for {name}', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
        table.add_column('Field', justify='center', style='#FF6C00', no_wrap=True, min_width=16)
        table.add_column('Value', justify='center', style='#FF6C00', no_wrap=True, min_width=16)

        table.add_row('Name', record.name.value)
        for phone in record.phones:
            table.add_row('Phone', phone.value)
        table.add_row('Birthday', record.birthday.value if record.birthday else 'N/A')
        table.add_row('Email', record.email.value if record.email else 'N/A')
        table.add_row('Address', record.address.value if record.address else 'N/A')

        console.print(table)
    else:
        print(f'Contact with name {name} not found.')

# функція додавання телефону до існуючого контакту?
@input_error        
def add_phone():
    name = input('Input contact name: ')
    if name in addressbook:
        phone = input('Enter the phone in format "1234567890": ')
        record: Record = addressbook.find_record(name)
        res = record.add_phone(phone)
        return print(res)
    else:
        return print(f'{name}\'s contact does not exist in phone book, please create it first')
        

        
# функція пошуку контакту за номером телефону  
@input_error 
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

# функція видалення контакту за ім'ям  
@input_error        
def delete_contact():
    name = input('Enter the name: ')
    if not name in addressbook:
        return f'contact {name} is not found'
    addressbook.delete(name)
    return print(f'contact {name} was deleted')

# функція твидалення номеру телефону з контакту
@input_error
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

# функція додавання електронної пошти котакту
@input_error
def add_email():
    name = input('Enter the name: ')
    if name in addressbook:
        email = input('Enter the email in format "example@example.com": ')
        record: Record = addressbook.find_record(name)
        record.add_email(email)
        return print(f"{email} for contact {name} added")
    else:
        return print(f"Contact not found. Please try again")

# функція додавання адреси контакту
@input_error
def add_address():
    name = input('Enter the name: ')
    if name in addressbook:
        address = input('Enter the address: ')
        record: Record = addressbook.find_record(name)
        record.add_address(address)
        return print(f"{address} for contact {name} added")
    else:
        return print(f"Contact not found. Please try again")

# функція додавання дня народження контакту
@input_error
def add_birthday():
    name = input('Enter the name: ')
    if name in addressbook:
        birthday = input('Enter the birthday in format dd.mm.yyyy: ')
        record: Record = addressbook.find_record(name)
        record.add_birthday(birthday)
        return print(f"{birthday} for contact {name} added")
    else:
        return print(f"Contact not found. Please try again")

# функція редагування телефону контакту
@input_error
def edit_phone():
    name = input('Enter the name: ')
    if name in addressbook:
        old_phone = input('Enter the number phone for change: ')
        new_phone = input('Enter the new phone: ')
        record: Record = addressbook.find_record(name)
        record.edit_phone(old_phone, new_phone)
        return print(f"{old_phone} was changed {new_phone} for contact {name}")
    else:
        return print(f"Contact not found. Please try again")

# функція, що виводити інформацію про найближці дня народження за вказаинй період
@input_error
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

# функція сортування файлів    
@input_error    
def clean():
    path = input('Enter path: ')
    run_func(path)
        
    
if __name__ == "__main__":
    pass

# help
def help():
    boot_logo()
    table_help = Table(title='[italic #FF6C00]Commands and description :question_mark:', header_style='#FF6C00', show_lines=True, border_style='#F0F0F0')
    table_help.add_column('Command', justify='center', style='#2771ea', no_wrap=True, min_width= 16)
    table_help.add_column('Description', justify='left', style='#2771ea', no_wrap=True, min_width=40)
    table_help.add_row('create-contact', 'create a new contact. Required data = name, phone, birthday. Additional = email, address')
    table_help.add_row('add-phone', 'add additional phone for existing contact')
    table_help.add_row('add-email','add/change email address for existing contact')
    table_help.add_row('add-birthday', 'add/change birthday for existing contact')
    table_help.add_row('add-address', 'add/change address for existing contact')
    table_help.add_row('edit-phone', 'change number for existing contact')
    table_help.add_row('show-contacts', 'show all contacts in address book')
    table_help.add_row('find-record','searching for records in address book by contact name and return result')
    table_help.add_row('find-phone', 'looking for phone number in the address book if exists return all data for the contact')
    table_help.add_row('remove-phone', 'remove phone number from the existing record')
    table_help.add_row('delete-contact', 'delete record from address book')
    table_help.add_row('uncoming-birthdays', 'shows days to birthday by period setted by user, by default 7 days')
    table_help.add_row('create-note','create new note. Requires note title, note data, at least one tag, for exiting from adding tag please put "e"')
    table_help.add_row('edit-note', 'allowed user to change note data in existing note by title')
    table_help.add_row('show-notes','shows all available notes')
    table_help.add_row('find-tag','searching for note by its tag, return table of notes with this tag')
    table_help.add_row('delete-note','delete note user should input note title')
    table_help.add_row('save-data', 'aving data for address and note books')
    table_help.add_row('load-data','loading data for address and note books')
    table_help.add_row('clean-folder','Some useful function to cleanup mess in yours "trash" folder')
    table_help.add_row('exit, quit', 'commands to exit from programm')
    
    console.print(table_help)


# лого
def boot_logo():
    print('\n'
        f"{BLUE}             ..:::.                  .:::.         ..................... ..........................{RESET}\n"
        f"{BLUE}         .!YG#&@@@#P7.           ^?5B&@@@&BY^     !#&#&&&&&&&&&&######&5 J&&&&&&&&&&&&&&&&&&&&&&&@P{RESET}\n"
        f"{BLUE}       :Y#@@@@#J!5@@@B~        !G@@@@@P77#@@@Y   !@@@@&#########@@@@@@@7.#@@@@@@@@@@@@@@@@@@@@@@@P:{RESET}\n"
        f"{BLUE}     .Y@@@@@@J.  .&@@@&^     ~B@@@@@B~   J@@@@5 :&@@@5. .....  Y@@@@@@P !GPPPPPPPPPPPGGJ^::::::::  {RESET}\n"
        f"{BLUE}    ~#@@@@@&~    ^@@@@@P    Y@@@@@@P.    5@@@@@~Y&##5        .Y@@@@@@P.JPPPPPP55PPP5Y!             {RESET}\n"
        f"{BLUE}   !@@@@@@#^     J@@@@@#.  P@@@@@@Y     .&@@@@@J ...        7#@@@@@@J ~@@GPPPG@@#J!~:              {RESET}\n"
        f"{BLUE}  ~@@@@@@&^     :&@@@@@B  5@@@@@@5      J@@@@@@7          ~G@@@@@@G~  :BB    P@P.                  {RESET}\n"
        f"{BLUE} .#@@@@@@!      P@@@@@@Y 7@@@@@@G      ~@@@@@@&:        ^P@@@@@@#7      :  ^B@?                    {RESET}\n"
        f"{BLUE} ?@@@@@@J      J@@@@@@&:.#@@@@@#:     :#@@@@@@Y       .J&@@@@@@Y:7YYYYYYYYP#P^                     {RESET}\n"
        f"{BLUE} G@@@@@G      J@@@@@@@! ~@@@@@@!     :B@@@@@@G.      7#@@@@@@P^ .~~~~~~~~^^.                       {RESET}\n"
        f"{BLUE} B@@@@&^     Y@@@@@@@?  !@@@@@5     ^#@@@@@@B:     ^G@@@@@@B!                                      {RESET}\n"
        f"{BLUE} P@@@@5    :P@@@@@@&!   ^@@@@@^    !&@@@@@@P.     ?@@@@@@@5.                                       {RESET}\n"
        f"{BLUE} ^@@@@7   7#@@@@@@P:     5@@@B   :5@@@@@@#7      Y@@@@@@@J                                         {RESET}\n"
        f"{BLUE}  ~#@@BJJB@@@@@&5~        Y@@@5?5&@@@@@B?.      Y@@@@@@@J                                          {RESET}\n"
        f"{BLUE}   .7P#@@@&#B57:           ^YB&@@@&#PJ~        ^BBBBBBBY                                           {RESET}\n"
        f"{BLUE}      .::::.                  .:::.                                                                {RESET}\n"
        
          
          "\n")
    