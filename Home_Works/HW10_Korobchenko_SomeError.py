# BOT assistent
# CLI - Command Line Interface
#              Architecture :
#                   - command`s parser
#                   - command`s processing functions (handler) - in--> str out-->str
#                   - request-answear loop

# Input - dict(name: telephone number)
# Requirements:
#              - telephone number format: 0675223345 - 10 digits;
#              - bot undestands commands:
#                          - "hello" - answear: "How can I help you?"
#                          - "add name telephone number" - save new contact
#                          - "change name telephone number" - save new telephone number for existed contact
#                          - "phone name" - show telephone number
#                          - "show all" - show all contacts (name telephone number)
#                          - "addnum name telephone number" - add aditional tel number for certain contact
#                          - "del name telephone number" - del tel number for certain contact
#                          - "good bye" or "close" or "exit" - bot stops work and messege "Good bye!"
#
#
# Additional requirements:
#                  UserDict Class:
#                         -user has Book of Contacts (AddressBook Class): 
#                                 |__> records (Record Class): --> dict {Record.name.value: value}
#                                                              --> Name object - separated atribute
#                                                              --> Phone objects - separated atribute
#
#                                          |__> fields (Field Class):
#                                                      - required (e.g name - Name Class) - only one
#                                                      - optional (e.g tel - Field Class) - one or more
#
#                AdressBook methods:

#                                - add_record --> add Record in self.data
#                                - del  record
#                                - edit record              
#                                - find record by fields
#
#                                           Record Methods: 
#                                                 - add  field Phone
#                                                 - del  field Phone
#                                                 - edit field Phone

import re
from collections import UserDict

error_type = ''

class AddressBook (UserDict):
        
    def add_record(self, name, phone):
        
        Name.value = name
        Phone.value = phone
        self.data[Name.value] = [(Record.phone.value)]

class Field:
    pass

class Name (Field):
    value = ''

class Phone (Field):
    value = ''

class Record:
    name = Name()
    phone = Phone()
        
    def add_phone (self, name, phone):
        add_book.data[name].append(phone)
       
    def del_phone (self, name, phone):
        add_book.data[name].remove(phone)

    def edit_phone (self, name, new_phone):
        
   
        add_book.data[name].clear()
        add_book.data[name].append(new_phone)


class TelDoesNotMathFormatError(Exception):
    pass


class NameDoesNotExistError(Exception):
    pass


def command_parser (command): # command`s parser
    command_id = ''
    name = ''
    phone = ''
       
    parsered_list = command.split (" ")
    if len(parsered_list) == 1:
        command_id = parsered_list[0].lower() # make all letters small
    
    elif len(parsered_list) == 2:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
    elif len(parsered_list) == 3:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
        phone = parsered_list[2]
    else:
        print ("Number of arguments do not fit to reqirements. Please try again!")
        
    return command_id, name, phone

### Decorator
def input_error(func): # decorator
    
    def inner(*args, **kwargs):
        global error_type
        func(*args, **kwargs) 

        if error_type == 'TelDoesNotMathFormatError': # added functional zone
            print('Give me name and phone please')
        elif error_type == 'NameDoesNotExistError':
            print('Enter user name please')

        error_type = ''
        
    return inner

### handlers:
def hello_func ():
    print('How can I help you?')

@input_error
def add_func (name, phone):   #1&2

    global error_type
    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            add_book.add_record(name, phone) ###2

            print ('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:
        error_type = 'TelDoesNotMathFormatError'
        print("Telephone number does not match format - should be 10 digits")

    

@input_error
def change_func (name, phone):    #1&2

    global error_type
    try:
        if name in add_book.data:
            if re.match(r"^[0-9]{10,10}$", phone):
                
                Record().edit_phone(name, phone) ### 2

                print ('Phone number has been changed successfully!')
            else:
                raise TelDoesNotMathFormatError
        
        else:
            raise NameDoesNotExistError

    except TelDoesNotMathFormatError:
        error_type = 'TelDoesNotMathFormatError'
        print("Telephone number does not match format - should be 10 digits") 

    except NameDoesNotExistError:
        error_type = 'NameDoesNotExistError'
        print('Name does not exist')
    
@input_error
def phone_func (name):           #1&2

    global error_type
    try:

        if name in add_book.data:   ### 2
            for key, value in add_book.data.items():  ### 2
                if key == name:
                    print(f'Phone number assigned for requested name is: {value}')
        else:
            raise NameDoesNotExistError

    except NameDoesNotExistError:
        error_type = 'NameDoesNotExistError'
        print('Name does not exist.') #  - decorator

def show_func ():

    if len(add_book.data) == 0:
        print('Data Base is empty yet. Please add someone!')
    else:
        print('Data Base contains next contacts:')
 
        for key, value in add_book.data.items():                   ### 2
            mystring = ', '.join(map(str, value))
            print(f'Name : {key} | Telephone number: {mystring}')
        
@input_error
def addnum_func (name, phone):   #1&2

    global error_type
    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            Record().add_phone(name, phone) ###2

            print ('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:
        error_type = 'TelDoesNotMathFormatError'
        print("Telephone number does not match format - should be 10 digits")

@input_error
def del_func (name, phone):   #1&2

    global error_type
    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            Record().del_phone(name, phone) ###2

            print ('Telephone number has been deleted successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:
        error_type = 'TelDoesNotMathFormatError'
        print("Telephone number does not match format - should be 10 digits")

def good_buy_func ():
    print('Good bye!')
    return 'stop'

### MAIN BODY FUNCTION
def main():
    # create dict
    #print('create dict')
    global add_book
    add_book = AddressBook()

    commands_dict = {'hello': hello_func, 'add': add_func, 'change': change_func,\
         'phone': phone_func, 'show': show_func, 'good': good_buy_func,\
         'close': good_buy_func, 'exit': good_buy_func, 'addnum': addnum_func, 'del': del_func }
    
    stop_flag = ''
      
    print ("Bot has been started!")
    while True:
        try:
            print('')
            command = input("Please, put you command in Command line! (from 1 to 3 arguments): ")   
            command_id, name, phone = command_parser (command) # passing vars to another func

            for key, value in commands_dict.items():
                if command_id == key and name == '' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'bay' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'all' and phone == '':
                    res = value()
                        
                elif command_id == key and name != '' and phone == '':
                    res = value(name)

                elif command_id == key and name != '' and phone != '':
                    res = value(name, phone)

            if command_id not in commands_dict:
                print('I do not know this command!')
                                               
            if stop_flag == 'stop':
                break

        except TypeError:
            print('Unsuccessful operation. Please, try again')
        
if __name__ == '__main__':
    main()