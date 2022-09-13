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
        self.accnt = first + '-' + mid + '-' + last
        Account.count += 1
    
    @classmethod
    def get_account_num(user):
        print(user.count)
    
    def deposit(self, value):
        if value >= 1:
            self.balance += value

p1 = Account("김민지",800)
p1.deposit(300)
print(p1.balance)

p2 = Account("김남훈", 0)
p2.deposit(300)
print(p2.balance)

p3 = Account("김재은", 50000)
p3.deposit(300)
print(p3.balance)