ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)