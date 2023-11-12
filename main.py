from servicenote import OPERATORS, note_book
from service_addressbook import FUNCTIONS, book
from pathlib import Path



def func_good_bye():
    book.save()
    note_book.save_data()
    print(f"Good bye!")
    exit()


EXIT = ["good bye", "close", "exit"]

def parser(text: str):
    for func in EXIT:
        if text == func:
            return func_good_bye()
    for func in OPERATORS.keys():
        if text.startswith(func):
            return func, text[len(func) :].strip().split()

    for func in FUNCTIONS.keys():
        if text.startswith(func):
            return func, text[len(func) :].strip().split()


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input.lower())
        if func in EXIT:
            current_func = func_good_bye
        elif func in FUNCTIONS:
            current_func = FUNCTIONS.get(func)
            print(current_func(*data))
        elif func in OPERATORS:
            current_func = OPERATORS.get(func)
            print(current_func(*data))




if __name__ == "__main__":
    main()
