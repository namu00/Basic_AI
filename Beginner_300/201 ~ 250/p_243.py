import datetime
now = datetime.datetime.now()

for d in range(5, 0, -1):
    delta = datetime.timedelta(days=d)
    date = now - delta
    print(date)