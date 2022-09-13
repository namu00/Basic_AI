import random

class Account:
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

if __name__ == "__main__":
    user = Account("김남훈","999,999,999$")
    print(user.name)
    print(user.bank)
    print(user.accnt)
    print(user.balance)