from collections import UserDict



class AddressBook (UserDict):
        
    def add_record(self, name, phone):
        
        
        
        self.data[name] = Record(name, phone)


class Field:
    pass

class Name (Field):
    value = ''

class Phone (Field):
    
    def __init__(self, value): # constructor
                   
        self.value = value             # field 1

class Record:
    
    def __init__(self, name, phone): # constructor
        self.name = name
        #Phone.value = phone            # field 1
        self.phone_stor = Phone(phone)             # field 2
    
    
    
    
    def add_phone (self, phone):
        add_book.data[self.name.value].append(phone)
       

    def del_phone (self, phone):
        add_book.data[self.name.value].remove(phone)

    def edit_phone (self, phone):
        
        index_edit = add_book.data[self.name.value].index(phone)

        new_phone = input('Enter new telephone number. Please! : ')
        add_book.data[self.name.value].remove(phone)
        add_book.data[self.name.value].insert(index_edit, new_phone)
        


# create dict
print('create dict')
add_book = AddressBook()

# add record
add_book.add_record('Serhii', '0675261531')
add_book.add_record('Andrii', '0325261531')

# show all 
print('show all')
print(add_book.data['Andrii'].phone_stor.value)
print(type(add_book.data['Serhii'].phone_stor.value))

# add phone
print("add phone")
add_book.data['Andrii'].phone_stor = Phone('77777')

#Record().add_phone('0962327381')
print(add_book.data['Andrii'].phone_stor.value)


""" # add phone
print("add phone")
Record().add_phone('5678908967')
print(add_book.data) """


""" # del phone
print("del phone")
Record().del_phone('0962327381')
print(add_book.data) """


""" # add phone
print("add phone")
Record().add_phone('0962327381')
print(add_book.data) """

""" # edit phone
print("edit phone")
Record().edit_phone('5678908967')
print(add_book.data) """




""" as_dict = AddressBook()
as_dict[Record.name.value] = '0675261531'
print(as_dict.data) """


""" print(dir(Name))
name_1 = Name()
name_1.name = 'Serhii'
print(name_1.name)
name_2 = Name()
name_2.name = 'Andrii'
print(name_2.name)


print(Record().name) """


