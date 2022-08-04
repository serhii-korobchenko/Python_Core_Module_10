class Human: # 1st level class
    name = ''
    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human): # 2nd level class
    field_description = "My Programming language"
    language = ""
    def make_some_code(self):
        print (f"{self.field_description} is {self.value}")


class PythonDeveloper(Developer): # 3rt level class
    value = "Python"


class JSDeveloper(Developer): # 3rt level class
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.name = 'Bob'
p_dev.voice()   # Hello! My name is Bob
p_dev.make_some_code()  # My Programming language is Python


js_dev = JSDeveloper()
js_dev.make_some_code()  # My Programming language is JavaScript
print()
print(dir(p_dev)) # show all class atributes