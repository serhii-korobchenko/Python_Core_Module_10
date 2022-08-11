
class Phones:

    def __init__(self, phone = '0') -> None:
        self.phone = phone

    

class Record:
    def __init__(self, name) -> None:
        self.name = name
       
        self.phone = Phones

    def phone_instance (self):
        instance_list = []
        instance_list.append(Phones())



instance_list = []
instance_list.append(Phones('0675261531'))

my_record = Record('Serhii')



print(my_record.name)
print(instance_list[0].phone)