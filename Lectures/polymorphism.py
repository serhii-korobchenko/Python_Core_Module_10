class Mammal:                   #                ->   Mamal  <-                   Chupakabra
    phrase = ''                 #              /                \
    def voice(self):     #voice 1             /                  \
        return self.phrase      #           Dog                  Cat

#                                                                   POLIMORHISM - Python assosiate
class Dog(Mammal):              #                              ^                    ^
    phrase = 'Bark!'            #                               \                  /
#                                                                \                /
#                                                                 - Method voice -
#                                                               (the same arguments)
class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):               #voice 2
        return 'Whooooo!!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)            # Recorded "Meow!"
r.record_animal(dog)            # Recorded "Bark!"
r.record_animal(strange_animal) # Recorded "Whooooo!!!"