#Pulls Current BTC Market Price in USD from CoinMarket API 
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'   #Can Change Currency BTC Value is converted to here
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ENTER COINMARKET API KEY HERE',       #Enter API Key Here
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  price = data['data'][0]['quote']['USD']['price']
  print('Current USD Price:', price)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

#Checks the value of your BTC wallet amount based off of current market price for 1 BTC
amt = str('ENTER BTC WALLET AMOUNT IN FLOAT FORMAT (DELETE QUOTATION MARKS)')       #Change Wallet Value Here 
value = float(amt) * float(price)
print("My BTC Wallet Currently Holds: ",str(amt))
print("This Is Currently Valued At: ",str(value), 'USD')
