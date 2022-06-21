import json

import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(URL)

data = json.loads(response.content.decode( "utf-8" ))

print(data)

print(data["chartName"], ":", data["bpi"]["USD"]["rate"], "$")
bitcoin_price = data["bpi"]["USD"]["rate_float"]
print(bitcoin_price)