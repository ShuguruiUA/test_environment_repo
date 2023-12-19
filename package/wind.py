# встановлюємо модуль prompt_toolkit: pip install prompt_toolkit

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# створємо список команд, які будуть у у меню підказок
command_menu = WordCompleter(['add_note', 'add_teg', 'seach', 'find_adress', 'find_note', 'add_birth', 'del_note', ' del_adress', 'quit'])

while True:
    # записуємо у змінну результат вводу користувача
    # команда prompt використовуємо як розширену версію input
    command_input = prompt('Введіть команду:  ', completer=command_menu)
    if command_input == 'quit':
        break
    asd = f'{command_input} mission complete'
    print(asd)