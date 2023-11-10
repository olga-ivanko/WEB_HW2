from datetime import datetime
from addressbook import AddressBook, Record
from pathlib import Path
import sort
import re


book = AddressBook()
book.load()


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help."
        except KeyError:
            return "Unknown rec_id. Try another or use help."
        except ValueError:
            return "Unknown or wrong format. Check phone and/or birthday"
        except AttributeError:
            return "Contacts was not found"

    return inner


def func_normalize_phone(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+38")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    return new_phone


def unknown(*args):
    return "Unknown command. Try again."


@user_error
def func_add(*args):
    rec_id = args[0].lower()
    phone = args[1]
    new_phone = func_normalize_phone(phone)
    new_record = Record(rec_id)
    new_record.add_phone(new_phone)

    if rec_id in book.keys():
        return f"Record alredy exist"
    elif new_phone == None:
        return f"Check the phone: {phone}. Wrong format."

    if len(args) >= 2:
        new_email = None
        new_address = None
        contact_birtday = None
        while True:
            user_input = input("Enter your choice: ")
            if user_input == "back":
                break
            if user_input == "birthday":
                user = input("Enter birthday: ")
                new_birthday = datetime(
                    year=int(user[6:]), month=int(user[3:5]), day=int(user[:2])
                )
                contact_birtday = new_birthday.date().strftime("%d %B %Y")
                new_record.add_birthday(new_birthday)
                print("Birthday added")
            elif user_input == "email":
                user = input("Enter email: ")
                new_email = user
                new_record.add_email(new_email)
                print(f"main {new_email} added to user {new_record.name.value}")
            elif user_input == "address":
                user = input("Enter address: ")
                new_address = user
                new_record.add_address(new_address)
                print("Address added")

        book[rec_id] = new_record
        if new_address:
            return f"Add record {rec_id = }, {new_phone = }, {contact_birtday = }, {new_email = }, {new_address = }"
        elif new_email:
            return f"Add record {rec_id = }, {new_phone = }, {contact_birtday = }, {new_email = }"
        return f"Add record {rec_id = }, {new_phone = }, {contact_birtday = }"

    book[rec_id] = new_record
    return f"Add record {rec_id = }, {new_phone = }"


@user_error
def add_birthday(*args):
    rec_id = args[0]
    birth = args[1]
    if not rec_id in book:
        return "Not user"
    new_birthday = datetime(
        year=int(birth[6:]), month=int(birth[3:5]), day=int(birth[:2])
    )
    book.find(rec_id).add_birthday(new_birthday)
    return "Add Birthday completed"


@user_error
def add_email(*args):
    rec_id = args[0]
    email = args[1]
    if not rec_id in book:
        return "Not user"
    book.find(rec_id).add_email(email)
    return "Add email completed"


def func_address(*args):
    rec_id = args[0]
    address = args[1]
    if not rec_id in book:
        return "Not user"
    book.find(rec_id).add_address(address)
    return "Add address completed"


@user_error
def func_change(*args):
    rec_id = args[0].lower()
    old_phone = func_normalize_phone(args[1])
    new_phone = func_normalize_phone(args[2])

    if old_phone == None:
        return f"Check the phone: {args[1]}. Wrong format."
    if new_phone == None:
        return f"Check the phone: {args[2]}. Wrong format."

    book.find(rec_id).edit_phone(old_phone, new_phone)
    return f"Record {rec_id} is updated with nes phone: {book.get(rec_id).phones[0]}"


@user_error
def func_phone(*args):
    rec_id = args[0]
    return f"Phone of {rec_id} is {book.get(rec_id).phones[0]}"


def func_hello(*args):
    return f"How can I help you?"


@user_error
def func_show_all(*args):
    if len(book) == 0:
        return f"Your contacts list is empty"
    line = ""
    for record in book.values():
        line += f"{record}\n"
    return line


@user_error
def func_show(*args):
    if len(book) == 0:
        return f"Your contacts list is empty"
    stop = int(args[0])
    line = ""
    for rec in book.iterator(stop):
        line += rec
    return line


@user_error
def func_find(*args):
    line = ""
    for record in book.values():
        str_rec = str(record.name)
        for ph in record.phones:
            str_rec += str(ph)
        found_rec = re.findall(args[0], str_rec)
        if len(found_rec) != 0:
            line += f"{record}\n"

    if len(line) == 0:
        return f'the search for key "{args[0]}" gave no results. Try other key.'
    print(f'result for "{args[0]}" search:')
    return line


@user_error
def func_remove(*args):
    rec_id = args[0]
    book.delete(rec_id)
    return f"Contact {rec_id} succesfully removed"


def func_sort_folder(*args):
    user_input = input("Enter directory path: ")
    path = Path(user_input)
    if path.exists():
        return sort.main(path)
    else:
        return f"The path {path} does not exist."


FUNCTIONS = {
    "hello": func_hello,
    "add": func_add,
    "change": func_change,
    "phone": func_phone,
    "show all": func_show_all,
    "show": func_show,
    "find": func_find,
    "email": add_email,
    "city": func_address,
    "birthday": add_birthday,
    "remove": func_remove,
    "sort folder": func_sort_folder,
    "": unknown
}
