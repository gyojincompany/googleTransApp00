import pprint
import json

import requests

url = "https://api.upbit.com/v1/ticker"

param = {"markets":"KRW-BTC"}

response = requests.get(url, params=param)

print(response)

result = response.json()
print(result)

print(result[0]['trade_price'])