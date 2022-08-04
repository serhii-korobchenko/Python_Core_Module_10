class Person:
    def __init__(self, name, age): # constructor
        self.name = name            # field 1
        self.age = age              # field 2

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34)  # call constructor
print(p.name)  # Boris
print(p.age)  # 34
print(p.greeting())  # Hi Boris