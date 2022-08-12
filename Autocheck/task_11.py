from collections import UserString
import re


class NumberString(UserString):
    

    
    
    def number_count(self):
        
        self.count = 0
        
        for letter in self.data:
            if re.match(r"\d", letter):
                self.count +=1
                
        return self.count        


our_list = NumberString('hjkhksjh4fskjhh1jnm7,nx7nmn,mncz9')
print(our_list.number_count())