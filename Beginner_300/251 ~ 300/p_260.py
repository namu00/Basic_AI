class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
mystock.print()      # OMG.print(mystock)
#클래스의 내부함수 print()에 넘겨주는 인자가 없어야만 하는데, self라는 인자가 전달되므로
#입력으로 받는 인자의 개수가 매칭되지 않아 오류가 발생한다.