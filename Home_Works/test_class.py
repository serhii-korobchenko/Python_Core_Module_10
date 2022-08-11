
class Phones:

    def __init__(self, phone) -> None:
        self.phone = phone

class Record:
    def __init__(self, name, phone) -> None:
        self.name = name
        Phones.phone = phone
        self.phone = Phones

    def phone_instance (self):
        instance_list = []
        instance_list.append(Phones())

phone_1 = Phones('0675261531')
phone_2 = Phones('7777777777')

my_record = Record('Serhii', '0675261531')


print(my_record.name)
print(my_record.phone.phone)