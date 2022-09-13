import random

class Account:
    count = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.d_count = 0
        self.deposit_log = []
        self.withdraw_log = []

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
            self.deposit_log.append("+" + str(value))

            self.d_count += 1
            if self.d_count % 5 == 0:
                self.balance = (self.balance * 1.01)
    
    def withdraw(self, value):
        if self.balance > value:
            self.balance -= value
            self.withdraw_log.append("-" + str(value))
    
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.accnt)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

p = Account("김재은", 50000)
p.deposit(100)
p.deposit(200)
p.deposit(300)
p.deposit_history()

p.withdraw(100)
p.withdraw(200)
p.withdraw_history()