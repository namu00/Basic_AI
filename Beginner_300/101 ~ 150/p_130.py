import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

volume = float(btc['max_price']) - float(btc['min_price'])
current = float(btc['opening_price'])
high = float(btc['max_price'])

if (current+volume) > high:
    print("상승장")
else:
    print("하락장")