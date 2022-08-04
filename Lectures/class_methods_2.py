class Human:
    name = ""     # field

    def hello(self, val): # method
        if self.name:
            return f"Hello {val}! I am {self.name}."
        return f"Hello {val}!"

bill = Human()
print(bill.hello("John"))   # Hello John!

bill.name = "Bill"
print(bill.hello("John"))   # Hello John! I am Bill.