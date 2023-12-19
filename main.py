from package.addressbook import Phone, Email
from package.note_book import Note, Notebook
import os
import pickle

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

with open('image.txt', 'r') as fh:
    all_file = fh.read()
    print(f'{RED}{all_file}{RESET}')

notebook = Notebook()

exit_list = ('exit', 'quit', 'end')
note_list = list()
note_file = './data/notebook.dat'
phone_file = './data/phonebook.dat'


notes_id = 0
list_notes = ['{:^85}'.format(
    '_'*85), '|{:^15}|{:^55}|{:^15}|'.format('Title', 'Note',
                                             'Tags'), '{:^85}'.format(
    '_'*85)]


def main():
    while True:
        operation = input('Bond says: ').lower()

        if operation.startswith(exit_list):
            Notebook.save_to_file(notebook, note_file)
            quit()

        elif operation.startswith('create_note'):
            x = input("Note's name: ")
            y = input("Note's title: ")
            z = input("Note's info: ")

            x = Note(y, z)
            # note_list.append(x)

            while True:
                tag_adder = input("Note's tag: ")
                if tag_adder.startswith('e'):
                    break
                else:
                    x.add_teg(tag_adder)
            notebook.add_note(x)

        elif operation.startswith('show_notes'):

            for k, v in notebook.items():
                #     x = v.note_title
                #     y = v.note_body
                #     z = '; '.join(p for p in v.tags)
                #     list_notes.append('|{:^15}|{:<55}|{:^15}'.format(x, y, z))
                # return [print(el) for el in list_notes]
                print(
                    f'Title: {v.note_title}, Note: {v.note_body} Tags: {"; ".join(p for p in v.tags)}')
            # print(Notebook.show_all(notebook))
            # for x in note_list:
            #     print(x)
        elif operation.startswith('save_notes'):
            Notebook.save_to_file(notebook, note_file)

        elif operation.startswith('load_notes'):
            if not os.path.exists('note_file'):
                pass
            Notebook.load_from_file(notebook, note_file)

        elif operation.startswith('find_tag'):
            find_tag = input('Enter the tag: ')
            Notebook.find_note_teg(notebook, find_tag)

        else:
            pass


main()
