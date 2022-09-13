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
    
    def withdraw(self, value):
        if self.balance > value:
            self.balance -= value
    
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.accnt)
        print("잔고: ", self.balance)

p1 = Account("김민지",800)
p1.display_info()

p2 = Account("김남훈", 0)
p2.display_info()

p3 = Account("김재은", 50000)
p3.display_info()