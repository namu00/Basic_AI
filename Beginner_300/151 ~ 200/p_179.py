my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)