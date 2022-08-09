from collections import UserDict



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
        


# create dict
print('create dict')
add_book = AddressBook()

# add record
add_book.add_record('Serhii', '0675261531')
add_book.add_record('Andrii', '0325261531')

# show all 
print('show all')
print(add_book.data)

# add phone
print("add phone")
Record().add_phone('Serhii', '0962327381')
print(add_book.data)


# add phone
print("add phone")
Record().add_phone('Andrii', '5678908967')
print(add_book.data)


 # del phone
print("del phone")
Record().del_phone('Serhii','0675261531')
print(add_book.data) 



# edit phone
print("edit phone")
Record().edit_phone('Andrii', '7777777777')
print(add_book.data)




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


