def math(e):
    def sol():
        i = 0
        while i != 2:
            i = int(input("데이터 입력(1), 프로그램 종료(2) :"))
            if i == 2:
                break
            d = list(input("데이터를 입력하세요: "))
            step =0
            for i in d:
                if i =="(":
                    step += 1
                elif i==")":
                    step -=1

                if step !=0:
                    return print(False)
            if step==0:
                return print(True)
    sol()
while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break