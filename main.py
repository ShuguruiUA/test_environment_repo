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
                              'quit', 'exit'])


def main():
    load()
    while True:
        # input('Bond says: ').lower()
        operation = prompt('Bond says: ', completer=command_menu)

        if operation.startswith(exit_list):
            # Notebook.save_to_file(notebook, note_file)
            # print(Notebook.save_to_file(notebook, note_file))
            save()
            print(f'Good bye and have a nice day!')
            quit()

        elif operation.startswith('create_note'):
            create_note()
            # id_counter = 0
            # # x = input("Note's name: ")
            # x = id_counter
            # y = input("Note's title: ")
            # z = input("Note's info: ")

            # x = Note(y, z)
            # # note_list.append(x)

            # while True:
            #     tag_adder = input("Note's tag: ")
            #     if tag_adder.startswith('e'):
            #         break
            #     else:
            #         x.add_teg(tag_adder)
            # notebook.add_note(x)
            # id_counter += 1

        elif operation.startswith('show_notes'):

            for value in notebook.values():
                print(
                    f'Title: {value.note_title} | Note: {value.note_body} | Tags: {"; ".join(t for t in value.tags)}')

            # for k, v in notebook.items():
                #     x = v.note_title
                #     y = v.note_body
                #     z = '; '.join(p for p in v.tags)
                #     list_notes.append('|{:^15}|{:<55}|{:^15}'.format(x, y, z))
                # return [print(el) for el in list_notes]
                # print(
                # f'Title: {v.note_title}, Note: {v.note_body} Tags: {"; ".join(p for p in v.tags)}')
            # print(Notebook.show_all(notebook))
            # for x in note_list:
            #     print(x)
        elif operation.startswith('save_notes'):
            save()

        elif operation.startswith('load_notes'):
            if not os.path.exists('note_file'):
                print('The file is not exist')
                pass
            else:
                load()
                print(f'Notes file load sucessful')

        # elif operation.startswith('find_tag'):
        #     find_tag = input('Enter the tag: ')
        #     Notebook.find_note_teg(notebook, find_tag)

        else:
            pass


if __name__ == "__main__":
    main()
