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

data_base = {}
error_type = ''

class AddressBook (UserDict):
    pass

class Record (AddressBook):
    pass

class Field (Record):
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

        if error_type == 'ValueError': # added functional zone
            print('Give me name and phone please')
        elif error_type == 'KeyError':
            print('Enter user name please')
        elif error_type == 'IndexError':
            print('IndexError')
        error_type = ''
        
    return inner



### handlers:
def hello_func ():
    print('How can I help you?')

@input_error
def add_func (name, phone):
    global data_base
    global error_type
    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            data_base[name] = phone
            print ('Information has been added successfully!')
        else:
            raise ValueError

    except ValueError:
        error_type = 'ValueError'
        print("Telephone number does not match format - should be 10 digits")


@input_error
def change_func (name, phone):
    global data_base
    global error_type
    try:
        if name in data_base:
            if re.match(r"^[0-9]{10,10}$", phone):
                
                data_base.update({name: phone})
                print ('Phone number has been changed successfully!')
            else:
                raise ValueError
        
        else:
            raise KeyError

    except ValueError:
        error_type = 'ValueError'
        print("Telephone number does not match format - should be 10 digits") 

    except KeyError:
        error_type = 'KeyError'
        print('Name does not exist')
    

@input_error
def phone_func (name):
    global data_base
    global error_type
    try:
        if name in data_base:
            for key, value in data_base.items():
                if key == name:
                    print(f'Phone number assigned for requested name is: {value}')
        else:
            raise KeyError

    except KeyError:
        error_type = 'KeyError'
        print('Name does not exist.') #  - decorator


def show_func ():
    global data_base
    if len(data_base) == 0:
        print('Data Base is empty yet. Please add someone!')
    else:
        print('Data Base contains next contacts:')
        for key, value in data_base.items():
            print(f'Name : {key} | Telephone number: {value}')

def good_buy_func ():
    print('Good bye!')
    return 'stop'
    

### MAIN BODY FUNCTION
def main():
    
    commands_dict = {'hello': hello_func, 'add': add_func, 'change': change_func,\
         'phone': phone_func, 'show': show_func, 'good': good_buy_func,\
         'close': good_buy_func, 'exit': good_buy_func}
    
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