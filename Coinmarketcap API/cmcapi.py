docmentation = 'https://coinmarketcap.com/api/documentation/v1/'

import requests
from requests import Session
import secret
from pprint import pprint as pp


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secret.api_key ,}

r = requests.get(url, headers=headers)


class CMC:
        def __init__(self, token):
            self.apiurl = 'https://pro-api.coinmarketcap.com'
            self.headers =  {'Accepts': 'application/json','X-CMC_PRO_API_KEY': token ,}
            self.session = Session()
            self.session.headers.update(self.headers)

        def GetAllCoins(self):
            url = self.apiurl + '/v1/cryptocurrency/map'
            r = self.session.get(url)
            data = r.json()['data']
            return data


        def GetPrice(self, symbol):
            url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
            paramaters = {'symbol': symbol}
            r = self.session.get(url, params=paramaters)
            data = r.json()['data']
            return data

cmc = CMC(secret.api_key)
pp(cmc.GetPrice('BTC'))
