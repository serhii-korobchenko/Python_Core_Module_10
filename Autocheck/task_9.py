from collections import UserDict


class LookUpKeyDict(UserDict):
    
    def lookup_key(self, value):
        
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys
        
   
    
        


our_dict = LookUpKeyDict()
our_dict.data = {
                "F": 1,	
                "FX": 2,
                "E": 3,	
                "D": 3,	
                "C": 4,	
                "B": 5,	
                "A": 5
                }
print(our_dict.lookup_key(2))

