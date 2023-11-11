from servicenote import OPERATORS, note_book
from service_addressbook import FUNCTIONS, book, user_error


def func_good_bye():
    book.save()
    note_book.save_data()
    print(f"Good bye!")
    exit()


exit_commands = ["good bye", "close", "exit"]
EXIT = {command: func_good_bye for command in exit_commands}
COMMANDS = {}
COMMANDS.update(EXIT)
COMMANDS.update(OPERATORS)
COMMANDS.update(FUNCTIONS)


def parser(text: str):
    for func in COMMANDS.keys():
        if text.startswith(func):
            return func, text[len(func) :].strip().split()


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input.lower())
        current_func = COMMANDS.get(func)
        print(current_func(*data))


if __name__ == "__main__":
    main()
