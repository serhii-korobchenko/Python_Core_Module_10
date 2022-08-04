from collections import UserList

class CountableList(UserList):
    def sum(self):
        print (sum(map(lambda x: int(x), self.data)))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
countable.sum()     # 15