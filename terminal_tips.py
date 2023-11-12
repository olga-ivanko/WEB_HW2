from prompt_toolkit.completion import NestedCompleter
from service_addressbook import FUNCTIONS, EXIT
from servicenote import OPERATORS


COMMANDS = {}
COMMANDS.update(EXIT)
COMMANDS.update(OPERATORS)
COMMANDS.update(FUNCTIONS)


def func_completer(COMANDS: dict):
    comp_dict = {}
    sorted_comand = sorted(COMANDS.keys())
    for key in sorted_comand[1:]:
        matching_key = next((existing_key for existing_key in comp_dict.keys() if key.startswith(existing_key)), None)
        if matching_key is None:
            comp_dict[key] = None
        else:
            key_suffix = key[len(matching_key):].strip()
            if comp_dict[matching_key] is None:
                comp_dict[matching_key] = {key_suffix}  
            else:
                comp_dict[matching_key].add(key_suffix) 
    return comp_dict

completer = NestedCompleter.from_nested_dict(func_completer(COMMANDS))



    