class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("불명", "미상", "모름")
areum.who()      # Human.who(areum)

areum.setInfo("아름", 25, "여자")
areum.who()      # Human.who(areum)