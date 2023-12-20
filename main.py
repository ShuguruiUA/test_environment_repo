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

command_menu = WordCompleter(['create_note', 'show_notes', 'save_notes', 'load_notes',
                              'quit', 'exit', 'find_tag', 'create_contact', 'show_contacts'])


def main():
    load()
    print(notebook)
    while True:
        # input('Bond says: ').lower()
        operation = prompt('Bond says: ', completer=command_menu)

        if operation.startswith(exit_list):

            save()
            print(f'Good bye and have a nice day!')
            quit()

        elif operation.startswith('create_note'):
            create_note()


        elif operation.startswith('show_notes'):
            show_notes()

        elif operation.startswith('save_notes'):
            save()

        elif operation.startswith('load_notes'):
            if not os.path.exists('note_file'):
                print('The file is not exist')
                pass
            else:
                load()
                print(f'Notes file load sucessful')

        elif operation.startswith('find_tag'):
            find_tag()

            
        elif operation.startswith('create_contact'):
            create_contact()
            
            
        elif operation.startswith('show_contacts'):
            show_contacts()

        else:
            pass


if __name__ == "__main__":
    main()
    
