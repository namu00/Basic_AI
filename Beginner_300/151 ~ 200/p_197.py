ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for c in ohlc[1:]:
    if c[-1] >= c[0]: print(c[-1])