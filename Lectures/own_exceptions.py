from msilib.schema import Class
import string


class NameTooShortError(Exception): # my own ecxeption
    pass


class NameStartsFromLowError(Exception):  # my own ecxeption
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError




while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 3 symbols. Try again.')
    except NameStartsFromLowError:
        print('Name should start from capital letter. Try again.')