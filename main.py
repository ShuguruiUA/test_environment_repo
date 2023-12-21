# from package.addressbook import Phone, Email
# from package.note_book import Note, Notebook
import os
import pickle
import pathlib
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from package.james_logic import *

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

with open('image.txt', 'r') as fh:
    all_file = fh.read()
    print(f'{RED}{all_file}{RESET}')

# notebook = Notebook()

exit_list = ('exit', 'quit', 'end')
note_list = list()

notes_id = 0

command_menu = WordCompleter(['create-note', 'show-notes', 'save-notes', 'load-notes',
                              'quit', 'exit', 'find-tag', 'create-contact', 'show-contacts', 'find-record', 'add-phone',
                              'find-phone', 'delete-contact', 'remove-phone','add-email', 'add-address', 'add-birthday', 'edit-phone', 'uncoming_birthdays'])

com_list = ['create-note', 'show-notes', 'save-notes', 'load-notes',
                              'quit', 'exit', 'find-tag', 'create-contact', 'show-contacts', 'find-record', 'add-phone',
                              'find-phone', 'delete-contact', 'remove-phone','add-email', 'add-address', 'add-birthday', 'edit-phone','uncoming_birthdays']
def main():
    if not os.path.exists(note_file):
        pass
    else:
        load()
    while True:
        # input('Bond says: ').lower()
        operation = prompt('Bond says: ', completer=command_menu).lower()

        if operation.startswith(exit_list):

            save()
            print(f'Good bye and have a nice day!')
            quit()

        elif operation.startswith('create-note'):
            create_note()


        elif operation.startswith('show-notes'):
            show_notes()

        elif operation.startswith('save-notes'):
            save()

        elif operation.startswith('load-notes'):
            if not os.path.exists('note-file'):
                print('The file is not exist')
                pass
            else:
                load()
                print(f'Notes file load successful')

        elif operation.startswith('find-tag'):
            find_tag()


        elif operation.startswith('create-contact'):
            create_contact()


        elif operation.startswith('show-contacts'):
            show_contacts()

        elif operation.startswith('find-record'):
            find_record()

        elif operation.startswith('add-phone'):
            add_phone()

        elif operation.startswith('add-email'):
            add_email()

        elif operation.startswith('add-address'):
            add_address()

        elif operation.startswith('add-birthday'):
            add_birthday()

        elif operation.startswith('edit-phone'):
            edit_phone()

        elif operation.startswith('find-phone'):
            find_phone()

        elif operation.startswith('delete-contact'):
            delete_contact()
            # return f'contact {delete_contact} was delete successfuly'

        elif operation.startswith('remove-phone'):
            remove_phone()
        
        elif operation.startswith('uncoming_birthdays'):
            uncoming_birthdays()

        else:
            pass


if __name__ == "__main__":
    main()