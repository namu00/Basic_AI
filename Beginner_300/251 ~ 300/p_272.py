import random

class Account:
    count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        first = ""
        mid = ""
        last = ""
        for i in range(3):
            first += str(random.randint(0,9))
        for i in range(2):
            mid += str(random.randint(0,9))
        for i in range(6):
            last += str(random.randint(0,9))
        self.accnt = first + '-' +mid + '-' + last
        Account.count += 1

p1 = Account("김민지","818,234,123,330 $")
print(p1.count)
p2 = Account("김남훈", "0 KRW")
print(p2.count)
p3 = Account("김재은", "50,000 EUR")
print(p3.count)