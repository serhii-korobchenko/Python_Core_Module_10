class Contacts:
    current_id = 3

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        self.record = {}
        self.record['id'] = self.current_id
        self.record['name'] = name
        self.record['phone'] = phone
        self.record['email'] = email
        self.record['favorite'] = favorite
        self.current_id +=1
        self.contacts.append(self.record)
        
        return self.record 

our_contacts = Contacts()
our_contacts.add_contacts('Serhii', '0675261531', 'jchild2008@gmail.com', True)
our_contacts.add_contacts('Serhii', '0675261531', 'jchild2008@gmail.com', True)
print(our_contacts.list_contacts())






