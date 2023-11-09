"""Тут реалізовані тільки мої функції"""
"""далі планую додати декоратори"""
from notebook import NoteBook

note_book = NoteBook()

def func_add_note(*args):
    title = ' '.join(args)
    if title not in note_book:
        input_text = input("Input text:\n")
        question = input("want to add tags? (Y/N)" )
        if question == 'y'.casefold():
            tags_input = input('Input tags: ') 
            tags = ['#' + tag.strip() for tag in tags_input.split()]
        else:
            tags = []
        if tags:
            note_book.add_note(title, input_text, tags)
            return 'ok' # тут напевно щось треба написати серйозніше
        else:
            note_book.add_note(title, input_text)
            return 'ok' 
    else:
        question = input(f"want edit note {title}? (Y/N)" ) 
        if question == 'y'.casefold():
            input_new_text = input("Input new text:\n")
            note_book.edit_note(title, input_new_text)
            return "ok" 
        else:
            return "ok"
        
def func_edit_note(*args):
    title = ' '.join(args)
    input_new_text = input("Input new text:\n")
    note_book.edit_note(title, input_new_text)
    return "all ok"

def func_edit_tags(*args):
    title = ' '.join(args)
    input_new_tags = input("Input new tags:\n")
    new_tags = ['#' + tag.strip() for tag in input_new_tags.split()]
    note_book.edit_note(title, None, new_tags)
    return "all ok"
        
def func_show_notes():
    return note_book

def func_search_notes(*args):
    keyword = ' '.join(args)
    return note_book.search_notes(keyword)

def func_sort_notes():
    return note_book.sort_notes()


OPERATORS = {
    "add note": func_add_note, # add note заголовок нотатку --> далі по підказкам
    "edit note": func_edit_note, # edit note заголовок --> далі по підказкам
    "edit tags": func_edit_tags, # edit tags заголовок --> далі по підказкам
    "show notes": func_show_notes, # show notes  (тут без заголовку)
    "show note": func_search_notes, # show note (будь яку слово з заголовку або #тег)
    "sort notes": func_sort_notes, # sort notes (без аргументів) - сортує, виводить та зберігає новий порядок нотатків, сортування за кількістю тегів, як замовляв викладач
    
}

"""все що вище треба вписати в основний main.py"""



    
#далі я нічого не міняв
def unknown(*args):
    return "Unknown command. Try again."

def parser(text: str):
    for func in OPERATORS.keys():
        if text.startswith(func):
            return func, text[len(func) :].strip().split()
        
    return unknown, []


def main():
    while True:
        user_input = input(">>>")
        func, data = parser(user_input.lower())
        current_func = OPERATORS.get(func)
        print(current_func(*data))


if __name__ == '__main__':
    
    main()
