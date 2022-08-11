class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info (self):
        return {'name': self.name,
                'age':  self.age,
                'adress': self.address}

    
class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        super().__init__(nickname, weight)
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self): 
        return self.owner.info()      


owner = Owner('Serhii', 44, 'Ukraine')

dog = Dog("Barbos", 23, "labrador", owner)
print(dog.who_is_owner())
        
        

    