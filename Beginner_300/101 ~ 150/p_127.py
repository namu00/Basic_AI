PID = input("주민등록번호: ")
PID = PID.split("-")[1]
if PID[0] == "1" or PID[0] == "3":
    print("남자")
else:
    print("여자")