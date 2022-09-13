import datetime 

def sol(a, b):
    dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    
    date = datetime.datetime(2020,a,b).weekday()
        
    return dic[date]

print(sol(5,24))