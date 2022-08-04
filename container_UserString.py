from collections import UserString


class TruncatedString(UserString):
    MAX_LEN = 7
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('abcdefghjklmnop')
ts.truncate()
print(ts)   # abcdefg